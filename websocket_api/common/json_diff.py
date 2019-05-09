import json_tools

def jsonDiff(a,b):
    result=json_tools.diff(a,b)
    print(result)

if __name__=="__main__":
    jsonDiff()