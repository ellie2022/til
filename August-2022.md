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
    첫째 줄의 if statement가 존재하면 파이썬은 이 모듈이 직접 실행대상이 된 경우에만 해당 프로그램을 수행한다.
    다시 말해, 다른 실행모듈에 import되어 실행될 때는 이 부분은 실행되지 않는다는 뜻.

    python의 실행 대상으로 불려질 때는 __name__변수의 값은 __main__이 되고,
    다른 모듈의 import 대상이 될 때는 파일명이 __name__값이 된다.
