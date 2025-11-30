def evaluate_candidate(profile):
    """Evaluate a candidate profile using rule-based legal logic."""
    score = 0
    reasons = []

    if profile.get("legal_background"):
        score += 2
        reasons.append("Strong legal foundation")

    if profile.get("ai_governance_and_regulation"):
        score += 2
        reasons.append("AI governance and regulation experience")

    if profile.get("saas_experience"):
        score += 2
        reasons.append("Hands-on SaaS and commercial experience")

    if profile.get("workflow_design"):
        score += 2
        reasons.append("Can translate law into structured workflows")

    if profile.get("client_facing"):
        score += 2
        reasons.append("Comfortable working directly with clients")

    recommendation = "Hire as Legal Engineer" if score >= 8 else "Needs further development"

    return {
        "Candidate": profile.get("name", "Unknown"),
        "Score": score,
        "Recommendation": recommendation,
        "Reasons": reasons,
    }


# This is me – candidate profile
candidate_profile = {
    "name": "Törenur Özbay",
    "legal_background": True,
    "ai_governance_and_regulation": True,
    "saas_experience": True,
    "workflow_design": True,
    "client_facing": True,
}

if __name__ == "__main__":
    result = evaluate_candidate(candidate_profile)

    print("Evaluation for:", result["Candidate"])
    print("Recommendation:", result["Recommendation"])
    print("Score:", result["Score"], "/ 10")
    print("Why:")
    for reason in result["Reasons"]:
        print("-", reason)
