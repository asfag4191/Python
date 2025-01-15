
første = str(input("Hva er første raden i en haiku?\n"))
andre = str(input("Hva er andre raden i en haiku?\n"))
tredje = str(input("Hva er tredje raden i en haiku?\n"))

første_l = len(første)
andre_l = len(andre)
tredje_l = len(tredje)

lengste_linje = max(første_l, andre_l, tredje_l) + 4

#toppen
print('@' * lengste_linje)

#tar jo trekker fra -2 for at den skal se bedre ut, @ tar opp litt plass så jeg. 
print('@' + ' ' * (lengste_linje-første_l-2) + første + ' @')
print('@' + ' ' * (lengste_linje-andre_l-2) + andre + ' @')
print('@' + ' ' * (lengste_linje-tredje_l-2) + tredje + ' @')

print('@' * lengste_linje)


