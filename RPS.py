import random


def player(prev_play, opponent_history=[]):
    # Store opponent's last moves
    if prev_play:
        opponent_history.append(prev_play)

    # Initialize guess to "R" as a fallback
    guess = "R"

    # Define the length of pattern to track
    pattern_length = 3
    sequence_map = {}

    # Only analyze if we have enough history
    if len(opponent_history) > pattern_length:
        # Get recent pattern
        recent_pattern = ''.join(opponent_history[-pattern_length:])

        # Build pattern frequencies
        for i in range(len(opponent_history) - pattern_length):
            pattern = ''.join(opponent_history[i:i + pattern_length])
            next_move = opponent_history[i + pattern_length]
            if pattern not in sequence_map:
                sequence_map[pattern] = {"R": 0, "P": 0, "S": 0}
            sequence_map[pattern][next_move] += 1

        # Determine the likely next move based on observed patterns
        if recent_pattern in sequence_map:
            likely_next_move = max(sequence_map[recent_pattern], key=sequence_map[recent_pattern].get)

            # Counter the likely next move with a slight variation to reduce ties
            # We favor the counter move but occasionally randomize to avoid predictable patterns
            if random.random() < 0.7:
                guess = {"R": "P", "P": "S", "S": "R"}[likely_next_move]  # 70% chance to counter directly
            else:
                # Choose an alternative counter for variation
                guess = random.choice(["R", "P", "S"])

        else:
            # Fallback to a counter of the last move if no pattern detected
            guess = {"R": "P", "P": "S", "S": "R"}[opponent_history[-1]]

    return guess
