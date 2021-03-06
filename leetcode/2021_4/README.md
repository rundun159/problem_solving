## Simulation
<div>
<h5> 1041. Robot Bounded In Circle (2021.4.2)</h5>
Found that after perform the given instruction once, it can only change its direction to one of 90,180,270,360 degrees.<br>
Meaning that after some iteration, it comes back to facing the north side.<br>
When it faces to the north again, if it is at the origin, it can be on a circle.<br>
Otherwise, it will go farther from the origin. <br>
<h5>52min. cost</h5>
<hr>
</div>


## DFS
<div>
<h5>17. Letter Combinations of a Phone Number (2021.4.5) </h5>
DFS임을 알고 접근했다.<br>
python에서 DFS를 구현한것이 처음이라 어색했지만, <br>결국 list에 append하고 pop하는 구조로
Stack을 사용해서 구현하면 된다.
<h5>21min. cost</h5>
<hr>
</div>

<div>
<h5>394. Decode String (2021.4.6) </h5>
대부분의 괄호 문제는 Stack을 활용해서 해결한다.
Stack과 재귀는 비슷한 메커니즘을 갖고 있기에, 재귀를 사용해서 풀게 되었다. <br>
처음 풀었을 때에는 main dfs, small dfs로 나눠서 두개로 구현했지만,
풀고 난 후에 refactoring을 거쳐서 main_dfs 하나만을 갖도록 수정했다.
<h5>34min. cost</h5>
<hr>
</div>
<div>
<h5>98. Validate Binary Search Tree (2021.4.6) </h5>
Binary Tree에서 각 subtree의 조건을 안다는 가정하에 구현했다. (Post Order)<br>
각 Subtree의 조건을 안다는 가정이 DFS로 이어지게 된다.
DFS는 재귀와 친하다.
<h5>19min. cost</h5>
<hr>
</div>



## BFS
<div>
<h5>199. Binary Tree Right Side View (2021.4.5) </h5>
Have to travel each layers from left to right. <br>
So, designed BFS.<br>
When the height get changed, add value to the returned list.
<h5>51min. cost</h5>
<hr>
</div>

## DP
<div>
<h5>91. Decode Ways (2021.4.2) </h5>
Repeated calculation was expected.<br>
From left to right, once a small right part of the given string is calculated, the result will be used again. <br>
So I used DP. <br>
There was also an exception. When the index is the last character. When idx+1 == self.len & idx+2 == self.len, this exception should be dealt with.
<br>
<h5>31min. cost</h5>
<hr>
</div>

## Hash
<div>
<h5>380.  Insert Delete GetRandom O(1) (2021.4.3) </h5>
Removing was the most difficult one.<br>
It was obvious that I should use a hash map and a list.
Mapping between them was not difficult, but I didn't know what to do in removing.<br>
It switches index with the last one with the one that will be removed. <br>

<br>
<h5>Checked Solution</h5>
<hr>
</div>

## Brute Force
<div>
<h5>221. Maximal Square (2021.4.4) </h5>
Neither BFS nor DFS. <br>
I failed to find any good way to optimize, but calculated brute force can work in given time.
Even this algorithm O(n^3), n is at most 3*10^2. 

<br>
<h5>About 50min. Cost</h5>
<hr>
</div>

## Topological Sorting
<div>
<h5>207. Course Schedule (2021.4.6) </h5>
문제 자체가 위상 정렬의 문제다. 위상 정렬 알고리즘이 기억이 안나서 Solution을 참고했다. <br>
python으로 구현하는 방식은 defaultdict, deque를 사용한다. 

1. defaultdict로 (array로 안하는 이유는 아예 edge가 없는 node도 존재할수 있기 때문?) <br>
각 node들의 incoming edge의 수, outgoing edge의 목적지 node들을 저장한다. <br>
2. deque에 incoming edge가 없는 node들을 저장한다. <br>
3. deque에서 하나씩 빼면서 edge를 없애고, 해당 edge의 목적지의 node의 incoming edge의 수를 하나 줄인다. <br>
3-1. 해당 목적지 node의 incoming edge의 수가 0이면 deque에 추가 <br>
4. deque가 비어있을때, 모든 edge가 제거되었다면, 해당 그래프는 topological sort가 가능한 그래프다. <br>
<br>
<h5>Used Solution</h5>
<hr>
</div>
