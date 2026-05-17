# =========================================================
# 📊 Student Grade Analyzer using NumPy
# =========================================================
# Objective:
# Analyze students' marks using NumPy arrays
# Import NumPy Library
import numpy as np


# =========================================================
# STEP 1 — Generate Random Student Scores
# =========================================================
# Generate 50 random marks between 0 and 100

scores = np.random.randint(0, 100, size=50)

print("=================================================")
print("📌 ORIGINAL STUDENT SCORES")
print("=================================================")
print(scores)


# =========================================================
# STEP 2 — Basic Statistical Analysis
# =========================================================

# Mean (Average Score)
mean_score = np.mean(scores)

# Median (Middle Value)
median_score = np.median(scores)

# Standard Deviation (Spread of Data)
std_deviation = np.std(scores)

# Highest Marks
highest_score = np.max(scores)

# Lowest Marks
lowest_score = np.min(scores)

print("\n=================================================")
print("📊 STATISTICAL ANALYSIS")
print("=================================================")

print(f"✅ Mean Score            : {mean_score:.2f}")
print(f"✅ Median Score          : {median_score}")
print(f"✅ Standard Deviation    : {std_deviation:.2f}")
print(f"✅ Highest Score         : {highest_score}")
print(f"✅ Lowest Score          : {lowest_score}")


# =========================================================
# STEP 3 — Find Failed Students
# =========================================================
# Students scoring below 40 are considered failed

failed_students = scores[scores < 40]

print("\n=================================================")
print("❌ FAILED STUDENTS (Marks < 40)")
print("=================================================")

print(failed_students)

print(f"\nTotal Failed Students: {len(failed_students)}")


# =========================================================
# STEP 4 — Find Distinction Students
# =========================================================
# Students scoring above 85 get distinction

distinction_students = scores[scores > 85]

print("\n=================================================")
print("🏆 DISTINCTION STUDENTS (Marks > 85)")
print("=================================================")

print(distinction_students)

print(f"\nTotal Distinction Students: {len(distinction_students)}")


# =========================================================
# STEP 5 — Normalize the Scores
# =========================================================
# Formula:
# normalized_value = (x - min) / (max - min)
#
# Purpose:
# Convert marks into range 0 to 1

normalized_scores = (
    (scores - np.min(scores))
    /
    (np.max(scores) - np.min(scores))
)

print("\n=================================================")
print("📈 NORMALIZED SCORES (0 to 1)")
print("=================================================")

print(normalized_scores)


# =========================================================
# STEP 6 — Reshape the Array
# =========================================================
# Convert 1D array into 5 rows × 10 columns
#
# Assume:
# 5 Subjects
# 10 Students

reshaped_scores = scores.reshape(5, 10)

print("\n=================================================")
print("🧩 RESHAPED SCORE MATRIX (5 × 10)")
print("=================================================")

print(reshaped_scores)


# =========================================================
# STEP 7 — Calculate Subject-wise Average
# =========================================================
# axis = 1 means row-wise calculation

subject_averages = np.mean(reshaped_scores, axis=1)

print("\n=================================================")
print("📚 SUBJECT-WISE AVERAGES")
print("=================================================")

for i, avg in enumerate(subject_averages, start=1):
    print(f"Subject {i} Average Marks : {avg:.2f}")


# =========================================================
# BONUS CHALLENGE
# =========================================================
# Weighted Final Scores
#
# Weightage:
# Theory   = 40%
# Practical = 60%
# =========================================================

# Generate Theory Marks
theory_marks = np.random.randint(0, 100, size=50)

# Generate Practical Marks
practical_marks = np.random.randint(0, 100, size=50)

# Calculate Final Weighted Scores
final_scores = (
    (0.4 * theory_marks)
    +
    (0.6 * practical_marks)
)

print("\n=================================================")
print("📝 WEIGHTED FINAL SCORES")
print("=================================================")

print(final_scores)


# =========================================================
# TOPPER ANALYSIS
# =========================================================

topper_score = np.max(final_scores)

print("\n=================================================")
print("🥇 TOPPER DETAILS")
print("=================================================")

print(f"Highest Final Score : {topper_score:.2f}")


# =========================================================
# FINAL SUMMARY
# =========================================================

print("\n=================================================")
print("📌 FINAL SUMMARY")
print("=================================================")

print(f"Total Students              : {len(scores)}")
print(f"Average Class Score         : {mean_score:.2f}")
print(f"Number of Failed Students   : {len(failed_students)}")
print(f"Number of Distinction       : {len(distinction_students)}")
print(f"Highest Score               : {highest_score}")
print(f"Lowest Score                : {lowest_score}")

print("\n✅ Student Grade Analysis Completed Successfully!")