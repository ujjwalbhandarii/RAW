def farg(fun1):
    def farg2():
        print("executing now")
        fun1()
        print("executed")
    return farg2

def decoratorF():
    print("hy there form decoratorF")

decoratorF = farg(decoratorF)
decoratorF()