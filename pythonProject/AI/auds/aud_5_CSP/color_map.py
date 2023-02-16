from constraint import *


def different(a,b):
    return a!=b

if __name__ == "__main__":
    problem = Problem()

    variables = ["WA", "NT", "Q", "NSW", "V", "SA", "T"]
    domain = ["red", "green", "blue"]

    problem.addVariables(variables,domain)

    problem.addConstraint(lambda a,b: a!=b,("Q","NT"))
    problem.addConstraint(lambda a,b: a!=b,("Q","NSW"))
    problem.addConstraint(lambda a,b: a!=b,("WA","NT"))
    problem.addConstraint(lambda a,b: a!=b,("WA","SA"))
    problem.addConstraint(lambda a,b: a!=b,("SA","NT"))
    problem.addConstraint(lambda a,b: a!=b,("Q","SA"))
    problem.addConstraint(lambda a,b: a!=b,("SA","V"))
    problem.addConstraint(lambda a,b: a!=b,("SA","NSW"))
    problem.addConstraint(lambda a,b: a!=b,("NSW","V"))

    result = problem.getSolution()
    print(result)



