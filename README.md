# CodingTestSolution




## 1. How To Use
1. solutions 디렉토리에 `solution()` 함수가 포함된 파이썬 파일을 생성하세요.  
   파일명은 문제번호로 지정해주세요. 실행할 때 이를 사용합니다.
   - Baekjoon solution 디렉토리 : `solutions/baekjoon/solutions`
   - Programmers solution 디렉토리 : `solutions/programmers/solutions`

2. testcase 디렉토리에 `TEST_CASE` 변수가 포함된 파이썬 파일을 생성하세요.  
   테스트케이스를 Dictionary형태로 작성해주세요.
   - Baekjoon testcase 디렉토리 : `solutions/baekjoon/testcase`
   - Programmers testcase 디렉토리 : `solutions/programmers/testcase`

3.  테스트를 시작하세요.
    - Baekjoon : `$python3 solutions baekjoon <문제번호>`
    - Programmers : `$python3 solutions programmers <문제번호>`

```
$ python3 solutions -h

usage: solutions [-h] S I

Hi! I can help you to solve problem.

positional arguments:
  S           Supported source : [baekjoon|programmers]
  I           Problem id

optional arguments:
  -h, --help  show this help message and exit
```

## 2. Example
```
$ python3 solutions programmers 72411

----------------TEST CASE : #0---------------
INPUT : {'course': [2, 3, 4],
 'orders': ['ABCFG', 'AC', 'CDE', 'ACDE', 'BCFG', 'ACDEH'],
 'result': ['AC', 'ACDE', 'BCFG', 'CDE']}
---------------------------------------------

-------------------RESULT--------------------
pass
-------------------END-----------------------






----------------TEST CASE : #1---------------
INPUT : {'course': [2, 3, 5],
 'orders': ['ABCDE', 'AB', 'CD', 'ADE', 'XYZ', 'XYZ', 'ACD'],
 'result': ['ACD', 'AD', 'ADE', 'CD', 'XYZ']}
---------------------------------------------

-------------------RESULT--------------------
pass
-------------------END-----------------------






----------------TEST CASE : #2---------------
INPUT : {'course': [2, 3, 4], 'orders': ['XYZ', 'XWY', 'WXA'], 'result': ['WX', 'XY']}
---------------------------------------------

-------------------RESULT--------------------
pass
-------------------END-----------------------
```
## 3. 문제 목록

| 출처 | ID | 난이도 | 제목 | 분류 | 링크 | 언어 |
| -- | -- | ---- | :-- | :-- | --- | --- |
