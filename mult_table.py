table_row = ''
for i in range(1,10):
    for j in range(1,10):
        table_row += str(i) + 'x' + str(j) + "=" + str(i*j) +'\t'
    print(table_row)
    table_row=''
