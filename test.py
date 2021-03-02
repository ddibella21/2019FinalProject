file = open("/Users/ddibella21/Desktop/CSP/Python/venv/score_saver.txt", "r")
overall_high_score = int(file.read())
print(overall_high_score)
file.close()

my_file = open("/Users/ddibella21/Desktop/CSP/Python/venv/score_saver.txt", "w")
my_file.write(str(15))
file.close()

# file = open("/Users/ddibella21/Desktop/CSP/Python/venv/score_saver.txt", "r")
# value = file.read()
# print(value)
# file.close()
