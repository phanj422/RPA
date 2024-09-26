def sumfunc(n):
    return sum(range(1, n + 1))
num = int(input("정수를 입력하세요 : "))
if num < 1:
    print("1 이상의 정수를 입력하세요")
else:
    result = sumfunc(num)
    print(f"1부터 {num}까지의 합은 {result} 입니다.")