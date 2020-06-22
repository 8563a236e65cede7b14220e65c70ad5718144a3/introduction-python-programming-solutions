"""
Review Question 9
Rotate a string by a particular value
    i.e. "cheer" rotated by 7 is "jolly"
         "melon" rotated by -10 is "cubed"
"""


def rotate_word(string, rotation):
    result = str()
    for each_char in string:
        temp = ord(each_char)
        if temp + rotation < ord("a"):
            temp = ord("z") - (ord("a") - (temp + rotation) - 1)
            temp = chr(temp)
        else:
            temp += rotation
            temp = chr(temp)
        result += temp
    return result


def main():
    user_string = input("Please enter a word to be rotated\n")
    rotation = int(input("Please enter the number of characters to rotate by\n"))
    result = rotate_word(user_string, rotation)
    print(f"{user_string} rotated by {rotation} is {result}")


if __name__ == "__main__":
    main()

