import file_operations
from faker import Faker

fake_name = Faker("ru_RU")
print(fake_name.name())
name_npc = {
    "first_name": fake_name.first_name(),
    "last_name": fake_name.last_name(),
}

