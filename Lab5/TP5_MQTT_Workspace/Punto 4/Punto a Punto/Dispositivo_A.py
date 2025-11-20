import paho.mqtt.client as mqtt

BROKER = "26cbfc677af6417dab48032407831a61.s1.eu.hivemq.cloud"
PORT = 8883
USERNAME = "hivemq.webclient.1763247657925"
PASSWORD = "MP0w$Ea9uHF;R12l&on>"
TOPIC = "lan/deviceA/status"

def on_connect(client, userdata, flags, reason_code, properties):
    print("Conectado ! Soy el Dispositivo A (publisher)", reason_code)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(USERNAME, PASSWORD)
client.tls_set()

client.on_connect = on_connect

client.connect(BROKER, PORT)

client.publish(TOPIC, "[Dispositivo A] Hola PacketLovers! 😎​")
print("Mensaje enviado con éxito desde el Dispositivo A.")
client.loop_forever()