# Trabajo Practico N1 - Repaso de fundamentos e introducción a Packet Tracer
**Integrantes**
---
- **Emiliano Castro**
- **Marcos Nieto**
- **Priscila Martinez**

---
## Desarrollo

### 1)

- **b)**

Si consideramos que la onda viaja a la velocidad de la luz y la longitud de onda, que es la distancia que recorre la misma en un ciclo, según la imagen tiene un valor de 60 [mm] (o $60x10^{-3}$ [m]), entonces tenemos:

<p align="center">$f [Hz] = \frac{c}{\lambda} = \frac{3x10^8 [m/s]}{60x10^{-3} [m]} = 5x10^9 [Hz] = 5 [GHz]$</p>

- **c)**

La onda electromagnética está dentro de las Microondas, que a su vez pertenecen a la región de radiofrecuencia (RF). Así mismo, pertenece a las bandas SHF (en inglés: Super High Frequency), que abarcan desde los 3 [GHz] hasta los 30 [GHz].

- **d)**

Las bandas SHF son ampliamente utilizadas en dispositivos de comunicación y detección. Por ejemplo: radares, satélites, celulares y hasta routers que hoy en día es común que manejen la banda de 5 [GHz].

- **e)**

La línea de trazos rojos representa la atenuación de las ondas electromagnéticas, es decir, la pérdida de energía que sufren las mismas al propagarse por un medio. Esto se debe a la absorción del medio, la dispersión al encontrarse con partículas y reflexión y desviación al toparse con obstáculos.



- **f)**

En el caso de los routers, propuesto como ejemplo en puntos anteriores, es afectado por la atenuación y se puede apreciar claramente este fenómeno. Cotidianamente podemos comprobar que la banda de 5 [GHz] que tienen los routers tiene un alcance bastante menor que la de 2.4 [GHz] debido a este fenómeno.

- **g)**

  - **i)**
Si, afecta notablemente las transmisiones de telefonía celular. Por ejemplo, si estamos en edificios o sótanos la señal se atenúa debido a la distancia y obstáculos. Por eso mismo, las torres de telefonía celular deben estar relativamente cerca unas de otras y usar amplificadores o repetidores.

  - **ii)**
También son afectados pero de diferente manera. La señal es atenuada por la resistencia del conductor y las pérdidas dieléctricas del aislamiento. Debido a esto, también se tienen que usar amplificadores y repetidores, especialmente en cables largos.

  - **iii)**
La atenuación todavía existe porque la fibra óptica usa la luz, que no es más que una onda electromagnética. Sin embargo, el efecto es mucho menor que en el caso del cable coaxial o la transmisión por aire. La luz sólo se debilita ligeramente por absorción y dispersión en el vidrio de la fibra. Por eso, la fibra permite transmitir datos a largas distancias sin perder calidad. Aunque en distancias demasiado largas, también se usan amplificadores ópticos.

---
### 2)

- **a)**
En el gráfico propuesto, se quiere representar un tipo de transmisión serial (los bits se envían uno tras otro por un solo canal) en un modo de transmisión síncrona (porque el receptor usa el reloj para leer cada bit en el momento exacto).

- **b)**
No es la mejor opción para una transmisión bidireccional, ya que se trata de una comunicación en modo simplex. En este caso, lo mejor sería una comunicación del tipo half-duplex o full-duplex.

- **c)**
La letra a representar es la “k” que en código ASCII es el 107 y en binario 01101011. Entonces la señal se vería así:
<p align="center">
  <img width="734" height="174" alt="image" src="https://github.com/user-attachments/assets/d382f6af-60a9-4a86-a865-79cc324e2db1" />
</p>


- **d)**

Mediríamos la señal, de acuerdo al ejemplo, en el instante T4. Es decir, en flancos descendentes de clock.

### 3)

- **a)**

Se está representando una técnica de modulación PSK (Phase Shift Keying), que consiste en la transmisión de información a través del cambio de fase de la onda portadora.

- **b)**
<p align="center">
<img width="596" height="116" alt="image" src="https://github.com/user-attachments/assets/7a4cf633-f88e-415a-964b-c7e4f601291b" />
</p>

- **c)**

Si nos basamos en técnicas de modulación con el mismo principio (cambio de algún parámetro de la onda portadora), también tenemos: ASK (modulación por amplitud), FSK (modulación por frecuencia) y QAM (modulación por amplitud y fase).

- **d)**

El BER es la tasa de error de bits, es decir, la proporción de bits que se reciben incorrectamente respecto a los bits transmitidos.
<p align="center">$BER = \frac{\text{Número de bits erróneos}}{\text{Número total de bits transmitidos}}$</p>

Es una tasa que indica la fiabilidad de la transmisión. Mientras más bajo sea, mejor es la técnica de modulación frente al ruido e interferencias.
Dadas las técnicas de modulación mencionadas anteriormente, si nos basamos en un mínimo BER y máxima robustez, la que mejor prestaciones tiene es la PSK.

---

### 4)

- **c)**

El router opera en la frecuencia 2.412 GHz, que corresponde al canal 1. Trabaja en la banda 2.4 Ghz, que pertenece a la zona del espectro electromagnético de ondas de radio, denominado UHF (Ultra High Frequency).

<p align="center">
<img width="612" height="245" alt="image" src="https://github.com/user-attachments/assets/a9d333ad-3194-4305-983f-a10505ef083d" />  
</p>

- **g)**

En este paso se realizaron pruebas para confirmar la conectividad de los dispositivos en la red.
- **ping** desde PC a laptop:

<p align="center">
<img width="577" height="192" alt="image" src="https://github.com/user-attachments/assets/325024bb-4891-4daa-a42e-9c9682c5863d" />
</p>

- **ping** desde Laptop a PC:

<p align="center">
<img width="582" height="183" alt="image" src="https://github.com/user-attachments/assets/6cfb57d9-d6ae-4fe2-a421-a4d46a273f8a" />
</p>

- **Trace route**  desde Laptop a PC
Se puede observar que no hubo saltos porque la red es local y solo tiene un router.

<p align="center">
<img width="587" height="135" alt="image" src="https://github.com/user-attachments/assets/718681c3-c4b9-4ccd-9101-5ee38a1b54c0" />
</p>

- **h)**
En este paso, el objetivo es visualizar la latencia y características de la conectividad cuando la Laptop se encuentra a distintas distancias respecto del router.
Como la densidad de potencia de la onda electromagnética que irradia el router es inversamente proporcional al cuadrado de la distancia, la Laptop dejará de detectar la señal en esa proporción. Esto se puede observar realizando un `ping` a distintas distancias desde el router:


**Primera Prueba** (Dentro de la zona de alcance):

<p align="center">
<img width="606" height="239" alt="image" src="https://github.com/user-attachments/assets/dc3c9575-f88a-4d75-8ddc-ee30b1c0ae5a" />
</p>

**Segunda Prueba** (Fuera de la zona de alcance):
En este caso el `ping` devuelve un “Request timed out”, ya que la Laptop deja de estar conectada a la red.

<p align="center">
<img width="603" height="239" alt="image" src="https://github.com/user-attachments/assets/b7935049-906a-4d7a-8302-179bec7ecbb6" />
</p>  
