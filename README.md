# Datasets_Syncing
When you want to see the filenames in directory A, find the same name of these files in directory B, and copy them into directory C.

This code uses the "os" and "shutil" modules to interact with the file system. It first sets the paths for directories A, B, and C. Then it gets the list of file names in directory A using the "os.listdir" function.

Next, it loops through each file name in directory A and checks if it exists in directory B using the "os.path.isfile" function. If it does exist, it copies the file from directory B to directory C using the "shutil.copy2" function.

Note: This code assumes that the directories A, B, and C already exist.
