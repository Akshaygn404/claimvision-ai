from report_generator import generate_report

cv_output = {
    "detected_parts": [
        "bumper_damage",
        "light_damage"
    ]
}

nlp_output = {
    "impact_side": "front-left",
    "collision_object": "pillar",
    "mentioned_parts": [
        "bumper_damage",
        "light_damage"
    ],
    "drivable": False
}

consistency_output = {
    "consistent": True
}

report = generate_report(
    cv_output,
    nlp_output,
    consistency_output
)

print(report)