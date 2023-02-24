from calclang import Calclang
import sys

calclang = Calclang()

if __name__ == '__main__':
    while(True):
        statement = input("calclang> ")
        if statement == "\q":
            break
        if statement == "\h":
            print("\\q to exit.\n\\h to print this\ncalclang statement to run.")
            continue
        try:
            print(calclang.run_statement(statement))
        except Exception as e:
            # print(str(e))
            raise
