from utils import *
from time import sleep

class IOESThread(QThread):
    def __init__(self, parent=None):
        super(IOESThread, self).__init__()
        self.argc = 0
        self.argv = []

    def registFunction(self, function, argc, argv):
        self.function = function
        self.argc = argc
        self.argv = argv

    def run(self):
        self.function(self.argc, self.argv)

if __name__ == "__main__":
    def testAdd(argc, argv):
        total = 0
        for i in range(argc):
            total += argv[i]
        print("subThread return %d" %total)

    ioesThread = IOESThread()
    argc = 2
    argv = [10, 20]
    ioesThread.registFunction(testAdd, argc, argv)
    ioesThread.start()

    sleep(2)
    print("main exit")