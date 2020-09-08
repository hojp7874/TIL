# Stack

> LIFO: 후입선출형 자료구조

![스택(Stack) 자료구조](Stack.assets/Pringles Original.png)



## 구조

![자료구조 Java 스택(Stack) 정리 (배열, 연결 리스트)](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F265CDC355348E98F37)

- top: 스텍의 맨 위에있는 원소. 스텍이 비어있으면 top == -1이 된다.



## 연산

| 연산    | 기능                                          |
| ------- | --------------------------------------------- |
| push    | 스텍에 원소를 삽입하는 연산                   |
| pop     | top에 있는 원소를 삭제하고 반환하는 연산      |
| isEmpty | 스텍이 공백인지 확인하는 연산                 |
| peek    | top에 있는 원소를 삭제하지 않고 반환하는 연산 |

- `push`: 원소를 추가하고 top에 1을 더한다.
- `pop`: top에 있는 원소를 삭제하고 top에 1을 뺀다.
- `isEmpty`: top이 -1이면 true

