import sys
class Graph:
    def set_data(self, data):
        Graph.data = data
    def draw(self):
        LIMIT_Y = [s for s in range(11)]
        for i in Graph.data:
            if i in LIMIT_Y:
                print(i, ' ', end='')
def main():
    graph1 = Graph()
    graph1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
    graph1.draw()
if __name__ == '__main__':
    main()

