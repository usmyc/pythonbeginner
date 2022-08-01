# try:
#     number = int(input('say something:'+ ''))
#     print(number)
# except:
#     print('woa')


try:
    value = 10/0
    number = int(input('say something:' + ''))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)
