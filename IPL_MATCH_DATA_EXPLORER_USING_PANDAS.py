# =========================================================
# 🏏 IPL MATCH DATA EXPLORER USING PANDAS
# =========================================================

import pandas as pd

# =========================================================
# STEP 1 — LOAD DATASET
# =========================================================

matches = pd.read_csv(r"try\tasks\matches.csv")

print("=================================================")
print("📌 FIRST 5 ROWS")
print("=================================================")

print(matches.head())


# =========================================================
# STEP 2 — DATASET INFORMATION
# =========================================================

print("\n=================================================")
print("📊 DATASET INFO")
print("=================================================")

print(matches.info())


# =========================================================
# STEP 3 — STATISTICAL SUMMARY
# =========================================================

print("\n=================================================")
print("📈 DATASET SUMMARY")
print("=================================================")

print(matches.describe())


# =========================================================
# STEP 4 — MATCHES PLAYED EACH SEASON
# =========================================================

print("\n=================================================")
print("🏏 MATCHES PLAYED EACH SEASON")
print("=================================================")

matches_per_season = matches['season'].value_counts()

print(matches_per_season)


# =========================================================
# STEP 5 — TEAM WITH MOST WINS
# =========================================================

print("\n=================================================")
print("🏆 TEAM WITH MOST WINS")
print("=================================================")

most_wins = matches['winner'].value_counts()

print(most_wins)

print("\nTop Winning Team:")
print(most_wins.idxmax())


# =========================================================
# STEP 6 — MATCHES AT SPECIFIC VENUE
# =========================================================

print("\n=================================================")
print("🏟️ MATCHES AT WANKHEDE STADIUM")
print("=================================================")

venue_matches = matches[
    matches['venue'] == 'Wankhede Stadium'
]

print(venue_matches)


# =========================================================
# STEP 7 — TOP 5 PLAYER OF THE MATCH
# =========================================================

print("\n=================================================")
print("⭐ TOP 5 PLAYER OF THE MATCH WINNERS")
print("=================================================")

top_players = matches[
    'player_of_match'
].value_counts().head(5)

print(top_players)


# =========================================================
# STEP 8 — CHECK NULL VALUES
# =========================================================

print("\n=================================================")
print("❓ NULL VALUES")
print("=================================================")

print(matches.isnull().sum())


# =========================================================
# STEP 9 — DROP NULL VALUES
# =========================================================

cleaned_matches = matches.dropna()

print("\n=================================================")
print("✅ CLEANED DATASET INFO")
print("=================================================")

print(cleaned_matches.info())


# =========================================================
# STEP 10 — SORT DATA BY SEASON
# =========================================================

print("\n=================================================")
print("📅 SORTED DATA")
print("=================================================")

sorted_matches = matches.sort_values(by='season')

print(sorted_matches.head())


# =========================================================
# STEP 11 — GROUPBY EXAMPLE
# =========================================================

print("\n=================================================")
print("📌 TOTAL WINS BY TEAM")
print("=================================================")

grouped = matches.groupby('winner').size()

print(grouped)


# =========================================================
# BONUS CHALLENGE
# =========================================================

print("\n=================================================")
print("🔥 BONUS CHALLENGE")
print("=================================================")

bat_first = matches[
    matches['toss_decision'] == 'bat'
]

field_first = matches[
    matches['toss_decision'] == 'field'
]

bat_win_percentage = (
    (bat_first['toss_winner'] == bat_first['winner']).mean()
) * 100

field_win_percentage = (
    (field_first['toss_winner'] == field_first['winner']).mean()
) * 100

print(f"Bat First Win %    : {bat_win_percentage:.2f}%")
print(f"Field First Win %  : {field_win_percentage:.2f}%")


# =========================================================
# FINAL MESSAGE
# =========================================================

print("\n=================================================")
print("✅ IPL DATA ANALYSIS COMPLETED SUCCESSFULLY!")
print("=================================================")