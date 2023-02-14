def arithmetic_arranger(problems, bool=False):

  first = ''
  second = ''
  lines = ''
  res = ''
  string = ''

  for i in problems:

    num1 = i.split(' ')[0]
    operator = i.split(' ')[1]
    num2 = i.split(' ')[2]

    if (len(problems) > 5):
      return 'Error: Too many problems.'

    try:
      num1 = int(num1)
      num2 = int(num2)
    except:
      return 'Error: Numbers must only contain digits.'

    if (len(str(num1)) > 4 or len(str(num2)) > 4):
      return 'Error: Numbers cannot be more than four digits.'

    if (operator == '+'):
      sum = str(int(num1) + int(num2))
    elif (operator == '-'):
      sum = str(int(num1) - int(num2))
    else:
      return 'Error: Operator must be + or -.'

    length = max(len(str(num1)), len(str(num2)))
    top = str(num1).rjust(length)
    bottom = operator + str(num2).rjust(length)
    line = ''
    sumx = str(sum).rjust(length)

    for x in range(length):
      line += '-'

    if i != problems[-1]:
      first += top + '    '
      second += bottom + '    '
      lines += line + '    '
      res += sumx + '    '
    else:
      first += top
      second += bottom
      lines += line
      res += sumx

  if (bool is True):
    string = first + '\n' + second + '\n' + lines + '\n' + res
  else:
    string = first + '\n' + second + '\n' + lines

  return string