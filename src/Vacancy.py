class Vacancy:
    def __init__(self, name, url, salary, description):
        self.name = name
        self.url = url
        self.salary = salary
        self.description = description

    def __str__(self):
        return f"{self.name} {self.url} {self.salary} {self.description}"
    @classmethod
    def vacancies_list(cls, vacancies_list):
        vacan_list = []
        for i in vacancies_list:
            vac_name = i["name"]
            vac_url = i["url"]
            vac_salary = i["salary"]
            vac_description = i["snippet"]["requirement"]
            vacancy_obj = cls(vac_name, vac_url, vac_salary, vac_description)
            vacan_list.append(vacancy_obj)
        return vacan_list

    def __lt__(self, other):
        if type(other) == int:
            return self.salary < other
        else:
            return self.salary < other.salary

    def __le__(self, other):
        if type(other) == int:
            return self.salary <= other
        else:
            return self.salary <= other.salary
    def __eq__(self, other):
        if type(other) == int:
            return self.salary == other
        else:
            return self.salary == other.salary
    def __ne__(self, other):
        if type(other) == int:
            return self.salary != other
        else:
            return self.salary != other.salary
    def __gt__(self, other):
        if type(other) == int:
            return self.salary > other
        else:
            return self.salary > other.salary
    def __ge__(self, other):
        if type(other) == int:
            return self.salary >= other
        else:
            return self.salary >= other.salary

    @staticmethod
    def check_data_int(value):
        if value:
            return value
        return 0
    @staticmethod
    def check_data_str(value):
        if value:
            return value
        return "Информация не была найдена"