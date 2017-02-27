[link](http://tdpc.contest.atcoder.jp/tasks/tdpc_iwi).

## I - iwi

----------

시간제한 : 2sec / 메모리제한 : 262.144MB

### Problem Statement

$s$ 는 i와 w로 이루어진 문자열이다. 스누케 군은, 여기서 연속된 세 문자가 "iwi"가 되는 부분을 제거하는 조작을 반복할 수 있다. (iwi 를 지우면, 그 좌우에 있던 문자열이 붙어, 길이가 3 짧은 새로운 문자열이 된다.)
조작 횟수의 최대치를 구해라.

----------

### Constraints

* $1 ≤ |s| ≤ 300$
* Each character in $s$ will be either 'i' or 'w'.

----------

### Input Format

입력은 다음의 형식으로 표준입력에 주어진다.

>
$s$

### Output Format

답을 첫 번째 행에 출력해라.

----------

### Sample Input 1

```
iwiwii
```

### Sample Output 1

```
2
```

먼저 세 번째 문자부터 다섯 번째 문자까지의 iwi를 지우는 것이 최적이다.

----------

### Sample Input 2

```
iwiwwwiiiwiwiwiiwii
```

### Sample Output 2

```
5
```
