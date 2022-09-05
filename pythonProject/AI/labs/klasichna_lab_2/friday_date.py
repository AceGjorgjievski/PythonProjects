from constraint import *

# given
# https://prnt.sc/fk1jyqIp1Ieb

def check_valid(Petar, Marija, Simona, Time):

    print(Petar, Marija, Simona, Time)

    if (Simona == 1 and Marija == 1 and Petar == 0) and Time == 14:
        return True

    if (Simona == 1 and Marija == 0 and Petar == 1) and Time == 19:
        return True

    if (Simona == 1 and Marija == 0 and Petar == 1) and Time == 16:
        return True

    if (Simona == 1 and Marija == 0 and Petar == 1) and Time == 13:
        return True

    return False


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----

    # marija_domain = [0, 1]
    # simona_domain = [0, 1]
    # petar_domain = [0, 1]

    domain = [0, 1]

    vreme_sostanok_domain = []

    for i in range(12, 20):
        vreme_sostanok_domain.append(i)

    # print(vreme_sostatok_domain)

    print(domain)

    problem.addVariable("Marija_prisustvo", domain)
    problem.addVariable("Petar_prisustvo", domain)
    problem.addVariable("Simona_prisustvo", domain)
    problem.addVariable("vreme_sostanok", vreme_sostanok_domain)

    variables_all = ["Petar_prisustvo",
                     "Marija_prisustvo",
                     "Simona_prisustvo",
                     "vreme_sostanok"]

    variables_all2 = ["Simona_prisustvo",
                     "Marija_prisustvo",
                     "Petar_prisustvo",
                     "vreme_sostanok"]

    # ----------------------------------------------------

    # ---Tuka dodadete gi ogranichuvanjata----------------

    # for i in range(len(variables_all)):
    #     for j in range(i + 1, len(variables_all)):
    #         for k in range(j + 1, len(variables_all)):
    #             for m in range(k + 1, len(variables_all)):
    #                 problem.addConstraint(check_valid,
    #                                       (variables_all[i], variables_all[j], variables_all[k], variables_all[m]))

    #problem.addConstraint(check_valid, (variables_all[0], variables_all[1], variables_all[2], variables_all[3]))
    for i in range(len(variables_all)):
        for j in range(i+1,len(variables_all)-1):
            problem.addConstraint()
    # print()
    # ----------------------------------------------------

    [print(solution) for solution in problem.getSolutions()]

