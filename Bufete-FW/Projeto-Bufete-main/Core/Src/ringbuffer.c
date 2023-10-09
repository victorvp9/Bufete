#include <stdint.h>
#include "main.h"
#include "ringbuffer.h"

/**
* @brief ring_buff initialization
* @param ring_buff: Ringbuffer pointer
* @retval None
*/
void Ringbuf_init(ring_buffer *ring_buff){
	ring_buff->head = 0;
	ring_buff->tail = 0;
}


/**
* @brief Writes a byte to the ring_buffer
* @param ring_buff: Ringbuffer pointer
* @param c: byte that will be written in buffer
* @retval None
*/
void write_byte(ring_buffer *buffer, uint8_t c) {
		unsigned int i = (unsigned int)((buffer->tail + 1) % UART_BUFFER_SIZE);
		if(i == buffer->tail){
			// está cheio
		} else{
			buffer->buffer[buffer->tail] = c;
			buffer->tail = i;
		}
}


/**
* @brief Writes a array to the ring buffer
* @param ring_buff: Ringbuffer pointer
* @param pData: array to be read
* @param pDataSize: array (pData) size.
* @retval None
*/
void write_array(ring_buffer *buffer, const uint8_t *pData, uint16_t pDataSize){
	 if(buffer->tail+pDataSize%UART_BUFFER_SIZE < buffer->head){
		 for(int i = 0; i < pDataSize; i++){
			 write_byte(buffer, pData[i]);
		 }
	 }
}


/**
* @brief Reads the next byte and return this byte or -1 if haven´t bytes to read.
* @param ring_buff: Ringbuffer pointer
* @retval uint8_t: byte that is read or (-1) if buffer is empty.
*/
 uint8_t read_byte(ring_buffer *buffer){
	 if(!isEmpty(buffer)){
		 uint8_t c = buffer->buffer[buffer->head];
		 buffer->head = (unsigned int)(buffer->head + 1) % UART_BUFFER_SIZE;
		 return c;
	 } else {
		 return -1;
	 }
}


 /**
 * @brief Reads all bytes of the ring buffer and write them to the array.
 * @param buffer: Ringbuffer pointer
 * @param payload: pointer to array that will receive buffer values.
 * @retval uint16_t: Last written array position
 */
 uint16_t read_buffer(ring_buffer *buffer, uint8_t *payload){
	 uint16_t position = 0;
	 while(!isEmpty(buffer)){
		payload[position] = read_byte(buffer);
		position++;
	}
	 return position-1;
 }

 /**
 * @brief Verify if buffer is empty
 * @param buffer: Ringbuffer pointer
 * @retval uint8_t: (1) if the ring_buffer is empty and (0) if not.
 */
 uint8_t isEmpty(ring_buffer *buffer){
	 if(buffer->head == buffer->tail){
		 return 1;
	 }else{
		 return 0;
	 }
 }

 /**
 * @brief Verify if buffer is full
 * @param buffer: Ringbuffer pointer
 * @retval uint8_t: 1 if the ring_buffer is full and 0 if not.
 */
 uint8_t isFull(ring_buffer *buffer){
	 if((buffer->tail+1)%UART_BUFFER_SIZE == buffer->head){
		 return 1;
	 }else {
		 return 0;
	 }

 }
