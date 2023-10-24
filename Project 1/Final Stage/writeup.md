# CSEE4119 Project 1 Final Stage Writeup

<div align = "center"><font size = 5> Tong Wu, tw2906 <div>

## Alpha = 0.1

Fairness:

![fairness_0.1](https://images.wu.engineer/images/2022/11/08/fairness_0.1.png)

Smoothness:

![smoothness_0.1](https://images.wu.engineer/images/2022/11/08/smoothness_0.1.png)

Utilisation:

![utilization_0.1](https://images.wu.engineer/images/2022/11/08/utilization_0.1.png)

## Alpha = 0.5

Fairness:

![fairness_0.5](https://images.wu.engineer/images/2022/11/08/fairness_0.5.png)

Smoothness: 

![smoothness_0.5](https://images.wu.engineer/images/2022/11/08/smoothness_0.5.png)

Utilisation:

![utilization_0.5](https://images.wu.engineer/images/2022/11/08/utilization_0.5.png)

## Alpha = 0.9

Fairness: 

![fairness_0.9](https://images.wu.engineer/images/2022/11/08/fairness_0.9.png)

Smoothness: 

![smoothness_0.9](https://images.wu.engineer/images/2022/11/08/smoothness_0.9.png)

Utilisation:

![utilization_0.9](https://images.wu.engineer/images/2022/11/08/utilization_0.9.png)

## Conclusion

According to the calculation of the EWMA: $T_{current}=\alpha T_{new}+(1-\alpha)T_{current}$: 

The higher $\alpha$ causing the throughput estimation more rely on the new calculated throughput, which can be seen as a algorithm that is volatile and place less emphasis on the integration result and more on the current throughput. The advantage is that the network speed will be fast, so when $\alpha = 0.9$, the utilisation is much less than others. The disadvantage is that causing serious unfairness for other connections in a same network. Also, unfairness brings unstable video quality to both peers. 

Less $\alpha$, such as $\alpha=0.1$, providing a smooth connection and high usage network link. It will seldomly bring unfair to other peers. However, high rely on the past estimation will causing this approach is hard to deal with the sudden situation such as when other connections has high concurrent traffic, low $\alpha$ will take long time to lower the video bitrate in order to ensure smoothness. 

Medium $\alpha = 0.5$, brings less good fairness as well as less utilization. This is because it looks at both past estimates and current throughput with the same weight. This approach has less unstable points and higher utilisation compare with high $\alpha$, and vice versa. However, its lack of a distinct strategy makes it not an efficient choice in most specific situations.