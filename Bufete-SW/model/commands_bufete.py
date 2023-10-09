from model.serial_bufete import handler_sing

# DEFINES:
CONNECT_ID = b"\x00"
TURN_ON_LEDS_ID = b"\x01"
TEST_LEDS_ID = b"\x02"




class CommandsBufete():
    def __init__(self):
        self.handler = handler_sing

    def connect(self):
        cmd = list()
        cmd.append(CONNECT_ID)
        self.handler.write(cmd)

        response = self.handler.receive()
        return response

    def turn_on_leds(self, led_id):
        LED_ARRAY = [b"\x00", b"\x00", b"\x00", b"\x00", b"\x00", b"\x00", b"\x00", b"\x00", b"\x00", b"\x00"]
        LED_ARRAY[led_id] = b"\x69"

        cmd = list()
        cmd.append(TURN_ON_LEDS_ID)
        cmd.extend(LED_ARRAY)

        self.handler.write(cmd)

        response = self.handler.receive()
        return response

    def test_led(self, led_id):
        LED_ARRAY = [b"\x00", b"\x00", b"\x00", b"\x00", b"\x00", b"\x00", b"\x00", b"\x00", b"\x00", b"\x00"]
        LED_ARRAY[led_id] = b"\x69"

        cmd = list()
        cmd.append(TEST_LEDS_ID)
        cmd.extend(LED_ARRAY)

        self.handler.write(cmd)

        response = self.handler.receive()
        return response
