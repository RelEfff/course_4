from src.Vacancy import Vacancy
from src.hh import HH
from src.utils import print_vacancies


# # Создание экземпляра класса для работы с API сайтов с вакансиями
#
#
# # Получение вакансий с hh.ru в формате JSON
# hh_vacancies = hh_api.get_vacancies("Python")
#
# # Преобразование набора данных из JSON в список объектов
# vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
#
#
#
# # Сохранение информации о вакансиях в файл
# json_saver = JSONSaver()
# json_saver.add_vacancy(vacancy)
# json_saver.delete_vacancy(vacancy)

# Функция для взаимодействия с пользователем
def main():
    hh_api = HH()
    search_query = input("Введите поисковый запрос: ")
    hh_vacancies = hh_api.load_vacancies(search_query)
    vacancies_list = Vacancy.vacancies_list(hh_vacancies)
    top_n = int(input("Введите количество вакансий для вывода по цене в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    min_salary = int(input("Введите минимальную зарплату: ")) # Пример: 100000
    #
    filtered_vacancies = Vacancy.filter_vacancies(vacancies_list, filter_words)
    #
    ranged_vacancies_by_salary = Vacancy.get_vacancies_by_salary(filtered_vacancies, min_salary)
    #
    sorted_vacancies = Vacancy.sort_vacancies(ranged_vacancies_by_salary)
    top_vacancies = Vacancy.get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    main()
