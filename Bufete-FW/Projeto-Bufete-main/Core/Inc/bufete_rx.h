/*
 * bufete_rx.h
 *
 *  Created on: Aug 21, 2023
 *      Author: victo
 */

#ifndef INC_BUFETE_RX_H_
#define INC_BUFETE_RX_H_
#include "ringbuffer.h"
#include "bufete_defines.h"

typedef struct {
	ring_buffer *ring_buff;
	unsigned char isPayloadFinish;
	UART_HandleTypeDef *huart_rx;
	uint8_t byte_rx;
} rx_buffer;


void rx_start(rx_buffer *_bufete_rx);
void rx_init(rx_buffer *_bufete_rx, UART_HandleTypeDef *selectedUart, ring_buffer *buffer);
void bufete_rx_read(rx_buffer *_bufete_rx, const uint8_t *pData, unsigned int size);
void bufete_rx_write_byte(rx_buffer *_bufete_rx);
void bufete_rx_write_array(rx_buffer *_bufete_rx, uint8_t *payload, uint16_t payloadSize);
uint16_t bufete_rx_translate(rx_buffer *_bufete_rx, uint8_t *payload);

#define INC_BUFETE_RX_H_



#endif /* INC_BUFETE_RX_H_ */
