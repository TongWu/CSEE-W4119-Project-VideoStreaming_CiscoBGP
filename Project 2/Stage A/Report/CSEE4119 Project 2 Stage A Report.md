# CSEE4119 Project 2 Stage A Report

<div align = "center"><font size = 5> Tong Wu, tw2906 <div>

## Task 1 - Set up interfaces and set up OSPF

The screenshot of ping results from MIAM-host to BOST-host.

![MIAM_host-BOST_host](https://images.wu.engineer/images/2022/11/24/MIAM_host-BOST_host.jpeg)

## Task 2 - Setup iBGP

### 1. The screenshot of **```show ip bgp summary```** results from ATLA router.

![ATLA_router_bgp_summary](./CSEE4119%20Project%202%20Stage%20A%20Report.assets/ATLA_router_bgp_summary-1669687740872-1.jpg)

### 2. The screenshot of **```show ip route bgp```** results from ATLA router.

![ATLA_router_bgp_route](./CSEE4119%20Project%202%20Stage%20A%20Report.assets/ATLA_router_bgp_route-1669687745566-3.jpg)

### 3, 4, 5. Solving the **important problem** for iBGP connections

To solving the iBGP connection problem, using loopback interface for BGP peering, and the command,

``````shell
neighbor update-source ${INTERFACE_NAME} # lo for loopback interface
``````

 is used for specify the using of interfaces [1] and avoiding the important problem regarding to the assignment document.

Using loopback interface peering because it will not make BGP session down if the physical interface used to establishing the session goes down [1].

For iBGP, loopback address peering is more commonly to use since there often has multiple path between two iBGP peers. However, in eBGP there is more likely to have one path between two eBGP peers, so it is not essential for eBGP, while eBGP use loopback address peering for load-balancing [2].

## References

[1] *Sample Configuration for iBGP and eBGP With or Without a Loopback Address*. (n.d.). Cisco. Retrieved 24 November 2022, from https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/13751-23.html

[2] *bgp ‘neighbor’: Do you use loopback or physical interface?* (2007, May 31). https://community.cisco.com/t5/routing/bgp-neighbor-do-you-use-loopback-or-physical-interface/td-p/726356

