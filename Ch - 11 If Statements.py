is_male = True
if is_male:
    print("You are a male")

is_male = False
if is_male:
    print("You are a male")
else:
    print("You are not a male")

is_male = True
is_tall = True
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")

is_male = False
is_tall = True
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")

is_male = False
is_tall = False
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")

is_male = True
is_tall = True
if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are either not a male or tall or both")

is_male = False
is_tall = True
if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are either not a male or tall or both")