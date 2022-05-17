from math import log10
print('\033[7;40m{:=^54}\033[m'.format('TABELA COMPLETA PARA MONTAGEM DE DIETA'))
print('\033[1;4mTAXA METABÓLICA BASAL OU BASAL METABOLIC RATE, PERCENTUAL DE GORDURA, DIVISÃO DE MACROS, E OUTRAS PARADAS...\033[m')
print('Começando a Avaliação...')
print('\033[34m=-\033[m'*42)
print('\033[33mEscolha:\033[m ')
print('''\033[33m[ 1 ] Masculino
[ 2 ] Feminino\033[m''')
sex = int(input('\033[7;40mSexo:\033[m '))
print('\033[34m=-\033[m'*42)
print('''\033[33mTaxa de atividade:
[ 1 ] Sedentários (pouco ou nenhum exercício)
[ 2 ] Levemente ativo (exercício leve 1 a 3 dias por semana)
[ 3 ] Moderadamente ativo (exercício moderado, faz esportes 3 a 5 dias por semana)
[ 4 ] Altamente ativo (exercício pesado de 5 a 6 dias por semana)
[ 5 ] Extremamente ativo (exercício pesado diariamente e até 2 vezes por dia)\033[m ''')
atividade = int(input('\033[7;40mNível de atividade:\033[m '))
print('\033[34m=-\033[m'*42)
idade = int(input('\033[1mIdade: '))
altura = int(input('Altura: '))
cintura = int(input('Cintura: '))
peso = int(input('Peso: '))
pescoco = int(input('Pescoço: '))
quadril = int(input('Quadril: '))
print('\033[34m=-\033[m'*42)
if sex == 1:
    if atividade == 1:
        calculobf = log10(cintura - pescoco)
        calculo2bf = log10(altura)
        calculo3bf = (1.033 - 0.191 * calculobf) + (0.155 * calculo2bf)
        calculo4bf = 495 / calculo3bf - 450
        print('\033[1mBF = {:.2f}%'.format(calculo4bf))
        masssamag = peso - peso * (calculo4bf / 100)
        print('Massa Magra = {:.2f} Kg'.format(masssamag))
        massagor = peso - masssamag
        print('Massa Gorda = {:.2f} Kg'.format(massagor))
        taxaMB = 66 + (13.8 * peso) + (5 * altura) - (6.8 * idade)
        print('Taxa metabólica Basal = {:.2f} Kcal'.format(taxaMB))
        manter = taxaMB * 1.2
        perder = manter - 355
        ganhar = manter + 355
        print('Calorias necessárias para manter o peso: {:.2f} Kcal'.format(manter))
        print('Calorias para ganhar peso: {:.2f} Kcal'.format(ganhar))
        print('Calorias para perder peso: {:.2f} Kcal'.format(perder))
        print('\033[34m=-\033[m' * 42)
        proteina = 2.5 * peso
        gordura = 0.8 * peso
        prokcal = proteina * 4
        gorkcal = gordura * 9
        carbokcal = manter - prokcal - gorkcal
        carboidrato = carbokcal / 4
        print('{:=^50}'.format('\033[1;4;7;40mMacros para manter peso!\033[m'))
        print('\033[1mProteína= {:.2f}g'.format(proteina))
        print('Carboidrato= {:.2f}g'.format(carboidrato))
        print('Gordura= {:.2f}g'.format(gordura))
        perderkcal = perder - prokcal - gorkcal
        carboperder = perderkcal / 4
        print('{:=^50}'.format('\033[1;4;7;40mMacros para perder peso!\033[m'))
        print('\033[1mProteína= {:.2f}g'.format(proteina))
        print('Carboidrato= {:.2f}g'.format(carboperder))
        print('Gordura= {:.2f}g'.format(gordura))
        ganharkcal = ganhar - prokcal - gorkcal
        carboganhar = ganharkcal / 4
        print('{:=^50}'.format('\033[1;4;7;40mMacros para ganhar peso!\033[m'))
        print('\033[1mProteína= {:.2f}g'.format(proteina))
        print('Carboidrato= {:.2f}g'.format(carboganhar))
        print('Gordura= {:.2f}g'.format(gordura))
    elif atividade == 2:
        calculobf = log10(cintura - pescoco)
        calculo2bf = log10(altura)
        calculo3bf = (1.033 - 0.191 * calculobf) + (0.155 * calculo2bf)
        calculo4bf = 495 / calculo3bf - 450
        print('\033[1mBF = {:.2f}%'.format(calculo4bf))
        masssamag = peso - peso * (calculo4bf / 100)
        print('Massa Magra = {:.2f} Kg'.format(masssamag))
        massagor = peso - masssamag
        print('Massa Gorda = {:.2f} Kg'.format(massagor))
        taxaMB = 66 + (13.8 * peso) + (5 * altura) - (6.8 * idade)
        print('Taxa metabólica Basal = {:.2f} Kcal'.format(taxaMB))
        manter = taxaMB * 1.375
        perder = manter - 406
        ganhar = manter + 406
        print('Calorias necessárias para manter o peso: {:.2f} Kcal'.format(manter))
        print('Calorias para ganhar peso: {:.2f} Kcal'.format(ganhar))
        print('Calorias para perder peso: {:.2f} Kcal'.format(perder))
        print('\033[34m=-\033[m' * 42)
        proteina = 2.5 * peso
        gordura = 0.8 * peso
        prokcal = proteina * 4
        gorkcal = gordura * 9
        carbokcal = manter - prokcal - gorkcal
        carboidrato = carbokcal / 4
        print('{:=^50}'.format('\033[1;4;7;40mMacros para manter peso!\033[m'))
        print('\033[1mProteína= {:.2f}g'.format(proteina))
        print('Carboidrato= {:.2f}g'.format(carboidrato))
        print('Gordura= {:.2f}g'.format(gordura))
        perderkcal = perder - prokcal - gorkcal
        carboperder = perderkcal / 4
        print('{:=^50}'.format('\033[1;4;7;40mMacros para perder peso!\033[m'))
        print('\033[1mProteína= {:.2f}g'.format(proteina))
        print('Carboidrato= {:.2f}g'.format(carboperder))
        print('Gordura= {:.2f}g'.format(gordura))
        ganharkcal = ganhar - prokcal - gorkcal
        carboganhar = ganharkcal / 4
        print('{:=^50}'.format('\033[1;4;7;40mMacros para ganhar peso!\033[m'))
        print('\033[1mProteína= {:.2f}g'.format(proteina))
        print('Carboidrato= {:.2f}g'.format(carboganhar))
        print('Gordura= {:.2f}g'.format(gordura))
    elif atividade == 3:
        calculobf = log10(cintura - pescoco)
        calculo2bf = log10(altura)
        calculo3bf = (1.033 - 0.191 * calculobf) + (0.155 * calculo2bf)
        calculo4bf = 495 / calculo3bf - 450
        print('\033[1mBF = {:.2f}%'.format(calculo4bf))
        masssamag = peso - peso * (calculo4bf / 100)
        print('Massa Magra = {:.2f} Kg'.format(masssamag))
        massagor = peso - masssamag
        print('Massa Gorda = {:.2f} Kg'.format(massagor))
        taxaMB = 66 + (13.8 * peso) + (5 * altura) - (6.8 * idade)
        print('Taxa metabólica Basal = {:.2f} Kcal'.format(taxaMB))
        manter = taxaMB * 1.55
        perder = manter - 458
        ganhar = manter + 458
        print('Calorias necessárias para manter o peso: {:.2f} Kcal'.format(manter))
        print('Calorias para ganhar peso: {:.2f} Kcal'.format(ganhar))
        print('Calorias para perder peso: {:.2f} Kcal'.format(perder))
        print('\033[34m=-\033[m' * 42)
        proteina = 2.5 * peso
        gordura = 0.8 * peso
        prokcal = proteina * 4
        gorkcal = gordura * 9
        carbokcal = manter - prokcal - gorkcal
        carboidrato = carbokcal / 4
        print('{:=^50}'.format('\033[1;4;7;40mMacros para manter peso!\033[m'))
        print('\033[1mProteína= {:.2f}g'.format(proteina))
        print('Carboidrato= {:.2f}g'.format(carboidrato))
        print('Gordura= {:.2f}g'.format(gordura))
        perderkcal = perder - prokcal - gorkcal
        carboperder = perderkcal / 4
        print('{:=^50}'.format('\033[1;4;7;40mMacros para perder peso!\033[m'))
        print('\033[1mProteína= {:.2f}g'.format(proteina))
        print('Carboidrato= {:.2f}g'.format(carboperder))
        print('Gordura= {:.2f}g'.format(gordura))
        ganharkcal = ganhar - prokcal - gorkcal
        carboganhar = ganharkcal / 4
        print('{:=^50}'.format('\033[1;4;7;40mMacros para ganhar peso!\033[m'))
        print('\033[1mProteína= {:.2f}g'.format(proteina))
        print('Carboidrato= {:.2f}g'.format(carboganhar))
        print('Gordura= {:.2f}g'.format(gordura))
    elif atividade == 4:
        calculobf = log10(cintura - pescoco)
        calculo2bf = log10(altura)
        calculo3bf = (1.033 - 0.191 * calculobf) + (0.155 * calculo2bf)
        calculo4bf = 495 / calculo3bf - 450
        print('\033[1mBF = {:.2f}%'.format(calculo4bf))
        masssamag = peso - peso * (calculo4bf / 100)
        print('Massa Magra = {:.2f} Kg'.format(masssamag))
        massagor = peso - masssamag
        print('Massa Gorda = {:.2f} Kg'.format(massagor))
        taxaMB = 66 + (13.8 * peso) + (5 * altura) - (6.8 * idade)
        print('Taxa metabólica Basal = {:.2f} Kcal'.format(taxaMB))
        manter = taxaMB * 1.725
        perder = manter - 510
        ganhar = manter + 510
        print('Calorias necessárias para manter o peso: {:.2f} Kcal'.format(manter))
        print('Calorias para ganhar peso: {:.2f} Kcal'.format(ganhar))
        print('Calorias para perder peso: {:.2f} Kcal'.format(perder))
        print('\033[34m=-\033[m' * 42)
        proteina = 2.5 * peso
        gordura = 0.8 * peso
        prokcal = proteina * 4
        gorkcal = gordura * 9
        carbokcal = manter - prokcal - gorkcal
        carboidrato = carbokcal / 4
        print('{:=^50}'.format('\033[1;4;7;40mMacros para manter peso!\033[m'))
        print('\033[1mProteína= {:.2f}g'.format(proteina))
        print('Carboidrato= {:.2f}g'.format(carboidrato))
        print('Gordura= {:.2f}g'.format(gordura))
        perderkcal = perder - prokcal - gorkcal
        carboperder = perderkcal / 4
        print('{:=^50}'.format('\033[1;4;7;40mMacros para perder peso!\033[m'))
        print('\033[1mProteína= {:.2f}g'.format(proteina))
        print('Carboidrato= {:.2f}g'.format(carboperder))
        print('Gordura= {:.2f}g'.format(gordura))
        ganharkcal = ganhar - prokcal - gorkcal
        carboganhar = ganharkcal / 4
        print('{:=^50}'.format('\033[1;4;7;40mMacros para ganhar peso!\033[m'))
        print('\033[1mProteína= {:.2f}g'.format(proteina))
        print('Carboidrato= {:.2f}g'.format(carboganhar))
        print('Gordura= {:.2f}g'.format(gordura))
    elif atividade == 5:
        calculobf = log10(cintura - pescoco)
        calculo2bf = log10(altura)
        calculo3bf = (1.033 - 0.191 * calculobf) + (0.155 * calculo2bf)
        calculo4bf = 495 / calculo3bf - 450
        print('\033[1mBF = {:.2f}%'.format(calculo4bf))
        masssamag = peso - peso * (calculo4bf / 100)
        print('Massa Magra = {:.2f} Kg'.format(masssamag))
        massagor = peso - masssamag
        print('Massa Gorda = {:.2f} Kg'.format(massagor))
        taxaMB = 66 + (13.8 * peso) + (5 * altura) - (6.8 * idade)
        print('Taxa metabólica Basal = {:.2f} Kcal'.format(taxaMB))
        manter = taxaMB * 1.9
        perder = manter - 562
        ganhar = manter + 562
        print('Calorias necessárias para manter o peso: {:.2f} Kcal'.format(manter))
        print('Calorias para ganhar peso: {:.2f} Kcal'.format(ganhar))
        print('Calorias para perder peso: {:.2f} Kcal\033[m'.format(perder))
        print('\033[34m=-\033[m' * 42)
        proteina = 2.5 * peso
        gordura = 0.8 * peso
        prokcal = proteina * 4
        gorkcal = gordura * 9
        carbokcal = manter - prokcal - gorkcal
        carboidrato = carbokcal / 4
        print('{:=^50}'.format('\033[1;4;7;40mMacros para manter peso!\033[m'))
        print('\033[1mProteína= {:.2f}g'.format(proteina))
        print('Carboidrato= {:.2f}g'.format(carboidrato))
        print('Gordura= {:.2f}g'.format(gordura))
        perderkcal = perder - prokcal - gorkcal
        carboperder = perderkcal / 4
        print('{:=^50}'.format('\033[1;4;7;40mMacros para perder peso!\033[m'))
        print('\033[1mProteína= {:.2f}g'.format(proteina))
        print('Carboidrato= {:.2f}g'.format(carboperder))
        print('Gordura= {:.2f}g'.format(gordura))
        ganharkcal = ganhar - prokcal - gorkcal
        carboganhar = ganharkcal / 4
        print('{:=^50}'.format('\033[1;4;7;40mMacros para ganhar peso!\033[m'))
        print('\033[1mProteína= {:.2f}g'.format(proteina))
        print('Carboidrato= {:.2f}g'.format(carboganhar))
        print('Gordura= {:.2f}g'.format(gordura))
elif sex == 2:
    if atividade == 1:
        calculobfF = log10(quadril + cintura - pescoco)
        calculo2bfF = log10(altura)
        calculo3bfF = (1.296 - 0.350 * calculobfF) + (0.221 * calculo2bfF)
        calculo4bfF = 495 / calculo3bfF - 450
        print('\033[1mBF = {:.2f}%'.format(calculo4bfF))
        masssamag = peso - peso * (calculo4bfF / 100)
        print('Massa Magra = {:.2f} Kg'.format(masssamag))
        massagor = peso - masssamag
        print('Massa Gorda = {:.2f} Kg'.format(massagor))
        taxaMBF = 655 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)
        print('Taxa metabólica Basal = {:.2f} Kcal'.format(taxaMBF))
        manter = taxaMBF * 1.2
        perder = manter - 355
        ganhar = manter + 355
        print('Calorias necessárias para manter o peso: {:.2f} Kcal'.format(manter))
        print('Calorias para ganhar peso: {:.2f} Kcal'.format(ganhar))
        print('Calorias para perder peso: {:.2f} Kcal'.format(perder))
        print('\033[34m=-\033[m' * 42)
        proteina = 2.5 * peso
        gordura = 0.8 * peso
        prokcal = proteina * 4
        gorkcal = gordura * 9
        carbokcal = manter - prokcal - gorkcal
        carboidrato = carbokcal / 4
        print('{:=^50}'.format('\033[1;4;7;40mMacros para manter peso!\033[m'))
        print('\033[1mProteína= {:.2f}g'.format(proteina))
        print('Carboidrato= {:.2f}g'.format(carboidrato))
        print('Gordura= {:.2f}g'.format(gordura))
        perderkcal = perder - prokcal - gorkcal
        carboperder = perderkcal / 4
        print('{:=^50}'.format('\033[1;4;7;40mMacros para perder peso!\033[m'))
        print('\033[1mProteína= {:.2f}g'.format(proteina))
        print('Carboidrato= {:.2f}g'.format(carboperder))
        print('Gordura= {:.2f}g'.format(gordura))
        ganharkcal = ganhar - prokcal - gorkcal
        carboganhar = ganharkcal / 4
        print('{:=^50}'.format('\033[1;4;7;40mMacros para ganhar peso!\033[m'))
        print('\033[1mProteína= {:.2f}g'.format(proteina))
        print('Carboidrato= {:.2f}g'.format(carboganhar))
        print('Gordura= {:.2f}g'.format(gordura))
    if atividade == 2:
        calculobfF = log10(quadril + cintura - pescoco)
        calculo2bfF = log10(altura)
        calculo3bfF = (1.296 - 0.350 * calculobfF) + (0.221 * calculo2bfF)
        calculo4bfF = 495 / calculo3bfF - 450
        print('\033[1mBF = {:.2f}%'.format(calculo4bfF))
        masssamag = peso - peso * (calculo4bfF / 100)
        print('Massa Magra = {:.2f} Kg'.format(masssamag))
        massagor = peso - masssamag
        print('Massa Gorda = {:.2f} Kg'.format(massagor))
        taxaMBF = 655 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)
        print('Taxa metabólica Basal = {:.2f} Kcal'.format(taxaMBF))
        manter = taxaMBF * 1.375
        perder = manter - 406
        ganhar = manter + 406
        print('Calorias necessárias para manter o peso: {:.2f} Kcal'.format(manter))
        print('Calorias para ganhar peso: {:.2f} Kcal'.format(ganhar))
        print('Calorias para perder peso: {:.2f} Kcal'.format(perder))
        print('\033[34m=-\033[m' * 42)
        proteina = 2.5 * peso
        gordura = 0.8 * peso
        prokcal = proteina * 4
        gorkcal = gordura * 9
        carbokcal = manter - prokcal - gorkcal
        carboidrato = carbokcal / 4
        print('{:=^50}'.format('\033[1;4;7;40mMacros para manter peso!\033[m'))
        print('\033[1mProteína= {:.2f}g'.format(proteina))
        print('Carboidrato= {:.2f}g'.format(carboidrato))
        print('Gordura= {:.2f}g'.format(gordura))
        perderkcal = perder - prokcal - gorkcal
        carboperder = perderkcal / 4
        print('{:=^50}'.format('\033[1;4;7;40mMacros para perder peso!\033[m'))
        print('\033[1mProteína= {:.2f}g'.format(proteina))
        print('Carboidrato= {:.2f}g'.format(carboperder))
        print('Gordura= {:.2f}g'.format(gordura))
        ganharkcal = ganhar - prokcal - gorkcal
        carboganhar = ganharkcal / 4
        print('{:=^50}'.format('\033[1;4;7;40mMacros para ganhar peso!\033[m'))
        print('\033[1mProteína= {:.2f}g'.format(proteina))
        print('Carboidrato= {:.2f}g'.format(carboganhar))
        print('Gordura= {:.2f}g'.format(gordura))
    if atividade == 3:
        calculobfF = log10(quadril + cintura - pescoco)
        calculo2bfF = log10(altura)
        calculo3bfF = (1.296 - 0.350 * calculobfF) + (0.221 * calculo2bfF)
        calculo4bfF = 495 / calculo3bfF - 450
        print('\033[1mBF = {:.2f}%'.format(calculo4bfF))
        masssamag = peso - peso * (calculo4bfF / 100)
        print('Massa Magra = {:.2f} Kg'.format(masssamag))
        massagor = peso - masssamag
        print('Massa Gorda = {:.2f} Kg'.format(massagor))
        taxaMBF = 655 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)
        print('Taxa metabólica Basal = {:.2f} Kcal'.format(taxaMBF))
        manter = taxaMBF * 1.55
        perder = manter - 458
        ganhar = manter + 458
        print('Calorias necessárias para manter o peso: {:.2f} Kcal'.format(manter))
        print('Calorias para ganhar peso: {:.2f} Kcal'.format(ganhar))
        print('Calorias para perder peso: {:.2f} Kcal'.format(perder))
        print('\033[34m=-\033[m' * 42)
        proteina = 2.5 * peso
        gordura = 0.8 * peso
        prokcal = proteina * 4
        gorkcal = gordura * 9
        carbokcal = manter - prokcal - gorkcal
        carboidrato = carbokcal / 4
        print('{:=^50}'.format('\033[1;4;7;40mMacros para manter peso!\033[m'))
        print('\033[1mProteína= {:.2f}g'.format(proteina))
        print('Carboidrato= {:.2f}g'.format(carboidrato))
        print('Gordura= {:.2f}g'.format(gordura))
        perderkcal = perder - prokcal - gorkcal
        carboperder = perderkcal / 4
        print('{:=^50}'.format('\033[1;4;7;40mMacros para perder peso!\033[m'))
        print('\033[1mProteína= {:.2f}g'.format(proteina))
        print('Carboidrato= {:.2f}g'.format(carboperder))
        print('Gordura= {:.2f}g'.format(gordura))
        ganharkcal = ganhar - prokcal - gorkcal
        carboganhar = ganharkcal / 4
        print('{:=^50}'.format('\033[1;4;7;40mMacros para ganhar peso!\033[m'))
        print('\033[1mProteína= {:.2f}g'.format(proteina))
        print('Carboidrato= {:.2f}g'.format(carboganhar))
        print('Gordura= {:.2f}g'.format(gordura))
    if atividade == 4:
        calculobfF = log10(quadril + cintura - pescoco)
        calculo2bfF = log10(altura)
        calculo3bfF = (1.296 - 0.350 * calculobfF) + (0.221 * calculo2bfF)
        calculo4bfF = 495 / calculo3bfF - 450
        print('\033[1mBF = {:.2f}%'.format(calculo4bfF))
        masssamag = peso - peso * (calculo4bfF / 100)
        print('Massa Magra = {:.2f} Kg'.format(masssamag))
        massagor = peso - masssamag
        print('Massa Gorda = {:.2f} Kg'.format(massagor))
        taxaMBF = 655 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)
        print('Taxa metabólica Basal = {:.2f} Kcal'.format(taxaMBF))
        manter = taxaMBF * 1.725
        perder = manter - 510
        ganhar = manter + 510
        print('Calorias necessárias para manter o peso: {:.2f} Kcal'.format(manter))
        print('Calorias para ganhar peso: {:.2f} Kcal'.format(ganhar))
        print('Calorias para perder peso: {:.2f} Kcal'.format(perder))
        print('\033[34m=-\033[m' * 42)
        proteina = 2.5 * peso
        gordura = 0.8 * peso
        prokcal = proteina * 4
        gorkcal = gordura * 9
        carbokcal = manter - prokcal - gorkcal
        carboidrato = carbokcal / 4
        print('{:=^50}'.format('\033[1;4;7;40mMacros para manter peso!\033[m'))
        print('\033[1mProteína= {:.2f}g'.format(proteina))
        print('Carboidrato= {:.2f}g'.format(carboidrato))
        print('Gordura= {:.2f}g'.format(gordura))
        perderkcal = perder - prokcal - gorkcal
        carboperder = perderkcal / 4
        print('{:=^50}'.format('\033[1;4;7;40mMacros para perder peso!\033[m'))
        print('\033[1mProteína= {:.2f}g'.format(proteina))
        print('Carboidrato= {:.2f}g'.format(carboperder))
        print('Gordura= {:.2f}g'.format(gordura))
        ganharkcal = ganhar - prokcal - gorkcal
        carboganhar = ganharkcal / 4
        print('{:=^50}'.format('\033[1;4;7;40mMacros para ganhar peso!\033[m'))
        print('\033[1mProteína= {:.2f}g'.format(proteina))
        print('Carboidrato= {:.2f}g'.format(carboganhar))
        print('Gordura= {:.2f}g'.format(gordura))
    if atividade == 5:
        calculobfF = log10(quadril + cintura - pescoco)
        calculo2bfF = log10(altura)
        calculo3bfF = (1.296 - 0.350 * calculobfF) + (0.221 * calculo2bfF)
        calculo4bfF = 495 / calculo3bfF - 450
        print('\033[1mBF = {:.2f}%'.format(calculo4bfF))
        masssamag = peso - peso * (calculo4bfF / 100)
        print('Massa Magra = {:.2f} Kg'.format(masssamag))
        massagor = peso - masssamag
        print('Massa Gorda = {:.2f} Kg'.format(massagor))
        taxaMBF = 655 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)
        print('Taxa metabólica Basal = {:.2f} Kcal'.format(taxaMBF))
        manter = taxaMBF * 1.9
        perder = manter - 550
        ganhar = manter + 550
        print('Calorias necessárias para manter o peso: {:.2f} Kcal'.format(manter))
        print('Calorias para ganhar peso: {:.2f} Kcal'.format(ganhar))
        print('Calorias para perder peso: {:.2f} Kcal'.format(perder))
        print('\033[34m=-\033[m' * 42)
        proteina = 2.5 * peso
        gordura = 0.8 * peso
        prokcal = proteina * 4
        gorkcal = gordura * 9
        carbokcal = manter - prokcal - gorkcal
        carboidrato = carbokcal / 4
        print('{:=^50}'.format('\033[1;4;7;40mMacros para manter peso!\033[m'))
        print('\033[1mProteína= {:.2f}g'.format(proteina))
        print('Carboidrato= {:.2f}g'.format(carboidrato))
        print('Gordura= {:.2f}g'.format(gordura))
        perderkcal = perder - prokcal - gorkcal
        carboperder = perderkcal / 4
        print('{:=^50}'.format('\033[1;4;7;40mMacros para perder peso!\033[m'))
        print('\033[1mProteína= {:.2f}g'.format(proteina))
        print('Carboidrato= {:.2f}g'.format(carboperder))
        print('Gordura= {:.2f}g'.format(gordura))
        ganharkcal = ganhar - prokcal - gorkcal
        carboganhar = ganharkcal / 4
        print('{:=^50}'.format('\033[1;4;7;40mMacros para ganhar peso!\033[m'))
        print('\033[1mProteína= {:.2f}g'.format(proteina))
        print('Carboidrato= {:.2f}g'.format(carboganhar))
        print('Gordura= {:.2f}g'.format(gordura))
else:
    print('Opção inválida. Tente de novo!')

