#password generator

import string
from random import*
mix=string.ascii_letters+string.punctuation+string.digits
password=" ".join(choice(mix)for x in range(randint(8,12)))
print(password)
