#SAFE RIDING CAR PROGRAM
def check_alarm(DRIV, PASS, BELTD, BELTP, IGN):
    """
    DRIV  : 1 if driver is seated
    PASS  : 1 if passenger is seated
    BELTD : 0 if driver's seatbelt is unfastened
    BELTP : 0 if passenger's seatbelt is unfastened
    IGN   : 1 if ignition is ON

    Returns: 'ALARM ON' if alarm should activate (LOW), else 'ALARM OFF'
    """
    if IGN == 1:
        if (
            (DRIV == 1 and PASS == 0 and BELTD == 0 and BELTP == 0) or
            (DRIV == 1 and PASS == 0 and BELTD == 0 and BELTP == 1) or
            (DRIV == 1 and PASS == 1 and BELTD == 0 and BELTP == 0) or
            (DRIV == 1 and PASS == 1 and BELTD == 0 and BELTP == 1) or
            (DRIV == 1 and PASS == 1 and BELTD == 1 and BELTP == 0)
        ):
            return "ALARM ON"
    return "ALARM OFF"

# TEST CASES
print(check_alarm(0, 0, 0, 0, 1))  
print(check_alarm(0, 0, 0, 1, 1))  
print(check_alarm(0, 0, 1, 0, 1))  
print(check_alarm(0, 0, 1, 1, 1))  
print(check_alarm(0, 1, 0, 0, 1))  
print(check_alarm(0, 1, 0, 1, 1))  
print(check_alarm(0, 1, 1, 0, 1))  
print(check_alarm(0, 1, 1, 1, 1))  
print(check_alarm(1, 0, 0, 0, 1))  #ALARM IS ACTIVATED
print(check_alarm(1, 0, 0, 1, 1))  #ALARM IS ACTIVATED
print(check_alarm(1, 0, 1, 0, 1))  
print(check_alarm(1, 0, 1, 1, 1))  
print(check_alarm(1, 1, 0, 0, 1))   #ALARM IS ACTIVATED  
print(check_alarm(1, 1, 0, 1, 1))   #ALARM IS ACTIVATED 
print(check_alarm(1, 1, 1, 0, 1))   #ALARM IS ACTIVATED
print(check_alarm(1, 1, 1, 1, 1))  
