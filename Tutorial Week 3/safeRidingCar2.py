# 🚗 SAFE RIDING CAR PROGRAM — STRICT 5 SCENARIOS
def check_alarm(DRIV, PASS, BELTD, BELTP, IGN):
    """
    Returns 'ALARM ON' only for the 5 specific scenarios defined in the pseudocode.
    Otherwise returns 'ALARM OFF'.
    """
    if (
        (DRIV == 1 and PASS == 0 and BELTD == 0 and BELTP == 0 and IGN == 1) or
        (DRIV == 1 and PASS == 0 and BELTD == 0 and BELTP == 1 and IGN == 1) or
        (DRIV == 1 and PASS == 1 and BELTD == 0 and BELTP == 0 and IGN == 1) or
        (DRIV == 1 and PASS == 1 and BELTD == 0 and BELTP == 1 and IGN == 1) or
        (DRIV == 1 and PASS == 1 and BELTD == 1 and BELTP == 0 and IGN == 1)
    ):
        return "ALARM ON"
    else:
        return "ALARM OFF"

# 🧪 Exhaustive Test Cases
print("🚦 SAFE RIDING CAR ALARM TESTS — STRICT MATCH")
print("-" * 50)

test_cases = [
    (0, 0, 0, 0, 1),
    (0, 0, 0, 1, 1),
    (0, 0, 1, 0, 1),
    (0, 0, 1, 1, 1),
    (0, 1, 0, 0, 1),
    (0, 1, 0, 1, 1),
    (0, 1, 1, 0, 1),
    (0, 1, 1, 1, 1),
    (1, 0, 0, 0, 1),  # ✅ ALARM ON
    (1, 0, 0, 1, 1),  # ✅ ALARM ON
    (1, 0, 1, 0, 1),
    (1, 0, 1, 1, 1),
    (1, 1, 0, 0, 1),  # ✅ ALARM ON
    (1, 1, 0, 1, 1),  # ✅ ALARM ON
    (1, 1, 1, 0, 1),  # ✅ ALARM ON
    (1, 1, 1, 1, 1),
]

for i, (DRIV, PASS, BELTD, BELTP, IGN) in enumerate(test_cases, start=1):
    result = check_alarm(DRIV, PASS, BELTD, BELTP, IGN)
    print(f"Test {i:02}: DRIV={DRIV}, PASS={PASS}, BELTD={BELTD}, BELTP={BELTP}, IGN={IGN} → {result}")
