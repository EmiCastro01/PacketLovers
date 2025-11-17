El objetivo principal de este inciso es separar accesos mediante VLANs. Para ello se crearon las siguientes:


- VLAN 10: Dispositivos de la clase Turista, solo acceso al servidor local.
- VLAN 20: Dispositivos de la clase Business, acceso al servidor local y a Internet.
- VLAN 99: PC del administrador. Acceso a todas las redes e internet.

Para la creación de este sistema, se eligió la topología sugerida:

[ IMAGEN DE LA TOPOLOGIA]

Para simular el ISP se utilizó un router con un Loopback a 8.8.8.8 (Simulando el servicio de DNS de Google)
Es decir, cuando una PC Business o Administrador acceden a “internet”, se están mandando paquetes al Loopback del router ISP.

## **Pasos para la creación y configuración del sistema**

Se utilizaron las direcciones sugeridas.

1. La conexión entre el switch SW y el router de la aeronave (R_Aircraft) se realizó con el puerto GigabitEthernet, ya que se usó un router más moderno que no tiene puerto de FastEthernet. Esto evita cuellos de botella con las salidas a internet, y prioriza la conexión principal antes que las individuales.

2. Se configuraron las VLANs en el switch. Los puertos del switch (FastEthernet0/2 - 8) Se configuraron como puertos de acceso con el comando switchport mode access asignados a su VLAN, según correspondiese la clase. El puerto GigabitEthernet0/1 se configuró como troncal con el comando switchport mode trunk.

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

De esta forma, Business y Admin tienen acceso a internet utilizando la IP pública del router (200.0.0.1), aplicando el comando overload para que el grupo de esas listas utilizaran la interfaz de salida con la misma IP.

5. Se estableció que interfaces son externas (Hacia el ISP) y cuales internas (VLANs) con ip nat outside/inside.

## **Funcionamiento y Pruebas de la red**

- Tabla de VLANs del switch:
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

- Verificaciones en el Router de la aeronave (R_Aircraft):

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

- Ping de PC Turista al Server Local 

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
- Acceso al Server Local con el Browser desde PC Turista

[ IMAGEN SERVER LOCAL PC TURISTA]

- Ping a Internet (`8.8.8.8`) desde PC Turista

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

- Acceso al server local con el Browser web (desde Business)

[IMAGEN SERVER LOCAL PC BUSINESS]

- Ping y tracert Internet (`8.8.8.8`) desde PC Business

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

- Ping desde Admin a todas las redes 

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


