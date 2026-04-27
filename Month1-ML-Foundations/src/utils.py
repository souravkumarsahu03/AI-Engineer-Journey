from typing import List

def calculate_average(numbers: List[float]) -> float:
    return sum(numbers)/len(numbers)

def greetings(name: str) -> str:
    return f"Hello {name}, welcome to AI journey."