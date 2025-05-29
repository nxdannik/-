from datetime import datetime  # щоб визначати теперішній час


class Danik:
    def __init__(self, first_name=None, last_name=None, birth_year=None):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    # Без self змінні first_name, last_name і birth_year були б просто локальними змінними в методі __init__, і після його виконання вони зникли б.
    # Тому self потрібно, щоб прив'язати ці змінні до конкретного об'єкта класу.

    def calculate_course(self):
        if self.birth_year is None:
            return None
        current_year = datetime.now().year
        age = current_year - self.birth_year
        return max(1, min(4, age - 15)) if age >= 15 else None

    def get_name_list(self):
        return [self.first_name, self.last_name] if self.first_name and self.last_name else []

    def get_birth_year(self):
        return self.birth_year if self.birth_year else []


# ---------------- використання -------------------------------------------------------------------------
Danik = Danik("Данило", "Сінкевич", 2008)
print("поточний рік:", datetime.now().year, ";", "рік народження:", Danik.get_birth_year())
print(Danik.calculate_course())  # Вираховує курс
print(Danik.get_name_list())  # Повертає список