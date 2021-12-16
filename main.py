# Erstellen aller Listen und erste Konfiguration
taetigkeiten_dev = ['pflegen, helfen, erziehen', 'Häuser, Brüken oder Fabriken entwerfen oder bauen',
                    'kalkulieren und rechnen', 'Maschinen steuern und bedienen', 'bedienen, verkaufen, werben',
                    'montieren, reparieren', 'mit Kindern oder Jugendlichen zu tun haben']
taetigkeiten = ['pflegen, helfen, erziehen', 'Häuser, Brüken oder Fabriken entwerfen oder bauen',
                'kalkulieren und rechnen', 'Maschinen steuern und bedienen', 'bedienen, verkaufen, werben',
                'montieren, reparieren', 'mit Kindern oder Jugendlichen zu tun haben',
                'hauptsächlich entwerfen, gestalten, zeichnen', 'programmieren, EDV Systeme einrichten / verwalten',
                'mit Material (Holz, Metall, Glas, Stein, ...) umgehen', 'zubereiten, kochen',
                'zeichnen, gestalten, fotographieren', 'mit anderen Menschen in einer Fremdsprache reden',
                'mit Literatur, Kultur, Medien umgehen', 'mich mit fremden Völkern, Kulturen... beschäftigen',
                'messen, prüfen, untersuchen', 'eine medizinische Tätigkeit ausüben',
                'in der Landwirtschaft oder im Gartenbau arbeiten', 'Texte verfassen', 'viel planen und organisieren',
                'tanzen, musizieren, Theater spielen', 'menschliches Verhalten erforschen',
                'anderen etwas beibringen können; unterrichten',
                'mich mit politischen oder gesellschaftlichen Themen beschäftigen', 'sichern, schützen',
                'mich mit philisophisch-theologischen Fragen beschäftigen', 'in Rechts- oder Steuerfragen beraten',
                'Sport treiben können']
arbeitsbedingungen = ['ein hohes Ansehen haben', 'eigenverantwortlich arbeiten', 'für mich alleine arbeiten',
                      'geregelte Arbeitszeit haben', 'viel unterwegs sein', 'mich selbstständig machen könnnen',
                      'gute Aufstiegsmöglichkeiten haben', 'mit anderen in der Gruppe zusammenarbeiten',
                      'im Ausland arbeiten können', 'im Freien arbeiten', 'viel Freizeit haben',
                      'einen sicheren Arbeitsplatz haben', 'Karriere machen',
                      'keine körperliche Belastung durch Lärm etc. haben', 'wenig Stress haben',
                      'in einem Büro arbeiten', 'im Sitzen arbeiten', 'überwiegend im Stehen arbeiten',
                      'andere Menschen führen', 'überwiegend mit dem Köpf arbeiten',
                      'überwiegend mit den Händen arbeiten', 'dass das Betriebsklima stimmt',
                      'ständig neues dazu lernen', 'mich engagieren und etwas voranbringen',
                      'dass meine Aufgaben klar strukturiert sind', 'einen kurzen Weg zu meiner Arbeitsstelle haben',
                      'viel selbst entscheiden können']
question_list_1 = []
question_list_2 = []
already_asked = []
answers_dict = {}
counter = 1
choose_prompt = None
working_list = None

def reset_load(load_list):
    global choose_prompt
    global question_list_1
    global question_list_2
    global working_list
    question_list_1.extend(load_list)
    working_list = load_list
    question_list_2 = question_list_1
    if load_list == taetigkeiten:
        choose_prompt = 'In meinem künftigen Beruf möchte ich...'
    elif load_list == arbeitsbedingungen:
        choose_prompt = 'In meinem Künftigen Beruf möchte ich...'
    else:
        choose_prompt = 'Something went wrong here :('


# Funktion, die prüft, ob Fragen schonmal gestellt worden sind oder ob nach der selben Sache gefragt wird und ggf. abfragt und Ergebnisse in answers_dict einfügt
def main_choose():
    for question_2 in question_list_1:
        for question_1 in question_list_2:
            if question_1 + question_2 not in already_asked and question_1 != question_2:
                done = False
                while not done:
                    # print(f'question 1: {question_1}\nquestion 2: {question_2}')
                    antwort = input(f'{choose_prompt}...\n{question_1}\noder\n{question_2}\n:')
                    if antwort == '1':
                        answers_dict[f'{question_2} & {question_1}'] = int(question_list_1.index(question_1)) + 1
                        done = True
                        already_asked.append(question_list_1.index(question_1) + question_list_1.index(question_2))
                    elif antwort == '2':
                        answers_dict[f'{question_2} & {question_1}'] = int(question_list_1.index(question_2)) + 1
                        done = True
                        already_asked.append(question_list_1.index(question_1) + question_list_1.index(question_2))
                    else:
                        print('Bitte mit 1 oder 2 antworten!')
            else:
                break


def analyse_output():
    global counter
    global working_list
    # Erstellung von Listen, die zur Analyse und zur Ausgabe benötigt werden
    analyse_list = list(answers_dict.values())
    out_list = []
    out_dict = {}

    # Analyse und Sortierung der Ergebnisse
    while counter <= len(working_list) - 1:
        pos = [i for i in range(len(analyse_list)) if analyse_list[i] == counter]
        out_dict[counter] = len(pos)
        counter += 1

    for k, v in dict.items(out_dict):
        out_list.append(f'{k} {v}')

    with open('out.txt', 'w', encoding='UTF-8') as f:
        for element in out_list:
            f.write(str(element) + "\n")
        f.close()


# reset_load(taetigkeiten)
# main_choose()
# analyse_output()
