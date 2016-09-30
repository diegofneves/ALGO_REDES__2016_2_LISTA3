print('Responda as perguntas apenas com SIM ou NAO')


for i in range(10):
    cont_sim = 0
    cont_nao = 0
    respotas = [input('Telefonou para a vitima? '), input('Esteve no local do crime? '),
                 input('Mora perto da vitima? '),
                 input('Devia para a vitima? '), input('Ja trabalhou com a vitima? ')]

    for resposta in respotas:
        if resposta.upper() == 'SIM':
            cont_sim = cont_sim + 1
        else:
            cont_nao = cont_nao + 1

    if cont_sim == 5:
        print('\nConsideramos o entrevistado como: Assassino \n')
        break
    elif cont_sim > 2 and cont_sim <= 4:
       print('\nConsideramos o entrevistado como: Cumplice \n')
    elif cont_sim == 2:
       print('\nConsideramos o entrevistado como: Suspeito \n')
    else:
        print('\nConsideramos o entrevistado como: Inocente \n')

