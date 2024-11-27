import os
import random


from faker import Faker


import file_operations


SKILLS_LIST = [
    "Стремительный прыжок",
    "Электрический выстрел",
    "Ледяной удар",
    "Стремительный удар",
    "Кислотный взгляд",
    "Тайный побег",
    "Ледяной выстрел",
    "Огненный заряд",
]

RUNIC_ALPHABET = {
    "а": "а͠",
    "б": "б̋",
    "в": "в͒͠",
    "г": "г͒͠",
    "д": "д̋",
    "е": "е͠",
    "ё": "ё͒͠",
    "ж": "ж͒",
    "з": "з̋̋͠",
    "и": "и",
    "й": "й͒͠",
    "к": "к̋̋",
    "л": "л̋͠",
    "м": "м͒͠",
    "н": "н͒",
    "о": "о̋",
    "п": "п̋͠",
    "р": "р̋͠",
    "с": "с͒",
    "т": "т͒",
    "у": "у͒͠",
    "ф": "ф̋̋͠",
    "х": "х͒͠",
    "ц": "ц̋",
    "ч": "ч̋͠",
    "ш": "ш͒͠",
    "щ": "щ̋",
    "ъ": "ъ̋͠",
    "ы": "ы̋͠",
    "ь": "ь̋",
    "э": "э͒͠͠",
    "ю": "ю̋͠",
    "я": "я̋",
    "А": "А͠",
    "Б": "Б̋",
    "В": "В͒͠",
    "Г": "Г͒͠",
    "Д": "Д̋",
    "Е": "Е",
    "Ё": "Ё͒͠",
    "Ж": "Ж͒",
    "З": "З̋̋͠",
    "И": "И",
    "Й": "Й͒͠",
    "К": "К̋̋",
    "Л": "Л̋͠",
    "М": "М͒͠",
    "Н": "Н͒",
    "О": "О̋",
    "П": "П̋͠",
    "Р": "Р̋͠",
    "С": "С͒",
    "Т": "Т͒",
    "У": "У͒͠",
    "Ф": "Ф̋̋͠",
    "Х": "Х͒͠",
    "Ц": "Ц̋",
    "Ч": "Ч̋͠",
    "Ш": "Ш͒͠",
    "Щ": "Щ̋",
    "Ъ": "Ъ̋͠",
    "Ы": "Ы̋͠",
    "Ь": "Ь̋",
    "Э": "Э͒͠͠",
    "Ю": "Ю̋͠",
    "Я": "Я̋",
    " ": " ",
}


fake_info = Faker("ru_RU")

updated_skills_list = []
for skill in SKILLS_LIST:
    updated_skill = skill
    for old_skill_name, new_skill_name in RUNIC_ALPHABET.items():
        updated_skill = updated_skill.replace(old_skill_name, new_skill_name)
    updated_skills_list.append(updated_skill)

output_dir = "results"
os.makedirs(output_dir, exist_ok=True)

for card_id in range(1, 11):
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

    file_name = os.path.join(output_dir, f"result_{card_id}.svg")
    file_operations.render_template(
        "template/charsheet.svg",
        file_name,
        npc_info,
    )
