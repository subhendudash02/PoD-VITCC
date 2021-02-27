# 26 Feb


def vowel_coll(word, vowel):
    s = []
    for i in word:
        if i in vowel and i not in s:
            s.append(i)
    return s

def inSequence(word, vowel):
    k = vowel_coll(word, vowel)
    x = k[0]
    for i in range(1, len(k)):
        if k[i] < x:
            return False
    else:
        return True

s = input().split()

vowel = ['a', 'e', 'i', 'o', 'u']

counts = []

for i in s:
    vv = list(vowel)
    p = vowel_coll(i, vv)
    counts.append(len(p))

for i in range(len(counts)):
    vv = list(vowel)
    if counts[i] == max(counts) and inSequence(s[i], vv) == True:
        print(s[i])
