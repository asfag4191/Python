def frame(text):
    if text.startswith('#'):
        text = '#' + text
    else:
        text = '# ' + text

    if text.endswith('#'):
        return text + '#' #feilen lå i denne setningen, lå til den med et ekstra mellomrom
    return text + ' #'


print('Testing frame... ', end='')
s = 'Carpe diem'
s = frame(s)
assert '## Carpe diem ##' == frame(s)
print('OK')

#step over Utfører hele den gjeldende linjen med kode uten å gå inn i detaljerte funksjonskall.
#step into går inn i funksjonskallet på nåværende linje
