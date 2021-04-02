## Simulation
<div>
<h5> 1041. Robot Bounded In Circle (2021.4.2)</h5>
Found that after perform the given instruction once, it can only change its direction to one of 90,180,270,360 degrees.<br>
Meaning that after some iteration, it comes back to facing the north side.<br>
When it faces to the north again, if it is at the origin, it can be on a circle.<br>
Otherwise, it will go farther from the origin. <br>
52min. cost
<hr>
</div>

## DFS

## BFS

## DP
<div>
<h5>91. Decode Ways (2021.4.2) </h5>
Repeated calculation was expected.<br>
From left to right, once a small right part of the given string is calculated, the result will be used again. <br>
So I used DP. <br>
There was also an exception. When the index is the last character. When idx+1 == self.len & idx+2 == self.len, this exception should be dealt with.
<br>
31min. cost
<hr>
</div>
