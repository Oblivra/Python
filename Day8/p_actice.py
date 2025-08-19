class Sample:
    a = 5

object = Sample()
object.a = 0

# DOES THIS CHANGE THE CLASS ATTRIBUTE ?

# Ans: NO
# because object.a is an instance variable, not a class variable.
# class variable ki value to vahi rahegi 
# object.a = 0 ye to instance(object) hai jiski khudki kuch value hamne daali hai 
# class vali value to vahi rahegi jo class me hai a = 5


# HOW TO CHANGE CLASS ATTRIBUTE VALUE ?

# Ans: Sample.a = 10 
