def solution(S, P, Q):
    N = len(S)
    M = len(P)

    impact_factors = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

    # Calculate prefix sums for each nucleotide type
    prefix_sums = [[0] * (N + 1) for _ in range(4)]
    for i in range(1, N + 1):
        for j in range(4):
            prefix_sums[j][i] = prefix_sums[j][i - 1]
        prefix_sums[impact_factors[S[i - 1]] - 1][i] += 1
        print(i, S[i-1])
        print(prefix_sums)

print(":1 ~ ~ ~ ~ ~ ~ ~ ~ ~")

S = "CAGCCTA"
P = [2, 5, 0]
Q = [4, 5, 6]
print(solution(S, P, Q))  # Output: [2, 4, 1]

print(":2 ~ ~ ~ ~ ~ ~ ~ ~ ~")

print(solution('AGCT', [], []))

print(":3 ~ ~ ~ ~ ~ ~ ~ ~ ~")

print(solution('AACT', [], []))