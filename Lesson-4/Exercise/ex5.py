def main():
    while True:
        n = int(input("Nhập 1 số nguyên n từ bàn phím, 10 < n < 100: "))
        if 10 < n < 100:
            break
        print("Giá trị không hợp lệ, vui lòng thử lại.")
        
    result_a = sum(range(1, n + 1))
    print(f"Tổng a: {result_a}")
    
    result_b = sum(i if i % 2 else -i for i in range(1, n + 1))
    print(f"Tổng b: {result_b}")

    result_c = sum(1 / i for i in range(1, n + 1))
    print(f"Tổng c: {result_c}")

    result_d = sum(2 ** i for i in range(1, n + 1))
    print(f"Tổng d: {result_d}")

    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    print(f"Giai thừa e: {factorial}")

    def is_prime(num):
        if num <= 1:
            return False
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                return False
        return True

    sum_f = sum(i for i in range(2, n + 1) if is_prime(i))
    print(f"Tổng f: {sum_f}")

if __name__ == "__main__":
    main()