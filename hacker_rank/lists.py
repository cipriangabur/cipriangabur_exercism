if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        action = input()
        action_steps = action.split()
        if "insert" in action:
            arr.insert(int(action_steps[1]), int(action_steps[2]))
        elif "print" in action:
            print(arr)
        elif action_steps[0] in ['remove', 'append']:
            exec(f"arr.{action_steps[0]}({int(action_steps[1])})")
        elif "sort" in action:
            arr.sort()
        elif "pop" in action:
            arr.pop(-1)
        elif "reverse" in action:
            arr = arr[::-1]
