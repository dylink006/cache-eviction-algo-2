
import random
def main(filepath, k, m, min, max):
    requests = []
    for i in range(m):
        requests.append(random.randint(min, max))

    with open(filepath, 'w') as f:
        f.write(f"{k} {m}\n")
        f.write(" ".join(str(r) for r in requests))

if __name__ == "__main__":
    main("../data/test_data_1", 3, 60, 1, 8)
    main("../data/test_data_2", 5, 75, 1, 12)
    main("../data/test_data_3", 7, 100, 1, 15)