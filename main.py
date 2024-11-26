import file_operations
from faker import Faker
import random

fake_info = Faker("ru_RU")

skills_list = ["Стремительный прыжок",
          "Электрический выстрел",
          "Ледяной удар",
          "Стремительный удар",
          "Кислотный взгляд",
          "Тайный побег",
          "Ледяной выстрел",
          "Огненный заряд"]
updated_skills_list = [skill_name.replace("е", "е͠") for skill_name in skills_list]
selected_skills = random.sample(updated_skills_list, 3)
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
    "skill_1": selected_skills[0],
    "skill_2": selected_skills[1],
    "skill_3": selected_skills[2],
}

file_operations.render_template("template/charsheet.svg", "results/result.svg", npc_info)