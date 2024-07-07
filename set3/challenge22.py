from challenge21v2 import MersenneTwister

from random import randint
from time import time, sleep
from itertools import count


def generator() -> int:
    sleep(randint(5, 30))
    time_value = int(time())

    rand_num = MersenneTwister()
    rand_num.seed(time_value) 

    sleep(randint(5, 30))

    return rand_num.get_num()

    """ 

        Why wait twice? 

        Well, the first delay (in this case, between 5 and 30 seconds) 
        establishes a little unpredictability as to the exact instance 
        of seeding the RNG. 

        The second wait adds a bit more uncertainty for the "attacker."
        Output generation is separated by 5 to 30 seconds from the instance
        of seeding. 

    """


def crack_MTseed(random_number: int) -> int:
    r = MersenneTwister()

    for ts in count(int(time()), -1):
        r.seed(ts)

        if r.get_num() == random_number:
            break

        """ 

            Initialize a loop from the current timestamp and change time
            value in a decreasing monotonic fashion. Get the randomly generated
            number by each decremented time value as the seed, check if it 
            is equal to the random number generated. If it is, break the loop
            and return the time stamp as t. This is the seed used to generate
            the random number.

        """

    return ts



if __name__ == '__main__':
    print("Sleeping...")
    
    rng_value = generator()
    print(f"\nRandom number generated --> {rng_value}")

    try:
        seed = crack_MTseed(rng_value)
        print(f"Cracked seed --> {seed}")
    except Exception:
        print("Seed not found")
        print("This should never have happened.")