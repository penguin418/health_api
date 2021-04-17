simple health api

실행방법
1. 먼저 요구 사항을 확인합니다.
   파이썬 3.8이상
2. requirements를 설치합니다
    ```shell
    pip install -r requirements.txt
    ```
3. config.py를 생성하여 필수 값들을 채워둡니다
   
    이때 config.py.example.py를 참조해주세요
    ```python
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.format(
            user='xxxxxxxxxxxxxx',
            pw='xxxxxxxxxxxxxxxx',
            url='xxx.xxx.xxx.xxx',
            db='xxxxxxxxxxxxxxxx')
    ```

4. 이제 실행하셔도 됩니다
    ```shell
        flask run
    ```

구현한 내용
- 1, 2번

- 1번의 경우, sum, mean, std 등의 추가적인 통계자료가 추가될 것을 고려하여 통계이름을 인자로 받도록 하였고, 결과 구조체에 stat_type과 테이블을 명시하여 추가적인 통계자료가 추가될 경우를 대비했습니다.

- 2번의 경우, 3번을 구현하지 못할 것을 대비해, 컨셉이라도 충분하게 제공해주는 것이 좋을 것같아 모든 필드를 전해주도록 설계했습니다.

구현하지 못한 내용
- 3번

- 문제를 살펴봤을 때, 3번의 경우 많은 횟수의 조인이 필요할 것이라 예상했고 