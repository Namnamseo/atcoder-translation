[link](http://tdpc.contest.atcoder.jp/tasks/tdpc_knapsack).

## H - 냅색

----------

시간제한 : 2sec / 메모리제한 : 262.144MB

### Problem Statement

$N$ 개의 물건이 있고, $i$ 번째의 물건의 무게, 가치, 색은 각각 $w_i, v_i, c_i$ 이다. 스누케 군은, 몇 개의 물건을 냅색에 넣기로 했다. 단, 냅색에 넣을 수 있는 물건의 무게의 총합은 $W$ 이하이며, 색은 $C$ 종류 이하여야 한다. 냅색에 넣을 수 있는 물건의 가치의 총합의 최대치를 구해라.

----------

### Constraints

* $1 ≤ N ≤100$
* $1 ≤ W ≤10000$
* $1 ≤ C ≤ 50$
* $1 ≤ w_i, v_i ≤ 10000$
* $1 ≤ c_i ≤ 50$

----------

### Input Format

입력은 다음의 형식으로 표준입력에 주어진다.

>
$N$ $W$ $C$
$w_1$ $v_1$ $c_1$
$\cdots$
$w_N$ $v_N$ $c_N$


### Output Format

답을 첫 번째 행에 출력해라.

----------

### Sample Input 1

```
4 5 2
1 10 1
1 20 2
1 30 3
10 100 4
```

### Sample Output 1

```
50
```

두 번째와 세 번째를 넣으면 된다.

----------

### Sample Input 2

```
10 20 2
4 5 6
3 3 9
5 2 9
4 1 6
6 8 3
3 7 6
2 4 9
4 7 3
6 5 6
3 2 9
```

### Sample Output 2

```
27
```

