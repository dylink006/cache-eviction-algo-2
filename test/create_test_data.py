
import random
def main(filepath, k, m, min_val, max_val):
    requests = []
    for i in range(m):
        requests.append(random.randint(min_val, max_val))

    with open(filepath, 'w') as f:
        f.write(f"{k} {m}\n")
        f.write(" ".join(str(r) for r in requests))

if __name__ == "__main__":
    main("../data/test_data_1", 3, 60, 1, 6)
    main("../data/test_data_2", 4, 80, 1, 12)
    main("../data/test_data_3", 6, 100, 1, 20)