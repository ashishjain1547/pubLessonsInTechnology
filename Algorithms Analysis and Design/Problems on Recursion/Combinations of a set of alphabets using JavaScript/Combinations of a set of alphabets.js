/*

Combinations ([A,B,C,D], 3) is equal to:
A + Combinations([B,C,D], 2) and
B + Combinations([C,D], 2)

~~~

Combs(ABCDE, 3) is equal to:
A + Combs(BCDE, 2) and
B + Combs(CDE, 2) and
C + Combs(DE, 2)

~~~

Combs(ABCDE, 2) is equal to:
A + Combs(BCDE, 1) and
B + Combs(CDE, 1) and
C + Combs(DE, 1) and
D + Combs(E, 1)

*/

function solution(A, n) {
    if (A.length == 1 || A.length == n) { 
        return [A]; 
    } else if (n == 1) {        
        return A.map(function (i){ return [i] });
    }
    
    const resultArr = []
    for (let i = 0; i < A.length - n + 1; i++) {
        let currentElement = A[i]

        otherElements = A.slice(i+1)
        subCombinations = solution(otherElements, n-1)
        
        for (let j = 0; j < subCombinations.length; j++) {
            
            resultArr.push([currentElement].concat(subCombinations[j]))
        }
    }

    return resultArr
}

console.log(solution(['A', 'B', 'C', 'D'], 2))
console.log("~~~")

console.log(solution(['A', 'B', 'C', 'D'], 3))
console.log("~~~")

console.log(solution(['A', 'B', 'C', 'D', 'E'], 2))
console.log("~~~")


console.log(solution(['A', 'B', 'C', 'D'], 4))
console.log("~~~")

console.log(solution(['A', 'B', 'C', 'D'], 1))
console.log("~~~")

/*
[
  [ 'A', 'B' ],
  [ 'A', 'C' ],
  [ 'A', 'D' ],
  [ 'B', 'C' ],
  [ 'B', 'D' ],
  [ 'C', 'D' ]
]
~~~
[
  [ 'A', 'B', 'C' ],
  [ 'A', 'B', 'D' ],
  [ 'A', 'C', 'D' ],
  [ 'B', 'C', 'D' ]
]
~~~
[
  [ 'A', 'B' ], [ 'A', 'C' ],
  [ 'A', 'D' ], [ 'A', 'E' ],
  [ 'B', 'C' ], [ 'B', 'D' ],
  [ 'B', 'E' ], [ 'C', 'D' ],
  [ 'C', 'E' ], [ 'D', 'E' ]
]
~~~
[ [ 'A', 'B', 'C', 'D' ] ]
~~~
[ [ 'A' ], [ 'B' ], [ 'C' ], [ 'D' ] ]
~~~

*/