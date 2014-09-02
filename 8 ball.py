import random
answers = ['yes','no','maybe''Reply hazy',
           'Yes and you also smell like tacos','No but Miley Cyrus is']

while True:
  print('Ask me a question')
  question = input('> ')

  answer= random.choice(answers)
  print(answer)
