def main(): # it is use only in functions
    
    try:
        a = int(input("Enter a number:"))
        print(a)


    except Exception as e:
        print(e)

    finally:
        print("i am inside finally")

main()