import os
import sys
from shutil import copyfile
import datetime

ext = [".jpg", ".JPG"]
months_in_year = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)

def move_files(dir, to_dir):
    print(f'moving from {dir} to {to_dir}') 

    if not os.path.exists(dir):
        print(f'could not find a valid path in :{dir}')
        
    for root, dirs, files in os.walk(dir):
        if len(files) == 0:
            print(f'could not find any files int {dir}')

        if len(files) > 0:
            for file in files:
                if file.endswith(tuple(ext)):
                    mod_date = modification_date(os.path.join(root, file))
                    mod_month = months_in_year[mod_date.month -1]
                    directory = to_dir + "/" + str(mod_date.year) + "/" + str(mod_month)

                    if not os.path.exists(directory):
                        print("creating dir: {}".format(directory))
                        os.makedirs(directory)

                    src = root + "/" + file
                    dst = directory + "/" + file
                    print(f'copying: {file} to {dst}')
                    copyfile(src, dst)

        for name in dirs:
            print("moving into {}".format(root + "/" + name))
            move_files(root + "/" + name, to_dir)

def main(argv):
    move_files(argv[0], argv[1])

if __name__ == "__main__":
    main(sys.argv[1:])
