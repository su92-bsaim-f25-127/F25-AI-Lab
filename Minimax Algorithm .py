import math

# Minimax Algorithm
minimax_count = 0

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    global minimax_count

    # Base case
    if curDepth == targetDepth:
        minimax_count += 1
        return scores[nodeIndex]

    if maxTurn:
        return max(
            minimax(curDepth + 1, nodeIndex * 2,
                    False, scores, targetDepth),
            minimax(curDepth + 1, nodeIndex * 2 + 1,
                    False, scores, targetDepth)
        )
    else:
        return min(
            minimax(curDepth + 1, nodeIndex * 2,
                    True, scores, targetDepth),
            minimax(curDepth + 1, nodeIndex * 2 + 1,
                    True, scores, targetDepth)
        )


# Driver code
scores = [3, 5, 2, 9, 3, 5, 2, 9]
treeDepth = int(math.log2(len(scores)))

result = minimax(0, 0, True, scores, treeDepth)

print("The optimal value is:", result)
print("Evaluated leaf nodes:", minimax_count)