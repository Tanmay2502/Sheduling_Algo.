def round_robin(processes):
    n = len(processes)
    remaining_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    total_waiting_time = 0
    total_turnaround_time = 0
    time = 0

    for i in range(n):
        remaining_time[i] = processes[i][1]

    while True:
        done = True
        for i in range(n):
            if remaining_time[i] > 0:
                done = False
                quantum = max(1, remaining_time[i] // 2)  # Half of the burst time
                time += quantum
                remaining_time[i] -= quantum

                if remaining_time[i] == 0:
                    turnaround_time[i] = time
                    waiting_time[i] = time - processes[i][1]

        if done:
            break

    for i in range(n):
        total_waiting_time += waiting_time[i]
        total_turnaround_time += turnaround_time[i]

    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n

    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i][0]}\t\t\t{processes[i][1]}\t\t\t{waiting_time[i]}\t\t\t{turnaround_time[i]}")

    print("Average Waiting Time:", avg_waiting_time)
    print("Average Turnaround Time:", avg_turnaround_time)

# Example usage:
processes = [("P1", 10), ("P2", 5), ("P3", 8), ("P4", 7)]
round_robin(processes)
