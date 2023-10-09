/*
 * teste.c
 *
 *  Created on: Sep 15, 2023
 *      Author: victo
 */

#include <bufete_functions.h>
#include "bufete_defines.h"
#include "led_bufete.h"
#include "sensor_bufete.h"
#include "tim.h"

static cmd_bufete cmd_list[] = {
	{
        .id = CMD_AUTH,
		.num_param = 0,
		.func = bufete_auth
    },
    {
    	.id = CMD_LED_ON,
		.num_param = 10,
		.func = bufete_led_on
    },
    {
        .id = CMD_LED_TEST,
		.num_param = 10,
		.func = bufete_led_test
    },
};

static uint8_t buffer[UART_BUFFER_SIZE];
static uint32_t data_size;

void bufete_check_payload(uint8_t *payload, uint32_t payloadSize){
	for(uint32_t i = 0; i < sizeof(cmd_list)/sizeof(cmd_bufete); i++){
		if(payload[0] == cmd_list[i].id){
			if(payloadSize-1 == cmd_list[i].num_param){
				cmd_list[i].func(payload, payloadSize);
				return;
			}
		}
	}
	data_size = 0;
}

uint32_t get_response(uint8_t **buff){
	*buff = buffer;
	return data_size;
}

void bufete_auth(uint8_t *payload, uint32_t payloadSize){
	buffer[0] = 0x00;
	buffer[1] = 0x00;
	data_size = 2;
}

void bufete_led_on(uint8_t *payload, uint32_t payloadSize){

	for(uint32_t i = 0; i < payloadSize; i++){
		if(payload[i] == 0x69){
			turnOnLed(i-1);
			// Zerando o timer
			htim2.Instance->CNT = 0;
			HAL_TIM_Base_Start(&htim2);
			while(checkImpact(i-1) == 0 && htim2.Instance->CNT < 127000000);
			uint32_t end_time = htim2.Instance->CNT;
			HAL_TIM_Base_Stop(&htim2);
			end_time = end_time/1600;
			if(end_time>70000){
				data_size = 0;
				turnOffLed(i-1);
				return;
			}
			buffer[0] = 0x01;
			buffer[1] = i;
			buffer[2] = (end_time & 0xFF000000) >> 24;
			buffer[3] = (end_time & 0x00FF0000) >> 16;
			buffer[4] = (end_time & 0x0000FF00) >> 8;
			buffer[5] = (end_time & 0x000000FF) >> 0;
			data_size = 6;

			turnOffLed(i-1);
			return;
		}
	}
}

void bufete_led_test(uint8_t *payload, uint32_t payloadSize){
	for(uint32_t i = 0; i < payloadSize; i++){
		if(payload[i] == 0x69){
			turnOnLed(i-1);
			HAL_Delay(300);
			turnOffLed(i-1);
			buffer[0] = 0x02;
			buffer[1] = i;
			data_size = 2;
			return;
		}
	}
}

