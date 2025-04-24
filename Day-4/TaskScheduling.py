def Find(tasks,time_slice):
    task_ids=list(range(1, len(tasks)+1))
    remaining=list(tasks)
    time = 0
    print("Test case 1:")

    while any(t > 0 for t in remaining):
        for i in range(len(remaining)):
            if remaining[i] > 0:
                run = min(time_slice,remaining[i])
                time += run
                remaining[i] -= run
                print(f"Task {task_ids[i]} run for {run} units. -{time}")
    print(f"Total execution time: {time}")

tasks=(10,5,8)
time_slice=4
Find(tasks,time_slice)
