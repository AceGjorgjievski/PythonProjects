from constraint import *

# given
# https://prnt.sc/fk1jyqIp1Ieb


def simona_constraint(vreme):
    if vreme == 13 or vreme == 14 or vreme == 16 or vreme == 19:
        return True
    return False

def marija_constraint(vreme):
    if vreme == 14 or vreme == 15 or vreme == 18:
        return True
    return False

def petar_constraint(vreme):
    if vreme == 12 or vreme == 13 or vreme == 16 or vreme == 17 or vreme == 18 or vreme == 19:
        return True
    return False

def simona_here(vreme):
    return vreme == 1

def check_valid(s, m, p, v):
    if s == 1 and not simona_constraint(v):
        return False
    if m == 1 and not marija_constraint(v):
        print(s, m, p, v)
        return False
    if p == 1 and not petar_constraint(v):
        return False
    return True

def at_least_two(s, m, p):
    if s == 1:
        return m == 1 or p == 1
    else:
        return False

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----

    marija_domain = [0, 1]
    simona_domain = [0, 1]
    petar_domain = [0, 1]

    vreme_sostanok = range(12,21)

    problem.addVariable(f'Simona_pristustvo', simona_domain)
    problem.addVariable(f'Petar_pristustvo', petar_domain)
    problem.addVariable(f'Marija_pristustvo', marija_domain)
    problem.addVariable(f'vreme_sostanok', vreme_sostanok)

    # ----------------------------------------------------



    # ---Tuka dodadete gi ogranichuvanjata----------------

    problem.addConstraint(simona_constraint, ['vreme_sostanok'])
    problem.addConstraint(simona_here, ['Simona_pristustvo'])
    problem.addConstraint(check_valid, ['Simona_pristustvo', 'Petar_pristustvo','Marija_pristustvo','vreme_sostanok'])
    problem.addConstraint(at_least_two, ['Simona_pristustvo', 'Petar_pristustvo','Marija_pristustvo'])
    print(problem.getSolutions())

