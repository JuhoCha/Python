phrase = "안녕하세요 반갑습니다";
print("안녕하세요\"반갑습니다");
#이건 문장 끝내는거
print("안녕하세요\n반갑습니다");
#이건 문장 한줄 바꾸는거 ln같은거임
print(phrase + " is mean Hi nice to meet you");
print(phrase.upper().isupper());
#is upper참이냐 거짓이냐 구분 이 경우 전부 대문자냐 했는데 아니니까 
print(phrase.lower().islower());
print(len(phrase));
#이 안에 얼마나 많은 글자 있는지 알 수 있음
print(phrase[0]);
#이렇게하면 0번째에 오는 문자가 오는데 G 파이썬을 비롯한 컴퓨터는 0부터 시작
print(phrase.index("반"));
#이렇게 하면 이게 몇번째에 오는지 알 수 있음
print(phrase.replace("안녕하세요", "어쩌라고 임마 전혀 안"));
#글자 바꿔줌
