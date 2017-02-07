

# K-factor determines the severity of each game
K = 200

# Given current ratings of two players, return their potential rating gains
def getPotentialRatingGains(rating_1, rating_2):
    # 1. Calculate transformed ratings R_n
    TRating_1 = 10 ** (rating_1/400.0)
    TRating_2 = 10 ** (rating_2/400.0)

    # 2. Calculate "Expected score"
    Expected_1 = TRating_1 / (TRating_1 + TRating_2)
    Expected_2 = TRating_2 / (TRating_1 + TRating_2)

    return {
        "player_1": {
            "wins": K*(1 - Expected_1),
            "loses": K*(0 - Expected_1)
        },
        "player_2": {
            "wins": K*(1 - Expected_2),
            "loses": K*(0 - Expected_2)
        }
    }
