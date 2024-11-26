import file_operations
from faker import Faker
import random

fake_info = Faker("ru_RU")

skills = ["Стремительный прыжок",
          "Электрический выстрел",
          "Ледяной удар",
          "Стремительный удар",
          "Кислотный взгляд",
          "Тайный побег",
          "Ледяной выстрел",
          "Огненный заряд"]

npc_info = {
    "first_name": fake_info.first_name(),
    "last_name": fake_info.last_name(),
    "job": fake_info.job(),
    "town": fake_info.city(),
    "strength": random.randint(3, 18),
    "agility": random.randint(3, 18),
    "endurance": random.randint(3, 18),
    "intelligence": random.randint(3, 18),
    "luck": random.randint(3, 18),
    "skill_1": random.choice(skills),
    "skill_2": random.choice(skills),
    "skill_3": random.choice(skills),
}

file_operations.render_template("template/charsheet.svg", "results/result.svg", npc_info)