# Trabajo Práctico N°2  

**Integrantes**:  
- _Emiliano Castro_
- _Marcos A. Nieto_
- _Priscila T. Martinez_
 
**PacketLovers**  

**Universidad Nacional de Córdoba**  
**Facultad de Ciencias Exactas, Físicas y Naturales**  

**Materia**: _Comunicaciones de Datos_  
**Profesores**: _Miguel A. Solinas_, _Santiago M. Henn_, _Facundo O. Cuneo_  
**Fecha**: 08/09/2025  


## Resumen

En este trabajo práctico se analizaron fenómenos físicos relevantes en la transmisión de señales, incluyendo el efecto Doppler y la interferencia electromagnética de tipo impulsivo, evaluando su impacto sobre distintas bandas de frecuencia y la integridad de la señal. Se exploraron conceptos de SNR y BER, relacionando la calidad de la transmisión con la tasa de errores en la comunicación digital. Además, se investigaron aspectos prácticos de redes Ethernet y cableado UTP, incluyendo la estructura de tramas, direccionamiento MAC y configuraciones de cable derecho y cruzado. A través de la captura de paquetes con Wireshark, se examinaron direcciones MAC locales y remotas, y se destacó la trazabilidad de dispositivos a nivel de red y enlace de datos, así como la relación con identificadores móviles como el IMEI y la protección ofrecida por VPNs. Se estudia la influencia de la señal, el ruido y los identificadores de red sobre la comunicación y la privacidad de los usuarios en redes locales e Internet.

---

## Introducción

La transmisión de información en sistemas de comunicación digital está sujeta a diversos fenómenos físicos y técnicos que afectan la calidad y confiabilidad de la señal. En este contexto, el efecto Doppler y la interferencia electromagnética representan problemas críticos que pueden alterar la recepción y decodificación de datos, dependiendo de la frecuencia y el medio de transmisión. De manera complementaria, el estudio de redes Ethernet y la estructura de tramas permite comprender cómo se garantiza la integridad de la información en redes locales y cómo los identificadores únicos, como direcciones MAC e IMEI, posibilitan la trazabilidad de los dispositivos. El presente trabajo combina análisis teórico y experimentación práctica mediante herramientas de captura de paquetes, abordando tanto la transmisión de señales como la privacidad de los dispositivos, y proporciona un marco técnico para interpretar la relación entre fenómenos físicos, protocolos de red y seguridad de la información.

---

## Desarrollo

### 1)

Considerando la siguiente figura:

<p align="center">
<img width="911" height="292" alt="image" src="https://github.com/user-attachments/assets/ebec1a72-1123-451e-b10c-1de7d02661fd" />
</p>

**a)**

En la figura se representa el efecto Doppler, un fenómeno físico que se produce cuando existe movimiento relativo entre un emisor, receptor o ambos. Gráficamente, se observa cómo la longitud de onda o frecuencia de la señal electromagnética que envía el barco es percibida de manera distinta por el satélite debido al fenómeno.
Algunas características de este fenómeno son:

- Se manifiesta en todo tipo de ondas.
- La velocidad de propagación de la onda no cambia, ya que depende solo del medio.
- La frecuencia percibida aumenta si el emisor y el receptor se acercan y disminuye si se alejan.
- La variación de la frecuencia percibida depende de la velocidad relativa y de la frecuencia emitida.


**b)**

Considerando lo estudiado en el laboratorio anterior, el efecto doppler afecta mayormente a las bandas de transmisión que trabajan a frecuencias altas (UHF, SHF, EHF). Esto se debe a que la variación de frecuencia producida por el efecto doppler es proporcional a la frecuencia de la portadora. Por lo tanto, a frecuencias elevadas, el cambio en la frecuencia es más significativo, lo que puede provocar pérdida de sincronización o interferencias. Por otro lado, las transmisiones más resilientes son las que operan a frecuencias medias/bajas (LF, MF, HF), en estas el efecto Doppler tendría un impacto menor.

**c)**

Entre las principales razones por las cuales no se debe encender un celular en un avión se encuentra que el dispositivo está constantemente buscando señal y tratando de conectarse a varias antenas a la vez. Esta actividad puede generar interferencias electromagnéticas que afectan los sistemas de navegación y comunicación del avión, especialmente durante fases delicadas como despegue y aterrizaje.

Si bien el efecto Doppler está presente debido al movimiento del avión y puede modificar ligeramente la frecuencia percibida de las señales entre el avión y las antenas, este fenómeno no es la causa principal de la prohibición del uso de celulares. El riesgo se centra principalmente en la posibilidad de que las señales emitidas por múltiples dispositivos interfieran con los equipos electrónicos sensibles del avión.

---
### 2)

**a)**

Considerando la siguiente figura:

<p align="center">
<img width="934" height="256" alt="image" src="https://github.com/user-attachments/assets/c8431ecd-93e1-4bb8-8aa5-cdf2008eb8d2" />
</p>

El fenómeno físico representado corresponde a interferencia electromagnética (EMI), más específicamente ruido impulsivo. Este tipo de ruido se caracteriza por ser de alta intensidad y corta duración, apareciendo de manera súbita sobre la señal y afectando temporalmente su transmisión. A diferencia de otros ruidos, como el térmico o de fondo, el ruido impulsivo no presenta periodicidad ni constancia, manifestándose mediante picos breves que pueden alterar la recepción de señales en sistemas de comunicación.

Características principales:

- Corta duración: se manifiesta en intervalos muy breves, de microsegundos a milisegundos.
- Alta intensidad: puede superar significativamente el nivel normal de la señal, generando picos repentinos.
- Aparición súbita: no es periódico ni constante, a diferencia de otros tipos de ruido.
- Efecto sobre la señal: provoca interferencias momentáneas que pueden afectar la transmisión o recepción de datos.
- Origen típico: generado por dispositivos eléctricos como motores, taladros, conmutaciones bruscas de circuitos o descargas breves que irradian pulsos electromagnéticos.

Este tipo de interferencia puede degradar la calidad de la señal, es decir, disminuir la Relación Señal a Ruido (SNR), lo que aumenta la probabilidad de errores de bit y afecta la comunicación inalámbrica.

**b)**

Considerando las bandas de transmisión estudiadas en el laboratorio anterior, el efecto del ruido impulsivo varía significativamente según la frecuencia:

Bandas de baja frecuencia (LF, MF, HF): Estas bandas son altamente susceptibles al ruido impulsivo. Las ondas largas se ven afectadas por descargas atmosféricas y chispas de equipos eléctricos, que generan ruido de banda ancha. En estas frecuencias, el ruido impulsivo suele ser la principal causa de degradación de la señal, superando al ruido térmico.

Bandas de alta frecuencia (VHF, UHF, SHF, EHF): A medida que aumenta la frecuencia, el impacto del ruido impulsivo de fuentes terrestres (como taladros o motores) disminuye debido a la mayor atenuación de las ondas y a la menor propagación del ruido. En estas bandas, el principal factor limitante es el ruido térmico generado por los componentes del receptor, aunque pueden presentarse interferencias locales de fuentes impulsivas cercanas, como routers Wi-Fi o dispositivos Bluetooth.

En resumen, las bandas bajas son más vulnerables al ruido impulsivo, mientras que las bandas altas son más resilientes, aunque aún pueden verse afectadas por interferencias locales.

**c)**


La Relación Señal a Ruido (SNR, Signal-to-Noise Ratio) es un cociente adimensional que mide la potencia de una señal deseada en relación con la potencia del ruido de fondo. Se calcula mediante la fórmula:

<p align="center">$\text{SNR} = \frac{P_{\text{señal}}}{P_{\text{ruido}}}$</p>

Una SNR elevada indica que la señal es significativamente más potente que el ruido, lo que se traduce en una mayor calidad de transmisión.

La SNR está directamente relacionada con la Tasa de Error de Bit (BER, Bit Error Rate), que se define como:

<p align="center">$\text{BER} = \frac{\text{Número de bits erróneos}}{\text{Número total de bits transmitidos}}$</p>

Cuando la SNR es alta, el receptor puede distinguir correctamente los bits, resultando en una BER baja. Por el contrario, si la SNR disminuye (es decir, aumenta el ruido relativo), la probabilidad de errores en la decodificación de bits se incrementa, aumentando la BER.

En resumen, existe una relación inversa entre SNR y BER: a mayor SNR, menor BER. Esta relación es fundamental en el diseño de sistemas de comunicación confiables, ya que permite establecer límites sobre la tasa de error para un determinado nivel de potencia de señal y ruido.

---
### 3)

**a)**

Ethernet es una familia de tecnologías de red que permite la interconexión de dispositivos en redes de área local (LAN) o redes de área extensa (WAN). Opera en la capa de enlace de datos y la capa física del modelo OSI, proporcionando un estándar confiable para la comunicación entre dispositivos.

Características principales:

- Transmisión orientada a tramas, sin requerir conexión previa.
- Tamaño de trama: mínimo 64 bytes, máximo 1518 bytes (sin contar etiquetas VLAN).
- Compatibilidad con medios físicos como par trenzado (UTP/STP), cable coaxial y fibra óptica.
- Direccionamiento mediante direcciones MAC de 48 bits, garantizando la identificación única de cada dispositivo.
- Detección de errores mediante un código de redundancia cíclica (CRC-32) en el campo FCS, asegurando la integridad de la información.

Estructura de la trama Ethernet:

- Preamble (7 bytes) + Start Frame Delimiter (SFD, 1 byte): utilizados para la sincronización entre transmisor y receptor, garantizando que el inicio de la trama sea correctamente identificado.

- Dirección MAC destino (6 bytes): identifica de manera única al dispositivo receptor de la trama dentro de la red local.

- Dirección MAC origen (6 bytes): especifica el dispositivo emisor de la trama, permitiendo la trazabilidad de la información transmitida.

- Campo Tipo/Longitud (2 bytes): indica el protocolo de capa superior encapsulado en el campo de datos (por ejemplo, IPv4, IPv6, ARP) o, en ciertos casos, la longitud del campo de datos.

- Datos/Payload (46–1500 bytes): contiene la información útil que se desea transmitir, normalmente un paquete de la capa de red.

- Frame Check Sequence (FCS/CRC, 4 bytes): permite la detección de errores en la transmisión mediante un código de redundancia cíclica (CRC), asegurando la integridad de la trama.

Evolución tecnológica:

- Ethernet (10 Mbps): versión inicial, implementada sobre coaxial y posteriormente sobre par trenzado.

- Fast Ethernet (100 Mbps): multiplica por diez la velocidad respecto a la versión original, manteniendo la misma estructura de trama y requiriendo cables Cat 5 o superiores.

- Gigabit Ethernet (1000 Mbps): eleva la velocidad hasta 1 Gbps, utilizando técnicas de codificación como 8B/10B y soportando cables Cat 5e/6 o fibra óptica, preservando la compatibilidad con la estructura de trama estándar.

**b)**

El cable UTP (Unshielded Twisted Pair) está compuesto por cuatro pares de hilos de cobre trenzados, sin blindaje adicional. Se utiliza principalmente en redes Ethernet por su bajo costo, flexibilidad y eficiencia en la transmisión de datos.

El diseño del cable UTP está directamente relacionado con la atenuación del ruido impulsivo y la interferencia electromagnética (EMI), fenómenos que afectan la integridad de la señal. Cada par de hilos transporta la misma señal en polaridades opuestas; el ruido electromagnético que impacta ambos hilos se cancela en el extremo receptor, preservando la señal original. Este principio de cancelación de ruido por trenzado es fundamental para garantizar la alta fidelidad de la transmisión.

Configuraciones de cableado:

- Cable derecho: los pines se conectan de manera idéntica en ambos extremos (p. ej., pin 1 → pin 1, pin 2 → pin 2). Se utiliza para conectar dispositivos distintos, como PC a switch o switch a router.

- Cable cruzado: intercambia los pares de transmisión y recepción (p. ej., pin 1 → pin 3, pin 2 → pin 6). Se emplea para conectar dispositivos similares, como PC a PC o switch a switch, en equipos que no cuentan con auto MDI/MDIX.

Actualmente, la mayoría de los dispositivos modernos implementan auto MDI/MDIX, lo que permite que la conexión funcione correctamente independientemente del tipo de cable, simplificando la instalación y reduciendo posibles errores de conexión.

**c)**

El primer paso fue identificar la puerta de enlace predeterminada (gateway) de la red. Para eso, desde Linux en la terminal se usó el comando `ip route`. 

<p align="center">
<img width="550" height="52" alt="image" src="https://github.com/user-attachments/assets/472d743c-b6e8-4167-9b3b-a8cd13aed74d" />
</p>

Conociendo esa dirección, se abrió wireshark en la interfaz de red activa y se aplicó un filtro para capturar únicamente en el tráfico con el gateway: `ip.addr == 192.168.1.1.` Configurado eso, se generó un `ping -c 4 192.168.1.1`

<p align="center">
<img width="500" height="190" alt="image" src="https://github.com/user-attachments/assets/c3d943ab-bd31-41f1-9ee5-d6e540107434" />
</p>

Mientras el ping estaba en curso, se capturó en tiempo real los paquetes ICMP. En la lista pueden observarse las solicitudes (Echo Request) enviadas desde la PC (192.168.1.3) hacia el router (192.168.1.1) y las respuestas (Echo Reply) correspondientes.

<p align="center">
<img width="1222" height="439" alt="captura3" src="https://github.com/user-attachments/assets/e13cc926-b438-4d09-9898-ce3d11799892" />
</p>

Finalmente, se seleccionó uno de los paquetes para analizarlo en detalle. En este caso se tomó un Echo Request, cuyo contenido en hexadecimal es el siguiente:

<p align="center">
<img width="436" height="113" alt="image" src="https://github.com/user-attachments/assets/b88e95a2-c979-4388-b109-238599d5cd8a" />
</p>

**d)**

Analizando la información del paquete capturado en el punto anterior, se puede identificar el encabezado Ethernet (primeros 14 bytes), los cuales indican:

- **MAC de destino:** ```f0:c4:78:70:e4:49``` (gateway)
- **MAC de origen:** ```c8:ff:28:e9:87:c9``` (PC)
- **Tipo de protocolo:** ```08 00``` (IPv4)

Consultando la dirección MAC de destino del gateway en [macaddress.io](https://macaddress.io), se obtiene el fabricante:

- **Empresa**: _Huawei Tech Co., Ltd_
- **Dirección**: _No.2 Xin Cheng Road, Room R6, Songshan Lake Technology Park, Dongguan 523808, China_

**e)** 

Para este ejercicio, se utilizó la IP pública de un compañero: `191.97.218.143` y en wireshark se aplicó el filtro  `ip.addr == 191.97.218.143` para considerar únicamente los paquetes dirigidos a esa dirección IP.

Desde la terminal se ejecutó el comando `-ping -c 4 191.97.218.143` y mediante Wireshark se registraron los paquetes enviados y sus respectivas respuestas, sin pérdidas. 

<p align="center">
<img width="1146" height="308" alt="image" src="https://github.com/user-attachments/assets/4e97bdb3-bbb9-4744-89c2-95654295cf9f" />
</p>

Se seleccionó un paquete reply para analizar su formato hexadecimal. Donde el encabezado Ethernet indicó:

- **MAC de origen:** ```c8:ff:28:e9:87:c9``` (gateway de la red remota)
- **MAC de destino:** ```f0:c4:78:70:e4:49``` (gateway local)
- **Tipo de protocolo:** ```08 00``` (IPv4)

Nuevamente en [macaddress.io](https://macaddress.io) se consultó la dirección MAC de origen y se obtuvo la siguiente información:
- **Fabricante**: _Liteon Tech Corp_
- **Dirección**: _4F, 90, Chien 1 Road, New Taipei City, Taiwan 23585_

En este caso, la comunicación se realizó de forma remota utilizando la IP pública de un compañero, ya que los equipos no se encuentran en el mismo dominio local. La dirección MAC observada durante el ping no corresponde ni al dispositivo del compañero ni al router de su red, dado que las direcciones MAC no se transmiten más allá del dominio de enlace local. Esto demuestra que, en comunicaciones a través de Internet, la MAC permanece oculta y únicamente la IP pública del router actúa como identificador visible, confirmando que la trazabilidad de la MAC se limita al ámbito de la red local.


