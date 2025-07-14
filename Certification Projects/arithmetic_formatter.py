def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_row = []
    second_row = []
    dash_row = []
    answer_row = []

    for problem in problems:
        parts = problem.split()
        
        if len(parts) != 3:
            return "Error: Each problem must have two operands and one operator."
        
        operand1, operator, operand2 = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(operand1), len(operand2)) + 2

        first_row.append(operand1.rjust(width))
        second_row.append(operator + operand2.rjust(width - 1))
        dash_row.append('-' * width)

        if show_answers:
            if operator == '+':
                result = str(int(operand1) + int(operand2))
            else:
                result = str(int(operand1) - int(operand2))
            answer_row.append(result.rjust(width))

    arranged_problems = (
        '    '.join(first_row) + '\n' +
        '    '.join(second_row) + '\n' +
        '    '.join(dash_row)
    )

    if show_answers:
        arranged_problems += '\n' + '    '.join(answer_row)

    return arranged_problems
