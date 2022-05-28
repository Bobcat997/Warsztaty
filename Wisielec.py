import random

words = ['python jest super', 'HTML to nie język programowania', 'Toyota to zabytkowy samochód']


def comp_choice(words):
  return random.choice(words)


def mask_word(word, letters):
  new_word = ''
  for letter in word:
    if letter.lower() in letters:
      new_word += letter
    else:
      if letter == ' ':
        new_word += ' '
      else:
        new_word += '-'
  return new_word

def main():
  attempt = 0
  word = comp_choice(words)
  l = []
  guessed = False
  while attempt < 10:
    print(f'\n{mask_word(word, l)}\n')
    user_input = input('Enter a Letter: ').lower()
    if len(user_input) > 1:
      if user_input.lower() == word.lower():
        print('you guessed!')
        guessed = True
        break
    else:
      l.append(user_input)
    attempt += 1
  if not guessed:
    print(f'\n{mask_word(word, l)}\n')

main()