# Script to generate `as<X>-links.txt` file from configs

<div align = "center"><font size = 5> Xindi Xu<div>

I created a script to generate the `as<X>-links.txt` file from config files generated from `save_config.sh`. I want to share it with the class as I think it'd save people's time.

Here's how to use it:

1. Create a `.py` file next to your config directory generated from `save_config.sh` and copy the script 

2. Update the DIRECTORY name (L3) and output file name (L6)

3. Run the script and you'll see the output file

```python
import os
ROUTERS = ['ATLA', 'BOST', 'GENE', 'LOND', 'MIAM', 'NEWY', 'PARI', 'ZURI']
DIRECTORY = 'configs_12-09-2022_04-34-44'


with open('as1000-links.txt', 'w') as o:
    for router in ROUTERS:
        with open(os.path.join(DIRECTORY, router + '.txt'), 'r') as f:
            lines = f.readlines()
            interface = ''
            cost = ''
            for line in lines:
                line = line.strip('\n')
                if 'interface' in line:
                    interface = line.split(' ')[-1].replace('port_', '')
                if 'ip ospf cost' in line:
                    cost = line.split(' ')[-1]
                    o.write(f'{router} {interface} {cost}\n')
```

