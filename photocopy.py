import os
import copy_files
import helpers


def main():
    """
    a handy script I wrote to organize my pictures into the home server
    ...because I am far too lazy to try an organize them manually
    *note* the mount must be made with the local user in order to mkdir on the shared folder
    i was able to re-mount with correct rights and resolve the issue:
    sudo mount -t cifs -o username=[sambauser],password=[sambauserpw],uid=[localuser] //[sambaip]/[sambsharefolder] /mnt/[localfolder]
    """
    dir_name = os.getenv('PICTURES_DIR')
    if dir_name is not None:
        listOfFiles = helpers.getListOfFiles(dir_name)
        copy_files.mount_copy("/mnt/share2/temp2", listOfFiles)
    else:
        print('we could not get the picture dir :(')


if __name__ == '__main__':
    main()
