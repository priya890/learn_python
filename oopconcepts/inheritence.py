class LoyaltyProgram:

    def __init__(self, pgm_type):
        self.pgm_type = pgm_type

    def display_program(self):
        print(f"Program enabled is {self.pgm_type}")


# single level inheritance
class Personalisation(LoyaltyProgram):

    def __init__(self, pgm_type):
        super().__init__(pgm_type)

    def benefits(self):
        print(f"{self.pgm_type} Benefits : Display all your favorite items your ordered last time")

    def games(self):
        print(f"{self.pgm_type} Benefits : Free game on first successful signup")


class LoyaltyRewards(LoyaltyProgram):

    def __init__(self, pgm_type):
        super().__init__(pgm_type)

    def benefits(self):
        print(f"{self.pgm_type} Benefits : Redeemable rewards")


pzn = Personalisation("Personalization")
print('_'*30)
pzn.display_program()
pzn.games()
pzn.benefits()

pzn = LoyaltyRewards("LoyaltyRewards")

print('_'*30)
pzn.display_program()
pzn.benefits()
print('_'*30)


# Multiple inheritance

class Employee:

    def __init__(self, name, yoe, company):
        self.name = name
        self.yoe = yoe
        self.company = company

    def display_company(self):
        print(f"Works in company : {self.company}")

    def display_name(self):
        print(f"Name is : {self.name}")

    def display_yoe(self):
        print(f"YOE is : {self.yoe}")


class Engineer:

    def __init__(self, expertise, sector):
        self.expertise = expertise
        self.sector = sector

    def display_expertise(self):
        print(f"Expertise is {self.expertise}")

    def display_sector(self):
        print(f"Works in {self.sector}")


class QualityEngineer(Employee, Engineer):

    def __init__(self, expertise, sector, name, yoe, company_name, subsection):
        Engineer.__init__(self, expertise, sector)
        Employee.__init__(self, name, yoe, company_name)
        self.subsection = subsection

    def display_quality_subsection(self):
        print(f"Ensures quality of {self.subsection} requirements")


presto_qa = QualityEngineer("Testing", "IT", "PrestoEmp", 12, "Presto", "Functional")
presto_qa.display_name()
presto_qa.display_yoe()
presto_qa.display_sector()
presto_qa.display_expertise()
presto_qa.display_quality_subsection()


class Animal:

    def __init__(self, type):
        self.type = type

    def can_walk(self):
        print(f"{self.type} can walk")

    def is_friendly(self, is_a_pet):
        if is_a_pet:
            print(f"{self.type} can be petted")
        else:
            print("Don't pet it")

    def sound(self):
        print(f"{self.type} can make a sound")


class Lion(Animal):

    def __init__(self, type):
        super().__init__(type)

    def is_friendly(self, is_a_pet):
        super().is_friendly(is_a_pet=False)

    def sound(self):
        print("Lion can roar")


lion_obj = Lion(type="Lion")
lion_obj.can_walk()

lion_obj.sound()

class A:

    def test_fun(self):
        print("Something")


class B(A):

    def test_fun_1(self):
        print("Test 2")


class C(B):

    def test_fun_2(self):
        print("Test 3")


class D:

    def test_fun_4(self):
        print("Test 4")

class E(B, D):

    def test_fun_5(self):
        print("Test 5")