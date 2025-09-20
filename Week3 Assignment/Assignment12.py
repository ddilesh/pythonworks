import numpy as np

class manualtester:
    def analyse(self,data):
        print(data[:5])

class automationtester:
    def analyse(self,data):
        print(np.min(data))

class performancetester:
    def analyse(self,data):
        print(np.percentile(data,95))
def show_analysis(tester, data):
    tester.analyse(data)

if __name__ == "__main__":
    execution_times = np.array([12, 8, 15, 20, 7, 25, 18, 30, 22, 10, 14, 28])

    manual=manualtester()
    automation=automationtester()
    performance=performancetester()

    show_analysis(manual, execution_times)
    show_analysis(automation, execution_times)
    show_analysis(performance, execution_times)



