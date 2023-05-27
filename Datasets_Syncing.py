import os
import shutil
import glob2

# Define the directories
dir_a = r"E:\Master_Thesis\datasets\New_sorting_datasets\G\I_g"
dir_b = r"E:\Master_Thesis\datasets\efigi_i"
dir_c = r"E:\Master_Thesis\datasets\New_sorting_datasets\I\I_i"

# Get a list of all file names in directory A
# files_a = os.listdir(dir_a)[0]
fits_files = [f for f in os.listdir(dir_a) if f.endswith('.fits')]

for fits_file in fits_files:
    src_path = os.path.join(dir_b, fits_file)
    dst_path = os.path.join(dir_c, fits_file)
    shutil.copyfile(src_path, dst_path)


    # # Loop over each file name in directory A
# for file_name in files_a:
#    # Check if the file exists in directory B
#    if os.path.isfile(os.path.join(dir_b, file_name)):
#       print(f"Moving {file_name} from {dir_b} to {dir_c}")
#       # If it does, copy it to directory C
#       shutil.copy2(os.path.join(dir_b, file_name), os.path.join(dir_c, file_name))