import paho.mqtt.client as mqtt
import random
import time

BROKER = "26cbfc677af6417dab48032407831a61.s1.eu.hivemq.cloud"
PORT = 8883
USER = "hivemq.webclient.1763254619945"
PASSWORD = "AQ7Dxs0*6&u<kIP1t$Xi"

TOPIC_DATA = "lan/sala2/sensor/temp"
TOPIC_CMD = "lan/broadcast/#"

running = False 

def on_connect(client, userdata, flags, rc):
    print("Conectado:", rc)
    client.subscribe(TOPIC_CMD)

def on_message(client, userdata, msg):
    global running
    cmd = msg.payload.decode()

    if cmd == "start":
        print(">> Recibido comando START")
        running = True

    elif cmd == "stop":
        print(">> Recibido comando STOP")
        running = False

client = mqtt.Client()
client.username_pw_set(USER, PASSWORD)
client.tls_set()

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_start()

while True:
    if running:
        value = round(random.uniform(15, 25), 2)
        client.publish(TOPIC_DATA, value)
        print(f"Publicado: {value}")
    time.sleep(2)
