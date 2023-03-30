# declaring the var
Number = 100

# redeclaring Variable
Number = Number * 1000

# A constant
SOME_CONSTANT = 18

# number and Number are 2 different variables
number = 1000

# defining and assigning value to a protected variable
_protect_var = "Protected Variable"

# defining and assigning value to a private variable
__private_var = "Test Private Var"

# assigning multiple variables to a single value
a = b = c = False

# assigning multiple variables to a multiple values
x = y = z = False, 0, "Apple"

print("Reassigned variable : %d " % Number)


# Local variable example
def ex_local_var():
    d = "local var"
    print("Local Var : %s " % d)


# global variable example
glo_var = "global"


def ex_global_var():
    print(f"Global Var {glo_var}")


# ex_local_var()
# ex_global_var()

# hands on for global keyword importance
num = 550


def add_5_without_global_kw():
    num = 15
    print(f"{num+5} Is the result for add_5_without_global_kw")


def add_5_with_global_kw():
    global num
    num = 15
    print(f"{num+5} Is the result for add_5_with_global_kw")


add_5_without_global_kw()
print("Value of the global variable 'num' %d" % num)
print("_"*30)
add_5_with_global_kw()
print("Value of the global variable 'num' %d" % num)
print("_"*30)

