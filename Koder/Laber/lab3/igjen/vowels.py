def vowels(text):
    text=text.lower()
    count=0
    for char in text:
        if char in ["a", "e", "i", "o", "u"]:
            count+=1
    return count


print("Tester vowels... ", end="")
assert 5 == vowels("Pingu in the city")
assert 9 == vowels("Frieren: Beyond Journey's End")
assert 3 == vowels("Programming")
assert 0 == vowels("Hmm")
print("OK")
