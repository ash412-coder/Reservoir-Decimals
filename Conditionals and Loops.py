def is_equal(left, right, tolerance) -> bool:
    return abs(left - right) <= tolerance

def get_decimal() -> float:
    attempts = 0
    while attempts < 3:
        user_input = input("Enter number: ")
        if user_input.strip() == "":
            attempts += 1
        else:
            try:
                return float(user_input)
            except ValueError:
                print("Invalid input. Try again.")
    print("I give up, you get 0")
    return 0.0

def check_decimal(tolerance: float) -> None:
    num1 = get_decimal()
    num2 = get_decimal()
    if is_equal(num1, num2, tolerance):
        print("Numbers ARE approximately equal")
    else:
        print("Numbers are NOT approximately equal")

#1 Tests
print("Task 1 Test:")
print(is_equal(1.23, 1.24, 0.02))  
print(is_equal(3.1415, 3.1416, 0.00001))  
print(is_equal(100.0, 100.0, 0.001))  


def check_reservoir(volume_m3, inflow_lph, outflow_lps) -> bool:
    if volume_m3 < 0 or inflow_lph < 0 or outflow_lps < 0:
        print("Volume cannot be negative")
        return False

    volume_L = volume_m3 * 1000
    inflow_lpm = inflow_lph / 60
    current_volume = volume_L / 2

    for minute in range(1, 481):
        current_volume += inflow_lpm - outflow_lps
        if current_volume <= 0:
            print(f"Reservoir runs out at minute {minute}")
            return False
        elif current_volume > volume_L:
            print(f"Reservoir overflows at minute {minute}")
            return False

    print("Reservoir is fine after 8 hours")
    return True

#2 Test
print("\nTask 2 Test Cases:")
check_reservoir(1500, 4800, 27.1)        
check_reservoir(120.25, 8500, 1.1)       
check_reservoir(550, 217.5, 10)          
check_reservoir(475, 75000, 5.5)         
check_reservoir(-550, 217.5, 10)         




def collatz(n: int) -> None:
    if n < 1:
        print("Starting number must be at least 1.")
        return
    while n != 1:
        print(n, end=' ')
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    print(n)  

#3 Test
print("\nTask 3 Test Case:")
collatz(35)
