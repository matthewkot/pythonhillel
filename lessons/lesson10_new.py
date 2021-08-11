import os

# currend_dir = os.getcwd()
# print(currend_dir)
#
# list_dir = os.listdir("homework")
# print(list_dir)
#
# tmp_path = os.path.join(currend_dir, "homework", "tmp", "test2")
# print(tmp_path)


def get_files_from_dir(base_dir, full_path = True):
    list_dir = os.listdir(base_dir)
    files = []
    for file_object in list_dir:
        path_object = os.path.join(base_dir,file_object)
        if os.path.isfile(path_object):
            files.append(path_object if full_path else file_object)
    return files

# aplhabet_files = get_files_from_dir("alphabet")
# print(aplhabet_files)
# homework_files = get_files_from_dir("homework", full_path=False)
# print(homework_files)


# def create_dir(path):
#     try:
#         os.mkdir(path)
#     except FileExistsError:
#         pass

os.makedirs("test_3_dir/test_4_dir", exist_ok=True)# Finish
