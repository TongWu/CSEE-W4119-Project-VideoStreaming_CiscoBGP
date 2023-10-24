# Project 2 Stage A Configuration Backup

```shell
# IN ${LOCATION}_HOST:
./goto.sh ${LOCATION} host
# To update ip address
ip address add ${IP}/${SUBNET_MASK} dev ${DEV_NAME}
# Show all ip addresses
ip address show
```

```shell
# In ${LOCATION}_router:
./goto.sh ${LOCATION} router
# To update interface
conf t
interface ${INTERFACE_NAME}
ip address ${IP}/${SUBNET_MASK}
exit
exit
# Show all interfaces
show interface
```

```shell
# Configure OSPF
./goto.sh ${LOCATION} router
conf t
router ospf
network ${IP}/${SUBNET_MASK} area 0
exit
exit
## Show connected OSPF neighbours
show ip ospf neighbor
```

## PARI

### Configuration

```markdown
PARI HOST
0. lo (not configured)
   subnet: 49.153.0.1/24 (deleted, config lo in PARI ROUTER)
1. PARIrouter
   subnet: 49.103.0.0/24
   subnet: 49.103.0.1/24 (use this) (as the example said in BYOI document)

PARI ROUTER
1. host
   IP: 49.103.0.2/24 (use this)
2. lo
   IP: 49.153.0.1/24 (use this)
3. port_GENE
   subnet: 49.0.3.0/24
   IP: 49.0.3.1/24 (use this)
4. port_LOND
   subnet: 49.0.4.0/24
   IP: 49.0.4.1/24 (use this)
5. port_MIAM
   subnet: 49.0.6.0/24
   IP: 49.0.6.1/24 (use this)
6. port_NEWY
   subnet: 49.0.5.0/24
   IP: 49.0.5.1/24 (use this)
7. port_ZURI
   subnet: 49.0.1.0/24
   IP: 49.0.1.2/24 (use this)
```

### Log

```shell
root@g49-proxy:~# ./goto.sh PARI host 
Linux PARI_host 5.15.0-1021-gcp #28~20.04.1-Ubuntu SMP Mon Oct 17 11:37:54 UTC 2022 x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Thu Nov 24 00:32:11 2022 from 158.49.0.2
root@PARI_host:~# ip address add 49.103.0.1/24 dev PARIrouter
root@PARI_host:~# exit
logout
Connection to 158.49.12.2 closed.
root@g49-proxy:~# ./goto.sh PARI router

Hello, this is FRRouting (version 7.5).
Copyright 1996-2005 Kunihiro Ishiguro, et al.
PARI_router# conf t
PARI_router(config)# interface port_GENE
PARI_router(config-if)# ip address 49.0.3.1/24
PARI_router(config-if)# exit
PARI_router(config)# exit
PARI_router# conf t
PARI_router(config)# interface port_LOND
PARI_router(config-if)# ip address 49.0.4.1/24
PARI_router(config-if)# exit
PARI_router(config)# interface port_MIAM
PARI_router(config-if)# ip address 49.0.6.1/24
PARI_router(config-if)# exit
PARI_router(config)# interface port_ZURI
PARI_router(config-if)# ip address 49.0.1.2/24
PARI_router(config-if)# exit
PARI_router(config)# exit
PARI_router# exit
Connection to 158.49.12.1 closed.
```

## LOND

### Configuration

```markdown
LOND HOST
1. LONDrouter
   subnet: 49.101.0.0/24
   subnet: 49.101.0.1/24 (use this) (as the example said in BYOI document)

PARI ROUTER
1. host
   IP: 49.101.0.2/24 (use this)
2. lo
   IP: 49.151.0.1/24 (use this)
3. port_BOST
   subnet: 49.0.7.0/24
   IP: 49.0.7.1/24 (use this)
4. port_NEWY
   subnet: 49.0.8.0/24
   IP: 49.0.8.1/24 (use this)
5. port_PARI
   subnet: 49.0.4.0/24
   IP: 49.0.4.2/24 (use this)
6. port_ZURI
   subnet: 49.0.2.0/24
   IP: 49.0.2.2/24 (use this)
```

### Log

```shell
root@g49-proxy:~# ./goto.sh LOND host 
Warning: Permanently added '158.49.10.2' (ECDSA) to the list of known hosts.
Linux LOND_host 5.15.0-1021-gcp #28~20.04.1-Ubuntu SMP Mon Oct 17 11:37:54 UTC 2022 x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
root@LOND_host:~# ip address add 49.101.0.1/24 dev LONDrouter
root@LOND_host:~# exit
logout
Connection to 158.49.10.2 closed.
root@g49-proxy:~# ./goto.sh LOND router

Hello, this is FRRouting (version 7.5).
Copyright 1996-2005 Kunihiro Ishiguro, et al.

LOND_router# conf t
LOND_router(config)# interface host
LOND_router(config-if)# ip address 49.101.0.2/24
LOND_router(config-if)# exit
LOND_router(config)# interface lo
LOND_router(config-if)# interface host
LOND_router(config-if)# ip address 49.151.0.1/24
LOND_router(config-if)# exit
LOND_router(config)# interface port_BOST
LOND_router(config-if)# ip address 49.0.7.1/24
LOND_router(config-if)# exit
LOND_router(config)# interface port_NEWY
LOND_router(config-if)# ip address 49.0.8.1/24
LOND_router(config-if)# exit
LOND_router(config)# interface port_PARI
LOND_router(config-if)# ip address 49.0.4.2/24
LOND_router(config-if)# exit
LOND_router(config)# interface port_ZURI
LOND_router(config-if)# ip address 49.0.2.2/24
LOND_router(config-if)# exit
```

## ZURI

### **Looks like do not configure this**

## GENE

```
conf t
interface host
ip address 49.102.0.2/24
exit
interface lo
ip address 49.152.0.1/24
exit
interface port_LOND
ip address 49.0.2.1/24
exit
interface port_PARI
ip address 49.0.1.1/24
exit
```

## NEWY

### Configuration

```markdown
NEWY HOST
1. NEWYrouter
   subnet: 49.105.0.0/24
   subnet: 49.105.0.1/24 (use this) (as the example said in BYOI document)
2. default
	gateway: 49.105.0.2

NEWY ROUTER
1. host
   IP: 49.105.0.2/24 (use this)
2. lo
   IP: 49.155.0.1/24 (use this)
3. port_ATLA
   subnet: 49.0.11.0/24
   IP: 49.0.11.1/24 (use this)
4. port_BOST
   subnet: 49.0.10.0/24
   IP: 49.0.10.1/24 (use this)
5. port_LOND
   subnet: 49.0.8.0/24
   IP: 49.0.8.2/24 (use this)
6. port_MIAM
   subnet: 49.0.12.0/24
   IP: 49.0.12.1/24 (use this)
7. port_PARI
   subnet: 49.0.5.0/24
   IP: 49.0.5.2/24 (use this)
```

### Log

```shell
root@g49-proxy:~# ./goto.sh NEWY host  
Warning: Permanently added '158.49.14.2' (ECDSA) to the list of known hosts.
Linux NEWY_host 5.15.0-1021-gcp #28~20.04.1-Ubuntu SMP Mon Oct 17 11:37:54 UTC 2022 x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
root@NEWY_host:~# ip address add 49.105.0.1/24 dev NEWYrouter
root@NEWY_host:~# exit
logout
Connection to 158.49.14.2 closed.
root@g49-proxy:~# ./goto.sh NEWY router

Hello, this is FRRouting (version 7.5).
Copyright 1996-2005 Kunihiro Ishiguro, et al.

NEWY_router# conf t
NEWY_router(config)# interface host
NEWY_router(config-if)# ip address 49.105.0.2/24
NEWY_router(config-if)# exit
NEWY_router(config)# interface lo
NEWY_router(config-if)# ip address 49.155.0.1/24
NEWY_router(config-if)# exit
NEWY_router(config)# interface port_ATLA
NEWY_router(config-if)# ip address 49.0.11.1/24
NEWY_router(config-if)# exit
NEWY_router(config)# interface port_BOST
NEWY_router(config-if)# ip address 49.0.10.1/24
NEWY_router(config-if)# exit
NEWY_router(config)# interface port_LOND
NEWY_router(config-if)# ip address 49.0.8.2/24
NEWY_router(config-if)# exit
NEWY_router(config)# interface port_MIAM
NEWY_router(config-if)# ip address 49.0.12.1/24
NEWY_router(config-if)# exit
NEWY_router(config)# interface port_PARI
NEWY_router(config-if)# ip address 49.0.5.2/24
NEWY_router(config-if)# exit
NEWY_router(config)# exit
```

## BOST

### Configuration

```markdown
BOST HOST
1. BOSTrouter
   subnet: 49.106.0.0/24
   subnet: 49.106.0.1/24 (use this) (as the example said in BYOI document)

BOST ROUTER
1. host
   IP: 49.106.0.2/24 (use this)
2. lo
   IP: 49.156.0.1/24 (use this)
3. port_LOND
   subnet: 49.0.7.0/24
   IP: 49.0.7.2/24 (use this)
4. port_NEWY
   subnet: 49.0.10.0/24
   IP: 49.0.10.2/24 (use this)
```

### Log

```shell
root@g49-proxy:~# ./goto.sh BOST host  
Warning: Permanently added '158.49.15.2' (ECDSA) to the list of known hosts.
Linux BOST_host 5.15.0-1021-gcp #28~20.04.1-Ubuntu SMP Mon Oct 17 11:37:54 UTC 2022 x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
root@BOST_host:~# ip address add 49.106.0.1/24 dev BOSTrouter
root@BOST_host:~# exit 
logout
Connection to 158.49.15.2 closed.
root@g49-proxy:~# ./goto.sh BOST router

Hello, this is FRRouting (version 7.5).
Copyright 1996-2005 Kunihiro Ishiguro, et al.

BOST_router# conf t
BOST_router(config)# interface host
BOST_router(config-if)# ip address 49.106.0.2/24
BOST_router(config-if)# exit
BOST_router(config)# interface lo
BOST_router(config-if)# ip address 49.156.0.1/24
BOST_router(config-if)# exit
BOST_router(config)# interface port_LOND
BOST_router(config-if)# ip address 49.0.7.2/24
BOST_router(config-if)# exit
BOST_router(config)# interface port_NEWY
BOST_router(config-if)# ip address 49.0.10.2/24
BOST_router(config-if)# exit
BOST_router(config)# exit
```

## ATLA

### Configuration

```markdown
ATLA HOST
1. ATLArouter
   subnet: 49.107.0.0/24
   subnet: 49.107.0.1/24 (use this) (as the example said in BYOI document)

ATLA ROUTER
1. host
   IP: 49.107.0.2/24 (use this)
2. lo
   IP: 49.157.0.1/24 (use this)
3. port_MIAM
   subnet: 49.0.13.0/24
   IP: 49.0.13.1/24 (use this)
4. port_NEWY
   subnet: 49.0.11.0/24
   IP: 49.0.11.2/24 (use this)
```

### Log

```shell
root@g49-proxy:~# ./goto.sh ATLA host  
Warning: Permanently added '158.49.16.2' (ECDSA) to the list of known hosts.
Linux ATLA_host 5.15.0-1021-gcp #28~20.04.1-Ubuntu SMP Mon Oct 17 11:37:54 UTC 2022 x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
root@ATLA_host:~# ip address add 49.107.0.1/24 dev ATLArouter
root@ATLA_host:~# exit
logout
Connection to 158.49.16.2 closed.
root@g49-proxy:~# ./goto.sh ATLA router

Hello, this is FRRouting (version 7.5).
Copyright 1996-2005 Kunihiro Ishiguro, et al.

ATLA_router# conf t
ATLA_router(config)# interface host
ATLA_router(config-if)# ip address 49.107.0.2/24
ATLA_router(config-if)# exit
ATLA_router(config)# interface lo
ATLA_router(config-if)# ip address 49.157.0.1/24
ATLA_router(config-if)# exit
ATLA_router(config)# interface port_MIAM
ATLA_router(config-if)# ip address 49.0.13.1/24
ATLA_router(config-if)# exit
ATLA_router(config)# interface port_NEWY
ATLA_router(config-if)# ip address 49.0.11.2/24
ATLA_router(config-if)# exit
ATLA_router(config)# exit
ATLA_router# exit
Connection to 158.49.16.1 closed.
```

## MIAM

### Configuration

```markdown
MIAM HOST
1. MIAMrouter
   subnet: 49.108.0.0/24
   subnet: 49.108.0.1/24 (use this) (as the example said in BYOI document)

MIAM ROUTER
1. host
   IP: 49.108.0.2/24 (use this)
2. lo
   IP: 49.158.0.1/24 (use this)
3. port_ATLA
   subnet: 49.0.13.0/24
   IP: 49.0.13.2/24 (use this)
4. port_GENE
   subnet: 49.0.9.0/24
   IP: 49.0.9.2/24 (use this)
5. port_NEWY
   subnet: 49.0.12.0/24
   IP: 49.0.12.2/24 (use this)
6. port_PARI
   subnet: 49.0.6.0/24
   IP: 49.0.6.2/24 (use this)
```

### Log

