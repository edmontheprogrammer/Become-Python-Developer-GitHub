import random

print(random.randint(1, 10))

print(random.random())

# Make your own version of a magic 8 ball that
# prints yes, no or may each time you ask it

magic_ball = random.randint(1, 3)


def magic_ball_eight(magic_ball):
    if magic_ball == 1:
        return "Yes"
    if magic_ball == 2:
        return "No"
    if magic_ball == 3:
        return "Maybe"


magic_ball_value = magic_ball_eight(magic_ball)
print(magic_ball_value)
