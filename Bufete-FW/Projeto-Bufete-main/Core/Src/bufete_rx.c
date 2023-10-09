/*
 * bufete_rx.c
 *
 *  Created on: Aug 21, 2023
 *      Author: victo
 */


#include <stdint.h>
#include "main.h"
#include "bufete_rx.h"



void rx_start(rx_buffer *_bufete_rx){
	HAL_UART_Receive_IT(_bufete_rx->huart_rx, &_bufete_rx->byte_rx, 1);
}

/**
* @brief rx_init
* @param _bufete_rx: rx_buffer pointer
* @param buffer: ring_buffer pointer
* @retval None
*/
void rx_init(rx_buffer *_bufete_rx, UART_HandleTypeDef *selectedUart, ring_buffer *buffer){
	Ringbuf_init(buffer);
	_bufete_rx->ring_buff = buffer;
	_bufete_rx->isPayloadFinish = 1;
	_bufete_rx->huart_rx = selectedUart;
	_bufete_rx->byte_rx = 0;
}

/**
* @brief UART MSP De-Initialization
* This function freeze the hardware resources used in this example
* @param _bufete_rx: rx_buffer pointer
* @retval None
*/
void bufete_rx_write_byte(rx_buffer *_bufete_rx){
	if(_bufete_rx->byte_rx == FLAG_SHDLC){
		if(_bufete_rx->isPayloadFinish == 0){
			_bufete_rx->isPayloadFinish = 1;
			return;
		}else {
			_bufete_rx->isPayloadFinish = 0;
			return;
		}
	}else if(_bufete_rx->isPayloadFinish==1){
		return;
	}else{
		write_byte(_bufete_rx->ring_buff, _bufete_rx->byte_rx);
	}
}


/**
* @brief UART MSP De-Initialization
* This function freeze the hardware resources used in this example
* @param _bufete_rx: rx_buffer pointer
* @param payload: pointer to array that have bytes to be read
* @param payloadSize: array(payload) size
* @retval None
*/
void bufete_rx_write_array(rx_buffer *_bufete_rx, uint8_t *payload, uint16_t payloadSize) {
	write_array(_bufete_rx->ring_buff, payload, payloadSize);
}


/**
* @brief UART MSP De-Initialization
* This function freeze the hardware resources used in this example
* @param _bufete_rx: rx_buffer pointer
* @param payload: array that will receive the translated buffer.
* @retval uint16_t: Last written array position
*/
uint16_t bufete_rx_translate(rx_buffer *_bufete_rx, uint8_t *payload){
	uint16_t size = 0;
	uint8_t byte;
	while(!isEmpty(_bufete_rx->ring_buff)){
		byte = read_byte(_bufete_rx->ring_buff);
		if(byte != FLAG_SHDLC){
			if(byte == ESCAPE_SHDLC_7D){
				byte = read_byte(_bufete_rx->ring_buff);
				if(byte == ESCAPE_SHDLC_5E){
					payload[size] = FLAG_SHDLC;
					size++;
				} else if(byte == ESCAPE_SHDLC_5D){ //seria somente else por que no caso não pode ter um 0x7d sozinho no meio do payload?
					payload[size] = ESCAPE_SHDLC_7D;
					size++;
				}
			} else{
				payload[size] = byte;
				size++;
			}
		}
	}
	_bufete_rx->ring_buff->head = 0;
	_bufete_rx->ring_buff->tail = 0;
	return size;
}


