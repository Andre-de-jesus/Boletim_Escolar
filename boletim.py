import time
import os
linha = ('-' * 67)
vazio = (' ')
diretoria = {'professores': ' '}
alunos = {'nome': ' ', 'idade': ' ', 'número de matricula': ' ', 'português': ' ', 'matematica': ' ', 'hístoria': ' ', 'geografia': ' ', 'ciências': ' ', 'artes': ' ', 'ingles': ' ', 'educaçao fisica': ' ', 'identidade e cultura': ' '}

while True:
    print(linha)
    print('Bem vindo ao colégio viver para aprender'.center(67))
    print(linha)
    print(vazio)
    print('Digite 1 se você é da coordenação')
    print('Digite 2 se você é professor')
    print('Digite 3 se você é aluno ou responsável')
    print(vazio)
    print(linha)
    print(vazio)
    escolha = int(input('Digite aqui sua escolha: '))
    os.system('clear') or None
    if escolha == 1:
        print(linha)
        print('Bem vindo a coordenação do colégio viver para aprender '.center(67))
        print(linha)
        print(vazio)
        diretoria['professores'] = str(input('Digite aqui seu nome completo: '))
        time.sleep(2)
        print(vazio)
        print('Professor cadastrado com sucesso !')
        time.sleep(1)
        print(vazio)
        os.system('clear') or None
    elif escolha == 2:
        print(linha)
        print('Bem vindo a sala dos professores'.center(67))
        print(linha)
        verificação = str(input('Digite aqui seu nome completo: '))
        if verificação in diretoria.values():
            print(vazio)
            print(vazio)
            print('Digite 1 se você deseja cadastrar um novo aluno')
            print(vazio)
            print(linha) 
            escolha1 = int(input('Digite aqui sua escolha: '))
            os.system('clear') or None
            if escolha1 == 1:
                    print(linha)
                    print('Bem vindo a sala dos professores'.center(67))
                    print(linha)
                    alunos['nome'] = str(input('Digite aqui o nome do aluno: '))
                    alunos['idade'] = int(input('Digite aqui a idade do aluno: '))
                    alunos['serie'] = int(input('Digite aqui a serie do aluno: '))
                    alunos['número de matricula'] = int(input('Digite aqui o número de matricula do aluno: '))
                    print(vazio)
                    time.sleep(1)
                    print
                    alunos['português'] = float(input('Digite aqui a nota da matéria de português do aluno: '))
                    alunos['matematica'] = float(input('Digite aqui a nota da matéria de matematica do aluno: '))
                    alunos['hístoria'] = float(input('Digite aqui a nota da matéria de historia do aluno: '))
                    alunos['geografia'] = float(input('Digite aqui a nota do aluno em geografia: '))
                    alunos['ciências'] = float(input('Digite aqui a nota do aluno em ciências: '))
                    alunos['artes'] = float(input('Digite aqui a nota do aluno em artes: '))
                    alunos['inglês'] = float(input('Digite aqui a nota do aluno em inglês: '))
                    alunos['educação fisíca'] = float(input('Digite aqui a nota do aluno em educação fisica: '))
                    alunos['identidade e cultura'] = float(input('Digite aqui a nota do aluno em identidade e cultura: '))
                    print(vazio)
                    print(linha)
                    os.system('clear') or None
    elif escolha == 3:
         print(linha)
         print('Bem vindo a sala do aluno'.center(67))
         print(linha)
         print(vazio)
         matricula = int(input('Digite aqui seu número de matricula: '))
         os.system('clear') or None
         if matricula in alunos.values():
           print(linha)
           print('Bem vindo a sala do aluno'.center(67))
           print(linha)
           print(vazio)
           print('Digite 1 se você deseja ver as notas do aluno')
           escolha3 = int(input('Digite aqui sua escolha: '))
           os.system('clear') or None
           if escolha3 == 1:
               print(linha)
               print('Bem vindo a sala do aluno'.center(67))
               print(linha)
               print(vazio)
               for chave, valor in alunos.items():
                   print(chave, valor)
    opção = str(input('Digite [S] se você deseja continuar ou digite [N] se você deseja encerrar o programa: '))
    os.system('clear') or None
   