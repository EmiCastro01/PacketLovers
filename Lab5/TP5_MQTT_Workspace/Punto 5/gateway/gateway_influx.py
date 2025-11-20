import paho.mqtt.client as mqtt
from influxdb_client import InfluxDBClient, Point, WritePrecision

# --- CONFIG MQTT ---
BROKER = "26cbfc677af6417dab48032407831a61.s1.eu.hivemq.cloud"
PORT = 8883
USER = "hivemq.webclient.1763254619945"
PASSWORD = "AQ7Dxs0*6&u<kIP1t$Xi"
TOPICS = ["lan/sala1/sensor/hum", "lan/sala1/sensor/temp", "lan/sala2/sensor/temp"]

# --- CONFIG INFLUX ---
INFLUX_URL = "http://localhost:8086"
INFLUX_TOKEN = "ideCmJ5xNZfjjzjNMjg02CI8XDQ804xNDucPGXf64SSb2HyKzsHFofI9ofwZhCv51AZ9YxA75ZQGQj7q9JUTmQ=="
INFLUX_ORG = "PacketLovers"
INFLUX_BUCKET = "sensores"

client_influx = InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN, org=INFLUX_ORG)
write_api = client_influx.write_api()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("MQTT conectado:", rc)
        for t in TOPICS:
            client.subscribe(t)
            print("Suscripto a:", t)
    else:
        print("Error de conexion:", rc)
    

def on_message(client, userdata, msg):
    partes = msg.topic.split("/")
    sala = partes[1]        # sala1, sala2...
    sensor = partes[3]      # temp o hum
    valor = float(msg.payload.decode())

    print(f"→ Sala: {sala} | Sensor: {sensor} | Valor: {valor}")

    # Crear punto para Influx
    p = (
        Point("mediciones")     
        .tag("sala", sala)
        .tag("sensor", sensor)
        .field("valor", valor)
    )

    # Guardar en Influx
    write_api.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=p)


client = mqtt.Client()
client.username_pw_set(USER, PASSWORD)
client.tls_set()

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_forever()
