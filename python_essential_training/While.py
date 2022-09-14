from datetime import datetime
# While loops
print(datetime.now().second)
wait_until = datetime.now().second + 2
while datetime.now().second != wait_until:
    1 + 1


# Pass
while datetime.now().second != wait_until:
    pass

# Break
wait_until = datetime.now().second + 2
while True:
    if datetime.now().second == wait_until:
        print(f'We are at {wait_until} seconds!')
        break


# Continue
# 'continue' forces the control flow to jump back to the top of the loop.
