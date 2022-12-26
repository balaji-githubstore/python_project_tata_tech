class Father:
    f_age = 65

    def __init__(self):
        print("father constructor")

    def father_style(self):
        print("father style - method")


class Son(Father):
    s_age = 40

    def __init__(self):
        super().__init__()
        print("Son constructor")

    def son_style(self):
        print("son style - method")


class GSon(Son):
    gs_age = 10

    def __init__(self):
        super().__init__()
        print("Gson constructor")

    def gson_style(self):
        print("GSon style - method")
