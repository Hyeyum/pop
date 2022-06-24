N = int(input()) #입력받을 식 개수

for i in range(N) :
    num_list = [] #숫자들 저장하는 리스트
    uInput = input()
    uInput = list(uInput) #사용자가 입력하는 식의 문자들을 리스트화
    
    for j in uInput : #사용자가 입력한 식의 문자가
        if '1' <= j <= '9' : #숫자일 때
            num_list.append(int(j)) #num_list에 저장

        else : # +, -, * 중 하나라면
            str2 = num_list.pop()
            str1 = num_list.pop()

            if j == '+' :
                num_list.append(str1+str2)
            elif j == '-' :
                num_list.append(str1-str2)
            elif j == '*' :
                num_list.append(str1*str2)
        
    print("%d"%(num_list[0]))
