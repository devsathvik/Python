#===== Declare Imports here if required =====


#===== Declare Global Variables / Functions here if required =====


#===== Declare Local Variables / Functions here if required =====


n = int(input())
strings = []
for _ in range(n):
    string = input()
    strings.append(string)


#===== Write Your Logic Here =====
for i in range(n - 1 , -1 , -1):
    print(strings[i])
    

pass