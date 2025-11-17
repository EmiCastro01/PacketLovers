# Trabajo Práctico N°4

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

## Desarrollo

### 1) Alcance de Redes y Virtualización

### **a)** Las redes se clasifican según su alcance en:
 
| **Nombre** | **Acrónimo** | **Alcance aproximado** | **Características principales** | **Ejemplo de uso** |
|-------------|---------------|------------------------|---------------------------------|--------------------|
| **Personal Area Network** | **PAN** | Hasta 10 m | Conecta dispositivos personales cercanos por cable o de forma inalámbrica. Posee bajo consumo energético y sencilla configuración, aunque es vulnerable a interferencias. Ofrece buena velocidad de transferencia y gran portabilidad. | Conexiones USB, NFC o Bluetooth, como entre un celular y un auricular. |
| **Local Area Network** | **LAN** | Hasta 1 km | Conecta varios equipos dentro de un mismo edificio o instalación. Ofrece gran velocidad de transmisión y baja latencia. Puede ser cableada mediante Ethernet o inalámbrica con Wi-Fi, siendo una red estable y de bajo costo de mantenimiento. | Se utiliza para enlazar computadoras y periféricos en hogares, oficinas o aulas. |
| **Campus Area Network** | **CAN** | Hasta 10 km | Interconecta múltiples redes LAN dentro de un área común. Ofrece alta velocidad y baja latencia mediante el uso de fibra óptica, Ethernet y Wi-Fi. Su conectividad centralizada facilita la administración, seguridad y acceso compartido. | Se aplica en redes universitarias o industriales que unen diferentes edificios o laboratorios. |
| **Metropolitan Area Network** | **MAN** | Entre 1 y 50 km | Une varias redes LAN dentro de una ciudad o zona metropolitana. Utiliza fibra óptica y enlaces inalámbricos de alta capacidad para ofrecer gran velocidad, ancho de banda y fiabilidad. Además, permite acceso remoto y gestión compartida de recursos. | Conexión de diferentes sucursales de una empresa o instituciones dentro de una misma ciudad. |
| **Wide Area Network** | **WAN** | Más de 100 km | Conecta redes LAN y MAN en distintos países o continentes. Ofrece alta capacidad de transferencia de datos y fiabilidad gracias al uso de fibra óptica, Internet y satélites. Su implementación es más costosa y compleja, pero brinda gran alcance y flexibilidad. | Se utiliza en redes bancarias o de empresas internacionales que operan en distintos países. |

### **b)** Redes VLAN (Virtual Local Area Network) 

Una VLAN es una red lógica o virtual que permite dividir una red LAN física en varios grupos independientes, manteniendo la misma infraestructura. Su función principal es separar y organizar el tráfico de red entre distintos departamentos, usuarios o servicios, sin necesidad de instalar más hardware. Por ejemplo, en lugar de crear varias redes físicas con diferentes switches, una VLAN permite que un solo switch actúe como varios virtuales, cada uno con su propio dominio de transmisión.

Gracias a esta segmentación, las VLAN mejoran el rendimiento, la seguridad y la administración de la red, evitando que la información llegue a equipos no autorizados y reduciendo el tráfico. Además permiten una gestión más flexible y escalable, ya que los dispositivos pueden pertenecer a diferentes redes lógicas sin importar su ubicación física. 

Las VLAN pueden clasificarse según dos criterios principales:

**Por su función:**

- **VLAN de datos:** Transporta el tráfico generado por los usuarios, como PCs, impresoras o clientes de red. Se utiliza para separar el tráfico de voz y de administración, manteniendo organizado el flujo de datos de los grupos de trabajo. Es común en entornos corporativos.

- **VLAN predeterminada:** Es la VLAN activa cuando el switch arranca con su configuración de fábrica. Todos los puertos pertenecen inicialmente a esta VLAN, permite comunicación inmediata entre dispositivos conectados. En switches Cisco corresponde a la VLAN 1, que no puede eliminar ni renombrar y transporta tráfico de control de capa 2 por defecto.

- **VLAN nativa:** Es la VLAN asignada a los puertos troncales (802.1Q) para recibir tráfico que llega sin etiqueta VLAN. Su función es mantener compatibilidad con dispositivos o situaciones donde no se utiliza etiquetado. Por defecto suele ser la VLAN 1, aunque por motivos de seguridad se recomienda utilizar una VLAN distinta y dedicada exclusivamente a este rol.

- **VLAN de administración:** Esta destinada exclusivamente a la gestión del switch y otros dispositivos de red mediante protocolos como HTTP, Telnet, SSH o SNMP. De forma predeterminada, la VLAN 1 suele actuar como VLAN de administración, pero no se recomienda utilizarla por motivos de seguridad. Por ello, es una práctica común crear una VLAN específica y separada para la administración remota.

**Por su método de asignación o configuración:**

- **VLAN por puerto:** Se basa en asociar cada puerto físico del switch a una VLAN determinada. De modo que, cualquier dispositivo que se conecte a un puerto del switch pasa a formar parte de una VLAN configurada para dicho puerto. Es una asignación sencilla y extendida, común en switches de gama baja y tiene la desventaja de que si un usuario cambia de puerto podría quedar en otra VLAN, lo que obliga a reconfigurar.

- **VLAN por dirección MAC:** En este caso, la asignación se hace según la dirección MAC del dispositivo. Esto permite movilidad sin modificar la configuración del switch, ya que el dispositivo conservará su VLAN sin importar a que puerto se conecte. Ofrece gran flexibilidad, pero exige un control constante de las direcciones MAC, por eso se suele implementar en switches de gama alta.

- **VLAN por protocolo:** Aquí la VLAN se determina analizando el protocolo de capa 3 presente en la trama (por ejemplo IPv4, IPv6, IPX, etc). Esto permite que distintos servicios o aplicaciones operen en redes lógicas separadas sobre la misma infraestructura física. Es útil cuando conviven varios protocolos, pero requiere hardware avanzado y es menos común debido a su complejidad y a la estandarización del uso de IP.

- **VLAN por subred:** Utiliza la información de la cabecera IP para decidir a qué VLAN se envían paquetes. A diferencia de otros métodos, la clasificación se realiza por tráfico y no por dispositivos, de modo que un mismo dispositivo podría generar paquetes destinados a distintas VLAN si utiliza múltiples subredes. Es una técnica avanzada y poco frecuente por su complejidad y fuerte dependencia del direccionamiento IP.


### **c)** Protocolo IEEE 802.1Q.

IEEE 802.1Q es un estándar que define cómo se agregan etiquetas (tags) dentro de una trama Ethernet para identificar redes lógicas. Su función principal es proporcionar un método común que permita que varias redes convivan en la misma infraestructura física sin interferencias, evitando incompatibilidades entre switches de distintos fabricantes.
Las redes VLAN dependen directamente del protocolo IEEE 802.1Q, porque es el mecanismo que hace posible que las VLAN funcionen más allá de un solo switch. Permite que los switches inserten, reconozcan y procesen una etiqueta que incluye, entre otros campos, un Identificador de VLAN (VLAN ID) de 12 bits que permite:

- Identificar a qué VLAN pertenece cada trama, incluso cuando varias VLAN comparten el mismo enlace físico.

- Extender una misma VLAN entre múltiples switches manteniendo su separación lógica.

- Operar enlaces troncales (trunks) que transportan simultáneamente tráfico de varias VLAN.

- Definir una VLAN nativa para el tráfico sin etiquetar.

- Preservar el aislamiento entre dominios de broadcast.

- Implementar segmentación y políticas de seguridad diferenciadas (voz, datos, administración, invitados, etc.)

### **d)** Tagging

El tagging es el proceso que consiste en introducir mediante el protocolo IEEE 802.1Q una etiqueta de 4 bytes dentro de la trama Ethernet para indicar a qué VLAN pertenece un paquete. Esta etiqueta se coloca entre las direcciones MAC y el campo Type/Length, con la siguiente estructura:

[ TPID | PCP | DEI | VLAN ID ]

- TPID (Tag Protocol Identifier): identifica que la trama usa 802.1Q.
- PCP (Priority Code Point): define la prioridad del tráfico (QoS).
- DEI (Drop Eligible Indicator): marca si la trama puede descartarse en caso de congestión.
- VLAN ID: indica a qué VLAN pertenece la trama (valor de 12 bits).

Al configurar VLAN en un switch, cada puerto trata estas etiquetas de manera distinta:

- Los puertos tagged conservan la etiqueta y transportan múltiples VLAN a la vez, típicamente en enlaces trunk entre switches, routers o AP.
- Los puertos untagged eliminan la etiqueta, dejando la trama limpia para dispositivos finales que trabajan en una única VLAN.

Gracias al tagging, las VLAN pueden coexistir en la misma infraestructura preservando la segmentación y el aislamiento a lo largo de toda la red.

---

### 2)  Considerando la siguiente topología en Packet-Tracer:

<p align="center">
<img width="562" height="106" alt="imagen1" src="https://github.com/user-attachments/assets/c2fea5b3-1601-4f29-acf0-e3a5b19c09b5" />
</p>

### **a)**
Se cambió el nombre de cada switch usando el comando hostname, con el fin de identificarlos facilmente durante las configuraciones:

<p align="center">
<img width="944" height="92" alt="imagen2" src="https://github.com/user-attachments/assets/d6c1dc33-f8d2-45fc-9482-3c0058259cc1" />
</p>

### **b)**
Se definieron las contraseñas de modo privilegiado, consola y vty, con el objetivo de proteger el acceso de cada switch y garantizar que solo usuarios autorizados puedan realizar configuraciones.

<p align="center">
<img width="743" height="193" alt="imagen 3" src="https://github.com/user-attachments/assets/77e3c07c-2f07-44e5-be91-22a00c089e27" />
</p>

### **c)**
Se encriptaron las contraseñas configuradas.

<p align="center">
<img width="788" height="41" alt="imagen4" src="https://github.com/user-attachments/assets/d0e41c12-82aa-4eef-871e-5336cca28e66" />
</p>

### **d)**
Se configuró la red VLAN1 para cada switch asignándole la dirección IP y máscara según la tabla de ruteo.

<p align="center">
<img width="663" height="194" alt="imagen5a" src="https://github.com/user-attachments/assets/1ceb06d3-cccf-4d00-9404-c391340bec38" /> <img width="663" height="196" alt="imagen5b" src="https://github.com/user-attachments/assets/a0046339-325f-4785-bfde-9f491d060620" />
</p>

### **e)**
Se utilizó `show ip interface brief` para identificar qué puertos estaban activos en cada switch y se verificó con la topografía.

<p align="center">
<img width="589" height="466" alt="imagen6" src="https://github.com/user-attachments/assets/b9f22324-2d7c-4fcb-b07c-ddc4b9d9ae99" />
<img width="590" height="464" alt="imagen6b" src="https://github.com/user-attachments/assets/de00878f-6c91-42a6-860d-1c827de38e32" />
</p>

Tras verificar el estado de las interfaces, se seleccionaron las que no estaban en uso y fueron deshabilitadas, dejando activos únicamente los puertos necesarios.

<p align="center">
<img width="426" height="549" alt="imagen7a" src="https://github.com/user-attachments/assets/cecc7817-1dbc-49c0-b26d-4b325a8d13b5" />
<img width="426" height="549" alt="imagen7bbb" src="https://github.com/user-attachments/assets/eef6f4f1-5bfa-4405-ad8f-d90a8d80d7a9" />
</p>

### **f)**
Finalmente, se guardaron los cambios realizados utilizando el comando `write memory`.

<p align="center">
<img width="762" height="111" alt="imagen8" src="https://github.com/user-attachments/assets/384775fb-cb6c-4cd2-93e2-539ab04ee5ed" />
</p>

### **g)**
Se verificó la comunicación entre las computadoras usando pings.

<p align="center">
<img width="407" height="198" alt="imagen9" src="https://github.com/user-attachments/assets/eea5ca31-59e5-4567-9e41-db99b199441d" />
</p>

### **h)**
Se crearon las VLAN 10, 20 y 99 en ambos switches, asignando los nombres `Laboratorio`, `Bar` y `Management` respectivamente.

<p align="center">
<img width="966" height="206" alt="imagen10" src="https://github.com/user-attachments/assets/aaa821d7-706c-4e46-b64b-44a1e207aa77" />
</p>

### **i)**

Con el comando `show vlan brief` se visualizó la tabla de VLAN configuradas, donde se observó que la VLAN por defecto corresponde a la VLAN 1.

<p align="center">
<img width="660" height="330" alt="imagen11" src="https://github.com/user-attachments/assets/f6a0d034-7209-43cd-a63c-0b45fec00e63" />
</p>

### **j)**
Se configuró el puerto F0/6 del sw-1 en modo access y se lo asignó a la VLAN 10 para vincular la PC-A con la VLAN Laboratorio.

<p align="center">
<img width="506" height="122" alt="imagen12" src="https://github.com/user-attachments/assets/f2f2f6a9-a6ec-4712-ab1c-c7b3cd01ca3b" />
</p>

### **k)**
Se retiró la dirección IP previamente asignada a la VLAN 1 y se configuró la interfaz VLAN 99 como nueva VLAN de administración.

<p align="center">
<img width="456" height="205" alt="imagen13" src="https://github.com/user-attachments/assets/a563b949-4665-4ff0-9758-70977b1c433f" />
</p>

### **l)**
Se ejecutaron los comandos `show vlan brief` y `show ip interface brief` para verificar la asignación de puertos a cada VLAN y el estado general de las interfaces. 

<p align="center">
<img width="667" height="300" alt="imagen15" src="https://github.com/user-attachments/assets/1c6cc503-4db1-4e1e-8ac3-511ce44ab51d" />
</p>

Mediante `show vlan brief` se observó:
- La VLAN1 por defecto contiene todos los puertos que no se asignaron
- La VLAN 10 (laboratorio) aparece correctamente configurada y con el puerto Fa0/6 asignado, que es donde se encuentra la PC-A.
- La VLAN 20 (bar) aparece como creada correctamente y sin puertos asociados.
- La VLAN 99 (management) aparece configurada y activa pero sin puertos de acceso asociados.
- Además se muestran las VLANS 1002-1005, que son las VLANs reservadas por Cisco, estas siempre aparecen en estado activa y no deben modificarse.

<p align="center">
 <img width="584" height="472" alt="imagen16" src="https://github.com/user-attachments/assets/8773974f-3c54-4258-ac41-bb415f6ac062" />
</p>

Al ejecutar `show ip interface brief` en el sw-1 aparecen:

- Los puertos apagados manualmente (administratively down) que fueron desactivados anteriormente.
- El puerto Fa0/1 con estado up/up que indica que el enlace físico entre los switches está activo y funcionando.
- El puerto Fa0/6 tiene como estado up/up lo que indica que la PC-A está conectada correctamente y con enlace activo.
- La interfaz VLAN1 aparece sin IP asignada, ya que se quitó previamente. Su estado up/up significa que la VLAN sigue activa porque todavía tiene puertos asociados (Fa0/1).
- La interfaz VLAN99 tiene como estado up/down, lo cual indica que la interfaz VLAN está habilitada, pero no tiene tráfico asociado porque aún no hay puertos que pertenezcan a esa VLAN.

### **m)**
Se configuró el sw-2 asociando la PC-B a VLAN 10 (laboratorio), se repitió la configuración de VLAN 99 y verificó la configuración con `show vlan brief`. 

<p align="center">
<img width="857" height="269" alt="imagen18" src="https://github.com/user-attachments/assets/c486eb36-9306-45c3-931b-c341ab6d26a6" />
</p>

### **n)**
Al hacer ping entre las PCs, se obtuvo lo siguiente:

<p align="center">
<img width="870" height="210" alt="imagen26" src="https://github.com/user-attachments/assets/dd7bdd39-e234-476c-8bf1-cbeef02f6c12" />
</p>

Aunque ambas estaban asociadas a la misma VLAN (laboratorio), la comunicación falló y en ambos casos se obtuvo como respuesta Request timed out. Debido a eso, se revisó la configuración de los switches con el comando show interfaces switchport y se observó que los puertos estaban funcionando en modo access.

El modo access, no etiqueta las tramas y solo transporta una única VLAN que por defecto es la VLAN nativa (VLAN1). Eso explica por qué aunque PC-A y PC-B estaban bien configuradas en VLAN 10, esa VLAN no viajaba entre los switches.

Para que se transporten todas las VLANs a través del enlace entre switches, es necesario configurarlos en modo trunk. Dicho modo permite que múltiples VLANs existan entre los switches y utiliza etiquetas 802.1Q para identificar a que VLAN pertenece cada trama. Para verificar esto, se reconfiguró cada switch y se probó nuevamente hacer pings entre las computadoras y switches.

<p align="center">
<img width="870" height="185" alt="imagen21" src="https://github.com/user-attachments/assets/5641013b-ff5d-4dfe-b6a9-b766c1535e9e" />
</p>

<p align="center">
<img width="870" height="309" alt="imagen25" src="https://github.com/user-attachments/assets/ff0b9596-7df0-4ad1-8248-eadc95617c1f" />
</p>

<p align="center">
<img width="870" height="87" alt="imagen24" src="https://github.com/user-attachments/assets/024eb452-2588-44a0-94a8-6d0845c9cecc" />
</p>

Ahora con el enlace trunk, la VLAN 10 del sw1 es la misma que la VLAN 10 del sw2, por lo que ya no estan aislados entre sí y las PCs pueden comunicarse correctamente. 

---

### 3) 

El objetivo principal de este inciso es separar accesos mediante VLANs. Para ello se crearon las siguientes:


- **VLAN 10**: Dispositivos de la clase Turista, solo acceso al servidor local.
- **VLAN 20**: Dispositivos de la clase Business, acceso al servidor local y a Internet.
- **VLAN 99**: PC del administrador. Acceso a todas las redes e internet.

Para la creación de este sistema, se eligió la topología sugerida:
<p align=center>
<img width="908" height="588" alt="Screenshot from 2025-11-16 18-15-02" src="https://github.com/user-attachments/assets/e09f6edb-727c-456a-a8b4-94116c9978b2" />
</p>
Para simular el ISP se utilizó un router con un Loopback a 8.8.8.8 (Simulando el servicio de DNS de Google)
Es decir, cuando una PC Business o Administrador acceden a “internet”, se están mandando paquetes al Loopback del router ISP.

## **Pasos para la creación y configuración del sistema**

Se utilizaron las direcciones sugeridas.

1. La conexión entre el switch SW y el router de la aeronave (R_Aircraft) se realizó con el puerto GigabitEthernet, ya que se usó un router más moderno que no tiene puerto de FastEthernet. Esto evita cuellos de botella con las salidas a internet, y prioriza la conexión principal antes que las individuales.

2. Se configuraron las VLANs en el switch. Los puertos del switch (FastEthernet0/2 - 8) Se configuraron como puertos de acceso con el comando `switchport mode access` asignados a su VLAN, según correspondiese la clase. El puerto GigabitEthernet0/1 se configuró como troncal con el comando `switchport mode trunk`.

3. En el Router de la aeronave (R_Aircraft) se crearon subinterfaces para cada VLAN (GigabitEthernet0/0.10-0.20-0.99) con el comando `encapsulation dot1Q [vlan]` para taggear el tráfico y siguiendo el protocolo IEEE 802.1Q. Luego se asignó la IP del gateway predeterminado a cada red.
Se configuraron Pools de DHCP en el router para determinar las IPs a cada VLAN. Para ello se estableció que IPs no repartir (usadas para los gateways y el servidor) con `ip dhcp excluded-address [ip_gateway][ip_server]`
Luego el armado de las pools:
```
ip dhcp pool [clase]
network [rango ]
default-router [gateway predeterminado de la red]
dns-server [dns]
```

En el caso de la pool de Turista, el servidor dns es el mismo server local. (10.10.99.10), y en el caso de las Business y Admin, el 8.8.8.8 (Loopback del ISP, simulando el servicio de DNS de Google).

4. Se implementó NAT para traducir las IPs privadas de Business y Admin a la pública del router. Se utilizan access lists (ACLs) identificando el tráfico que puede salir. Para que el tráfico permitido pueda salir a Internet, era necesarios estos pasos, con los siguientes comandos:
`access-list [nro clase] permit [ip clase] [máscara]`

De esta forma, Business y Admin tienen acceso a internet utilizando la IP pública del router (200.0.0.1), aplicando el comando `overload` para que el grupo de esas listas utilizaran la interfaz de salida con la misma IP.

5. Se estableció que interfaces son externas (Hacia el ISP) y cuales internas (VLANs) con `ip nat outside/inside`.

## **Funcionamiento y Pruebas de la red**

- <ins>Tabla de VLANs del switch</ins>
```

Switch>show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Fa0/1, Fa0/9, Fa0/10, Fa0/11
                                                Fa0/12, Fa0/13, Fa0/14, Fa0/15
                                                Fa0/16, Fa0/17, Fa0/18, Fa0/19
                                                Fa0/20, Fa0/21, Fa0/22, Fa0/23
                                                Fa0/24, Gig0/2
10   Turista                          active    Fa0/2, Fa0/3, Fa0/4
20   Business                         active    Fa0/5, Fa0/6
99   Admin                            active    Fa0/7, Fa0/8
1002 fddi-default                     active    
1003 token-ring-default               active    
1004 fddinet-default                  active    
1005 trnet-default                    active
```

- <ins>Verificaciones en el Router de la aeronave (R_Aircraft)</ins>

```
Router#show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol 
GigabitEthernet0/0     unassigned      YES unset  up                    up 
GigabitEthernet0/0.10  10.10.10.1      YES manual up                    up          
GigabitEthernet0/0.20  10.10.20.1      YES manual up                    up          
GigabitEthernet0/0.99  10.10.99.1      YES manual up                    up          
GigabitEthernet0/1     200.0.0.1       YES manual up                    up 
GigabitEthernet0/2     unassigned      YES unset  administratively down down 
Vlan1                  unassigned      YES unset  administratively down down
```
Se pueden observar las tres subinterfaces (0.10, 0.20 y 0.99) con sus respectivas IPs asignadas.
Además, se puede ver la interfaz GigabitEthernet0/1 con la IP pública.

```

Router#show ip route
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
       i - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area
       * - candidate default, U - per-user static route, o - ODR
       P - periodic downloaded static route

Gateway of last resort is 200.0.0.2 to network 0.0.0.0

     10.0.0.0/8 is variably subnetted, 6 subnets, 2 masks
C       10.10.10.0/24 is directly connected, GigabitEthernet0/0.10
L       10.10.10.1/32 is directly connected, GigabitEthernet0/0.10
C       10.10.20.0/24 is directly connected, GigabitEthernet0/0.20
L       10.10.20.1/32 is directly connected, GigabitEthernet0/0.20
C       10.10.99.0/24 is directly connected, GigabitEthernet0/0.99
L       10.10.99.1/32 is directly connected, GigabitEthernet0/0.99
     200.0.0.0/24 is variably subnetted, 2 subnets, 2 masks
C       200.0.0.0/30 is directly connected, GigabitEthernet0/1
L       200.0.0.1/32 is directly connected, GigabitEthernet0/1
S*   0.0.0.0/0 [1/0] via 200.0.0.2
```
Se puede observar el estado C (connected) de las subinterfaces y la ruta por defecto hacia el ISP.

```
Router#show access-lists
Standard IP access list 20
    10 permit 10.10.20.0 0.0.0.255
Standard IP access list 99
    10 permit 10.10.99.0 0.0.0.255
Extended IP access list 100
    10 permit udp any any eq bootps (6 match(es))
    20 permit udp any any eq bootpc
    30 permit ip 10.10.10.0 0.0.0.255 10.10.99.0 0.0.0.255
    40 permit ip 10.10.10.0 0.0.0.255 10.10.20.0 0.0.0.255
    50 deny ip 10.10.10.0 0.0.0.255 any

```
Las ACLs extendidas se utilizaron para establecer el permiso del tráfico udp para los puertos del servidor y cliente DHCP para que este funcionara correctamente. Inicialmente, sin estas configuraciones, el servicio DHCP no funcionaba. También se estableció el tráfico ip que venga de la VLAN turista hacia la admin, para los pings de prueba (necesario para que el ping a turistas respondan correctamente).
La última regla (50) es la negación al tráfico de la red turista a cualquier destino (`any`).

- <ins>Ping de PC Turista al Server Local</ins> 

```
C:\>ping 10.10.99.10

Pinging 10.10.99.10 with 32 bytes of data:

Reply from 10.10.99.10: bytes=32 time<1ms TTL=127
Reply from 10.10.99.10: bytes=32 time<1ms TTL=127
Reply from 10.10.99.10: bytes=32 time<1ms TTL=127
Reply from 10.10.99.10: bytes=32 time<1ms TTL=127

Ping statistics for 10.10.99.10:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms
```
- <ins>Acceso al Server Local con el Browser desde PC Turista</ins>

<p align=center>
<img width="690" height="714" alt="Screenshot from 2025-11-16 17-38-48" src="https://github.com/user-attachments/assets/9e7f79aa-21e6-4dae-b14e-f8d8478c9fa0" />
</p>
- <ins>Ping a Internet (`8.8.8.8`) desde PC Turista</ins>

```
C:\>ping 8.8.8.8

Pinging 8.8.8.8 with 32 bytes of data:

Reply from 10.10.10.1: Destination host unreachable.
Reply from 10.10.10.1: Destination host unreachable.
Reply from 10.10.10.1: Destination host unreachable.
Reply from 10.10.10.1: Destination host unreachable.

Ping statistics for 8.8.8.8:
    Packets: Sent = 4, Received = 0, Lost = 4 (100% loss),
```

- <ins>Acceso al server local con el Browser web (desde Business)</ins>
<p align=center>
<img width="690" height="714" alt="Screenshot from 2025-11-16 17-41-15" src="https://github.com/user-attachments/assets/1ee52b84-e961-42f7-902f-1ed9a0ee8d32" />
</p>

- <ins>Ping y tracert Internet (`8.8.8.8`) desde PC Business</ins>

```
C:\>ping 8.8.8.8

Pinging 8.8.8.8 with 32 bytes of data:

Reply from 8.8.8.8: bytes=32 time<1ms TTL=254
Reply from 8.8.8.8: bytes=32 time<1ms TTL=254
Reply from 8.8.8.8: bytes=32 time<1ms TTL=254
Reply from 8.8.8.8: bytes=32 time<1ms TTL=254

Ping statistics for 8.8.8.8:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms

C:\>tracert 8.8.8.8

Tracing route to 8.8.8.8 over a maximum of 30 hops: 

  1   0 ms      0 ms      0 ms      10.10.20.1
  2   0 ms      0 ms      0 ms      8.8.8.8

Trace complete.
```
Observar como el paquete pasa por el gateway de la red Business.

- <ins>Ping desde Admin a todas las redes</ins> 

```
C:\>ping 10.10.10.11

Pinging 10.10.10.11 with 32 bytes of data:

Reply from 10.10.10.11: bytes=32 time<1ms TTL=127
Reply from 10.10.10.11: bytes=32 time<1ms TTL=127
Reply from 10.10.10.11: bytes=32 time<1ms TTL=127
Reply from 10.10.10.11: bytes=32 time<1ms TTL=127

Ping statistics for 10.10.10.11:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms

C:\>ping 10.10.20.2

Pinging 10.10.20.2 with 32 bytes of data:

Reply from 10.10.20.2: bytes=32 time<1ms TTL=127
Reply from 10.10.20.2: bytes=32 time<1ms TTL=127
Reply from 10.10.20.2: bytes=32 time<1ms TTL=127
Reply from 10.10.20.2: bytes=32 time<1ms TTL=127

Ping statistics for 10.10.20.2:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms

C:\>ping 10.10.99.10

Pinging 10.10.99.10 with 32 bytes of data:

Reply from 10.10.99.10: bytes=32 time<1ms TTL=128
Reply from 10.10.99.10: bytes=32 time<1ms TTL=128
Reply from 10.10.99.10: bytes=32 time<1ms TTL=128
Reply from 10.10.99.10: bytes=32 time=1ms TTL=128

Ping statistics for 10.10.99.10:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 1ms, Average = 0ms

C:\>ping 8.8.8.8

Pinging 8.8.8.8 with 32 bytes of data:

Reply from 8.8.8.8: bytes=32 time<1ms TTL=254
Reply from 8.8.8.8: bytes=32 time<1ms TTL=254
Reply from 8.8.8.8: bytes=32 time<1ms TTL=254
Reply from 8.8.8.8: bytes=32 time<1ms TTL=254

Ping statistics for 8.8.8.8:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms
```


