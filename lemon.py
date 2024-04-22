#lemon case study
l=int(input('num of lemon'))
print('extra by {}'.format(l-21) if l>21 else 'less by {}'.format(21-l) if l<21 else 'sufficient')