secret_word = 'giraffe'
guess = ''
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word:
    guess = input('Enter guess')
    guess_count += 1
    if guess_count == guess_limit:
        out_of_guesses = True
    if out_of_guesses:
        print('you lose!')
        break
    else:
        continue
if guess == secret_word:
    print('you win!')
