class BowlingStatsCalculator:
    def __init__(self, scores):
        self.scores = scores

    def calculate_average(self):
        return sum(self.scores) / len(self.scores)

    def calculate_median(self):
        sorted_scores = sorted(self.scores)
        n = len(sorted_scores)
        midpoint = n // 2
        if n % 2 == 1:
            return sorted_scores[midpoint]
        else:
            return (sorted_scores[midpoint - 1] + sorted_scores[midpoint]) / 2

    def calculate_mode(self):
        from collections import Counter
        score_counts = Counter(self.scores)
        max_count = max(score_counts.values())
        return [score for score, count in score_counts.items() if count == max_count]

    def top_n_scores(self, n=10):
        return sorted(self.scores, reverse=True)[:n]

# User Input
user_input = input("Enter bowling scores separated by commas: ")

# Parse the user input into a list of integers
scores = [int(score.strip()) for score in user_input.split(',')]

# Create an instance of BowlingStatsCalculator
calculator = BowlingStatsCalculator(scores)

# Calculate and display various statistics
print("Average Score:", calculator.calculate_average())
print("Median Score:", calculator.calculate_median())
print("Mode Score(s):", calculator.calculate_mode())
print("Top 10 Scores:", calculator.top_n_scores())
