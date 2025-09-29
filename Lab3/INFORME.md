# Trabajo Práctico N°3 

**Integrantes**:

- _Emiliano Castro_ 
- _Marcos A. Nieto_ 
- _Priscila T. Martinez_ 

**PacketLovers**

**Universidad Nacional de Córdoba**  
**Facultad de Ciencias Exactas, Físicas y Naturales**  

**Materia**: _Comunicaciones de Datos_  
**Profesores**: _Miguel A. Solinas_, _Santiago M. Henn_, _Facundo O. Cuneo_  
**Fecha**: 29/09/2025

---

## Resumen 

En este trabajo se analizan distintos estándares y tecnologías de comunicaciones de datos. Se abordan los orígenes y evolución de IEEE 802.3 (Ethernet) y IEEE 802.11 (Wi-Fi), considerando compatibilidad, seguridad y aplicaciones actuales. También se estudian las fibras ópticas monomodo y multimodo, con énfasis en la dispersión modal, la Ley de Snell y los costos asociados a su implementación. Se comparan medios de transmisión alámbricos e inalámbricos, junto con protocolos de comunicación como Wi-Fi, Bluetooth, ZigBee, NFC, LTE, GSM, 5G, LoRa, NB-IoT y Z-Wave.  

En la parte práctica, se identificaron las versiones de IEEE 802.11 utilizadas en redes abiertas de la Facultad (FCEFyN, UNC-LIBRE), verificando los esquemas de seguridad implementados y contrastándolos con versiones previas. Este análisis permitió vincular la teoría con la práctica, resaltando la relación entre la evolución de los estándares y la protección efectiva de las redes inalámbricas.  

Palabras clave: IEEE 802.3, IEEE 802.11, Wi-Fi 7, fibra óptica, dispersión modal, Ley de Snell, protocolos inalámbricos, seguridad de redes.  



## Introducción

La necesidad de transmitir información de manera rápida, segura y confiable ha impulsado la creación de múltiples estándares de comunicación, tanto alámbricos como inalámbricos. Ethernet, estandarizado en 1983 bajo IEEE 802.3, marcó el inicio de redes locales cableadas de alta capacidad, mientras que la aparición de IEEE 802.11 en 1997 permitió el desarrollo de redes inalámbricas, que con el tiempo alcanzaron tasas de transmisión y niveles de seguridad comparables a las redes cableadas.  

Paralelamente, la fibra óptica se consolidó como medio físico de referencia para enlaces de alta velocidad y largas distancias, superando las limitaciones de interferencia y ancho de banda presentes en otros soportes. Al mismo tiempo, la proliferación de protocolos inalámbricos y de corto alcance (Wi-Fi, Bluetooth, ZigBee, entre otros) refleja la necesidad de soluciones adaptadas a diferentes entornos y requerimientos.  

Este trabajo tiene como objetivo analizar la evolución de estas tecnologías, comparar sus características principales y aplicar los conceptos estudiados en un relevamiento práctico de redes inalámbricas disponibles en la Facultad. De esta manera, se busca establecer la relación entre la teoría y la práctica, destacando el impacto de la estandarización y la seguridad en los sistemas de comunicación actuales.  



## Desarrollo

### 1) 

**a)**

El estándar IEEE 802.3, publicado por primera vez en 1983, estableció las bases de lo que hoy conocemos como Ethernet. Su origen está vinculado al trabajo de Xerox PARC en la década de 1970, donde se diseñó el primer prototipo de Ethernet para interconectar computadoras en entornos de laboratorio. Posteriormente, el IEEE estandarizó y formalizó la tecnología, adoptando un esquema de control de acceso al medio basado en CSMA/CD (Carrier Sense Multiple Access with Collision Detection). A lo largo del tiempo, 802.3 ha evolucionado con sucesivas enmiendas que permitieron incrementar la velocidad de transmisión desde los 10 Mbps iniciales hasta estándares actuales que superan los 400 Gbps, utilizando distintos medios físicos como cable coaxial, par trenzado y fibra óptica. Su campo de aplicación se encuentra principalmente en las redes cableadas de área local (LAN), donde garantiza transmisión confiable, baja latencia y alta capacidad de integración en infraestructuras de red corporativas, industriales y domésticas.
Por otra parte, el estándar IEEE 802.11 fue publicado en 1997 como respuesta a la creciente necesidad de desarrollar redes de área local inalámbricas (WLAN). A diferencia de 802.3, este estándar emplea como medio de transmisión el espectro radioeléctrico, definiendo técnicas de modulación y protocolos de acceso al medio específicos para comunicaciones sin cables. Desde sus primeras versiones, que ofrecían velocidades limitadas y un alcance modesto, 802.11 evolucionó en distintas enmiendas como 802.11b, 802.11g, 802.11n, 802.11ac y 802.11ax (Wi-Fi 6/6E), cada una ampliando la capacidad de transmisión, la eficiencia espectral y la seguridad mediante mecanismos como WPA/WPA2/WPA3. Más recientemente, se ha publicado 802.11be (Wi-Fi 7), cuya versión definitiva fue aprobada en 2025.

**b)**
Ir a la facuuu

**c)**
Cuando una red Wi-Fi opera bajo un determinado protocolo de la familia IEEE 802.11 (por ejemplo, 802.11ac o 802.11ax), la capacidad de un dispositivo para conectarse dependerá de la compatibilidad de su interfaz de red inalámbrica (NIC) con dicho protocolo. En el caso de dispositivos más antiguos, cuyas NIC solo soporten versiones previas (por ejemplo, 802.11g o 802.11n), existen dos escenarios principales:

1. **Compatibilidad Descendente (Backward Compatibility)**:
Muchos puntos de acceso permiten operar simultáneamente con estándares antiguos y nuevos. Así, la notebook antigua podrá conectarse, aunque la velocidad de transmisión se limitará al máximo que soporte su NIC, reduciendo el throughput efectivo y, potencialmente, afectando el rendimiento global de la red.

2. **Falta de Compatibilidad**:
Si el punto de acceso solo admite el protocolo más reciente, la NIC antigua no podrá conectarse, ya que no reconoce los mecanismos de modulación y control de tramas del estándar moderno.

Desde el punto de vista ingenieril, esto refleja la evolución de las capas física (PHY) y de enlace de datos (MAC) en IEEE 802.11. Cuando se habilita compatibilidad descendente, los AP operan en modos mixtos, introduciendo cierta ineficiencia espectral debido al overhead necesario para interoperar con dispositivos antiguos.

**d)**
La versión del protocolo Wi‑Fi utilizada en una red está directamente relacionada con su nivel de seguridad, ya que cada estándar incorpora mejoras en autenticación y cifrado. Protocolos antiguos como 802.11b/g/n (Wi‑Fi 4) emplean mecanismos vulnerables como WEP o WPA, mientras que versiones más modernas como 802.11ac/ax/be (Wi‑Fi 5, 6 y 7) utilizan WPA2/WPA3, cifrado AES‑CCMP y protecciones frente a ataques de suplantación o descifrado de tráfico.

Además, mantener dispositivos antiguos conectados puede obligar al AP a operar en modos de compatibilidad descendente, limitando el uso de las funciones de seguridad más avanzadas. Por ello, actualizar APs y clientes a estándares recientes no solo mejora el rendimiento, sino también la robustez de la red frente a intrusiones.

[] VOlver a la facuuu

**e)**
|              |    Wi-Fi 5   |   Wi-Fi 6    |   Wi-Fi 7    |
|--------------|--------------|--------------|--------------|
| Versión IEEE |   802.11ac   | 802.11ax     | 802.11be     |
|Tasa de datos máxima| Hasta 3.5 Gbps    | Hasta 9.6 Gbps     | Hasta 46 Gbps      |
|Banda(s)      | 5 GHz        | 2.4 GHz y 5 GHz (6GHz Opcional con 6E) | 2.4 GHz, 5 GHz y 6 GHz |
|Ancho de Banda| 20 / 40 / 80 / 160 MHz | 20 / 40 / 80 / 160 Mhz | 20 / 40 / 80 / 160 / 320 Mhz |
|Modulación| 256-QAM | 1024-QAM | 4096-QAM |
| Sistema de Seguridad | WPA2-PSK / WPA2-Enterprise | WPA3-Personal / WPA3-Enterprise (Compatible con WPA2) | WPA3-Personal / WPA3-Enterprise (Compatibilidadompatible con WPA2) + mejoras indirectas por MLO y eficiencia de operación |

### 2)

En base a la siguiente Figura:

<p align="center">
<img width="499" height="100" alt="image" src="https://github.com/user-attachments/assets/551889df-0407-4d64-b532-187743d94e7b" />
</p>

**a)**
Los tipos de transmisión ilustrados en la figura son: la Fibra Óptica Monomodo (SMF, Single Mode Fiber) y la Fibra Óptica Multimodo (MMF, Multi Mode Fiber).


La SMF se caracteriza por poseer un núcleo de diámetro muy reducido, típicamente de entre 8 y 10 micrómetros. Gracias a esta dimensión tan pequeña, únicamente un modo de propagación de la luz puede transmitirse, lo que elimina la dispersión modal y permite alcanzar grandes distancias con una mínima atenuación de la señal. Como fuente de transmisión se utilizan láseres de alta precisión, lo que le otorga a esta fibra la capacidad de soportar anchos de banda extremadamente elevados. En consecuencia, la fibra monomodo es la solución preferida para enlaces de larga distancia, troncales de telecomunicaciones y aplicaciones donde se requiere máxima capacidad y estabilidad en la transmisión.
La MMF presenta un núcleo considerablemente más grande, con diámetros que oscilan entre 50 y 62,5 micrómetros. Esta mayor sección permite que la señal de luz se propague en múltiples modos, es decir, en diferentes trayectorias dentro del núcleo, lo que genera rebotes y distintos tiempos de llegada. Como consecuencia, se produce dispersión modal, un fenómeno que limita tanto la distancia máxima como el ancho de banda alcanzable.
La diferencia fundamental es la Dispersión Modal. En la MMF, el ensanchamiento del pulso luminoso reduce la velocidad de bits máxima (Tasa de Transmisión) que puede soportar, ya que los pulsos adyacentes comienzan a superponerse (Inter-Symbol Interference - ISI). La SMF evita este fenómeno por su diseño de núcleo estrecho, lo que la hace superior en rendimiento para enlaces de largo recorrido y alta capacidad.

La Fibra Óptica Monomodo (SMF) es más costosa de implementar que la Multimodo:
- **Costo de Componentes**: Aunque el cable de fibra SMF en sí mismo puede ser comparable o incluso más económico que el MMF, los transceptores ópticos (láseres) requeridos para la SMF son mucho más caros. Se necesitan láseres de alta precisión y alineación estricta para inyectar la potencia lumínica eficazmente en el núcleo extremadamente pequeño de la fibra monomodo. En contraste, la MMF utiliza LEDs o VCSEL más económicos.
- **Costo de Instalación**: Las labores de empalme y conexión para la SMF exigen mayor precisión, lo que requiere equipos de empalme por fusión más sofisticados y técnicos especializados, incrementando los costos operativos de la instalación. Por otro lado, en la MMF el acoplamiento óptico es más tolerante a desalineaciones, simplificando la instalación en entornos de Red de Área Local (LAN).

**b)**
La Ley de Snell establece que al propagarse un rayo de luz entre dos medios con diferentes índices de refracción n1 y n2, los ángulos de incidencia (θ1) y refracción (θ2) están relacionados mediante la expresión:

<p align="center">
n1 sin(θ1) = n2 sin(θ2)
</p>

En el contexto de la fibra óptica, el núcleo presenta un índice de refracción n1 mayor que el del revestimiento n2. Esta diferencia permite que, para ángulos de incidencia superiores al ángulo crítico, se produzca reflexión total interna en la interfaz núcleo-revestimiento, fenómeno que garantiza que la luz permanezca confinada dentro del núcleo durante su propagación, minimizando pérdidas y atenuación.
- En fibra de modo único (single-mode), el diámetro reducido del núcleo limita la propagación de la luz a una única trayectoria que cumpla la condición de reflexión total interna. La Ley de Snell determina el ángulo crítico que permite que este único modo se mantenga estable, evitando interferencias entre trayectorias.
- En fibra multimodo (multimode), el mayor diámetro del núcleo admite múltiples ángulos de incidencia que satisfacen la condición de reflexión total interna, posibilitando la propagación simultánea de varios modos. Cada modo corresponde a un ángulo distinto dentro de los límites establecidos por la Ley de Snell, lo que genera múltiples trayectorias de luz dentro del núcleo.
Es decir, la Ley de Snell ayuda a determinar la cantidad de modos de propagación que puede soportar una fibra óptica, siendo un factor crítico para el diseño y la aplicación de fibras de modo único o multimodo en sistemas de comunicación.

**c)**
Las conexiones inalámbricas y las transmisiones por fibra óptica representan dos enfoques distintos para la transmisión de datos, pero comparten principios fundamentales de comunicación digital. Ambas utilizan señales moduladas para transportar información, dependen de protocolos de capa física y enlace de datos, y buscan maximizar el throughput minimizando errores y latencia.

En este sentido, la fibra óptica actúa como backbone o columna vertebral de la red, proporcionando alta capacidad, baja latencia y gran estabilidad, aunque con un costo elevado. Las conexiones inalámbricas, en cambio, permiten movilidad, flexibilidad y acceso sin cables, pero suelen tener mayor latencia, menor throughput y mayor sensibilidad a interferencias, lo que limita su desempeño en enlaces de larga distancia o de alta capacidad.

En la práctica, las redes modernas combinan ambos enfoques: la fibra garantiza la robustez y capacidad del enlace troncal hasta los puntos de distribución, mientras que la conexión inalámbrica permite que los usuarios finales accedan a la red de forma flexible y sin cables. Esta combinación refleja un compromiso entre desempeño, costo y movilidad en el diseño de sistemas de comunicación de datos.

### 3)

**a)**

| Protocolo | ¿Está estandarizado?  Si/No   | Si aplica: ¿Cuál(es) estándares? (si tiene varios, mencionar la última versión) |
|-----------|------------------------------|----------------------------------------------------------------------------------|
| Wi-Fi    | Sí                           | IEEE 802.11be (Wi-Fi7)                                                            |
| Bluetooth | Sí                           | Bluetooth 6.0                                                     |
| Zigbee    | Sí                           | ZigBee PRO (basado en IEEE 802.15.4)                                             |
| NFC       | Sí                           | NFC Release 15                                                        |
| LTE      | Sí                           | 3GPP Release 18                                            |
| GSM      | Sí                           | 3GPP Release 18                                                            |
| 5G       | Sí                           | 3GPP Release 18                                                            |
| LoRa      | Sí                           | LoRaWAN v1.1.0                                                            |
| NB-IoT   | Sí                           | 3GPP Release 18                                                            |
| SigFox    | No                           | -                                                             |
| Z-Wave    | Sí                           | Z-Wave 800 Series                                                            |


**b)**

<p align="center">
<img width="650" height="381" alt="image" src="https://github.com/user-attachments/assets/c95bf077-92fd-4603-8583-4829cab92c55" />
</p>

**c)**

| Característica    | UTP |  Fibra Óptica  | Wi-Fi 802.11be  |  Bluetooth 5.4  |  5G    |
|------------------|-----|----------------|-----------------|-----------------|--------|
| Ancho de Banda   | ~40 Gbps | ~1 Tbps   | ~46 Gbps        | ~2 Mbps        | ~20 Gbps |
| Distancias       | ~100m/segmento | ~cientos de Km     | ~200 m          | ~240 m       | ~20 km |
| Inmunidad a EMI/RFI | Baja | Muy Alta           | Media           | Baja            | Media Alta   |
| Costos de medios/conectores/dispositivos | Bajo | Alto               | Medio           | Muy Bajo            | Alto   |
| Disponible en Packet Tracer | Sí  | Sí             | Sí              | No              | No     |

## 4)

**a)**
Existen dos tecnologías principales que permiten la conexión a internet y la comunicación con tierra desde una avión.
- Air-to-Ground (A2G): Esta tecnología proporciona conectividad del vehículo aéreo con la red terrestre mediante estaciones base en la tierra. Estas estaciones reciben y transmiten datos a la aeronave y viceversa.
El avión o dron detecta el área de cobertura donde se encuentra y puede comunicarse con el sistema de antenas terrestres como lo muestra la figura siguiente:

<p align="center">
<img width="539" height="241" alt="image" src="https://github.com/user-attachments/assets/2460fac4-317d-497b-9ca0-c2157a5ef74a" />
</p>

La arquitectura del sistema está compuesta por tres bloques: las Estaciones de Aeroneave, Estaciones Terrestres (base), y la Core Network que puede ser Internet, o alguna red específica, conectadas por backhaul que depende de la tecnología de A2G.
Las estaciones de aeronave son un receptor y transmisor y receptor de radio, y un sistema de red local que gestiona los sistemas de entretenimiento a bordo. Las estaciones terrestres son torres de comunicación, similares a las celulares, con la diferencia de que sus transmisores se dirigen hacia arriba y se ubican a distancias mucho mayores (entre 50Km y 150Km).
La tecnología A2G está actualmente en constante evolución. Un ejemplo de esto es la problemática de A2G basado en LTE en relación a la velocidad de las aeronaves (efecto doppler) al intentar usar antenas LTE para el sistema, ya que las subportadoras de LTE tienen frecuencias muy cercanas y el efecto doppler causado por la alta velocidad del avión genera un corrimiento en la frecuencia que induce errores en la comunicación. 
Esta tecnología tiene como ventaja la velocidad de transmisión de datos, y como desventaja el factor geográfico.

- Satelital: La tecnología satelital proporciona conectividad a bordo del avión mediante la comunicación entre el aeroneave y satélites en órbita. Existen dos principales tipos según la distancia de satélites: Geoestacionarios (GEO), ubicados a unos 36.000Km de la Tierra, ofrecen cobertura amplia con antenas de gran potencia pero latencia alta por la distancia. Y los satélites de Órbita Baja (LEO) operan entre 500 y 2.000 km de altura. Presentan menor latencia que los GEO pero requieren una estructura de varios cientos o miles de satélites.
	La arquitectura está formada por La estación de aeronave, Enlace Satelital, Gateway terrestre y Core Network 	mediante backhaul. Cuando la estación de aeronave transmite mediante el enlace satelital, el satélite 	    retransmite a una estación en tierra.
Las ventaja de este sistema es la cobertura global, sin importar el terreno (océanos, zonas polares, etc.) y la desventaja es la complejidad del sistema y la latencia.

<p align="center">
<img width="343" height="314" alt="image" src="https://github.com/user-attachments/assets/9cd4151f-639b-4e29-9d64-b448a578cd4d" />
</p>

**b)**
En el siguiente paper publicado el 27 de Agosto de 2025 se aborda el tema de la calidad de un sistema A2G donde hay múltiples usuarios, múltiples antenas, y se utiliza NOMA (Non Orthogonal Multiple Access). En este contexto, se compara la calidad con respecto a la utilización de OMA. 
La diferencia entre ambos estándares es la forma en la que los usuarios (aeronaves en este caso) interactúan con los paquetes. En un sistema basado en OMA, los usuarios distinguen sus señales por cambios de frecuencia, tiempo y código. En un sistema NOMA, todos los usuarios reciben la misma señal, pero a diferentes potencias, dependiendo de la distancia o “debilidad” del canal.
https://arxiv.org/pdf/2508.20003[Paper]

**c)**
Aunque al usuario le parezca que interactúa con una única red, en realidad en el avión hay dos redes, que pueden ser separadas virtualmente: la LAN, con un servidor dedicado que hostea todos los servicios a bordo, y la WAN mediante A2G o satélite (como se vió en los incisos anteriores) que ofrece conectividad a internet. Esta última es limitada en ancho de banda y velocidad, y el proveedor suele cobrar el acceso y limita el volumen de datos.
Para dividir el flujo de los datos se utiliza segmentación y ruteo: el servidor dedicado se encuentra en la red local y utiliza una IP privada accesible por los usuarios, y un gateway para el flujo hacia afuera (internet).
Para que se respete la política de esta división, se suele utilizar un portal cautivo que redirige todo el tráfico a una dirección de autenticación, donde el usuario debe pagar o solo usar la red local para acceder al contenido.
El portal cautivo puede ser implementado en el servidor dedicado o en un firewall que controle el acceso a la WAN. En este último caso, el firewall inspecciona los paquetes y bloquea cualquier intento de acceder a internet sin autenticación previa.

---

### Referencias

[1] <https://pxcom.aero/atg-connectivity-tech-challenging-satellite-dominance/>  
[2] <https://tec.gov.in/public/pdf/Studypaper/DA2GC_Paper%2008-10-2020%20v2.pdf/>  
[3] [Stallings - Comunicaciones y Redes de Computadores 7ed](https://drive.google.com/file/d/14wtpr0_eigALENVraeLnF5faYEM4aQB9/view?usp=drive_link)  
