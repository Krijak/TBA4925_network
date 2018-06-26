
def main():
    #fh, abs_path = mkstemp()
    antImages = 4000
    first = 4
    second = 4
    newFileName = '%s_%s_bench_door_%s'%(first, second, antImages)

    with open(newFileName + '_local.txt','w') as new_file:
        with open('4_4_bench_door_4000_final.txt') as old_file:
            lines = old_file.readlines()
            for line in lines:
                strings = line.split('/')
                del strings[0]
                print (strings[0])
                strings[0] = 'E:/kristina'
                new_line = '/'.join(strings)
                print(new_line)
                new_file.write(new_line)



if __name__ == '__main__':
    main()