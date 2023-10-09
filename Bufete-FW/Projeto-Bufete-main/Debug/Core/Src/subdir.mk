################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (11.3.rel1)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Core/Src/adc.c \
../Core/Src/bufete_functions.c \
../Core/Src/bufete_rx.c \
../Core/Src/bufete_tx.c \
../Core/Src/gpio.c \
../Core/Src/led_bufete.c \
../Core/Src/main.c \
../Core/Src/ringbuffer.c \
../Core/Src/sensor_bufete.c \
../Core/Src/stm32f3xx_hal_msp.c \
../Core/Src/stm32f3xx_it.c \
../Core/Src/syscalls.c \
../Core/Src/sysmem.c \
../Core/Src/system_stm32f3xx.c \
../Core/Src/tim.c \
../Core/Src/usart.c 

OBJS += \
./Core/Src/adc.o \
./Core/Src/bufete_functions.o \
./Core/Src/bufete_rx.o \
./Core/Src/bufete_tx.o \
./Core/Src/gpio.o \
./Core/Src/led_bufete.o \
./Core/Src/main.o \
./Core/Src/ringbuffer.o \
./Core/Src/sensor_bufete.o \
./Core/Src/stm32f3xx_hal_msp.o \
./Core/Src/stm32f3xx_it.o \
./Core/Src/syscalls.o \
./Core/Src/sysmem.o \
./Core/Src/system_stm32f3xx.o \
./Core/Src/tim.o \
./Core/Src/usart.o 

C_DEPS += \
./Core/Src/adc.d \
./Core/Src/bufete_functions.d \
./Core/Src/bufete_rx.d \
./Core/Src/bufete_tx.d \
./Core/Src/gpio.d \
./Core/Src/led_bufete.d \
./Core/Src/main.d \
./Core/Src/ringbuffer.d \
./Core/Src/sensor_bufete.d \
./Core/Src/stm32f3xx_hal_msp.d \
./Core/Src/stm32f3xx_it.d \
./Core/Src/syscalls.d \
./Core/Src/sysmem.d \
./Core/Src/system_stm32f3xx.d \
./Core/Src/tim.d \
./Core/Src/usart.d 


# Each subdirectory must supply rules for building sources it contributes
Core/Src/%.o Core/Src/%.su Core/Src/%.cyclo: ../Core/Src/%.c Core/Src/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=gnu11 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32F303xC -c -I../Core/Inc -I../Drivers/STM32F3xx_HAL_Driver/Inc/Legacy -I../Drivers/STM32F3xx_HAL_Driver/Inc -I../Drivers/CMSIS/Device/ST/STM32F3xx/Include -I../Drivers/CMSIS/Include -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -fcyclomatic-complexity -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-Core-2f-Src

clean-Core-2f-Src:
	-$(RM) ./Core/Src/adc.cyclo ./Core/Src/adc.d ./Core/Src/adc.o ./Core/Src/adc.su ./Core/Src/bufete_functions.cyclo ./Core/Src/bufete_functions.d ./Core/Src/bufete_functions.o ./Core/Src/bufete_functions.su ./Core/Src/bufete_rx.cyclo ./Core/Src/bufete_rx.d ./Core/Src/bufete_rx.o ./Core/Src/bufete_rx.su ./Core/Src/bufete_tx.cyclo ./Core/Src/bufete_tx.d ./Core/Src/bufete_tx.o ./Core/Src/bufete_tx.su ./Core/Src/gpio.cyclo ./Core/Src/gpio.d ./Core/Src/gpio.o ./Core/Src/gpio.su ./Core/Src/led_bufete.cyclo ./Core/Src/led_bufete.d ./Core/Src/led_bufete.o ./Core/Src/led_bufete.su ./Core/Src/main.cyclo ./Core/Src/main.d ./Core/Src/main.o ./Core/Src/main.su ./Core/Src/ringbuffer.cyclo ./Core/Src/ringbuffer.d ./Core/Src/ringbuffer.o ./Core/Src/ringbuffer.su ./Core/Src/sensor_bufete.cyclo ./Core/Src/sensor_bufete.d ./Core/Src/sensor_bufete.o ./Core/Src/sensor_bufete.su ./Core/Src/stm32f3xx_hal_msp.cyclo ./Core/Src/stm32f3xx_hal_msp.d ./Core/Src/stm32f3xx_hal_msp.o ./Core/Src/stm32f3xx_hal_msp.su ./Core/Src/stm32f3xx_it.cyclo ./Core/Src/stm32f3xx_it.d ./Core/Src/stm32f3xx_it.o ./Core/Src/stm32f3xx_it.su ./Core/Src/syscalls.cyclo ./Core/Src/syscalls.d ./Core/Src/syscalls.o ./Core/Src/syscalls.su ./Core/Src/sysmem.cyclo ./Core/Src/sysmem.d ./Core/Src/sysmem.o ./Core/Src/sysmem.su ./Core/Src/system_stm32f3xx.cyclo ./Core/Src/system_stm32f3xx.d ./Core/Src/system_stm32f3xx.o ./Core/Src/system_stm32f3xx.su ./Core/Src/tim.cyclo ./Core/Src/tim.d ./Core/Src/tim.o ./Core/Src/tim.su ./Core/Src/usart.cyclo ./Core/Src/usart.d ./Core/Src/usart.o ./Core/Src/usart.su

.PHONY: clean-Core-2f-Src

