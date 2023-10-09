/*
 * led_bufete.h
 *
 *  Created on: Sep 15, 2023
 *      Author: victo
 */

#ifndef INC_LED_BUFETE_H_
#define INC_LED_BUFETE_H_
#include "main.h"
#include "stm32f3xx_hal.h"

typedef struct {
	GPIO_TypeDef *port;
	uint16_t pin;
} led_bufete;

void leds_init();
void turnOnLed(uint32_t led_id);
void turnOffLed(uint32_t led_id);

#endif /* INC_LED_BUFETE_H_ */
