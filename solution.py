def check_sequence(sequence):
    opening_brackets = '([{'
    closing_brackets = ')]}'
    stack = []

    for element in sequence:
        if element in opening_brackets:
            stack.append(element)
        else:
            i = closing_brackets.find(element)
            assert i != -1

            if len(stack) == 0:
                return False

            if stack[-1] != opening_brackets[i]:
                return False

            stack.pop()

    return len(stack) == 0

if __name__ == '__main__':
    assert check_sequence('([])')
    assert not check_sequence('{[(]}')
