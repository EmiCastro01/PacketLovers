import paho.mqtt.client as mqtt

BROKER = "26cbfc677af6417dab48032407831a61.s1.eu.hivemq.cloud"
PORT = 8883
USERNAME = "hivemq.webclient.1763425829401"
PASSWORD = "ev9H;6>73<IDkMabCuU,"
TOPIC = "lan/broadcast/#"

def on_connect(client, userdata, flags, reason_code, properties):
    print("Conectado ! Soy el Cliente 2 (subscriber)", reason_code)
    client.subscribe(TOPIC)
    
def on_message(client, userdata, msg):
    print(f"[Cliente 2] Mensaje recibido en {msg.topic}: {msg.payload.decode()}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(USERNAME, PASSWORD)
client.tls_set()

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT)
client.loop_forever()