is_gender = False

if not(is_gender):
    print('gender is not True')
    gender = input('pls give me a gender:')
    if (gender == ''):
        print('what!')
    else:
        is_gender = True
        print('thats okey')
else:
    print('gender is True')
