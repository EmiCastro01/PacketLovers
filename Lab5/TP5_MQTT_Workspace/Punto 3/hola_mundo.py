import paho.mqtt.client as mqtt

BROKER = "26cbfc677af6417dab48032407831a61.s1.eu.hivemq.cloud"
PORT = 8883
USERNAME = "hivemq.webclient.1763247657925"
PASSWORD = "MP0w$Ea9uHF;R12l&on>"
TOPIC = "test/PacketLovers"

def on_connect(client, userdata, flags, reason_code, properties):
    print("Conectado !", reason_code)
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print(f"Mensaje recibido en {msg.topic}: {msg.payload.decode()}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(USERNAME, PASSWORD)
client.tls_set()

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT)
print("Suscrito al topic:", TOPIC)
print("Esperando mensajes...")
client.loop_forever()


