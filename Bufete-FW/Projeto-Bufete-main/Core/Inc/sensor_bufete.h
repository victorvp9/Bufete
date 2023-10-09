/*
 * sensor_bufete.h
 *
 *  Created on: Oct 5, 2023
 *      Author: victo
 */

#ifndef INC_SENSOR_BUFETE_H_
#define INC_SENSOR_BUFETE_H_

#include "main.h"
#include "stm32f3xx_hal.h"

//Struct que representa um sensor
typedef struct
{
    //ADC
	ADC_HandleTypeDef* ad;
	//ADC pin
	uint32_t canal;
    //tempo em multiplos de ms que o impacto precisa para ser registrado
	//usar HAL delay
	uint32_t debounce_time;
    //threshold
	uint32_t limit;
	//Configuração
	ADC_ChannelConfTypeDef config;

}punch_sensor_t;

/*!
 * @function sensorListInit
 *
 * @abstract Inicia o vetor de sensores usando a função sensorInit para cada posição.
 *
 * @param	hadc1	ponteiro para o conversor ad que o sensor utilizará (*hadc1) definido e iniciado na main;
 * @param	hadc2	ponteiro para o conversor ad que o sensor utilizará (*hadc2) definido e iniciado na main;
 * @param	hadc3	ponteiro para o conversor ad que o sensor utilizará (*hadc3) definido e iniciado na main;
 *
 */
void sensorListInit(ADC_HandleTypeDef *hadc1, ADC_HandleTypeDef *hadc2, ADC_HandleTypeDef *hadc3);

/*!
 * @function sensorInit
 *
 * @abstract Preenche os campos do struct sensor, passe apenas as configurações.
 *
 * @param	adc		ponteiro para o conversor ad que o sensor está utilizando o *hadcx que passamos para ler do ad, por exemplo;
 * @param	res		resolução do adc utilizado, útil para determinar o threshold
 * @param	time	tempo de debounce do impacto do soco
 * @param	sensor	sensor de impacto sendo preenchido pela função
 *
 */
void sensorInit(ADC_HandleTypeDef* adc, uint32_t canal, uint32_t time, punch_sensor_t* sensor);
/*!
 * @function checkImpact
 *
 * @abstract Checa se o impacto causado foi válido para o teste
 *
 * @param sensor	sensor que será lido pelo ad para verificar o impacto
 *
 * @result 1 se a força do impacto foi maior que fora determinado, ou 0 se não foi.
 */
//uint32_t checkImpact(punch_sensor_t* sensor);
uint32_t checkImpact(uint32_t sensor_id);


#endif /* INC_SENSOR_BUFETE_H_ */
