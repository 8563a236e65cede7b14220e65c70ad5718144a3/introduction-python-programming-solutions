"""
Program 9.18
Write a Program to Delete All the Files
and Subdirectories from the Extinct_Animals Directory
"""
import os

os.mkdir("Chapter09/Extinct_Animals")
os.mkdir("Chapter09/Extinct_Animals/Africa")
os.mkdir("Chapter09/Extinct_Animals/Africa/Asia")

with open("Chapter09/Extinct_Animals/Africa/Bonin_Thrush.rtf", "w") as f:
    f.write("abc")

with open("Chapter09/Extinct_Animals/Africa/Asia/Koala_Lemur.txt", "w") as f:
    f.write("abc")


def delete_files_recursively(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                print(f"{file_path} is deleted")
                os.remove(file_path)
            except Exception as e:
                print(e)


def cleanup():
    os.rmdir("Chapter09/Extinct_Animals/Africa/Asia")
    os.rmdir("Chapter09/Extinct_Animals/Africa")
    os.rmdir("Chapter09/Extinct_Animals")


def main():
    temp = input("Press enter to continue")
    delete_files_recursively("Chapter09/Extinct_Animals")
    cleanup()


if __name__ == "__main__":
    main()
