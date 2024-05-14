import random
import json

# John Doe's weight
weight = 175

# Beginner and intermediate strength standards
strength_standards = {
    "Back Squat": {"beginner": 0.77, "intermediate": 1.51},
    "Deadlift": {"beginner": 0.89, "intermediate": 1.74},
    "Power Clean": {"beginner": 0.49, "intermediate": 0.97},
    "Bench Press": {"beginner": 0.57, "intermediate": 1.14},
    "Incline Bench Press": {"beginner": 0.46, "intermediate": 0.94},
    "Dip": {"beginner": 0.09, "intermediate": 0.49},
    "Overhead Press": {"beginner": 0.37, "intermediate": 0.74},
    "Pull-up": {"beginner": 0.97, "intermediate": 1.29},
    "Pendlay Row": {"beginner": 0.46, "intermediate": 0.91}
}

# Function to generate John Doe's lifting abilities
def generate_lifting_abilities(weight, strength_standards):
    john_doe = {
        "John Doe": {
            "last_name": "Doe",
            "first_name": "John",
            "weight": weight,
            "liftn": {}
        }
    }

    for lift, standards in strength_standards.items():
        beginner_multiplier = random.uniform(0.8, 1.0)
        intermediate_multiplier = random.uniform(1.0, 1.2)

        john_doe["John Doe"]["liftn"][lift] = {
            "beginner": round(weight * standards["beginner"] * beginner_multiplier, 2),
            "intermediate": round(weight * standards["intermediate"] * intermediate_multiplier, 2)
        }

    return john_doe

# Generate John Doe's lifting abilities
john_doe_data = generate_lifting_abilities(weight, strength_standards)

# Output John Doe's data as JSON
print(json.dumps(john_doe_data, indent=2))
