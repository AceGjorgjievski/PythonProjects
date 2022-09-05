from constraint import *



if __name__ == '__main__':
    problem = Problem()


    variables = ["WA","NT","SA","Q","NSW","V","T"]
    domain = ["blue", "green", "red"]

    problem.addVariables(variables,domain)

    problem.addConstraint(lambda a, b: a != b, ("WA", "NT"))
    problem.addConstraint(lambda a, b: a != b, ("WA", "SA"))
    problem.addConstraint(lambda a, b: a != b, ("NT", "SA"))
    problem.addConstraint(lambda a, b: a != b, ("SA", "Q"))
    problem.addConstraint(lambda a, b: a != b, ("SA", "NSW"))
    problem.addConstraint(lambda a, b: a != b, ("SA", "V"))
    problem.addConstraint(lambda a, b: a != b, ("Q", "NSW"))
    problem.addConstraint(lambda a, b: a != b, ("NSW", "V"))

    result = problem.getSolutions()

    print(result)

