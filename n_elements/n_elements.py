import sys


def main():
    """
    Основная функция, принимает значение n-элементов,
    выводит результат.
    """

    input_number = int(sys.stdin.readline())
    print(count_subsequence(input_number))


def count_subsequence(input_number):
    """
    Рассчет последовательности.
    """
    result = ""
    for digit in range(1, input_number + 1):
        element_str = str(digit) * digit
        result = result + element_str
    return result


if __name__ == "__main__":
    main()
