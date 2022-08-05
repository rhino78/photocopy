import os
import helpers


def get_difference(list_a, list_b):
    """
    returns a list of everything in a but not in b
    """
    return [x for x in list_a if x not in list_b]


def main():
    """
    script to double check that we got all the photos

    """
    dir_name = os.getenv('PICTURES_DIR')
    check_dir_name = '/mnt/share/temp'
    listOfToCheckFiles = helpers.getfiles(check_dir_name)
    listOfFile = helpers.getfiles(dir_name)

    print(f'found {len(listOfFile)} files in pictures')
    print(f'found {len(listOfToCheckFiles)} files in temp')
    non_match = list(get_difference(listOfFile, listOfToCheckFiles))
    print(f'    iterating over the {len(non_match)} missing files:')
    for n in non_match:
        print(f"        non match: {n}")


if __name__ == '__main__':
    main()
