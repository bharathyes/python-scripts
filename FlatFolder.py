import os
import sys
import shutil

source = sys.argv[1]
destination = sys.argv[2]

success_count = 0
failed_count = 0
total_files = 0

platform = sys.platform
if platform == "win32":
    delimiter = "\\"
else:
    delimiter = "/"

text_file = open("Output.txt", "w")
text_file.write("Copied Files: \n")


def copy_file(src):
    global success_count
    global failed_count
    global total_files
    if os.path.exists(src) and os.path.exists(destination):
        for root, dirs, files in os.walk(src):
            text_file.write("\n\t Root: " + root)
            text_file.write("\nFiles: ")
            total_files += files.__len__()
            text_file.write("".join(files))
            for file in files:
                if os.path.isfile(destination + ''.join(file)):
                    print("! ERR FileExists: " + "".join(file))
                    failed_count += 1
                    text_file.write("! ERR FileExists: " + "".join(file))
                else:
                    file_path = root + delimiter + "".join(file)
                    print("Copying: " + file_path)
                    shutil.copy2(file_path, destination)
                    success_count += 1


if os.path.isdir(source):
    if os.path.isdir(destination):
        copy_file(source)
    else:
        print("Invalid Destination. Creating folder ....")
        os.system("mkdir " + destination)
        copy_file(source)
else:
    print("Invalid Source. Doesn't exist or is a file")


print("\n\n End of script. \n Success : " + str(success_count)
      + "\n Failures : " + str(failed_count)
      + "\n Missed files " + str(total_files-success_count-failed_count))
text_file.write("\n\n End of script. \n Success : " + str(success_count)
                + "\n Failures : " + str(failed_count)
                + "\n Missed files " + str(total_files-success_count-failed_count))
text_file.close()
