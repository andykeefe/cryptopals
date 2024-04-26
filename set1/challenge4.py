from challenge3v2 import crack_xor, score_text

"""
    import crack_xor and score_text functions from challenge 3
"""

if __name__ == '__main__':
    
    with open("4.txt") as f:
        single_line = [bytes.fromhex(line.strip()) for line in f]

        """
            txt file is opened and read as file f.
            
            strip() function strips off trailing whitespace or new line
            characters so that each line is read individually.

            bytes.fromhex() converts hex string into bytes and stores all 
            of this information in the single_line variable
        """

    best_score = float('inf')
    
    """
        best_score initialized to infinity. Therefore any score from
        score_text will be lower than the initial value
    """
    best_text = None

    for line in single_line:
        candidate = crack_xor(line)
        score = score_text(candidate)

        """
            Iterate over each line in the encrypted data.

            crack_xor on each individual line and store in candidate varable.

            score_text on the candidate and store in score variable
        """

        if score < best_score:
            best_score = score
            best_text = candidate

            """
                best_score initialized to infinity, so it will be replaced by
                immediately successive value. Each newly scored variable is 
                compared to the current variable; if the current score is lower
                than the current best_score, current score replaces it.

                The candidate with the best score is placed in best_text.
            """

    best_text = best_text.rstrip()
    
    """
        rstrip() removes any whitespace in the decrypted text, including
        newline characters
    """
    print(best_text)



