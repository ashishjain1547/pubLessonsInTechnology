function solution(A) {
    let resultArr = []

    if (A.length > 1) {
        for (let i = 0; i < A.length; i++) {
            const currentElement = A[i];

            otherElements = A.slice(0,i).concat(A.slice(i+1));

            subPermutations = solution(otherElements);
            for (let j = 0; j < subPermutations.length; j++) {
                resultArr.push([currentElement].concat(subPermutations[j]));
            }
        }
    }

    else if(A.length == 1) {
        return [A]
    }

    return resultArr
}

console.log(solution(['A', 'B']))

// https://www.tutorialspoint.com/generating-all-possible-permutations-of-array-in-javascript