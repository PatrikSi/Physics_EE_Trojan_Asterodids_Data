spkid = []

replace = '            JDTDB,            Calendar Date (TDB),                      X,                      Y,                      Z,             X_s,             Y_s,             Z_s,'

for spk in spkid:
    with open(f'{spk}.txt', 'r') as fin:
        data = fin.read().splitlines(True)
        dat = data[34:-58]
        dat.pop(1)
        dat.pop(2)
        dat.insert(0, replace)
        dat.pop(1)
        dat[1] = '\n'
        dat.pop(2)
        print(dat)
    with open(f'{spk}.txt', 'w') as fout:
        fout.writelines(dat)
