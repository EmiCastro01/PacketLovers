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
<img width="803" height="241" alt="imagenpto1" src="https://github.com/user-attachments/assets/49110fa3-c665-47ce-97e8-1de2b132c24b" />
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
<img width="746" height="207" alt="imagenpunto2" src="https://github.com/user-attachments/assets/6d0c9a79-42c6-42bb-9719-0155aaac89d2" />
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
<img width="550" height="52" alt="capturaiproute" src="https://github.com/user-attachments/assets/774df845-009b-4a9d-a6d1-f3f5d2513ead" />
</p>

Conociendo esa dirección, se abrió wireshark en la interfaz de red activa y se aplicó un filtro para capturar únicamente en el tráfico con el gateway: `ip.addr == 192.168.1.1.` Configurado eso, se generó un `ping -c 4 192.168.1.1`

<p align="center">
 <img width="500" height="190" alt="imagenping3c" src="https://github.com/user-attachments/assets/3c8708c8-214c-48eb-ae28-430df8dc7f53" />
</p>

Mientras el ping estaba en curso, se capturó en tiempo real los paquetes ICMP. En la lista pueden observarse las solicitudes (Echo Request) enviadas desde la PC (192.168.1.3) hacia el router (192.168.1.1) y las respuestas (Echo Reply) correspondientes.

<p align="center">
<img width="1220" height="170" alt="imagenwhiresharkping3c" src="https://github.com/user-attachments/assets/2286c132-d50e-4cfd-8c0a-a298047e12f8" />
</p>

Finalmente, se seleccionó uno de los paquetes para analizarlo en detalle. En este caso se tomó un Echo Request, cuyo contenido en hexadecimal es el siguiente:

<p align="center">
<img width="427" height="107" alt="imagenpaquetehex3c" src="https://github.com/user-attachments/assets/25ce548e-0074-49e0-ae4e-7a124818c660" />
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
<img width="1151" height="320" alt="imagenwiresharkping3e" src="https://github.com/user-attachments/assets/14a8bfee-2f40-4e53-b97e-7b8fd1adfe08" />
</p>

Se seleccionó un paquete reply para analizar su formato hexadecimal. Donde el encabezado Ethernet indicó:

- **MAC de origen:** ```c8:ff:28:e9:87:c9``` (gateway de la red remota)
- **MAC de destino:** ```f0:c4:78:70:e4:49``` (gateway local)
- **Tipo de protocolo:** ```08 00``` (IPv4)

Nuevamente en [macaddress.io](https://macaddress.io) se consultó la dirección MAC de origen y se obtuvo la siguiente información:
- **Fabricante**: _Liteon Tech Corp_
- **Dirección**: _4F, 90, Chien 1 Road, New Taipei City, Taiwan 23585_

En este caso, la comunicación se realizó de forma remota utilizando la IP pública de un compañero, ya que los equipos no se encuentran en el mismo dominio local. La dirección MAC observada durante el ping no corresponde ni al dispositivo del compañero ni al router de su red, dado que las direcciones MAC no se transmiten más allá del dominio de enlace local. Esto demuestra que, en comunicaciones a través de Internet, la MAC permanece oculta y únicamente la IP pública del router actúa como identificador visible, confirmando que la trazabilidad de la MAC se limita al ámbito de la red local.

### **4)**

- **Privacidad de un dispositivo en la red y trazabilidad de dirección MAC**

En la actualidad, la privacidad de los dispositivos en la red se encuentra en constante riesgo debido a la trazabilidad, entendida como la capacidad de rastrear un equipo mediante sus identificadores únicos. Este fenómeno se presenta tanto a escala global de Internet como en entornos locales, comprometiendo la confidencialidad de los usuarios.

En la capa de red (Capa 3 del modelo OSI), la dirección IP constituye el principal vector de trazabilidad. Los Proveedores de Servicios de Internet (ISP) asignan estas direcciones y mantienen registros que permiten asociar el tráfico con una ubicación geográfica o un suscriptor específico. Incluso si la IP cambia, la persistencia de los registros de conexión posibilita reconstruir la actividad de un usuario. Si bien el cifrado extremo a extremo protege el contenido de las comunicaciones, los metadatos asociados —direcciones IP de origen y destino, tiempos de conexión y volumen de tráfico— permanecen visibles y representan un canal efectivo de seguimiento.

En la capa de enlace de datos (Capa 2), la dirección MAC (Media Access Control) cumple un rol crítico en la trazabilidad dentro de redes locales. Su carácter único permite identificar dispositivos en un dominio de broadcast, facilitando inventario, control de acceso y monitoreo de actividad. Aunque no se transmite más allá del router, su persistencia habilita la construcción de perfiles en entornos LAN. Existen técnicas como la aleatorización de MAC o el MAC spoofing que buscan mitigar este riesgo, aunque no eliminan la posibilidad de correlación con otros identificadores o patrones de tráfico.

- **IMEI y MAC**

De manera análoga, en el ámbito de la telefonía móvil, el IMEI (International Mobile Equipment Identity) es un identificador único asignado a cada dispositivo. Su función es permitir la gestión y control por parte de los operadores, incluyendo la capacidad de bloquear terminales en caso de robo o pérdida. Tanto el IMEI como la dirección MAC son identificadores persistentes que posibilitan la trazabilidad, aunque en dominios distintos: el primero en redes móviles y el segundo en redes locales de datos.

- **¿Una VPN oculta la dirección MAC?**

Por su parte, una VPN (Virtual Private Network) no oculta la dirección MAC, que sigue siendo visible dentro de la red local, pero sí protege la privacidad en la capa de red al ocultar la dirección IP pública y cifrar el tráfico en tránsito por Internet. De esta forma, evita que sitios web, servicios en línea o posibles interceptores externos asocien directamente la actividad del usuario con su ubicación geográfica.


En síntesis, la trazabilidad de dispositivos es un fenómeno multicapas: mientras que la dirección IP permite la asociación entre usuarios y ubicaciones a escala global, la dirección MAC lo hace a nivel local, y el IMEI en redes móviles. En todos los casos, aunque el contenido pueda cifrarse, los metadatos continúan expuestos y constituyen la base del seguimiento. La protección efectiva de la privacidad requiere combinar técnicas de ofuscación (MAC aleatoria, MAC spoofing, direcciones IPv6 temporales, VPN, DNS cifrado) con políticas de seguridad y retención mínima de datos, reduciendo así la posibilidad de rastreo y perfilado de los usuarios.


## Referencias

[1] https://openstax.org/books/f%C3%ADsica-universitaria-volumen-1/pages/17-7-el-efecto-doppler  
[2] https://www.bbc.com/mundo/noticias-63007583  
[3] [Stallings - Comunicaciones y Redes de Computadores 7ed](https://drive.google.com/file/d/14wtpr0_eigALENVraeLnF5faYEM4aQB9/view?usp=drive_link)  
