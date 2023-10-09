/*
 * led_bufete.c
 *
 *  Created on: Sep 15, 2023
 *      Author: victo
 */


#include "led_bufete.h"

static led_bufete led_list[] = {
		{
			.port = GPIOA,
			.pin = GPIO_PIN_15,
		},
//		{
//			.port = GPIOB,
//			.pin = GPIO_PIN_4
//		},
//		{
//			.port = GPIOB,
//			.pin = GPIO_PIN_12,
//		},
		{
			.port = GPIOB,
			.pin = GPIO_PIN_13
		},
		{
			.port = GPIOB,
			.pin = GPIO_PIN_5
		},
		{
			.port = GPIOB,
			.pin = GPIO_PIN_6
		},
		{
			.port = GPIOB,
			.pin = GPIO_PIN_7
		},
		{
			.port = GPIOB,
			.pin = GPIO_PIN_8
		},
		{
			.port = GPIOB,
			.pin = GPIO_PIN_9
		},
		{
			.port = GPIOC,
			.pin = GPIO_PIN_13
		},
		{
			.port = GPIOC,
			.pin = GPIO_PIN_14
		},
		{
			.port = GPIOC,
			.pin = GPIO_PIN_15
		},
};

void leds_init(){
	for(uint32_t i = 0; i < sizeof(led_list)/sizeof(led_bufete); i++){
		HAL_GPIO_Init(led_list[i].port, led_list[i].pin);
		HAL_GPIO_WritePin(led_list[i].port, led_list[i].pin, GPIO_PIN_RESET);
	}
}

void turnOnLed(uint32_t led_id){
	HAL_GPIO_WritePin(led_list[led_id].port, led_list[led_id].pin, GPIO_PIN_SET);
}

void turnOffLed(uint32_t led_id){
	HAL_GPIO_WritePin(led_list[led_id].port, led_list[led_id].pin, GPIO_PIN_RESET);
}
