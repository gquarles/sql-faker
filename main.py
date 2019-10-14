import sys
import os.path
import re

if __name__ == '__main__':
    if len(sys.argv) != 3 and len(sys.argv) != 2:
        print('Please use main.py [inputfile] [outputfile]')
        exit()
    if os.path.isfile(sys.argv[1]) == False:
        print('Please input a valid text file')
        exit()

    sqlData = []

    try:
        with open(sys.argv[1]) as inputfile:
            for line in inputfile:
                sqlData.append(line.strip('\n').split('\t'))
    except:
        print('Unable to read file at {}'.format(sys.argv[2]))

    print('Found', len(sqlData) - 1, 'rows with', len(sqlData[0]), 'columns')

    sqlString = 'SELECT '

    for i, column in enumerate(sqlData[0]):
        sqlString = sqlString + '"' + sqlData[1][i] + '" as "' + column + '", '
    
    sqlString = sqlString[:-2]

    for i, sql in enumerate(sqlData):
        if i == 0 or i == 1:
            pass
        else:
            sqlString = sqlString + ' UNION SELECT '
            for entry in sqlData[i]:
                sqlString = sqlString + '"' + entry + '", '
            sqlString = sqlString[:-2]
    
    if len(sys.argv) == 2:
        print(sqlString)
    else:
        try:
            out = open(sys.argv[2], 'w')
            out.write(sqlString)
            out.close()
            print('Wrote to file {}'.format(sys.argv[2]))
        except:
            print('Unable to write to file at {}'.format(sys.argv[2]))