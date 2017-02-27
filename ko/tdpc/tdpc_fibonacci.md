[link](http://tdpc.contest.atcoder.jp/tasks/tdpc_fibonacci).

## T - 피보나치

----------

시간제한 : 2sec / 메모리제한 : 262.144MB

### Problem Statement


수열 {$a_i$} 를 다음과 같이 정의한다.
* $a_1 = a_2 = ... = a_K = 1$
* $a_i$ = $a_{i-1}$ + ... + $a_{i-K} (i > K)$

$a_N$ 을 `mod 1,000,000,007` 으로 구하여라.

----------

### Constraints

* $2 ≤ K ≤ 1000$
* $1 ≤ N ≤ 10^9$

----------

### Input Format

입력은 다음의 형식으로 표준입력에 주어진다.

>
$K$ $N$

### Output Format

답을 첫 번째 줄에 출력하여라.

----------

### Sample Input 1

```
2 10
```

### Sample Output 1

```
55
```

$K$ = 2 인 경우 수열은 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... 가 된다.

----------

### Sample Input 2

```
3 10
```

### Sample Output 2

```
105
```

