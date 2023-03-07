"""Дано:
файл в хранилище объемом в 3ГБ
ограничения в ОС: оперативная память - 1 ГБ
Необходимо:
скопировать файл в другую директорию"""


def main():
    with open('file_1.csv', 'r') as rf:
        with open('copy_file_1.csv', 'w') as wf:
            for line in rf:
                wf.write(line)


if __name__ == '__main__':
    main()
