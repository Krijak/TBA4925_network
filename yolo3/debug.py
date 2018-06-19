#from PIL import Image
annotation_path = 'annotations/final_train.txt'

def get_random_debug(annotation_line):
    line = annotation_line.split()
    print (line[0])
    #image = Image.open(line[0])

with open(annotation_path) as f:
        lines = f.readlines()
        count = 0
        for i in lines:
            print (count)
            get_random_debug(i)
            count = count + 1