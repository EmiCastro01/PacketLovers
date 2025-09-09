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

---

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

### **a)**

En la figura se representa el efecto Doppler, un fenómeno físico que se produce cuando existe movimiento relativo entre un emisor, receptor o ambos. Gráficamente, se observa cómo la longitud de onda o frecuencia de la señal electromagnética que envía el barco es percibida de manera distinta por el satélite debido al fenómeno.
Algunas características de este fenómeno son:

- Se manifiesta en todo tipo de ondas.
- La velocidad de propagación de la onda no cambia, ya que depende solo del medio.
- La frecuencia percibida aumenta si el emisor y el receptor se acercan y disminuye si se alejan.
- La variación de la frecuencia percibida depende de la velocidad relativa y de la frecuencia emitida.


### **b)**

Considerando lo estudiado en el laboratorio anterior, el efecto doppler afecta mayormente a las bandas de transmisión que trabajan a frecuencias altas (UHF, SHF, EHF). Esto se debe a que la variación de frecuencia producida por el efecto doppler es proporcional a la frecuencia de la portadora. Por lo tanto, a frecuencias elevadas, el cambio en la frecuencia es más significativo, lo que puede provocar pérdida de sincronización o interferencias. Por otro lado, las transmisiones más resilientes son las que operan a frecuencias medias/bajas (LF, MF, HF), en estas el efecto Doppler tendría un impacto menor.

**c)**

Entre las principales razones por las cuales no se debe encender un celular en un avión se encuentra que el dispositivo está constantemente buscando señal y tratando de conectarse a varias antenas a la vez. Esta actividad puede generar interferencias electromagnéticas que afectan los sistemas de navegación y comunicación del avión, especialmente durante fases delicadas como despegue y aterrizaje.

Si bien el efecto Doppler está presente debido al movimiento del avión y puede modificar ligeramente la frecuencia percibida de las señales entre el avión y las antenas, este fenómeno no es la causa principal de la prohibición del uso de celulares. El riesgo se centra principalmente en la posibilidad de que las señales emitidas por múltiples dispositivos interfieran con los equipos electrónicos sensibles del avión.

---
### 2)
### **a)**

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

### **b)**

Considerando las bandas de transmisión estudiadas en el laboratorio anterior, el efecto del ruido impulsivo varía significativamente según la frecuencia:

Bandas de baja frecuencia (LF, MF, HF): Estas bandas son altamente susceptibles al ruido impulsivo. Las ondas largas se ven afectadas por descargas atmosféricas y chispas de equipos eléctricos, que generan ruido de banda ancha. En estas frecuencias, el ruido impulsivo suele ser la principal causa de degradación de la señal, superando al ruido térmico.

Bandas de alta frecuencia (VHF, UHF, SHF, EHF): A medida que aumenta la frecuencia, el impacto del ruido impulsivo de fuentes terrestres (como taladros o motores) disminuye debido a la mayor atenuación de las ondas y a la menor propagación del ruido. En estas bandas, el principal factor limitante es el ruido térmico generado por los componentes del receptor, aunque pueden presentarse interferencias locales de fuentes impulsivas cercanas, como routers Wi-Fi o dispositivos Bluetooth.

En resumen, las bandas bajas son más vulnerables al ruido impulsivo, mientras que las bandas altas son más resilientes, aunque aún pueden verse afectadas por interferencias locales.

### **c)**



La Relación Señal a Ruido (SNR, Signal-to-Noise Ratio) es un cociente adimensional que mide la potencia de una señal deseada en relación con la potencia del ruido de fondo. Se calcula mediante la fórmula:

<p align="center">$\text{SNR} = \frac{P_{\text{señal}}}{P_{\text{ruido}}}$</p>

Una SNR elevada indica que la señal es significativamente más potente que el ruido, lo que se traduce en una mayor calidad de transmisión.

La SNR está directamente relacionada con la Tasa de Error de Bit (BER, Bit Error Rate), que se define como:

<p align="center">$\text{BER} = \frac{\text{Número de bits erróneos}}{\text{Número total de bits transmitidos}}$</p>


Cuando la SNR es alta, el receptor puede distinguir correctamente los bits, resultando en una BER baja. Por el contrario, si la SNR disminuye (es decir, aumenta el ruido relativo), la probabilidad de errores en la decodificación de bits se incrementa, aumentando la BER.

En resumen, existe una relación inversa entre SNR y BER: a mayor SNR, menor BER. Esta relación es fundamental en el diseño de sistemas de comunicación confiables, ya que permite establecer límites sobre la tasa de error para un determinado nivel de potencia de señal y ruido.

