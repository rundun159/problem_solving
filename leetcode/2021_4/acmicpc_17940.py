import heapq
def main():

    first_input  = input()
    first_input = first_input.split(' ')
    n = int(first_input[0])
    end = int(first_input[1])
    company = [None for i in range(n)]
    edge = [[None for i in range(n)] for j in range(n)]
    for i in range(n):
        company[i] = int(input())
    for i in range(n):
        row = input()
        row = row.split(' ')
        for j in range(n):
            edge[i][j] = int(row[j])

#     n = 6
#     end = 3
#     company = [0, 1, 1, 0, 1, 0]
#     edge = [
# [    0 ,3 ,1 ,0 ,10, 0],
# [    3 ,0 ,0 ,15 ,0 ,0],
# [    1 ,0 ,0 ,0 ,0 ,1],
# [    0 ,15 ,0 ,0 ,10 ,0],
# [    10 ,0 ,0 ,10 ,0 ,1],
# [    0 ,0 ,1 ,0 ,1 ,0]
#         ]
    # print(end)
    # for e in edge:
    #     print(e)

    heap = []
    max_int = 1<<31 -1
    distances = [[max_int, max_int] for i in range(n)]
    distances[0] = [0,0]
    heapq.heappush(heap, (distances[0],0))
    while heap:
        # print(heap)
        front = heapq.heappop(heap)
        now_dist_t , node = front
        change = False

        if distances[node][0] > now_dist_t[0]:
            change = True
        elif distances[node][0] == now_dist_t[0] and distances[node][1] > now_dist_t[1]:
            change = True
        if change:
            distances[node] = now_dist_t

        for next_node in range(n):
            if edge[node][next_node]:
                new_dist_0 , new_dist_1 = now_dist_t
                if company[node] != company[next_node]:
                    new_dist_0 += 1
                new_dist_1 += edge[node][next_node]
                change = False
                if distances[next_node][0] > new_dist_0:
                    change = True
                elif distances[next_node][0] == new_dist_0 and distances[next_node][1] > new_dist_1:
                    change = True
                if change:
                    distances[next_node] = [new_dist_0, new_dist_1]
                    heapq.heappush(heap, (distances[next_node], next_node))
    return distances[end][0], distances[end][1]

if __name__ == '__main__':
    ret = main()
    print(ret[0])
    print(ret[1])
