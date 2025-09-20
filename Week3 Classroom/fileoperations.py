def testreport():
    with open("report.txt", "w") as f:
        f.write("Testcase1 -pass\n")
        f.write("Testcase2 fail\n")
        f.write("Testcase3 -pass\n")
        
def appendreport():
    with open("report.txt", "a") as f:
        f.write("Testcase 4 -pass\n")
        f.write("Testcase 5 -fail\n")

def readfile():
    total=0
    Passed=0
    Failed=0
    with open("report.txt","r") as f:
      for line in f:
         line=line.strip()
         print(line)
         total+=1
         if "pass" in line:
             Passed+=1
         elif "fail" in line:
             Failed+=1

    print(f"total test {total}")
    print(f"total pass {Passed}")
    print(f"total fail {Failed}")

if __name__ == "__main__":
    testreport()
    appendreport()
    readfile() 
         



