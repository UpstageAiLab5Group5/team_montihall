def monty_hall_no_random():
    doors = [0, 1, 2]
    total_cases = 0
    switch_wins = 0
    stay_wins = 0
    switch_win_rate = switch_wins / total_cases
    stay_win_rate = stay_wins / total_cases
    print(f"선택을 유지한 경우 승리 확률: {stay_win_rate:.2%}")
    print(f"선택을 바꾼 경우 승리 확률: {switch_win_rate:.2%}")

if __name__ == "__main__":
    monty_hall_no_random()
