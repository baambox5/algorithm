paren = '()()((()))'

for ch in paren:
    if ch == '(':
        push(ch)
    else:
        if isEmpty():
            # 잘못된 표현
            break
        if ')' and pop() != '(':
            # 잘못된 표현
            break
