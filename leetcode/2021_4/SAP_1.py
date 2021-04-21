from collections import defaultdict
def main():
    cities = defaultdict(bool)
    city_num = int(input())
    for i in range(city_num):
        city = input()
        cities[city] = True
    return len(cities.keys())
if __name__ == '__main__':
    test_case = int(input())
    for i in range(test_case):
        print(main())