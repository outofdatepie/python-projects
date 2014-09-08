import random
while True:

    print ('Welcome to the magic 8 ball!')
    print ('Ask me a question')
    question =input()
    answers =['No','Maybe','Yes','Yes and you also smell like pie']

    answer = random.choice(answers)
    print(answer)
