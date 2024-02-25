import struct
import sys
class DataBase:
    lst_data = []
    FIELDS = ['id', 'name', 'old', 'salary']
    def select(self, a, b):
        return self.lst_data[a:b]
    def insert(self, data):
        for i in data:
            data_s = i.split()
            self.lst_data.append(dict(zip(self.FIELDS, data_s)))

def main():
    lst_in = list(map(str.strip, sys.stdin.readlines()))
    db = DataBase()
    db.insert(lst_in)

if __name__ == '__main__':
    main()

