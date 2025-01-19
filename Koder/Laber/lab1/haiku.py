
første = str(input())
andre = str(input())
tredje = str(input())

første_l = len(første)
andre_l = len(andre)
tredje_l = len(tredje)

lengste_linje = max(første_l, andre_l, tredje_l) + 4


print('@' * lengste_linje)

print('@' + ' ' * (lengste_linje - første_l - 3) + første + ' @')
print('@' + ' ' * (lengste_linje - andre_l - 3) + andre + ' @')
print('@' + ' ' * (lengste_linje - tredje_l - 3) + tredje + ' @')

print('@' * lengste_linje)
