import pickle

def merge(l, lEsq, lDir, dicionario_alunos):
	i = 0 
	j = 0
	k = 0
	
	while i < len(lEsq) and j < len(lDir):
		if f_m1_antes_de_m2(lEsq[i], lDir[j], dicionario_alunos): #lEsq[i] < lDir[j]
			l[k] = lEsq[i]
			i += 1
		else:
			l[k] = lDir[j]
			j += 1
		k += 1
		
	while i < len(lEsq):
		l[k] = lEsq[i]
		i += 1
		k += 1
			
	while j < len(lDir):
		l[k] = lDir[j]
		j += 1
		k += 1

def mSort(l, dicionario_alunos):
	if len(l) > 1:
		meio = len(l) // 2
		lEsq = l[:meio]
		lDir = l[meio:]
		
		mSort(lEsq, dicionario_alunos)
		mSort(lDir, dicionario_alunos)
		
		merge(l, lEsq, lDir, dicionario_alunos)

#Lista com os seguintes critérios de ordenação, nesta ordem.

def f_m1_antes_de_m2(m1, m2, dicionario_alunos):
	nome1 = dicionario_alunos[m1][0]
	nome2 = dicionario_alunos[m2][0]
	print(nome1, nome2)
	ano1 = dicionario_alunos[m1][1][0]
	ano2 = dicionario_alunos[m2][1][0]
	if ano1 > ano2:
		return True
	if ano1 < ano2:
		return False
	if ano1 == ano2:
		semestre1 = dicionario_alunos[m1][1][1]
		semestre2 = dicionario_alunos[m2][1][1]
		if semestre1 > semestre2:
			return True
		if semestre1 < semestre2:
			return False
		if semestre1 == semestre2:
			pontos1 = sum(dicionario_alunos[m1][2])
			pontos2 = sum(dicionario_alunos[m2][2])
			faltas1 = dicionario_alunos[m1][3]
			faltas2 = dicionario_alunos[m2][3]

			if faltas1 == 0:
				pontos1 += 2

			if faltas2 == 0:
				pontos2 += 2

			if pontos1 > 100:
				pontos1 = 100

			if pontos2 > 100:
				pontos2 = 100
			if pontos1 > pontos2:
				return True
			if pontos1 < pontos2:
				return False
			if pontos1 == pontos2:
				if nome1 > nome2:
					return True
				else:
					if m1 > m2:
						return True
					else:
						return False

def main():
	#inicializando o arquivo final
	arquivo = open('entrada100.bin','rb')
	dicionario_alunos = pickle.load(arquivo)
	lista_matriculas = []
	arquivo_saida = open('saida100_1.txt','w')
	#início das funções

	#Passo 1: Criar lista de matrículas a partir do dicionário de matrículas
	for chave in dicionario_alunos:
	  lista_matriculas.append(chave)

	#Passo 2: ordenar lista_matriculas
	mSort(lista_matriculas, dicionario_alunos)
	#lista_matriculas = mSort(lista_matriculas, dicionario_alunos)
	#ordenacaoQuickSort(m1,m2,dicionario_alunos,lista_matriculas)

	#escrita do arquivo final
	for matricula in lista_matriculas:
		ano = dicionario_alunos[matricula][1][0]
		semestre = dicionario_alunos[matricula][1][1]
		nome = dicionario_alunos[matricula][0]
		pontos = sum(dicionario_alunos[matricula][2])
		pprova = dicionario_alunos[matricula][2][0]
		ptrab = dicionario_alunos[matricula][2][1]
		pmarat = dicionario_alunos[matricula][2][2]
		pbonus = dicionario_alunos[matricula][2][3]
		pfaltas = dicionario_alunos[matricula][3]
		#inicializando as variáveis de texto
		if pfaltas == 0:
			pontos = sum(dicionario_alunos[matricula][2]) + 2
			if pbonus > 0:
				string_sem_faltas_e_com_bonus = f'{ano}/{semestre} {matricula} {nome} - {pontos} ({pprova}+{ptrab}+{pmarat} +{pbonus}E +2P = {pontos})'
				print(string_sem_faltas_e_com_bonus)
				arquivo_saida.write(string_sem_faltas_e_com_bonus+'\n')
			else:
				string_sem_faltas = f'{ano}/{semestre} {matricula} {nome} - {pontos} ({pprova}+{ptrab}+{pmarat} +2P = {pontos})'
				print(string_sem_faltas)
				arquivo_saida.write(string_sem_faltas+'\n')
			#arquivo_final.write(string)
		else:
			if pbonus > 0:
				string_com_bonus = f'{ano}/{semestre} {matricula} {nome} - {pontos} ({pprova}+{ptrab}+{pmarat} +{pbonus}E = {pontos})'
				print(string_com_bonus)
				arquivo_saida.write(string_com_bonus+'\n')
			else:
				string_comum = f'{ano}/{semestre} {matricula} {nome} - {pontos} ({pprova}+{ptrab}+{pmarat} = {pontos})'
				print(string_comum)
				arquivo_saida.write(string_comum+'\n')
				#arquivo_final.write(string_comum)

#chamada da função
if __name__ == "__main__":
  main()