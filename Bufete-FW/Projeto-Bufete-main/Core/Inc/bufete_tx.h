/*
 * bufete_tx.h
 *
 *  Created on: Aug 21, 2023
 *      Author: victo
 */

#ifndef INC_BUFETE_TX_H_
#define INC_BUFETE_TX_H_

typedef struct {
	UART_HandleTypeDef *huart_tx;
} tx_bufete;

void tx_init(tx_bufete *tx, UART_HandleTypeDef *selectedUart);
void bufete_tx_transmit(tx_bufete tx, const uint8_t *pData, uint32_t pDataSize);
#define INC_BUFETE_TX_H_



#endif /* INC_BUFETE_TX_H_ */
