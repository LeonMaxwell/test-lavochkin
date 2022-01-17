def add_data():
    primary = None
    try:
        with open('check.txt', 'r') as f:
            primary = f.read()
    except:
        with open("check.txt", "w+") as f:
            primary = 'first'
            f.write(primary)
            print(primary)
    return primary


def main():
    if not add_data():
        with open("check.txt", "w+") as f:
            f.write('first')
            print("first")
    print("run")
    while True:
        number = input("Input integer number -> ")
        try:
            number = int(number)
            if number == 42:
                print("The Ultimate Question")
            else:
                number += 1
                print(number)
            if input("Do you want to continue? [Y]: ").upper() == "Y":
                continue
            else:
                break
        except ValueError:
            continue


if __name__ == '__main__':
    main()