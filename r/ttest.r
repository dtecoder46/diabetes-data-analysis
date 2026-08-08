class1 = read.csv("diabetes_class1.csv")

# Diastolic benchmark for hypertension: 80 mmHg
# H0: average blood pressure = 80 mmHg
# Ha: average blood pressure > 80 mmHg

blood_pressure = class1[2]

results = t.test(blood_pressure,  alternative='g', mu=80)

results2 = t.test(blood_pressure,  alternative='l', mu=80)

print(results)
print(results2)
