def calculate_internal_score(data: dict) -> tuple[int, str]:
    """
    Calculates the internal lead score based on the criteria defined in the manual.
    Returns (score, status).
    """
    score = 0

    # 1. Phone (+10) - Mandatory field, so assume +10 if present
    if data.get("phone"):
        score += 10

    # 2. CLT Status
    # "Mais de 3 anos" -> +30
    # "2-3 anos" -> +15
    clt_years = data.get("clt_years")
    if clt_years == "Mais de 3 anos":
        score += 30
    elif clt_years == "2-3 anos":
        score += 15

    # 3. Income
    # "Renda acima de R$3.000" -> +25
    # Options: "Abaixo de R$1.500", "R$1.500–R$3.000", "R$3.000–R$5.000", "Acima de R$5.000"
    income = data.get("income")
    if income in ["R$3.000–R$5.000", "Acima de R$5.000"]:
        score += 25

    # 4. Financing History
    # "Nunca tentou financiar" -> +20
    # data["tried_financing"] is boolean? Or string "Sim"/"Não"?
    # Squeeze page sends boolean or string?
    # Manual 5.4 says buttons [Sim] [Não]. JS likely sends boolean.
    # Assuming boolean for now, or check both.
    tried = data.get("tried_financing")
    if tried is False or tried == "false" or tried == "Não":
        score += 20

    # Determine Status
    # 70-100: Hot
    # 40-69: Warm
    # 0-39: Cold

    if score >= 70:
        status = "hot"
    elif score >= 40:
        status = "warm"
    else:
        status = "cold"

    return score, status
