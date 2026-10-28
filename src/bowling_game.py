class BowlingGame:
    def __init__(self) -> None:
        self.rolls: list[int] = []

    def roll(self, pins: int) -> None:
        if pins < 0 or pins > 10:
            raise ValueError("Pins must be between 0 and 10")

        self.rolls.append(pins)

    def _is_strike(self, roll_index: int) -> bool:
        return self.rolls[roll_index] == 10

    def _is_spare(self, roll_index: int) -> bool:
        return (
            not self._is_strike(roll_index)
            and self.rolls[roll_index] + self.rolls[roll_index + 1] == 10
        )

    def score(self) -> int:
        total = 0
        roll_index = 0

        for i in range(10):
            if roll_index >= len(self.rolls):
                break

            if self._is_strike(roll_index):
                if roll_index + 2 >= len(self.rolls):
                    break
                total += self._score_frame(roll_index)
                roll_index += 1

            elif roll_index + 1 >= len(self.rolls):
                break

            elif self._is_spare(roll_index):
                if roll_index + 2 >= len(self.rolls):
                    total += 10
                    break
                total += self._score_frame(roll_index)
                roll_index += 2

            else:
                total += self._score_frame(roll_index)
                roll_index += 2

        return total

    def _score_frame(self, roll_index: int) -> int:
        if self._is_strike(roll_index):
            return (
                10
                + self.rolls[roll_index + 1]
                + self.rolls[roll_index + 2]
            )

        if self._is_spare(roll_index):
            return 10 + self.rolls[roll_index + 2]

        return self.rolls[roll_index] + self.rolls[roll_index + 1]