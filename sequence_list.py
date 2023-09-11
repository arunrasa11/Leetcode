def solution(sequence):
    n = len(sequence)
    if n == 1:
        return True

    for i in range(n - 1):
        if sequence[i] >= sequence[i + 1]:
            seq1 = list(sequence)
            seq1.pop(i)
            seq2 = list(sequence)
            seq2.pop(i + 1)
            break

    fail = False
    for i in range(len(seq1) - 1):
        if seq1[i] >= seq1[i + 1]:
            fail = True
            break

    for i in range(len(seq2) - 1):
        if seq2[i] >= seq2[i + 1]:
            if fail:
                return False
    return True


sequence=[10, 1, 2, 3, 4, 5]
print(solution(sequence))



