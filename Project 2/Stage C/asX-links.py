import os
ROUTERS = ['ATLA', 'BOST', 'GENE', 'LOND', 'MIAM', 'NEWY', 'PARI', 'ZURI']
DIRECTORY = 'configs_12-13-2022_05-46-59'


with open('as49-links.txt', 'w') as o:
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