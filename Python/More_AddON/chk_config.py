import configparser as cnfp

cfg = cnfp.ConfigParser()
cfg.read("rubi.cnf")

iz = cfg['DEFAULT']
tester = cfg['Testing']

print(iz['Group'])
print(iz['Fandom'])

wording = []
wording.append(tester['Test1'])
wording.append(tester['Test2'])

print(f'Please {wording[0]} {wording[1]}')