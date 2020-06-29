"""
Program 10.4
Change the File Extension from .txt to .csv of
All the files (including from Sub Directories)
for a Given Path
"""
import os
import glob


def rename_files_recursively(directory_path):
    print("File extension changed from .txt to .csv")
    for file_path in glob.glob(directory_path + r"/**/*.txt", recursive=True):
        print(f"File with .txt extension {file_path} changed to ", end="")
        try:
            pre, ext = os.path.splitext(file_path)
            print(f"File with .csv extension {pre + '.csv'}")
            os.rename(file_path, pre + ".csv")
        except Exception as e:
            print(e)


def main():
    rename_files_recursively("Chapter10/test_10_4")


if __name__ == "__main__":
    main()
