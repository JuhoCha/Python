lucky_nums = [4, 5, 15, 16, 23, 42]
friends = ["Kevin", "Karl", "Oscar", "Hazard", "Messi"]
friends.extend(lucky_nums) #이렇게 하면 넘버랑 친구들 다 나오게 된다
friends.append("Ronaldo") #친구들 뒤에 하나가 추가된다
friends.insert(1, "손흥민") #이거하면 1번 순서에 있는애 이름이 바뀌게 된다
friends.remove("Messi") #이거하면 지워지고
friends.clear() #리스트 삭제
friends.pop() #제일 마지막 요소 지우는거임
print(friends)
friends.sort() #알파벳 순서대로 정렬
lucky_nums.reverse() #역순으로 정렬
print(lucky_nums)
print(friends.index("Kevin"))#몇번째 순서에 나오는지 알려줌
print(friends.count("Kevin"))#몇번 나오는지 알려줌

friends2 = friends.copy()
print(friends2)
