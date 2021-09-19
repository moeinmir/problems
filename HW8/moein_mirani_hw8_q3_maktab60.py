import re
def find_at_end(string,word):
  if re.search(f'{word}$',string):
    print(f"your string has {word} at the end")
  else:
    print(f"your string has not {word} at the end")


find_at_end("hello world","world")
find_at_end("hello world","y")
