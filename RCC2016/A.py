targetPass = input()
targetPassLetters = set(targetPass)
N = int(input())

tries = map(lambda i: input(), range(0, N))

tryResults = map(
    lambda tryStr: (
        len([c for i, c in enumerate(tryStr) if targetPass[i] == c]),
        len([c for i, c in enumerate(tryStr) if targetPass[i] != c and c in targetPassLetters])
    ),
    tries
)

for rightCharsCnt, wrongPlaceCharsCnt in tryResults:
    print(rightCharsCnt, wrongPlaceCharsCnt)