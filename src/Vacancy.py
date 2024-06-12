class Vacancy:
    def __init__(self, name, url, salary, description):
        self.name = name
        self.url = url
        self.salary = salary
        self.description = description

    def __str__(self):
        return f"{self.name}\n {self.url}\n {self.salary}\n {self.description}\n---------------------------------------------------------------------"
    @classmethod
    def vacancies_list(cls, vacancies_list):
        vacan_list = []
        for i in vacancies_list:
            vac_name = i["name"]
            vac_url = i["url"]
            vac_salary = i["salary"]
            vac_description = cls.check_data_str(i["snippet"]["requirement"])
            vacancy_obj = cls(vac_name, vac_url, vac_salary, vac_description) # Vacancy == cls
            vacan_list.append(vacancy_obj)
        return vacan_list

    def __lt__(self, other):
        if type(other) == int:
            return self.salary["from"] < other
        else:
            return self.salary["from"] < other.salary["from"]

    def __le__(self, other):
        if type(other) == int:
            return self.salary["from"] <= other
        else:
            return self.salary["from"] <= other.salary["from"]
    def __eq__(self, other):
        if type(other) == int:
            return self.salary["from"] == other
        else:
            return self.salary["from"] == other.salary["from"]
    def __ne__(self, other):
        if type(other) == int:
            return self.salary["from"] != other
        else:
            return self.salary["from"] != other.salary["from"]
    def __gt__(self, other):
        if type(other) == int:
            return self.salary["from"] > other
        else:
            return self.salary["from"] > other.salary["from"]
    def __ge__(self, other):
        if type(other) == int:
            return self.salary["from"] >= other
        else:
            return self.salary["from"] >= other.salary["from"]

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

    @staticmethod
    def filter_vacancies(vacancies_list, filter_words):
        filter_list = []
        for vacancy in vacancies_list:
            for word in filter_words:
                if word in vacancy.description:
                    filter_list.append(vacancy)
                    break
        return filter_list
