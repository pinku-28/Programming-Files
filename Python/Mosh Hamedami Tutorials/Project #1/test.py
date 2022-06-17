from ProcessWorkbook import process_workbook as pw

filename = input('filename: ')
worksheet = input('worksheet: ')
minmax_col = input('column: ')

pw.process_workbook(filename)
