import RUN_script

file = open("linesText.txt", 'r', encoding='utf8')
linesText = file.readlines()

file.close()

for line in linesText:
    words = line.strip().split('___')
    print(words)
    RUN_script.run_script(mimdumpPort=words[0])