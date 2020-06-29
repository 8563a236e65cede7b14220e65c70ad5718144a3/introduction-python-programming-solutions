"""
Review Question 10
Remove all leading zeroes from an IP address
"""
import re


def main():
    ip = input("Enter ip address ")
    pattern = re.compile(r"\b(\d{1,3})\b.\b(\d{1,3})\b.\b(\d{1,3})\b.\b(\d{1,3})\b")
    lead_0 = re.compile(r"(^0+)(\d+)")
    match_object = pattern.search(ip)
    ip_stripped = str()
    if match_object:
        group_list = match_object.groups()
        for each_group in group_list:
            match_0 = lead_0.search(each_group)
            if match_0:
                ip_stripped += match_0.group(2) + "."
            else:
                ip_stripped += each_group + "."
        print(ip_stripped[:-1])
    else:
        print("Invalid format")


if __name__ == "__main__":
    main()
