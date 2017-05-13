from collections import Counter

from src.random_points import distance


def raw_majority_vote(labels):
    votes = Counter(labels)
    winner, _ = votes.most_common(1)[0]


def majority_vote(labels):
    """assume labels are ordered from nearest to farthest"""
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len([count
                       for count in vote_counts.values()
                       if count == winner_count])

    if num_winners == 1:
        return winner
    else:
        return majority_vote(labels[:-1])


def knn_classify(k, labeled_points, new_point):
    """each labeled point should be a pair (point label)"""

    # order the labeled points from nearest to farthest
    by_distance = sorted(labeled_points,
                         key = lambda (point, _) : distance(point, new_point))

    #find the labels for the k nearest
    k_nearest_labels = [label for _, label in by_distance[:k]]

    #and let them vote
    return majority_vote(k_nearest_labels)

def some_function():
    for k in [1, 3, 5, 7]:
        num_correct = 0

        for city in cities:
            location, actual_lang = city
            other_cities = [other_city
                            for other_city in cities
                            if other_city != city]

            predicted_lang = knn_classify(k, other_cities, location)

            if predicted_lang == actual_lang:
                num_correct += 1

        print(k, "neighbours", num_correct, "correct out of", len(cities))