def foo(array=None):
    if array == None :
        array=[]
    array.append("hello")
    return array

print(foo())
print(foo())

print(foo([1,2,3 ]))
print(foo())

