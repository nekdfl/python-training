class Pupol:

    def __init__(self, name, age, predmet_list, teacher):
        self._name = name
        self._age = age
        self._predmet_list = predmet_list
        self._teacher = teacher

    def __repr__(self):
        return self._name

    def __str__(self):
        return f"pupol name is {self._name}"

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def get_predmet_list(self):
        return self._predmet_list

    def set_predmet_list(self, predmet_list):
        self._predmet_list = predmet_list

    def get_teacher(self):
        return self._teacher

    def set_teacher(self, teacher):
        self._teacher
