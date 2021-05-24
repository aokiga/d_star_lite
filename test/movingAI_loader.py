passable = ['.', 'G', 'W', 'S']


def read_map_from_ai_file(path):
    tasks_file = open(path)

    tasks_file.readline()

    height = int(tasks_file.readline().split()[1])
    width = int(tasks_file.readline().split()[1])

    tasks_file.readline()

    cells = [[0 for _ in range(width)] for _ in range(height)]
    i = 0
    j = 0

    for l in tasks_file:
        j = 0
        for c in l:
            if c in passable:
                cells[i][j] = 0
            else:
                cells[i][j] = 1
            j += 1
            if j == width:
                break

        if j != width:
            raise Exception("Size Error. Map width = ", j, ", but must be", width, "(map line: ", i, ")")

        i += 1
        if i == height:
            break

    return height, width, cells


def read_tasks_from_ai_file(path, amount):
    tasks = []
    tasks_file = open(path)
    tasks_file.readline()
    bucket = -1
    for line in tasks_file.readlines():
        curBucket = int(line.split()[0])
        if curBucket == bucket:
            continue
        bucket = curBucket
        task = line.split()[4:]
        tasks.append((int(task[1]), int(task[0]), int(task[3]), int(task[2])))
        if len(tasks) == amount:
            break
    return tasks
