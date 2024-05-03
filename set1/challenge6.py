from itertools import combinations
from base64 import b64decode
from dataclasses import dataclass
from typing import Optional
from pprint import pprint

from challenge2v2 import xor1
from challenge3v2 import score_text, frequencies
from challenge5 import vigenere_xor


@dataclass(order=True)
class ScoredGuess:
    score: float = float('inf')
    key: Optional[int] = None
    ciphertext: Optional[bytes] = None
    plaintext: Optional[bytes] = None

    @classmethod
    def from_key(cls, ct, key_val):
        full_key = bytes([key_val]) * len(ct)
        pt = xor1(ct, full_key)
        score = score_text(pt)
        return cls(score, key_val, ct, pt)

        """ 

            ScoredGuess is a data class to conveniently organize and compare several
            decryption attempts. We can call score, key, etc. as attributes in the 
            crack_xor function conveniently. 

            By setting the order of the data class to True, we make comparison possible
            between ScoredGuess objects.

        """


def crack_xor(ct: bytes) -> ScoredGuess:
    best_guess = ScoredGuess()
    ct_len = len(ct)
    ct_freq = {b: ct.count(b) / ct_len for b in range(256)}

    for candidate_key in range(256):
        score = 0
        for letter, frequency_expected in frequencies.items():
            score += abs(frequency_expected - ct_freq[ord(letter) ^ candidate_key])
        guess = ScoredGuess(score, candidate_key)
        best_guess = min(best_guess, guess)

    if best_guess.key is None:
        exit('No key found')

    best_guess.ciphertext = ct
    best_guess.plaintext = xor1(ct, bytes([best_guess.key]) * len(ct))

    return best_guess

    """

        Try all possible keys from 0 to 255, calculate score for each decryption attempt,
        and return best guess as ScoredGuess object. 

    """

weights = {n: bin(n).count("1") for n in range(256)}

def hamming_distance(a: bytes, b: bytes) -> bytes:
    return sum(weights[byte] for byte in xor1(a, b))


MAX_KEYSIZE = 40

def guess_keysize(ct: bytes, number_guesses: int = 1) -> list[tuple[float, int]] :
    def get_score(size: int) -> float:
        chunks = (ct[:size], ct[size:2*size], ct[2*size:3*size], ct[3*size:4*size])

        average = sum(hamming_distance(a, b) for a, b in combinations(chunks, 2)) / 6
        return average / size

    scores = [(get_score(size), size) for size in range(2, MAX_KEYSIZE+1)]
    scores.sort()
    return scores[:number_guesses]
    
    """

        guess_keysize takes in decoded ciphertext and returns the top 5 size guesses.
        get_score takes blocks (chunks) of the ciphertext and finds the average
        Hamming Distance between them for key sizes from 2 to 41. 

        At each key size, the ciphertext is divided into blocks of that size and 
        Hamming distance is calculated between blocks.

    """

def crack_vigenere(ciphertext: bytes, keysize: int) -> tuple[float, bytes] :
    chunks = [ciphertext[i::keysize] for i in range(keysize)]
    cracks = [crack_xor(chunk) for chunk in chunks]

    combined_score = sum(guess.score for guess in cracks) / keysize
    key = bytes(guess.key for guess in cracks)

    return combined_score, key

    """ 

        Parameters for crack_vigenere are the ciphertext and the top 5 guesses
        for keysizes.

        First we divide the ciphertext into blocks based on the given keysize, then
        iterate through each block of the ciphertext. Each block is treated as a 
        single-byte XOR operation, trying all possible key values from 0 to 255 and
        calculating a score for each attempt. 

        The combined score is calculated by summing up all scores in ScoredGuess objects
        and divides it by the keysize to give an average score per byte of the key.

    """

if __name__ == '__main__':
    with open("program_data/6.txt") as f:
        base64 = f.read()
    
    ciphertext = b64decode(base64)
    
    keysizes = guess_keysize(ciphertext, 5)

    print("Best key size guesses (confidence, size):")
    pprint(keysizes)

    candidates = [crack_vigenere(ciphertext, guess) for _, guess in keysizes]
    candidates.sort()
    
    best_candidate = candidates[0]
    best_key = best_candidate[1]

    print("-------------------\nTop Key:", best_key)
    
    print("\nPlaintext = \n")   
    print(vigenere_xor(best_key, ciphertext).decode("ascii"))
