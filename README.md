# Programming Assignment 2: Cache Replacement Policies

This repo implements and compares three cache replacement policies:

- FIFO (First-In, First-Out)
- LRU (Least Recently Used)
- OPTFF (Optimal Farther-in-the-Future)

Given a cache size and a sequence of page requests, the program simulates each policy and reports the total number of cache misses for each one.

## Author

Dylan McGarry (UFID: 66318896)

## Input Format

Each input file contains two lines:

<k> <m>
<request_1> <request_2> ... <request_m>

- k is the cache size.
- m is the number of requests.
- The second line contains the request sequence as space-separated integers.

Example:

3 10
1 2 3 4 1 2 5 1 2 3

## Output Format

For each input file, the program prints the number of cache misses for each policy in the format:

FIFO  : <misses>
LRU   : <misses>
OPTFF : <misses>

Example:

FIFO  : 8
LRU   : 7
OPTFF : 6

## Setup

This project uses only Python’s standard library, so no additional packages are required.

## Running

To run the simulator on a single input file:

python3 main.py <filename>

Example:

python3 main.py ../data/test_data_1

You can also run the program on multiple input files in one command:

python3 main.py <filename1> <filename2> <filename3>

Example:

python3 main.py ../data/test_data_1 ../data/test_data_2 ../data/test_data_3

If no file path is provided, the program prints a usage message.

## Generating Test Data

The file create_test_data.py creates random request sequences and writes them to files in the expected input format.

To run it:

pyhon3 create_test_data.py

This generates example files such as:

- ../data/test_data_1
- ../data/test_data_2
- ../data/test_data_3

Each generated file contains the cache size and number of requests on the first line and the request sequence on the second line as required for main.py to run

## Cache Policies

### FIFO

FIFO evicts the page that has been in the cache the longest.

### LRU

LRU evicts the page that has not been used for the longest time.

### OPTFF

OPTFF evicts the page whose next use is farthest in the future (or is never used again). This is the optimal offline policy and serves as a benchmark for comparison.

### Files

- main.py is the CLI entry point that reads input files, runs all three cache simulations, and prints miss counts.
- fifo.py contains the FIFO cache implementation.
- lru.py contains the LRU cache implementation.
- optff.py contains the OPTFF cache implementation.
- create_test_data.py generates sample/random input files for testing.