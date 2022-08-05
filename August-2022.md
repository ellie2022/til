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

