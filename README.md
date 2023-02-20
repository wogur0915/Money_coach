# Money Coach

## 연락처

* 문희범: ejungto99@naver.com
* 임재혁: wogur091511@naver.com
* 최안드레이: andrewendlesss@gmail.com

## 소개

MC(Money Coach)는 사용자가 입력한 가계부 내역을 토대로 소비 성향 및 소비 플랜을 제시해주는 컴퓨터(Windows, MacOS) 기반 프로그램으로 사회 초년생의 입장에서, 같은 사회 초년생들에게 무언가 도움이 될만한 것은 없을까? 하여 기획 및 제작을 진행하게 된 프로그램입니다.


## 목적

- 사용자에게 가계부 시스템 제공
- 입력된 가계부 내용에서 최다 소비 카테고리를 파악하여 소비 성향 도출
- 전체적인 수입 및 지출 내역을 분석하여 소비 플랜 제시

-----

## 의존성

```
[ OS ] (권장사항)
Windows >= 21H1 (Windows 10)
macOS Monterey >= 12.2

[ Language ]
Python >= 3.10.4

[ Library ]
tkinter >= 8.6
DateTime >= 4.4 
```

## 설치 방법

#### Git 환경
```
git clone https://github.com/KorBasilion/OSS-Basic-Project
```
#### Windows 환경
- Code Zip 파일 다운로드 및 압축 해제

## 사용 방법

- 1. 프로젝트 폴더 내에서 mainview.py 실행
- 2. 내역 버튼을 클릭 후 + 버튼을 눌러 가계부 형식에 맞춰 내용 입력, 기존에 저장한 파일이 있을 경우 불러오기 클릭 후 파일 선택
- 3. 삭제하고 싶은 내역이 있을 경우, 해당 내역을 선택 후 - 버튼 클릭 혹은 해당 내역을 더블클릭
- 4. 값을 입력한 후 통계, 자산에서 입력 데이터를 토대로한 수치 확인
- 5. 입력한 값을 저장하고 싶을 때에는 상단의 저장하기 클릭

## 실행화면

![moneycoach_thumb](https://user-images.githubusercontent.com/34836246/219988655-0d527f2d-b993-45e0-b82b-ffd0b0fd3ab4.png)


## License

```
The MIT License (MIT)

Copyright (c) 2022 COMMA

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
