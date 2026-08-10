from datetime import datetime


def generate_report(cv_output, nlp_output, consistency_output):
    detected = cv_output.get("detected_parts", [])
    side = nlp_output.get("impact_side", "unknown")
    obj = nlp_output.get("collision_object", "unknown object")
    drivable = nlp_output.get("drivable")

    safety = (
        "Vehicle may be drivable with caution."
        if drivable
        else "Vehicle should be inspected before further driving."
    )

    consistency_text = (
        "Customer statement is consistent with image findings."
        if consistency_output.get("consistent")
        else f"Possible discrepancy detected: {consistency_output.get('missing_in_cv')}"
    )

    report = f"""
CLAIMVISION AI - VEHICLE DAMAGE ASSESSMENT
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

------------------------------------------------------------
ACCIDENT SUMMARY
------------------------------------------------------------
Impact side: {side}
Collision object: {obj}

------------------------------------------------------------
DETECTED DAMAGE
------------------------------------------------------------
{chr(10).join(f'- {part}' for part in detected)}

------------------------------------------------------------
SAFETY ASSESSMENT
------------------------------------------------------------
{safety}

------------------------------------------------------------
CONSISTENCY CHECK
------------------------------------------------------------
{consistency_text}

------------------------------------------------------------
RECOMMENDED NEXT STEPS
------------------------------------------------------------
- Perform workshop inspection
- Capture additional close-up photos if needed
- Obtain repair quotation
- Submit claim for adjuster review

------------------------------------------------------------
END OF REPORT
------------------------------------------------------------
"""

    return report