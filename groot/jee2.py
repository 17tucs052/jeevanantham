import sys, csv ,operator
      data = csv.reader(open('File.csv'),delimiter=',')
      sortedlist = sorted(data, key=operator.itemgetter(0) reverse=True)    
  
      with open("cj.csv", "wb") as f:
          fileWriter = csv.writer(f, delimiter=',')
          for row in sortedlist:
              fileWriter.writerow(row)