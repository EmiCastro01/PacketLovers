# Trabajo Práctico N°5

**Integrantes**:  
- _Emiliano Castro_  
- _Marcos A. Nieto_  
- _Priscila T. Martinez_  

**PacketLovers**

**Universidad Nacional de Córdoba**  
**Facultad de Ciencias Exactas, Físicas y Naturales**

**Materia**: _Comunicaciones de Datos_  
**Profesores**: _Miguel A. Solinas_, _Santiago M. Henn_, _Facundo O. Cuneo_  
**Fecha**: 18/11/2025  

---

## Resumen
En este trabajo se implementó un sistema de comunicación basado en el protocolo MQTT empleando el modelo Publisher–Subscriber. Se configuró un broker en HiveMQ Cloud, se desarrollaron clientes en Python y WebSocket, y se realizaron pruebas de comunicación punto a punto, broadcasting y manejo de sensores distribuidos. Se monitoreó el tráfico utilizando Wireshark y se evaluaron aspectos de seguridad, transporte de datos, QoS y el impacto de la arquitectura centralizada del broker. Además, se integró una base de datos InfluxDB junto a Grafana para visualizar en tiempo real las mediciones generadas por los sensores simulados.

## Introducción
La comunicación entre dispositivos distribuidos es un componente esencial en sistemas modernos como IoT, automatización industrial y monitoreo remoto. MQTT (Message Queuing Telemetry Transport) surge como un protocolo liviano y eficiente pensado para entornos con recursos limitados y redes inestables.

Este trabajo práctico tiene como objetivo implementar una arquitectura pub/sub completa utilizando MQTT, comprender su funcionamiento, analizar el tráfico generado y evaluar sus ventajas y limitaciones como alternativa de comunicación. Asimismo, se construyó un escenario de sensores distribuidos y se integró con herramientas de persistencia y visualización de datos.

## Marco teórico

### Protocolo MQTT
MQTT es un protocolo de mensajería ligero basado en el patrón Publisher–Subscriber. Funciona sobre TCP/IP y permite la transmisión eficiente de datos en dispositivos con conectividad limitada.

Las principales características de MQTT incluyen su ligereza y eficiencia, lo que lo hace ideal para dispositivos IoT; su funcionamiento sobre TCP/IP; y la capacidad de gestionar calidad de servicio (QoS) en la entrega de mensajes. Además, permite la suscripción a tópicos específicos, lo que hace que los clientes reciban únicamente la información relevante para ellos. MQTT también soporta la persistencia de mensajes, garantizando que la información llegue incluso si un cliente está temporalmente desconectado.

**Ventajas**
- Ligero, eficiente y escalable.  
- Adecuado para dispositivos de baja potencia.  
- Permite comunicación confiable en redes inestables.  
- Tópicos flexibles que facilitan la organización de mensajes.

**Desventajas**
- Dependencia total del broker.  
- No apto para grandes volúmenes de datos o archivos.  
- Requiere configuración adicional para garantizar seguridad (TLS, auth).

MQTT se utiliza ampliamente en sensores, actuadores, telemetría vehicular, domótica, automatización industrial y notificaciones en tiempo real.

### Patrón de diseño Pub/Sub
En el modelo Publisher–Subscriber, los publicadores envían mensajes a tópicos sin conocer quién los recibirá, mientras que los suscriptores se registran en los tópicos que les interesan.

Esto proporciona:

- Desacoplamiento temporal y espacial.  
- Escalabilidad al permitir agregar o eliminar clientes sin afectar al resto.  
- Flexibilidad, ya que múltiples publicadores y suscriptores pueden interactuar sin configuración explícita.

MQTT implementa este patrón y lo optimiza para entornos distribuidos.

## Resultados
Se eligió configurar y ejecutar el broker MQTT llamado HiveMQ.

<img width="896" height="355" alt="image" src="https://github.com/user-attachments/assets/2fda7e26-b7ca-44ca-b734-7a96dbfa6fdd" />

---

### Verificación del broker
Para confirmar el funcionamiento del broker se implementaron dos clientes:

- Subscriber en Python usando `paho-mqtt`.  
- Publisher mediante WebClient MQTT desde el navegador.

El subscriber recibía correctamente los mensajes publicados desde el WebClient, confirmando la operación del broker.

<img width="897" height="478" alt="image" src="https://github.com/user-attachments/assets/591b1a1e-51a1-4e00-a585-6e0254b2eced" />


---

### Comunicación punto a punto
Ambos clientes (publisher y subscriber) fueron reimplementados en Python.

- Dispositivo A publica en `lan/deviceA/status`.  
- Dispositivo B se suscribe al mismo tópico.  

Al enviar mensajes desde A, el dispositivo B los recibe sin problemas, verificando la comunicación directa mediante un tópico compartido.

<img width="892" height="152" alt="image" src="https://github.com/user-attachments/assets/56491993-7de5-4e86-b6ad-1afa6c863ea1" />


---

### Broadcasting
Se diseñó un esquema de broadcast utilizando comodines MQTT.

- Cliente central publica en: `lan/broadcast/all`  
- Clientes 1 y 2 suscriptos a: `lan/broadcast/#`  

El comodín `#` permite recibir todos los mensajes que compartan el prefijo `lan/broadcast/`.

Ambos clientes reciben correctamente los mensajes enviados por la central.

<img width="895" height="485" alt="image" src="https://github.com/user-attachments/assets/5c5720d2-d180-429a-b112-dda945f8351e" />


---

### Jerarquía de sensores y gateway central
Se creó una estructura de tópicos simulando sensores en distintas salas:

- `lan/sala1/sensor/temp`  
- `lan/sala1/sensor/hum`  
- `lan/sala2/sensor/temp`

Cada sensor fue implementado como un cliente MQTT independiente y configurado para escuchar un tópico de control general, desde donde se enviaron los comandos `start` y `stop`. Esto permitió activar o desactivar simultáneamente todos los sensores sin modificar cada script individualmente.

<img height="500" alt="image" src="https://github.com/user-attachments/assets/37c8d3ed-57eb-46bf-909b-4288b8f697fc" />


<img width="896" height="471" alt="image" src="https://github.com/user-attachments/assets/df4f55c2-1aaa-4883-a1fd-fc50b9174366" />


<img width="894" height="472" alt="image" src="https://github.com/user-attachments/assets/67de7da4-9209-4e82-b4e3-9499e0bf5432" />

<br><br>

Mientras los sensores generaban datos, un cliente central actuó como gateway, procesando cada publicación y extrayendo la información relevante: sala, tipo de sensor y valor. Este gateway almacenó las mediciones en InfluxDB, lo que permitió disponer de registros temporales eficientes sin necesidad de archivos planos.
Posteriormente, se utilizó Grafana para visualizar en tiempo real las mediciones históricas. Los paneles creados mostraron las variaciones de temperatura y humedad para cada sala, lo que permitió observar la frecuencia de publicación y el comportamiento de la simulación.

<img width="893" height="481" alt="image" src="https://github.com/user-attachments/assets/09484569-fc88-42e1-a38b-b9dc107632ea" />

<br><br>

Por último, se realizó una captura de tráfico utilizando Wireshark mientras los sensores y el gateway se comunicaban con el broker MQTT en HiveMQ Cloud.

El paquete analizado (frame 30927) corresponde a tráfico enviado desde el broker (54.73.92.158) hacia el cliente en la red local (192.168.0.50). A nivel de transporte, se trata de un segmento TCP cuyo puerto origen es 8883 (MQTT sobre TLS) y puerto destino es un puerto efímero del cliente (53247). El payload corresponde a un registro TLS de tipo “Application Data” y aparece como “Encrypted Application Data”, por lo que el contenido MQTT no es legible en la captura. Esto demuestra que la comunicación broker-cliente se realiza de forma cifrada mediante TLS y que los topics/valores publicados no pueden extraerse sin las claves de sesión.


<img width="895" height="452" alt="image" src="https://github.com/user-attachments/assets/11410671-1ac6-47c6-8596-15013f27beb6" />



<img width="895" height="112" alt="image" src="https://github.com/user-attachments/assets/2f66ef49-6dea-4731-849e-15aa26cce985" />


---

### 6)
**a)**
En esta actividad, los sensores se comunican con el broker MQTT utilizando TCP (Transmission Control Protocol) como protocolo de transporte. Además, dado que se está utilizando HiveMQ Cloud, la comunicación está protegida mediante TLS (Transport Layer Security) sobre TCP en el puerto 8883, lo que garantiza la confidencialidad e integridad de los mensajes.


**b)**
Los datos enviados por los clientes están protegidos frente a modificaciones durante el tránsito gracias a TCP, que garantiza entrega completa y en orden, y TLS, que detecta cualquier alteración (integridad). TLS también cifra los mensajes MQTT, evitando que terceros puedan leer los mensajes de los clientes o comandos del broker central (confidencialidad). La disponibilidad depende del broker central (HiveMQ Cloud en este caso) y de la conexión de red; si el broker o la conexión falla, los clientes no pueden transmitir datos, por lo que esta garantía no está totalmente asegurada.
En resumen, el modelo pub/sub ofrece flexibilidad y escalabilidad, pero las garantías de seguridad y disponibilidad no están aseguradas por el modelo en sí, sino que dependen de medidas adicionales de infraestructura, configuración del broker y protocolos de protección. 


**c)**
Los niveles de QoS (Quality of Service) en MQTT juegan un rol fundamental en la fiabilidad de los mensajes, ya que determinan cómo se garantiza que la información enviada por un dispositivo llegue correctamente a su destino. Cada nivel de QoS define un grado distinto de seguridad en la entrega: el QoS 0 envía el mensaje solo una vez sin confirmación, lo que lo hace rápido pero menos confiable; el QoS 1 asegura que el mensaje llegue al menos una vez, lo que aumenta la fiabilidad aunque puede generar duplicados; y el QoS 2 garantiza que cada mensaje se entregue exactamente una vez, evitando pérdidas o duplicaciones, aunque a costa de un mayor consumo de recursos y tiempo. De esta manera, los niveles de QoS permiten a MQTT adaptar la fiabilidad de la comunicación según la importancia de los datos, equilibrando velocidad, eficiencia y seguridad en la transmisión de información.


**d)**
El modelo pub/sub (Publisher-Subscriber) ofrece varias ventajas frente al modelo tradicional cliente-servidor, principalmente por su desacoplamiento entre emisores y receptores. En un modelo cliente-servidor, los clientes deben conocer al servidor y establecer una conexión directa para cada comunicación, lo que genera dependencia y sobrecarga si hay muchos clientes o si el servidor falla. En cambio, en pub/sub, los publicadores envían mensajes a un tema sin conocer quién los recibe, y los suscriptores reciben únicamente la información de los temas a los que están suscritos. Esto permite escalar más fácilmente, agregar o eliminar clientes sin afectar a los demás y reducir la carga de la red, ya que no se necesitan múltiples conexiones directas.


**e)**
Aunque MQTT es un protocolo muy eficiente para la comunicación entre dispositivos distribuidos, tiene algunas limitaciones en comparación con una red LAN tradicional. En primer lugar, MQTT depende de un broker central para gestionar los mensajes, lo que introduce un punto único de falla, mientras que en una LAN los dispositivos pueden comunicarse directamente entre sí sin intermediarios. Además, MQTT está diseñado para transmitir mensajes ligeros y frecuentes, pero no es adecuado para transferir grandes volúmenes de datos o archivos pesados, algo que una LAN puede manejar fácilmente gracias a su mayor ancho de banda. También, la latencia de MQTT puede ser mayor que en una LAN, especialmente si el broker se encuentra lejos de los clientes o si hay muchos mensajes en cola. Finalmente, aunque MQTT puede implementarse sobre LAN, su seguridad requiere configuración adicional (como TLS y autenticación), mientras que muchas LAN pueden usar controles de acceso físicos y lógicos integrados.


**f)**
Depender de un broker central en la comunicación MQTT tiene varias implicaciones importantes. En primer lugar, convierte al broker en un punto único de falla: si el broker deja de funcionar, los mensajes no pueden ser enviados ni recibidos, interrumpiendo toda la comunicación entre dispositivos. Además, esta dependencia puede generar cuellos de botella cuando hay muchos clientes conectados o un volumen elevado de mensajes, afectando el rendimiento y aumentando la latencia. También implica que la gestión de la seguridad y el acceso debe concentrarse en el broker, ya que todos los datos pasan por él; cualquier vulnerabilidad en el broker puede comprometer la comunicación de toda la red. Por último, la dependencia de un broker central puede limitar la flexibilidad de despliegue, ya que los clientes necesitan mantener conectividad constante con él para intercambiar mensajes.


---

## Discusión y Conclusiones
La implementación del sistema distribuido basado en MQTT permitió analizar su comportamiento en un entorno real y evaluar la interacción entre los distintos componentes involucrados. El uso de HiveMQ Cloud posibilitó trabajar con un broker externo bajo cifrado TLS, permitiendo verificar tanto la seguridad de las comunicaciones como la estabilidad del canal. La configuración de tópicos jerárquicos y las pruebas de publicación, suscripción y simulación de sensores ofrecieron una visión clara de cómo se organiza y circula la información en aplicaciones IoT. Por otra parte, la integración con InfluxDB y Grafana aportó herramientas efectivas para almacenar y visualizar series temporales, reforzando la importancia del monitoreo continuo en este tipo de sistemas. El análisis del tráfico en Wireshark complementó el estudio al mostrar el comportamiento del protocolo a bajo nivel y confirmar la correcta aplicación del cifrado.

---

## Referencias

- [¿Qué es MQTT?](https://aws.amazon.com/es/what-is/mqtt/) 
- [Patrón de diseño Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview?hl=es-419)  
- [HiveMQ Cloud - Documentation](https://docs.hivemq.com/hivemq-cloud/quick-start-guide.html)




