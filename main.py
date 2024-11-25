import file_operations
from faker import Faker

name_npc = {
    "first_name": "Артем",
    "last_name": "Литвич"
}

file_operations.render_template("charsheet.svg", "result.svg", name_npc)