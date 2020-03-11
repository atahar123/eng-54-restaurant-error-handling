# open and write to the file
def add_to_order():
    try:
        # open the file using with
        # use open function with write capabilities
        with open('order.txt', 'w') as your_order:
            # write some code to file
            your_order.write('some stuff' + '\n')

    except FileNotFoundError as err:
        print('Check file')
        print(err)
    finally:
        print('Everything done, byeeeee')


def write_to_file(arg, file):
    try:
        # open the file using with
        # use open function with write capabilities
        with open(file, 'a') as your_order:
            # write some code to file
            your_order.write(arg + '\n')

    except FileNotFoundError as err:
        print('Check file')
        print(err)
    finally:
        print('Thank you')


def open_and_print(name_file):
    try:
        # with automatically closes files for us
        with open(name_file, 'r') as file:
            lines_list = file.readlines()
            for line in lines_list:
                print(line.strip('\n'))

    except FileNotFoundError as err:
        print('Check files')
        print(err)

    finally:
        print("Thank you and bye")
