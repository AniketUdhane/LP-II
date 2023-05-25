'''
def job_scheduling(jobs):
    # Sort the jobs in increasing order of deadlines
    sorted_jobs = sorted(jobs, key=lambda x: x[1])

    # Initialize the schedule and current time
    schedule = []
    current_time = 0

    # Iterate over the sorted jobs and schedule them
    for job in sorted_jobs:
        duration = job[0]
        deadline = job[1]

        # Check if the job can be scheduled without missing the deadline
        if current_time + duration <= deadline:
            schedule.append(job)
            current_time += duration

    return schedule

# Example usage
jobs = [(2, 5), (1, 4), (4, 7), (3, 6), (2, 3)]
schedule = job_scheduling(jobs)

print("Scheduled Jobs:")
for job in schedule:
    print(f"Duration: {job[0]}, Deadline: {job[1]}")

'''

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
