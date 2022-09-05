from constraint import *



def valid_check_all(t1, t2):
    # print(t1)
    # print(t2)

    # you can solve this with split "_"

    day1 = t1[:3]
    day2 = t2[:3]

    time1 = t1[-2:]
    time2 = t2[-2:]

    # print(t1, day1, day2, time1, time2)

    if day1 == day2 and abs(int(time1) - int(time2)) < 2:
        return False

    return True


def valid_check_ml(t1, t2):
    time1 = t1[-2:]
    time2 = t2[-2:]


    if abs(int(time1) - int(time2)) < 2:
        return False
    return True



# https://prnt.sc/qGYp4SeX4no5

if __name__ == '__main__':
    problem = Problem()

    casovi_AI = input()
    casovi_ML = input()
    casovi_R = input()
    casovi_BI = input()

    AI_predavanja_domain = ["Mon_11", "Mon_12",
                            "Wed_11", "Wed_12",
                            "Fri_11", "Fri_12"]
    ML_predavanja_domain = ["Mon_12", "Mon_13", "Mon_15",
                            "Wed_12", "Wed_13", "Wed_15",
                            "Fri_12", "Fri_13", "Fri_15"]
    R_predavanja_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15",
                           "Wed_10", "Wed_11", "Wed_12", "Wed_13", "Wed_14", "Wed_15",
                           "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]

    BI_predavanja_domain = ["Mon_10", "Mon_11",
                            "Wed_10", "Wed_11",
                            "Fri_10", "Fri_11"]

    AI_vezhbi_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13",
                        "Thu_10", "Thu_11", "Thu_12", "Thu_13"]

    ML_vezhbi_domain = ["Tue_11", "Tue_13", "Tue_14",
                        "Thu_11", "Thu_13", "Thu_14"]

    BI_vrzhbi_domain = ["Tue_10", "Tue_11",
                        "Thu_10", "Thu_11"]

    # ---------------------------add Variables--------------------#

    variables_all = []
    variables_ml = []

    # AI - predavanja
    for i in range(int(casovi_AI)):
        variables_all.append(f"AI_cas_{i + 1}")
        problem.addVariable(f"AI_cas_{i + 1}", AI_predavanja_domain)

    # ML - predavanja
    for i in range(int(casovi_ML)):
        variables_all.append(f"ML_cas_{i + 1}")
        variables_ml.append(f"ML_cas_{i + 1}")
        problem.addVariable(f"ML_cas_{i + 1}", ML_predavanja_domain)

    # R - predavanja
    for i in range(int(casovi_R)):
        variables_all.append(f"R_cas_{i + 1}")
        problem.addVariable(f"R_cas_{i + 1}", ML_predavanja_domain)

    # BI - predavanja
    for i in range(int(casovi_BI)):
        variables_all.append(f"BI_cas_{i + 1}")
        problem.addVariable(f"BI_cas_{i + 1}", BI_predavanja_domain)


    # --------------------------------------------------------------- #

    # AI - vezhbi
    variables_all.append(f"AI_vezbi")
    problem.addVariable(f"AI_vezbi", AI_vezhbi_domain)

    # ML - vezhbi
    variables_all.append(f"ML_vezbi")
    variables_ml.append(f"ML_vezbi")
    problem.addVariable(f"ML_vezbi", ML_vezhbi_domain)

    # BI - vezhbi
    variables_all.append(f"BI_vezbi")
    problem.addVariable(f"BI_vezbi",BI_vrzhbi_domain)

    # -------------------------------add Constrains---------------------#

    for i in range(len(variables_all)):
        for j in range(i+1, len(variables_all)):
            problem.addConstraint(valid_check_all, (variables_all[i], variables_all[j]))

    for i in range(len(variables_ml)):
        for j in range(i+1, len(variables_ml)):
            problem.addConstraint(valid_check_ml, (variables_ml[i], variables_ml[j]))


    print(problem.getSolution())




