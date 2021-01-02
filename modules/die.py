# Dice Roll
import random

x = random.randint(1, 6)
print(f"The Dice Landed at {x}")

ENV.HELPER.update({
    "die": "\
```.die``` [No Arguemts Present]\
\nUsage: Roll a Dice.\
"
})

