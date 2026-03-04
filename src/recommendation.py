def recommend_coaches(predicted_passengers, coaches):

    seats_per_coach = 72
    capacity = coaches * seats_per_coach

    if predicted_passengers > capacity:

        extra = int((predicted_passengers - capacity) / seats_per_coach) + 1

        return f"Add {extra} extra coaches"

    elif predicted_passengers < capacity * 0.5:

        return "Train underutilized"

    else:

        return "Capacity sufficient"