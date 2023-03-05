# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    int_list = [int(i) for i in input().split()]
    int_tuple = tuple(int_list)
    print(int_tuple)
    print(hash(int_tuple))