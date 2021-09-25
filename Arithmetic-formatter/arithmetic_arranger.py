def arithmetic_arranger(problems, flag=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    arranged_problem = {
        'first': '',
        'second': '',
        'line': '',
        'ans': ''
    }
    for prob in problems:
        prob = prob.split()
        if prob[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not prob[0].isdigit() or not prob[2].isdigit():
            return "Error: Numbers must only contain digits."
        if len(prob[0]) > 4 or len(prob[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        l = max(len(prob[0]), len(prob[2])) + 2
        arranged_problem['line'] += '-'*l + '    '
        arranged_problem['first'] += ' '*(l-len(prob[0])) + prob[0] + '    '
        arranged_problem['second'] += prob[1]+' ' + \
            ' ' * (l-2-len(prob[2])) + prob[2] + '    '
        if flag:
            if prob[1] == '+':
                s = str(int(prob[0])+int(prob[2]))
                arranged_problem['ans'] += ' '*(l-len(s)) + s + '    '
            elif prob[1] == '-':
                s = str(int(prob[0])-int(prob[2]))
                arranged_problem['ans'] += ' '*(l-len(s)) + s + '    '

    arranged_problem['first'] = arranged_problem['first'].rstrip()
    arranged_problem['first'] += '\n'
    arranged_problem['second'] = arranged_problem['second'].rstrip()
    arranged_problem['second'] += '\n'
    arranged_problem['line'] = arranged_problem['line'].rstrip()

    if flag:
        arranged_problem['line'] += '\n'
        arranged_problem['ans'] = arranged_problem['ans'].rstrip()

    arranged_problems = arranged_problem['first'] + \
        arranged_problem['second']+arranged_problem['line']
    if flag:
        arranged_problems += arranged_problem['ans']
    return arranged_problems
