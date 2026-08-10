#compare nlp output with cv output from predict_json.py
def check_consistency(cv_parts, nlp_parts):
    cv_set = set(cv_parts)
    nlp_set = set(nlp_parts)

    missing_in_cv = list(nlp_set - cv_set)
    extra_in_cv = list(cv_set - nlp_set)

    return {
        "consistent": len(missing_in_cv) == 0,
        "missing_in_cv": missing_in_cv,
        "extra_in_cv": extra_in_cv
    }


if __name__ == "__main__":
    cv_parts = ["bumper_damage", "light_damage"]
    nlp_parts = ["bumper_damage", "light_damage"]

    print(check_consistency(cv_parts, nlp_parts))
