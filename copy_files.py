import shutil
import logging
import os
import helpers


def mount_copy(dest, listOfFiles):
    """
    this function takes advantage of mounting a shared dir locally
    eliminating the need for the sambaclient copy
    """
    copied = 0
    for file in listOfFiles:
        month, year = helpers.get_oldest(
            [os.path.getctime(file), os.path.getmtime(file), os.path.getatime(file)])

        raw_file_name = os.path.basename(file)
        if " " in raw_file_name:
            raw_file_name = raw_file_name.replace(" ", "_")
            logging.warning(f"new file name: : {raw_file_name}")

        final_dst = dest + "/" + year + "/" + month + "/" + raw_file_name
        os.makedirs(os.path.dirname(final_dst), exist_ok=True)
        shutil.copyfile(file, final_dst)
        copied += 1
    print(f'copied {copied} files')
