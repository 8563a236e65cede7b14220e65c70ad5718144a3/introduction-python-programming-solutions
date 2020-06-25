"""
Program 9.12
Save Dictionary in Python Pickle
"""
import pickle


def main():
    bbt = {"cooper": "sheldon"}
    with open("Chapter09/filename.pickle", "wb") as handle:
        pickle.dump(bbt, handle)
    with open("Chapter09/filename.pickle", "rb") as handle:
        bbt = pickle.load(handle)
        print(f"Unpickling {bbt}")


if __name__ == "__main__":
    main()
