# CSEE4119 Project 2 Stage C Report

<div align = "center"><font size = 5> Tong Wu, tw2906 <div>

## Task - Implement intradomain routing policy

![image-20221213002300819](https://images.wu.engineer/images/2022/12/13/image-20221213002300819.png)

### Goal 1

The diagram above shoes the configuration of ospf weight for each interface. The land links, which are solid lines, given a much lower cost than undersea lines. In this case, if two nodes are able to connected by full land link, than it will prefer land link by calculating the cost. For example, the link between BOST and MIAM, if using traceroute to test, the packets will traced to NEWY but not other nodes.

![image-20221213002440773](https://images.wu.engineer/images/2022/12/13/image-20221213002440773.png)

### Goal 2

As shown in the diagram above, each undersea links are set to different cost according to the category. By using `iperf3`, the configuration should be $2$. Diagrams below shows the result from `iperf3` in different nodes.

The link of `LOND <-> BOST` has bandwidth $10$ Mbps, which is **Medium BW**.

![image-20221212224530523](https://images.wu.engineer/images/2022/12/12/image-20221212224530523.png)

The link of `LOND <-> NEWY` has bandwidth $50$ Mbps, which is **High BW**.

![image-20221212224933510](https://images.wu.engineer/images/2022/12/12/image-20221212224933510.png)

The link of `PARI <-> NEWY` has bandwidth $100$ Mbps, which is **High BW**.

![image-20221212224658853](https://images.wu.engineer/images/2022/12/12/image-20221212224658853.png)

The link of `PARI <-> MIAM` has bandwidth $10$ Mbps, which is **Medium BW**.

![image-20221212225100465](https://images.wu.engineer/images/2022/12/12/image-20221212225100465.png)

To validate the configuration, the screenshot below shows the traceroute from LOND host to BOST loopback. If no configuration set, the packets will go through LOND -> BOST since it is directly connected. However, after configure the weight, packets will go through NEWY then BOST, which has less cost.

![image-20221213002923221](https://images.wu.engineer/images/2022/12/13/image-20221213002923221.png) 

### Goal 3

From the diagram above can know that the cost for interface port_ATLA and port_NEWY are set as the same, so the packet will balanced go through two nodes. To validate it, the screenshot below shows the traceroute from MIAM host to NEWY loopback, which shows that the packets will be load balanced.

![image-20221213003416145](https://images.wu.engineer/images/2022/12/13/image-20221213003416145.png)

### Goal 4

From the diagram above can know that the cost for interface port_LOND and port_PARI are set as the same, so the packet will balanced go through two nodes. For the LOND side, interface port_PARI is set weight to $6$, which is higher than port_ZURI, so the packets from LOND to PARI will pass ZURI.

### Goal 5

As shown in the diagram above, two high bandwidth undersea links are set lower cost than other undersea links, and ATLA is directed to prefer NEWY rather than load balance, so packets between ATLA and ZURI will go through high bandwidth in balance. To validate it, the screenshot below shows the traceroute from ATLA host to ZURI loopback, which shows that the packets will be load balanced.

![image-20221213004552493](https://images.wu.engineer/images/2022/12/13/image-20221213004552493.png)

### Traceroute from ATLA-host to ZURI loopback

![image-20221213000858731](https://images.wu.engineer/images/2022/12/13/image-20221213000858731.png)

The expected result can be seen from the screenshot, since the packets are balanced to LOND and PARI.

## Task - Advertise your prefix at the IXP

### Screenshot of the relevant parts of the out route-map

![image-20221217234153321](https://images.wu.engineer/images/2022/12/17/image-20221217234153321.png)

The route map “tasktwo” is set to contain the community value of my peers on the different group, and set the local preference to 1000 to ensure follow the map. Then, set the IXP neighbour to apply the route map on the outgoing router.

### Looking Glass entry of another AS

`http://34.171.188.127:2500/66_NEWYrouter.txt`

![image-20221217234248825](https://images.wu.engineer/images/2022/12/17/image-20221217234248825.png)

Which can shows that the connection between AS66 and AS49 is goes through the IXP.

### Traceroute from another AS

![image-20221217234418751](https://images.wu.engineer/images/2022/12/17/image-20221217234418751.png)

Where the traceroute go through the IXP.

## Task - Implement policy at IXP

### Screenshot of the relevant parts of the route-map at NEWY

![image-20221221142558453](https://images.wu.engineer/images/2022/12/21/image-20221221142558453.png)

The prefix list contains all IP address of the ASes from the same block. Use route-map to block the advertisement. Add additional permit with higher preference to allow advertise to irrelevant ASes.

### `show ip bgp` in router NEWY

![image-20221221142809901](https://images.wu.engineer/images/2022/12/21/image-20221221142809901.png)

### Looking Glass for the router ZURI of the stub AS

![image-20221219225838158](https://images.wu.engineer/images/2022/12/19/image-20221219225838158.png)

### Looking Glass for the AS in another group but connected to the same IXP

`http://34.171.188.127:2500/66_NEWYrouter.txt`

![image-20221222210758711](https://images.wu.engineer/images/2022/12/22/image-20221222210758711.png)

## Task - Implement BGP routing policy

### No-valley Routing

Use the IP prefix-list to record the IP prefix of each peer and providers. Then, use route map to deny the prefix-list and set the community to no-advertise.

### Prefer-customer Routing

Use the route map to set the local preference. The provider has the minimum preference value, and the customer has the largest. Then, apply the route map on each routers for the neighbour BGP outgoing link.

### Configuration

#### ATLA

![image-20221223041032593](https://images.wu.engineer/images/2022/12/23/image-20221223041032593.png)

#### BOST

![image-20221223041042201](https://images.wu.engineer/images/2022/12/23/image-20221223041042201.png)

#### GENE

![image-20221223041050533](https://images.wu.engineer/images/2022/12/23/image-20221223041050533.png)

#### LOND

![image-20221223041101904](https://images.wu.engineer/images/2022/12/23/image-20221223041101904.png)


#### MIAM

![image-20221223041111475](https://images.wu.engineer/images/2022/12/23/image-20221223041111475.png)

#### NEWY

![image-20221223041121725](https://images.wu.engineer/images/2022/12/23/image-20221223041121725.png)

#### PARI

![image-20221223041131043](https://images.wu.engineer/images/2022/12/23/image-20221223041131043.png)

#### ZURI

![image-20221223041143719](https://images.wu.engineer/images/2022/12/23/image-20221223041143719.png)

### Prove the no-valley routing

`http://34.171.188.127:2500/47_NEWYrouter.txt`

![image-20221223003353308](https://images.wu.engineer/images/2022/12/23/image-20221223003353308.png)

`http://34.171.188.127:2500/48_NEWYrouter.txt`

![image-20221223003419900](https://images.wu.engineer/images/2022/12/23/image-20221223003419900.png)

`http://34.171.188.127:2500/50_NEWYrouter.txt`

![image-20221223003435611](./CSEE4119%20Project%202%20Stage%20C%20Report.assets/image-20221223003435611.png)

From the screenshots above, the providers and peer do not receive other providers and peer advertise from AS49.

### Prove the prefer-customer routing

![image-20221223003857964](https://images.wu.engineer/images/2022/12/23/image-20221223003857964.png)

![image-20221223003911649](https://images.wu.engineer/images/2022/12/23/image-20221223003911649.png)

The first screenshot shows the traceroute to peer, the trace will go to AS52 (customer), then is the peer.

The second screenshot shows the traceroute to provider, the trace will go to AS50 (peer), then is the provider.

Two screenshots shows the relationship and order between provider, peer, and customer. 

## Task - Implement inbound traffic engineering

### Make provider arrives in priority via BOST

Use the `set metric` sentence in route map, set the MED of the link from LOND to AS47 (provider) to 100. Then apply the metric to the inbound eBGP.

![image-20221223034556932](https://images.wu.engineer/images/2022/12/23/image-20221223034556932.png)

`http://34.171.188.127:2500/47_MIAMrouter.txt`

![image-20221223040054292](https://images.wu.engineer/images/2022/12/23/image-20221223040054292.png)

The MIAM router of AS47 shows that it will prefer to enter via BOST.

