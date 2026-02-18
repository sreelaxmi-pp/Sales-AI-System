import json

def detect_changes(old_file, new_file):

    with open(old_file) as f:
        old_data = json.load(f)

    with open(new_file) as f:
        new_data = json.load(f)

    changes = []

    for old_plan, new_plan in zip(old_data["plans"], new_data["plans"]):

        if old_plan["price"] != new_plan["price"]:
            changes.append(
                f"Price changed for {old_plan['name']}"
            )

        new_features = set(new_plan["features"]) - set(old_plan["features"])
        for feature in new_features:
            changes.append(
                f"New feature added in {new_plan['name']}: {feature}"
            )

    return changes