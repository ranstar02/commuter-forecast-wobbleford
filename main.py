#!/usr/bin/env python3
"""Write one original weather-forecast line for a fictional city."""

import os

FORECAST = (
    "Light rain in Wobbleford tomorrow, clearing by noon - "
    "the ducks have filed a formal complaint, "
    "and the 8:40 commuters are signing it too."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORECAST)


if __name__ == "__main__":
    main()
