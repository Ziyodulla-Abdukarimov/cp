N = int(input())
scores = list(map(int, input().split()))

max_score = scores[0]  # Aslida oxirgi raunddagi g'oliblik ma'lumotini olib tashlaymiz
possible_winners = 1  # oxirgi g'olibni qo'lga kiritish imkoniyatini 1 bilan boshlaymiz

for i in range(1, N):
    if scores[i] < max_score:  # keyingi o'quvchining balli oxirgi g'olibdan kam bo'lsa
        break  # bu o'quvchi g'oliblikka erishish imkoniyati yo'q
    possible_winners += 1  # aks holda, g'oliblikka erishish imkoniyati mavjud

print(possible_winners)
