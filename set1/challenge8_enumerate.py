""" 

    This program prints out enumerated lines from 8.txt challenge data. This
    will show all enumerated lines in the original ciphertext after being stripped of
    whitespace and trivial characters. 

"""

def main():
    with open("program_data/8.txt") as f:
        ct_lines = [line.strip() for line in f]

    for index, line in enumerate(ct_lines):
        print(f"Index: {index}, Line: {line}")


main()
