from utils import calculate_average, greetings

def func() -> None:
    print(greetings('Sourav'))
    data = [23.5,45,77,99.34]
    print(f'Your average is : {calculate_average(data)}')

if __name__ == "__main__":
    func()