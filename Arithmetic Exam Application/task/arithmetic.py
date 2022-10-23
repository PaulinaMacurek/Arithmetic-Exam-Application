import random


class ArithmeticExam:
    op = {'+': lambda x, y: x + y,
          '-': lambda x, y: x - y,
          '*': lambda x, y: x * y}

    def __init__(self):
        self.mark = 0

    def __str__(self):
        return 'An arithmetic exam with two levels.'

    def generate_task(self):
        x = random.randint(2, 9)
        y = random.randint(2, 9)
        operator = random.choice(list(self.op.keys()))
        equation = str(x) + operator + str(y)
        print(f'How much is {equation} = ?')
        return self.op[operator](x, y)

    @staticmethod
    def generate_integral_squares():
        x = random.randint(11, 29)
        print(f'How much is {x} to square = ?')
        return x * x

    def generate_exam(self, level_, nb_of_task=1):
        for i in range(nb_of_task):
            if level_ == 1:
                result = self.generate_task()
            else:
                result = self.generate_integral_squares()

            if result == self.check_input():
                print('Right!')
                self.mark += 1
            else:
                print('Wrong!')

    def display_mark(self):
        print(f'Your mark is {self.mark}/5')

    @staticmethod
    def check_input():
        while True:
            option = input()
            if option != '' and option[0] == '-' and option[1:].isnumeric():
                return int(option[1:]) * (-1)
            elif option != '' and option.isnumeric():
                return int(option)
            else:
                print("Inncorrect format")


def input_level():
    while True:
        print('Which level do you want? Enter a number:\n'
              '1 - simple operations with numbers 2-9\n'
              '2 - integral squares of 11-29')
        try:
            level = int(input())
        except ValueError:
            print('Incorrect format.')
            continue
        if level == 1 or level == 2:
            return level
        else:
            print('Incorrect format.')


def save_the_result(my_exam_, level_):
    print('What is your name?')
    name = input()
    with open("results.txt", 'a', encoding='utf-8') as file:
        print(f"{name}: {my_exam_.mark}/5 in level {level_} " + (
            "(simple operations with numbers 2-9). " if level_ == 1 else '(integral squares 11-29).'),
              file=file,
              flush=True)
    print('The results are saved in "results.txt".')


def main():
    my_exam = ArithmeticExam()
    level = input_level()
    my_exam.generate_exam(level, 5)
    my_exam.display_mark()
    print('Would you like to save your result to the file? Enter yes or no.')
    if input() in ['yes', 'Yes', 'YES', 'y']:
        save_the_result(my_exam, level)
    else:
        exit()


if __name__ == "__main__":
    main()
