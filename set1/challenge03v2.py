from challenge2v2 import xor1



frequencies = {
 'a': 0.07621311704656691,
 'b': 0.014867988764413507,
 'c': 0.024251119156260628,
 'd': 0.039868377210473885,
 'e': 0.12689755900495658,
 'f': 0.02205683052184707,
 'g': 0.018419248969754727,
 'h': 0.06101710716449914,
 'i': 0.06589944253674268,
 'j': 0.0011532531925950095,
 'k': 0.005854313736661194,
 'l': 0.03898444661974238,
 'm': 0.02395072086956672,
 'n': 0.06968031752444188,
 'o': 0.07443317087655875,
 'p': 0.015149396354822169,
 'q': 0.0011377153501798073,
 'r': 0.060286828570984635,
 's': 0.06055097189204307,
 't': 0.08602612774523463,
 'u': 0.02799919203219441,
 'v': 0.010434524395275806,
 'w': 0.021307561232047318,
 'x': 0.0015779542186105371,
 'y': 0.022800920530841755,
 'z': 0.0016746341269717954,
 'A': 0.001191234585165504,
 'B': 0.001983664548340817,
 'C': 0.0013638772786677509,
 'D': 0.0010876489690641558,
 'E': 0.0016349263074662787,
 'F': 0.00037636107183489835,
 'G': 0.0005835323040375947,
 'H': 0.0014139436597834026,
 'I': 0.005227620759248037,
 'J': 0.0005973437195177744,
 'K': 0.00018300125511238176,
 'L': 0.0015451521068451102,
 'M': 0.003114474190780535,
 'N': 0.0005593623269472801,
 'O': 0.0004575031377809544,
 'P': 0.0006560422353085384,
 'Q': 1.7264269350224695e-06,
 'R': 0.0004298803068205949,
 'S': 0.001073837553583976,
 'T': 0.0017385119235676268,
 'U': 0.0001467462894769099,
 'V': 0.00012775559319166274,
 'W': 0.0011653381811401668,
 'X': 0.0002037183783326514,
 'Y': 0.0006422308198283587,
 'Z': 1.7264269350224695e-06
 }


"""
Frequencies were obtained using Jane Austen's Pride and Prejudice. The program will be in the directory titled ch3_freq.py

"""



def score_text(text: bytes) -> float:
    score = 0.0
    length = len(text)

    for letter, frequency_expected in frequencies.items():
        frequency_actual = text.count(ord(letter)) / length
        err = abs(frequency_expected - frequency_actual)
        
        """
            Return the absolute value of the difference between expected 
            frequencies found in Pride and Prejudice and the actual frequencies
            found in the XORed plaintext. A low value of err indicates that the 
            decrypted text is similar to actual english letter frequency
        """
        
        score += err

    return score


def crack_xor(ciphertext: bytes) -> bytes:
    best_guess = (float('inf'), None)

    for candidate_key in range(256):
        full_key = bytes([candidate_key]) * len(ciphertext)
        
        """
            Start with candidate key and lengthen it to the number of bytes in the ciphertext
        """
        plaintext = xor1(full_key, ciphertext)
        
        """
            Imported xor1 function from the previous challenge2v2.py
            This will XOR every possible single character key with the 
            ciphertext and store it in variable plaintext
        """

        score = score_text(plaintext)
        
        
        
        curr_guess = (score, plaintext)
        
        best_guess = min(best_guess, curr_guess)

        """
            curr_guess stores the value of the score and the plaintext and best_guess
            stores the minimum score value between the current guess and the previous
            guess
        """

    return best_guess[1]

if __name__ == '__main__':

    ciphertext = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

    print(crack_xor(ciphertext))
