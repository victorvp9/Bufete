/*
 * sensor_bufete.c
 *
 *  Created on: Oct 5, 2023
 *      Author: victo
 */


#include "sensor_bufete.h"
#include "main.h"


#define THRESHOLD 3000 //Pressupondo que usaremos um ADC de 12bits
#define TIMEOUT 100 //Usado para conversão do AD


static punch_sensor_t sensor_list[] = {
		{
			.ad = 0,
			.canal = 1,
			.config = { 0 },
			.debounce_time = 0,
			.limit = 3
		},
		{
			.ad = 0,
			.canal = 12,
			.config = { 0 },
			.debounce_time = 0,
			.limit = 2
		},
		{
			.ad = 0,
			.canal = 3,
			.config = { 0 },
			.debounce_time = 0,
			.limit = 2
		},
		{
			.ad = 0,
			.canal = 12,
			.config = { 0 },
			.debounce_time = 0,
			.limit = 3
		},
		{
			.ad = 0,
			.canal = 1,
			.config = { 0 },
			.debounce_time = 0,
			.limit = 2
		},
		{
			.ad = 0,
			.canal = 2,
			.config = { 0 },
			.debounce_time = 0,
			.limit = 2
		},
		{
			.ad = 0,
			.canal = 3,
			.config = { 0 },
			.debounce_time = 0,
			.limit = 1
		},
		{
			.ad = 0,
			.canal = 4,
			.config = { 0 },
			.debounce_time = 0,
			.limit = 1
		},
		{
			.ad = 0,
			.canal = 1,
			.config = { 0 },
			.debounce_time = 0,
			.limit = 1
		},
		{
			.ad = 0,
			.canal = 2,
			.config = { 0 },
			.debounce_time = 0,
			.limit = 1
		},
};

void sensorListInit(ADC_HandleTypeDef *hadc1, ADC_HandleTypeDef *hadc2, ADC_HandleTypeDef *hadc3){
	for(uint32_t i = 0; i < sizeof(sensor_list)/sizeof(punch_sensor_t); i++){
		if(sensor_list[i].limit == 1){
			sensorInit(hadc1, sensor_list[i].canal, sensor_list[i].debounce_time, &sensor_list[i]);
		} else if(sensor_list[i].limit == 2){
			sensorInit(hadc2, sensor_list[i].canal, sensor_list[i].debounce_time, &sensor_list[i]);
		} else if (sensor_list[i].limit == 3){
			sensorInit(hadc3, sensor_list[i].canal, sensor_list[i].debounce_time, &sensor_list[i]);
		}
	}
}

//Inicializar o sensor
void sensorInit(ADC_HandleTypeDef* adc, uint32_t canal, uint32_t time, punch_sensor_t* sensor) {
	//Inicializa as informações do sensor
	sensor-> ad = adc;
	sensor-> debounce_time = time;
	sensor-> limit = THRESHOLD;

	//Reconfigura o pino do ADC
	ADC_ChannelConfTypeDef sConfig = {0};

	sConfig.Channel = canal;
	sConfig.Rank = ADC_REGULAR_RANK_1;
	sConfig.SingleDiff = ADC_SINGLE_ENDED;
	sConfig.SamplingTime = ADC_SAMPLETIME_1CYCLE_5;
	sConfig.OffsetNumber = ADC_OFFSET_NONE;
	sConfig.Offset = 0;

	sensor -> config = sConfig;
}


static void configure_ADC_Pin(punch_sensor_t* sensor){

	if (HAL_ADC_ConfigChannel(sensor->ad, &(sensor->config)) != HAL_OK)
	  {
		Error_Handler();
	  }
}

static uint32_t get_ADC_Read(ADC_HandleTypeDef* adc, uint32_t timeout){

	uint32_t value;
	HAL_ADC_Start(adc);

	HAL_ADC_PollForConversion(adc, timeout);
	value = HAL_ADC_GetValue(adc);

	HAL_ADC_Stop(adc);

	return value;
}


uint32_t checkImpact(uint32_t sensor_id){
	punch_sensor_t *sensor = &sensor_list[sensor_id];
	ADC_HandleTypeDef* adc = sensor->ad;
	uint32_t threshold = sensor->limit;
	uint32_t delay = sensor->debounce_time;
	uint32_t value = 0;
	uint32_t impact = 0;
	uint32_t i = 0;

	configure_ADC_Pin(sensor);
	value = get_ADC_Read(adc, TIMEOUT);

	while(i<2000){

		if(value > 0){
			if(value < threshold){
				return impact;
			}
			else{
				HAL_Delay(delay);
				value = get_ADC_Read(adc, TIMEOUT);
				if(value > threshold){
				impact = 1;
				return impact;
				}
		 	}
		}
		i++;
	}

	return impact;
}



//uint32_t checkImpact(punch_sensor_t* sensor){
//	ADC_HandleTypeDef* adc = sensor->ad;
//	uint32_t threshold = sensor->limit;
//	uint32_t delay = sensor->debounce_time;
//	uint32_t value = 0;
//	uint32_t impact = 0;
//	uint32_t i = 0;
//
//	configure_ADC_Pin(sensor);
//	value = get_ADC_Read(adc, TIMEOUT);
//
//	while(i<2000){
//
//		if(value > 0){
//			if(value < threshold){
//				return impact;
//			}
//			else{
//				HAL_Delay(delay);
//				value = get_ADC_Read(adc, TIMEOUT);
//				if(value > threshold){
//				impact = 1;
//				return impact;
//				}
//		 	}
//		}
//		i++;
//	}
//
//
//	return impact;
//}
