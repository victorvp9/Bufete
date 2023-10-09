/*
 * ringbuffer.h
 *
 *  Created on: Aug 21, 2023
 *      Author: victo
 */

#ifndef INC_RINGBUFFER_H_
#define INC_RINGBUFFER_H_

#include "bufete_defines.h"

typedef struct{
  uint8_t buffer[UART_BUFFER_SIZE];
  unsigned int head;
  unsigned int tail;
}ring_buffer;


void Ringbuf_init(ring_buffer *ring_buff);
void write_byte(ring_buffer *buffer, uint8_t c);
void write_array(ring_buffer *buffer, const uint8_t *pData, uint16_t pDataSize);
uint8_t read_byte(ring_buffer *buffer);
uint16_t read_buffer(ring_buffer *buffer, uint8_t *payload);
uint8_t isEmpty(ring_buffer *buffer);
uint8_t isFull(ring_buffer *buffer);

#endif /* INC_RINGBUFFER_H_ */
