def backtracing(result):
    path.append(1)
    result.append(path)
    path.pop()

path = []

def combine():
    
    result = []
    
    backtracing(result)
    print(result)
    
combine()