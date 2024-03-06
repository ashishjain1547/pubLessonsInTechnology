class TreeNode {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

function buildExpressionTree(expression) {
    const tokens = expression.split(/\s/).filter(token => token.trim() !== ''); // Tokenize expression

    console.log(tokens);
    
    // Helper function to build the expression tree recursively
    function buildTree(start, end) {
        if (start === end) {
            // Base case: single variable
            return new TreeNode(tokens[start]);
        }

        // Find the operator with the lowest precedence
        let minPrecedence = Infinity; 
        let minIndex = -1;
        
        for (let i = start; i < end; i++) {
            if (tokens[i] === '+' || tokens[i] === '-') {
                const precedence = 1;
                if (precedence <= minPrecedence) {
                    minPrecedence = precedence;
                    minIndex = i;
                }
            } else if (tokens[i] === '*' || tokens[i] === '/') {
                const precedence = 2;
                if (precedence <= minPrecedence) {
                    minPrecedence = precedence;
                    minIndex = i;
                }
            }
        }

        console.log(minIndex);

        // Create the current node with the operator
        const currentNode = new TreeNode(tokens[minIndex]);

        // Recursively build left and right subtrees
        currentNode.left = buildTree(start, minIndex - 1);
        currentNode.right = buildTree(minIndex + 1, end);

        return currentNode;
    }

    // Build the tree starting from the root
    return buildTree(0, tokens.length - 1);
}

// Example usage:
const expression = "X + Y * Z";
console.log(expression);
const expressionTree = buildExpressionTree(expression);
console.log(expressionTree);

const expressions = [
    "X + Y * Z",
    "X / Y - Z",
    "X - Y * Z + A",
    "X * Y - Z / A",
    "X / Y / Z", // To check operators with same precedence are operated on from left to right.
    "X * Y / Z",
    "Z - Y + X"
]

expressions.forEach(function(item){
    const expressionTree = buildExpressionTree(item);
    console.log(expressionTree);      
})