def player(prev_play, opp_history=[], my_history=[], patterns={}):
    # New match starts -> forget everything from the last opponent
    if prev_play == "":
        opp_history.clear()
        my_history.clear()
        patterns.clear()
    else:
        opp_history.append(prev_play)

    beats = {"R": "P", "P": "S", "S": "R"}
    n = 3
    guess = "R"

    # Each round = my move + their move, e.g. "RP"
    rounds = [m + o for m, o in zip(my_history, opp_history)]

    if len(rounds) > n:
        # Learn: after these n rounds, the opponent played X
        key = "".join(rounds[-(n + 1):-1]) + opp_history[-1]
        patterns[key] = patterns.get(key, 0) + 1

        # Predict: after the last n rounds, which move was most common?
        recent = "".join(rounds[-n:])
        counts = {m: patterns.get(recent + m, 0) for m in "RPS"}
        predicted = max(counts, key=counts.get)
        guess = beats[predicted]

    my_history.append(guess)
    return guess