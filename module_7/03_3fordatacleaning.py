files = [' Ravi.csv ', '  RAj.csv ', 'final.TXT ']
for file in files:
    file = file.strip().lower().replace('txt', 'csv')
    print(file)
    
    '''
    TIP
    CLEAN first
    TRANSFORM second
    '''
    