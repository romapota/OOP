import sys
class StreamData:
    def create(self, fields, lst_values):
        l = lst_values.split(' ')
        if len(fields) != len(l):
            return False
        else:
            StreamData.id = l[0]
            StreamData.title = l[1]
            StreamData.pages = l[2]
class StreamReader:
    FIELDS = ('id', 'title', 'pages')
    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        sd = StreamData()
        for i in lst_in:
            res = sd.create(self.FIELDS, i)
        return sd, res
def main():
    sr = StreamReader()
    data, result = sr.readlines()

if __name__ == '__main__':
    main()


