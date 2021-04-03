import random
from string import punctuation,digits,ascii_letters

symbols=punctuation+digits+ascii_letters

secured_random=random.SystemRandom()

password="".join(secured_random.choice(symbols) for i in range(8))

print(password)