
months = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(months["Nov"])
print(months["Jan"])
print(months.get("Aug"))
print(months.get("hello"))
print(months.get("hello", "Invalid key"))

monthsConversion = {
    0: "January",
    1: "February",
}

print(monthsConversion[0])
print(monthsConversion.get(1))