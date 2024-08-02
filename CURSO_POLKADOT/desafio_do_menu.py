def menu():
    alunos = {}

    def listar_alunos(**kwargs):
        if kwargs.get('listagem'):
            if alunos:
                for matricula, dados in alunos.items():
                    print(f"\nMatrícula: {matricula}, \nNome: {dados['nome']}, \nIdade: {dados['idade']}")
            else:
                print("\nNenhum aluno cadastrado.")
        else:
            print("\nErro: Parâmetro 'listagem' não fornecido.")

    def adicionar_aluno(**kwargs):
        matricula = kwargs.get('matricula')
        nome = kwargs.get('nome')
        idade = kwargs.get('idade')
        
        if matricula and nome and idade is not None:
            alunos[matricula] = {'nome': nome, 'idade': idade}
            print(f"\nAluno {nome} adicionado com sucesso.")
        else:
            print("\nErro: Dados incompletos para adicionar aluno.")
    
    def remover_aluno(**kwargs):
        matricula = kwargs.get('matricula')
        
        if matricula and matricula in alunos:
            del alunos[matricula]
            print(f"\nAluno com matrícula {matricula} removido com sucesso.")
        else:
            print("\nErro: Aluno não encontrado ou matrícula não fornecida.")
    
    def atualizar_idade(**kwargs):
        matricula = kwargs.get('matricula')
        nova_idade = kwargs.get('idade')
        
        if matricula in alunos and nova_idade is not None:
            alunos[matricula]['idade'] = nova_idade
            print(f"\nIdade do aluno com matrícula {matricula} atualizada para {nova_idade}.")
        else:
            print("\nErro: Aluno não encontrado ou idade não fornecida.")
    
    def first():
        listar_alunos(listagem=True)

    def second():
        matricula = input("\nDigite a matrícula do aluno: ")
        nome = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        adicionar_aluno(matricula=matricula, nome=nome, idade=idade)

    def third():
        matricula = input("\nDigite a matrícula do aluno para remover: ")
        remover_aluno(matricula=matricula)

    def fourth():
        matricula = input("\nDigite a matrícula do aluno: ")
        idade = int(input("Digite a nova idade do aluno: "))
        atualizar_idade(matricula=matricula, idade=idade)

    def fifth():
        print("Saindo do programa...")
        return True

    opcoes = {
        '1': first,
        '2': second,
        '3': third,
        '4': fourth,
        '5': fifth
    }

    while True:
        print("\nMenu:")
        print("1. Listar alunos")
        print("2. Adicionar aluno")
        print("3. Remover aluno")
        print("4. Atualizar idade de um aluno")
        print("5. Sair")
        
        opcao = input("\nEscolha uma opção (1-5): ")
        action = opcoes.get(opcao, None)

        if action:
            if action():
                break
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
