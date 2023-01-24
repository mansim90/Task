from datetime import datetime
import pandas as pd

def date_detection(date):
    today = datetime.today().date()

    actual=[]
    for i in date:
       i = i.replace(".", "/")

       i = datetime. strptime(i, '%m/%d/%Y %H:%M')

       if (i.date() == today):
            actual.append("True")
       else:
           actual.append("False")

    return actual


if __name__ == '__main__':

    exceldates = pd.read_excel("Date.xlsx")
    date=[]
    status=[]
    for i in exceldates.date:
            date.append(i)

    for i in exceldates.status:
            status.append(i)

    print(status)
    function_output=date_detection(date)
    for i in range(len(function_output)):

        if(function_output[i]=="True"):
            function_output[i]="Pass"
        else:
            function_output[i]="Fail"

    print(function_output)

    for i in range(len(function_output)):
        if(status[i]==function_output[i]):
            print("equal")
        else:
            print("Not equal")