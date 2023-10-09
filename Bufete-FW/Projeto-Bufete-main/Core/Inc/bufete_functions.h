/*
 * teste.h
 *
 *  Created on: Sep 15, 2023
 *      Author: victo
 */

#ifndef INC_TESTE_H_
#define INC_TESTE_H_
#include <stdint.h>


typedef enum{
	CMD_AUTH = 0x00,
	CMD_LED_ON = 0x01,
	CMD_LED_TEST = 0x02,
}cmd_id;


typedef void (*cmd_func)(uint8_t *, uint32_t);


typedef struct{
	uint8_t id;
	uint8_t num_param;
	cmd_func func;
}cmd_bufete;


uint32_t get_response(uint8_t **buff);
void bufete_check_payload(uint8_t *payload, uint32_t payloadSize);
void bufete_auth(uint8_t *payload, uint32_t payloadSize);
void bufete_led_on(uint8_t *payload, uint32_t payloadSize);
void bufete_led_test(uint8_t *payload, uint32_t payloadSize);


#endif /* INC_TESTE_H_ */
