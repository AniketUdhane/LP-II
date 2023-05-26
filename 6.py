# job sch
# User input for number of jobs and their respective deadlines and profits
n = int(input("Enter the number of jobs: "))
jobs = []
for i in range(n):
    deadline, profit = map(int, input(f"Enter deadline and profit for job {i+1}: ").split())
    jobs.append((deadline, profit))

# Sorting jobs in descending order of profit
jobs.sort(key=lambda x: x[1], reverse=True)

# Greedy algorithm for scheduling jobs
schedule = [0] * n
for i in range(n):
    for j in range(min(n, jobs[i][0])-1, -1, -1):
        if schedule[j] == 0:
            schedule[j] = i+1
            break

# Printing the schedule
print("Job sequence:", schedule)
