# Report

## 1) Empirical Comparison

For the three input files located in the data folder created with create_test_data.py, OPTFF had the fewest cache misses in every case. On File1, FIFO had 33 misses, LRU had 35, and OPTFF had 22. On File2, FIFO had 59 misses, LRU had 57, and OPTFF had 40. On File3, FIFO had 71 misses, LRU had 72, and OPTFF had 45.

These results show that OPTFF performed best overall, which is what we would expect since it replaces the item whose next use is farthest in the future. FIFO and LRU were much closer to each other, but neither was consistently better across all three files. FIFO did slightly better than LRU on File1 and File3, while LRU did slightly better than FIFO on File2. Overall, the difference between FIFO and LRU was small in these tests, but OPTFF clearly outperformed both of them.

## 2) Bad Sequence for LRU or FIFO

Yes, such a sequence exists. For k = 3, one example is 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5

For this sequence, OPTFF has strictly fewer misses than both LRU and FIFO. With cache size 3, OPTFF gives 7 misses. On the same sequence, FIFO gives 9 misses and LRU gives 10 misses.

This happens because OPTFF always evicts the item whose next use is farthest in the future, so it makes the best possible choice at each miss. LRU and FIFO do not know the future, so they can evict an item that will be needed again soon. In this sequence, that causes both of them to make extra replacements later, which increases the total number of misses. So this example shows that for k = 3, there is definitely a request sequence where OPTFF performs strictly better than LRU, and also strictly better than FIFO.

## 3) Prove OPTFF is Optimal

Assume for contradiction that OPTFF is not optimal. Then for some fixed request sequence, there is an offline algorithm A with fewer misses than OPTFF. Choose such an algorithm A that agrees with OPTFF for as long as possible, and let t be the first step where they differ. Before time t, both algorithms have made the same decisions, so their cache contents are identical. At time t, the request must be a miss, since on a hit there is no eviction choice to differ on. Suppose OPTFF evicts page x, while A evicts a different page y. Since OPTFF evicts the page used farthest in the future, page x is requested no earlier than page y. Now modify A to create a new algorithm A′ that is identical to A, except that at time t it evicts x instead of y. After that, follow A as closely as possible. Because y is needed before x, keeping y cannot be worse than keeping x. So A′ has no more misses than A. But now A′ is still optimal and agrees with OPTFF one step longer than A, which contradicts the choice of A.
Therefore the assumption was false. No offline algorithm can have fewer misses than OPTFF on any fixed request sequence, so OPTFF is optimal.
