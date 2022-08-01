from Question import Question
question_prompts = [
    'What color are apples\n(a)Red/Green\n(b)White\n(c)Orange',
    'What color are bananas\n(a)Red/Green\n(b)Purple\n(c)Yellow',
    'What color are melons\n(a)Red/Green\n(b)Purple\n(c)Orange'
]
questions = [
    Question(question_prompts[0], 'a'),
    Question(question_prompts[1], 'c'),
    Question(question_prompts[2], 'b'),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print('You got' + str(score) + '/' + str(len(questions)) + 'correct')

run_test(questions)