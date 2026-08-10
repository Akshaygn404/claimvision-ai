import spacy
import re

nlp = spacy.load("en_core_web_sm")

PART_MAP = {
    "bumper": "bumper_damage",
    "front bumper": "bumper_damage",
    "rear bumper": "bumper_damage",
    "door": "door_damage",
    "fender": "fender_damage",
    "bonnet": "hood_damage",
    "hood": "hood_damage",
    "windshield": "windscreen_damage",
    "windscreen": "windscreen_damage",
    "headlight": "light_damage",
    "taillight": "light_damage",
    "tail light": "light_damage",
    "indicator": "light_damage",
    "mirror": "mirror_damage"
}

DAMAGE_WORDS = [
    "dent", "dented",
    "scratch", "scratched",
    "crack", "cracked",
    "broken", "damaged",
    "shattered"
]

SIDE_PATTERNS = {
    "front-left": [r"front left", r"left front"],
    "front-right": [r"front right", r"right front"],
    "rear-left": [r"rear left", r"left rear"],
    "rear-right": [r"rear right", r"right rear"],
    "front": [r"front"],
    "rear": [r"rear"],
    "left": [r"left side", r"left"],
    "right": [r"right side", r"right"]
}

OBJECTS = [
    "wall", "pole", "pillar",
    "truck", "car", "bike",
    "tree", "barrier", "divider"
]


def extract_claim_info(text: str):
    text_lower = text.lower()
    doc = nlp(text)

    mentioned_parts = set()

    for phrase, label in PART_MAP.items():
        if phrase in text_lower:
            mentioned_parts.add(label)

    damage_keywords = []

    for word in DAMAGE_WORDS:
        if word in text_lower:
            damage_keywords.append(word)

    impact_side = None

    for side, patterns in SIDE_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, text_lower):
                impact_side = side
                break
        if impact_side:
            break

    collision_object = None

    for obj in OBJECTS:
        if obj in text_lower:
            collision_object = obj
            break

    drivable = None

    if any(p in text_lower for p in [
        "still drivable",
        "can drive",
        "drivable"
    ]):
        drivable = True

    if any(p in text_lower for p in [
        "cannot drive",
        "not drivable",
        "towed",
        "engine won't start"
    ]):
        drivable = False

    return {
        "impact_side": impact_side,
        "collision_object": collision_object,
        "mentioned_parts": sorted(list(mentioned_parts)),
        "damage_keywords": damage_keywords,
        "drivable": drivable
    }


if __name__ == "__main__":
    sample = """
    I was reversing the car and hit a wall.
    The rear bumper is dented and the left taillight is broken.
    The car is still drivable.
    """

    print(extract_claim_info(sample))