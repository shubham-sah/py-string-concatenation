word1 = input("First one here: ")
word2 = input("Second one here: ")

final1 = "This sentence consists of 2 words, " + word1 + "and " + word2
final2 = "This sentence consists of 2 words, {} and {}".format(word1, word2)
final3 = (f'This sentence consists of 2 words {word1} and  {word2}')

print(final3)
