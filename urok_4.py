
def array_search(A:list, N:int, x:int):


def test_array_search():
    A1=[1,2,3,4,5]
    m=test_array_search(A1,5,8)
    if m == -1:
        print("#test1-ok")
    else:
        print("#test1-fail")


    A2=[-1,-2,-3,-4,-5]
    m=test_array_search(A2,5,-3)
    if m == 2:
        print("#test2-ok")
    else:
        print("#test2-fail")


    A3=[10,20,30,10,10]
    m=test_array_search(A3,5,10)
    if m == 0:
        print("#test3-ok")
    else:
        print("#test3-fail")
test_array_search()
