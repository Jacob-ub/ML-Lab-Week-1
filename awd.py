

# 1
scores = [72, 85, 90, 68, 88]


print("Scores:", scores)

average = sum(scores) / len(scores)
print("Average score:", average)

print("Highest score:", max(scores))
print("Lowest score:", min(scores))

#2
study_hours = [1, 2, 3, 4, 5]
exam_scores = [50, 55, 65, 70, 80]

for hours, score in zip(study_hours, exam_scores):
    print(f"Input: {hours} hours → Output: {score} marks")


#3
def pass_fail(score):
    if score >= 60:
        return "Pass"
    else:
        return "Fail"

scores = [45, 67, 82, 59]

for s in scores:
    print(f"Score: {s} → Result: {pass_fail(s)}")

#4

sizes = [500, 800, 1000, 1200]
prices = [50, 80, 100, 130]

for size, price in zip(sizes, prices):
    print(f"House size: {size} sq ft → Price: {price}")

positive_trend = True

for i in range(1, len(prices)):
    if prices[i] <= prices[i - 1]:
        positive_trend = False
        break

#5



if positive_trend:
    print("Positive trend")
