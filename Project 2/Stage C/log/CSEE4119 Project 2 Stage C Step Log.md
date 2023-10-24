# CSEE4119 Project 2 Stage C Step Log

## 3.4.1 Task - Implement intradomain routing policy

![image-20221212224742906](https://images.wu.engineer/images/2022/12/12/image-20221212224742906.png)

![image-20221212224757371](https://images.wu.engineer/images/2022/12/12/image-20221212224757371.png)

The first step is to measure the undersea link bandwidth by `iperf3`

The link of `LOND <-> BOST` has bandwidth $10$ Mbps, which is **Medium BW**.

![image-20221212224530523](https://images.wu.engineer/images/2022/12/12/image-20221212224530523.png)

The link of `LOND <-> NEWY` has bandwidth $50$ Mbps, which is **High BW**.

![image-20221212224933510](https://images.wu.engineer/images/2022/12/12/image-20221212224933510.png)

The link of `PARI <-> NEWY` has bandwidth $100$ Mbps, which is **High BW**.

![image-20221212224658853](https://images.wu.engineer/images/2022/12/12/image-20221212224658853.png)

The link of `PARI <-> MIAM` has bandwidth $10$ Mbps, which is **Medium BW**.

![image-20221212225100465](https://images.wu.engineer/images/2022/12/12/image-20221212225100465.png)

So the configuration should be $2$.

### LOND ROUTER

```
interface port_BOST
ip ospf cost 40
exit
interface port_NEWY
ip ospf cost 20
exit
interface port_PARI
ip ospf cost 16
exit
interface port_ZURI
ip ospf cost 5
exit
```

### PARI ROUTER

```
interface port_LOND
ip ospf cost 5
exit
interface port_NEWY
ip ospf cost 20
exit
interface port_MIAM
ip ospf cost 40
exit
interface port_GENE
ip ospf cost 10
exit
interface port_ZURI
ip ospf cost 5
exit
exit
```

### GENE ROUTER

```
interface port_PARI
ip ospf cost 10
exit
interface port_MIAM
ip ospf cost 80
exit
exit
```

### BOST ROUTER

```
interface port_LOND
ip ospf cost 40
exit
interface port_NEWY
ip ospf cost 10
exit
exit
```

### NEWY ROUTER

```
interface port_BOST
ip ospf cost 10
exit
interface port_ATLA
ip ospf cost 4
exit
interface port_MIAM
ip ospf cost 10
exit
interface port_PARI
ip ospf cost 20
exit
interface port_LOND
ip ospf cost 20
exit
exit
```

### MIAM ROUTER

```
interface port_NEWY
ip ospf cost 10
exit
interface port_ATLA
ip ospf cost 6
exit
interface port_PARI
ip ospf cost 40
exit
interface port_GENE
ip ospf cost 80
exit
exit
```

### ATLA ROUTER

```
interface port_NEWY
ip ospf cost 4
exit
interface port_MIAM
ip ospf cost 6
exit
exit
```

### ZURI ROUTER

```
interface port_LOND
ip ospf cost 5
exit
interface port_PARI
ip ospf cost 5
exit
exit
```