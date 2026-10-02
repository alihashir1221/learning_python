def clean_name(name):
        lo_cleaned = name.strip().lower()
        up_cleaned = lo_cleaned.upper()
        return lo_cleaned, up_cleaned
lo_cleaned, up_cleaned = clean_name("MarriAAA")
print(up_cleaned)
print(lo_cleaned)
