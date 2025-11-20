import paho.mqtt.client as mqtt

BROKER = "26cbfc677af6417dab48032407831a61.s1.eu.hivemq.cloud"
PORT = 8883
USERNAME = "hivemq.webclient.1763425829401"
PASSWORD = "ev9H;6>73<IDkMabCuU,"
TOPIC = "lan/broadcast/all"

def on_connect(client, userdata, flags, reason_code, properties):
    print("Conectado ! Soy la central (publisher)", reason_code)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(USERNAME, PASSWORD)
client.tls_set()

client.on_connect = on_connect

client.connect(BROKER, PORT)


client.publish(TOPIC, "[Central] Hola a todos los subscribers! ")
print("Mensaje enviado con éxito desde la central.")
client.loop_forever()

