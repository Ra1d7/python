path = ''
def sortfile():
    global path
    try:
        f = open(path)
        print('\033[31m\033[1mFile Opened..\033[0m\n')
        for line in f.readlines():
            secs = line.split('|')
            rpnum = secs[3].replace("RP = ",'')
            rpnum = rpnum.replace(' ','')
            if int(rpnum) > 120:
                print('\033[32m {}\033[0m'.format(line))
    except:
        print('\033[1;91mINVALID PATH\033[0m')
        main()
def main():
    global path
    path = input('Path of File: ')
    print('Trying To Open File: {}'.format(path))
    sortfile()
print('\033[33mLeague of legends results Sorter for LolSamurai config')
print('Made by Raid7\033[0m')
main()
