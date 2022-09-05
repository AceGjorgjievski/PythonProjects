from constraint import *


def not_same_term_all(t1, t2):
    split1 = t1.split("_")
    split2 = t2.split("_")

    day1 = split1[0]
    day2 = split2[0]

    time1 = split1[1]
    time2 = split2[1]

    if day1 == day2 and abs(int(time1) - int(time2)) < 2:
        return False

    return True


def not_same_term_ml(t1, t2):
    h1 = t1[-2:]
    h2 = t2[-2:]

    if h1 == h2:
        return False
    return True


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    casovi_AI = input()
    casovi_ML = input()
    casovi_R = input()
    casovi_BI = input()

    AI_predavanja_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_predavanja_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_predavanja_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12",
                           "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_predavanja_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_vezbi_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_vezbi_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_vezbi_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

    # ---Tuka dodadete gi promenlivite--------------------

    variables_all = []
    variables_ml = []

    for i in range(int(casovi_AI)):
        problem.addVariable(f"AI_cas_{i + 1}", AI_predavanja_domain)
        variables_all.append(f"AI_cas_{i + 1}")

    for i in range(int(casovi_ML)):
        problem.addVariable(f"ML_cas_{i + 1}", AI_predavanja_domain)
        variables_all.append(f"ML_cas_{i + 1}")
        variables_ml.append(f"ML_cas_{i + 1}")

    for i in range(int(casovi_R)):
        problem.addVariable(f"R_cas_{i + 1}", R_predavanja_domain)
        variables_all.append(f"R_cas_{i + 1}")

    for i in range(int(casovi_BI)):
        problem.addVariable(f"BI_cas_{i + 1}", BI_predavanja_domain)
        variables_all.append(f"BI_cas_{i + 1}")

    # ----

    problem.addVariable(f"AI_vezbi", AI_vezbi_domain)
    variables_all.append(f"AI_vezbi")
    problem.addVariable(f"ML_vezbi", ML_vezbi_domain)
    variables_all.append(f"ML_vezbi")
    variables_ml.append(f"ML_vezhbi")
    problem.addVariable(f"BI_vezbi", BI_vezbi_domain)
    variables_all.append(f"BI_vezbi")

    # ---Tuka dodadete gi ogranichuvanjata----------------

    for i in range(len(variables_all)):
        for j in range(i + 1, len(variables_all)):
            problem.addConstraint(not_same_term_all, (variables_all[i], variables_all[j]))

    for i in range(len(variables_ml)):
        for j in range(i + 1, len(variables_ml)):
            problem.addVariable(not_same_term_ml, (variables_ml[i], variables_ml[j]))

    # ----------------------------------------------------
    solution = problem.getSolution()

    print(solution)
