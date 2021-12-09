taetigkeiten = ['pflegen, helfen, erziehen', 'Häuser, Brüken oder Fabriken entwerfen oder bauen',
                'kalkulieren und rechnen', 'Maschinen steuern und bedienen', 'bedienen, verkaufen, werben',
                'montieren, reparieren', 'mit Kindern oder Jugendlichen zu tun haben']
question_list_1 = []
question_list_2 = []
answers_dict = {}
counter = 1

question_list_1.clear()
question_list_2.clear()
answers_dict.clear()
question_list_1.extend(taetigkeiten)
question_list_2 = question_list_1

for question_2 in question_list_1:
    for question_1 in question_list_2:
        if question_1 != question_2:
            done = False
            while done == False:
                # print(f'question 1: {question_1}\nquestion 2: {question_2}')
                antwort = input(f'In meinem künftigen Beruf möchte ich...\n{question_1}\noder\n{question_2}\n:')
                if antwort == '1':
                    answers_dict[f'{question_2} & {question_1}'] = int(question_list_1.index(question_1)) + 1
                    done = True
                elif antwort == '2':
                    answers_dict[f'{question_2} & {question_1}'] = int(question_list_1.index(question_2)) + 1
                    done = True
                else:
                    print('Bitte mit 1 oder 2 antworten!')
                # counter += 1
        else:
            break

analyse_list = list(answers_dict.values())
out_list = []
out_dict = {}
while counter <= 6:
    pos = [i for i in range(len(analyse_list)) if analyse_list[i] == counter]
    out_dict[counter] = len(pos)
    counter += 1

out_dict = {k: v for k, v in sorted(out_dict.items(), key=lambda item: item[1], reverse=True)}


for k, v in dict.items(out_dict):
    out_list.append(f'{k} kommt insgesamt {v}-mal vor.')

with open('out.txt', 'w', encoding='UTF-8') as f:
    for element in out_list:
        f.write(str(element) + "\n")
    f.close()
