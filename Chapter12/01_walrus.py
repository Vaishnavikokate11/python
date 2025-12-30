# using walrus oprator
if (n := len([1,2,5,8])) >3: #instant of declaring variable and check condition wa can directly use it
    print(f"List is too long {n} element, expected <=3")