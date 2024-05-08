BLOCK_SIZE = 16  # Assume 16 byte plaintext blocks given the challenge description


def chunks(ciph_bytes: bytes, chunk_size: int) -> list[bytes]:
    chunk = [ciph_bytes[index:index+chunk_size] for index in range(0, len(ciph_bytes), chunk_size)]
    
    """ 

        Generate indices starting at 0 up to the length of each line in ciphertext, with a step size of
        16 according to our BLOCK_SIZE variable, using the range() function. 
        
        Iterate over each index generated from range function. For each index in ciph_bytes, slice from
        current index to index+chunk_size. Effectively slicing every 16 bytes of data to create chunks.
        Return a list of chunks. 

    """
    return chunk


if __name__ == '__main__':
    with open("program_data/8.txt") as file:
        comp_ciphertext = [bytes.fromhex(line.strip()) for line in file]

        """ 

            Read ciphertext, translate into bytes and remove leading and trailing bytes
            and trivial whitespace with strip(). This logically creates "lines" of the 
            ciphertext that we can "indexify". Is that a word? It is now.

            The ciphertext is read in as a list to make it iterable, which will allow us
            to use the enumerate() function effectively. 

        """

    for i, line_ct in enumerate(comp_ciphertext):
        
        """ 

            enumerate() logically "indexifies" the comp_ciphertexts variable to create numbered
            lines of the ciphertext.

            Python docs gives a good example for how this works in a list, so I'll write that below:

            >>> seasons = ['Spring', 'Summer', 'Winter', 'Fall']
            >>> list(enumerate(seasons))
            [(0, 'Spring'), (1, 'Summer'), (2, 'Winter'), (3, 'Fall')]

            For a real illustration of how this functions in the context of this program, see
            challenge8_enumerate.py in this set. 

        """
        block_num = len(line_ct) // BLOCK_SIZE
        
        unique_blocks = len(set(chunks(line_ct, BLOCK_SIZE)))

        """ 

            Use chunks() function for each enumerate line in ciphertext. The set() function effectively
            "extracts" blocks that do not have duplicate elements. "Duplicate elements" in a set are not
            allowed. len() counts the number of unique chunks, this gives us out unique_blocks variable.

        """
        
        recurring_blocks = block_num - unique_blocks

        """ 

            Take the total nubmer of blocks, subtract from number of unique blocks to get the number
            of recurring blocks.

        """
        
        if recurring_blocks == 0:
            continue
        
        print(f"\nProbable ECB mode detected: Line {i} has {recurring_blocks} duplicate blocks.\n")
        
        if recurring_blocks > 0:
            print("Likely ECB line: " + line_ct.hex() + "\n")
        
