""" 

    This program prints out enumerated lines from 8.txt challenge data. This
    will show all enumerated lines in the original ciphertext after being stripped of
    whitespace and trivial characters. 

    This program is only useful for illuminating what happens when using the enumerate
    function in the grand scheme of challenge 8. I put it in here for educational 
    purposes.

"""

def main():
    with open("program_data/8.txt") as f:
        ct_lines = [line.strip() for line in f]

    for index, line in enumerate(ct_lines):
        print(f"Index: {index}, Line: {line}")


main()
