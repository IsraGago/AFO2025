abcdario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# recorriendo del revés porque los indices se mueven
for i in range(len(abcdario) - 1, -1, -1):
    if i % 3 == 0:
        del abcdario[i]

print(abcdario)
