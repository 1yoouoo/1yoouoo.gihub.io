graph = {
    1:[2,3,4],
    2:[1,3,4],
    3:[1,2,4],
    4:[1,2,3]
}

def BT(num, visited = []):
    visited.append(num)
    for item in graph[num]:
        if not item in visited:
            visited = BT(item, visited)
    return visited


print(BT(2, visited))