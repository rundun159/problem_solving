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

## BFS

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
