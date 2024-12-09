def create_matrix(file_path):
    matrix = []
    with open(file_path, 'r') as f:
        for line in f.readlines():
            matrix.append([int(x) for x in line.strip().split(' ')])
    return matrix

def is_monotonic(lst):
    return all(lst[i] < lst[i+1] for i in range(len(lst)-1)) or \
           all(lst[i] > lst[i+1] for i in range(len(lst)-1))

def is_within_range(lst):
    for i in range(1, len(lst)):
        if not (1 <= abs(lst[i] - lst[i-1]) <= 3):
            return False
    return True

def is_safe_report(lst):
    return is_monotonic(lst) and is_within_range(lst)

def is_safe_with_dampener(lst):
    if is_safe_report(lst):
        return True

    for i in range(len(lst)):
        new_lst = lst[:i] + lst[i+1:]
        if is_safe_report(new_lst):
            return True

    return False

def count_safe_reports(matrix):
    safe_reports = 0
    for row in matrix:
        if is_safe_with_dampener(row):
            safe_reports += 1
    return safe_reports

readings = create_matrix('input.txt')
safe_reports = count_safe_reports(readings)
print(safe_reports)
