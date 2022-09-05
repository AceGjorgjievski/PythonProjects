from constraint import *




if __name__ == '__main__':
    problem = Problem()

    domain = [0, 1]
    vreme_sostanok_domain = []

    for i in range(12,20):
        vreme_sostanok_domain.append(i)

    problem.addVariable("Marija_prisustvo", domain)
    problem.addVariable("Petar_prisustvo", domain)
    problem.addVariable("Simona_prisustvo", domain)
    problem.addVariable("vreme_sostanok", vreme_sostanok_domain)

    variables_all = ["Petar_prisustvo",
                     "Marija_prisustvo",
                     "Simona_prisustvo",
                     "vreme_sostanok"]





