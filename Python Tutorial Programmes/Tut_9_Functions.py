def my_function(username,greeting):
    print ("Hello, %s, from My function, %s!" % (username,greeting))

my_function("John","Nice to meet you")
# ------------------------
def sum(a, b):
    return a + b

print (sum (3,4))
# ------------------------
def list_benefits():
    return "More organized code", \
           "More readable code", \
           "Easier code reuse", \
           "Allowing programmers to share and connect code together"

def built_sentence(benefits):
    result = ""
    for benefit in benefits:
        result += "%s - is a benefit of functions! " % benefit
    return result

print (built_sentence(list_benefits()))