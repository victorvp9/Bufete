/*
 * bufete_tx.c
 *
 *  Created on: Aug 21, 2023
 *      Author: victo
 */
#include <stdint.h>
#include "main.h"
#include "bufete_tx.h"
#include "bufete_defines.h"

/**
* @brief Transmit data with the huart1 with Bufete communication protocol
* @param huart1: UART pointer
* @param pData: pointer to array that contain the payload that will be send.
* @param pDataSize: array (pData) size
* @retval uint8_t: byte that is read or (-1) if buffer is empty.
*/

void tx_init(tx_bufete *tx, UART_HandleTypeDef *selectedUart) {
	tx->huart_tx = selectedUart;
}

void bufete_tx_transmit(tx_bufete tx, const uint8_t *pData, uint32_t pDataSize) {

	uint8_t start = FLAG_SHDLC;
	uint8_t scape = ESCAPE_SHDLC_7D;
	uint8_t data;
	HAL_UART_Transmit(tx.huart_tx, &start, 1, 500);

	for(int i=0;i<pDataSize;i++){
		data = pData[i];
		if(data==FLAG_SHDLC){
			HAL_UART_Transmit(tx.huart_tx, &scape, 1, 500);
			data = ESCAPE_SHDLC_5E;
		} else if(data == ESCAPE_SHDLC_7D){
			HAL_UART_Transmit(tx.huart_tx, &data, 1, 500);
			data = ESCAPE_SHDLC_5D;
		}
		HAL_UART_Transmit(tx.huart_tx, &data, 1, 500);
	}

	HAL_UART_Transmit(tx.huart_tx, &start, 1, 500);
}
