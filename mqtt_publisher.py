from common.utility import Common
from time import sleep
import paho.mqtt.client as mqtt

host = "192.168.100.30"
port = 1883
topic = "/word/test"

# MQTTブローカーに5種類の文字列をランダムに送信する
if __name__ == "__main__":
    client = mqtt.Client(protocol=mqtt.MQTTv311)
    client.connect(host,port,keepalive=60)

    while True:
        client.publish(topic, Common.get_random_words(3, 3))
        sleep(1)
    pass
