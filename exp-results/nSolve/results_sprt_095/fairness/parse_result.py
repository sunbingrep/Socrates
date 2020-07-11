from pytimeparse.timeparse import timeparse

folders = ['./']
file_names = ['log_bank.txt', 'log_census.txt', 'log_credit.txt']

end = 'analysis precision'

for folder in folders:
    print(folder)

    for name in file_names:
        print('#################################\n')

        print(name)
        path = folder + name

        file = open(path, 'r')
        lines = file.readlines()

        H0 = 0
        H1 = 0
        time = 0

        for line in lines:
            if 'H0' in line:
                H0 = H0 + 1
            elif 'H1' in line:
                H1 = H1 + 1
            elif line.startswith('real'):
                time = time + timeparse(line[5:])

        time = round(time)
        min = int(time / 60)
        sec = time - min * 60

        print('H0: {}'.format(H0))
        print('H1: {}'.format(H1))
        print('Time: {}m{}s'.format(min, sec))

        print('\n#################################')
