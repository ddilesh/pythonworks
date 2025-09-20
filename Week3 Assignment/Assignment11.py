import numpy as np

class testreport:
    def __init__(self,execution_times):
        self.execution_times=np.array(execution_times)

    def avgtime(self):
        mean=np.mean(self.execution_times)
        print(mean)
    def maxe(self):
        max=np.max(self.execution_times)
        print(max)
class regressionreport(testreport):
    def __init__(self, execution_times):
        super().__init__(execution_times)
    def slowtest(self,threshold):
       slow_tests = self.execution_times[self.execution_times > threshold]
       print(slow_tests)

if __name__ == "__main__":
    times=np.array([10,30,45,67,89,42,22,45,70,90])
    report=regressionreport(times)
    report.execution_times
    print(report.execution_times)
    report.avgtime()
    report.maxe()
    report.slowtest(40)

        

