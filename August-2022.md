# Aug-01-2022
## python 문서 from django page

- unbound variables
    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    선언하지 않은 변수에 값을 할당하는 것은 허용
    값을 할당하지 않은 변수를 참조하는 것은 에러

- running scripts
    모듈은 객체이고 유용한 attribute를 갖고 있다. 
    가령 다음 코드처럼..
        if __name__ == '__main__':
            print(approximate_size(1000000000000, False))
            print(approximate_size(1000000000000))
    첫째 줄의 if statement가 존재하면 파이썬은 이 모듈이 직접 실행대상($ python this_module로 실행한 경우)이 된 경우에만 해당 프로그램을 수행한다. 
    다시 말해, 다른 실행모듈에 import되어 실행될 때는 이 부분은 실행되지 않는다는 뜻.

    python의 실행 대상으로 불려질 때는 __name__변수의 값은 __main__이 되고,
    다른 모듈의 import 대상이 될 때는 파일명이 __name__값이 된다.

# Aug-02-2022
## python 문서 from django page
### Chapter 2. Native Datatypes
- python에서 모든 값은 datatype을 가지지만, 선언할 필요는 없다. 처음 할당된 값을 기준으로 python이 type을 알아내고 내부적으로 관리한다.

- native datatypes :
    Booleans : True or False
    Numbers : 정수, 소수, 분수, 복소수(integers, floats, fractions, complex numbers)
    Strings : Unicode character의 연속
    Bytes and byte arrays : e.g. a JPEG image file
    Lists : ordered sequences of values
    Tuples : ordered, immutable sequences of values
    Sets : unordered bags of values
    Dictionaries : unordered bags of key-value pairs


# Aug-03-2022
## python 문서 from django page
### Numbers
- Coercing integers to floats and vice-versa
    int() function으로 float를 int화 할때는 truncate됨
    따라서 -0.9, 0.9 모두 int()후에는 0이 됨 (floor가 아니고 true trucate function)
    -1.11을 floor하면 내리기 때문에 -2
    true truncate하면 -1이 된다

    
# Aug-05-2022
## python 문서 from django page
### Numerical operations
- 11/2 : 5.5 floating point division. 젯수와 피젯수가 정수라도 소수를 돌려줌
- 11//2 : 5  나눈 후 소수점 이하는 버리고 정수값만 리턴
- -11/2 : -6 음수일때는 floor한 값을 리턴한다. (floor division)

# Aug-12-2022
## python 문서 from django page
### Numbers in a boolean context 
- Zero values are false, and non-zero values are true.
### Lists
- 생성 : square bracket으로 둘러싸고 comma로 분리
    ex) a_list = ['a', 'b', 'ground', 'z', 'end']
    list.py에서 연습한 내용 참조

### Tuples : an immutable list
- 괄호로 둘러싸고 comma로 분리.  변경할 수 없는 리스트. 한번 생성되면 바꿀 수 없다.
    ex) a_tuple = ('a', 'b', 'ground', 'z', 'end')
- list와 다른점은 변경할 수 없다는 것.  
    그리고 append(), extend(), insert(), remove(), pop() 등 변경가능한 method가 없다는 것
- 다중 값을 한번에 할당하기
    ex) v = ('a', 2, True)
        (x, y, z) = v
    위와 같이 하면, x, y, z에 v의 값이 차례로 할당됨
    어떤 이름에 범위의 값을 할당하고 싶을 때..
    ex) (MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)
    이렇게 하면, MONDAY는 0, TUESDAY는 1, SUNDAY는 6이 된다.

### Sets
- set은 unordered bag of unique values
    set에는 변경가능한 데이터유형의 값이 들어갈 수 있다.
    2개의 set에 대하여 표준 set operation(union, intersection, set difference 등)을 수행할 수 있다.
- 생성 : 중괄호로 둘러싸고 comma로 분리
    ex) a_set = {1}
    a_set = {1, 2}
- list로부터 set을 생성하는 것도 가능하다 : 
    a_list = ['a', 'b', 'ground', True, False, 42]
    a_set = set(a_list)
    이렇게 하면 a_set은...: 
    {'a', False, 'b', True, 'ground', 42}
    set은 unordered이기 때문에 list의 순서를 기억하지 않는다.
    이떄 원래 list는 변하지 않음
- set의 값을 변경하는 method : add(), update()
    set의 원소는 unique vlaue이므로, 동일한 내용을 add하면 아무 일도 일어나지 않음
    --> 에러가 나지 않고, 그냥 no-op임
    


