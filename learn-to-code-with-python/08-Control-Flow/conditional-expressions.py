zip_code = "902110"

if len(zip_code) == 5:
    check = "valid"
else:
    check = "invalid"

check = "Valid" if len(zip_code) == 5 else "Invalid"
print(check)