# Elabore duas estruturas, como é apresentado a seguir:
# CLIENTE	DOCUMENTOS
# cod_cli	num_doc
# nome	    cod_cli
# fone	    dia_venc
#           dia_pag
#           valor
#           juros

# Sabe-se que um documento só pode ser cadastrado para um cliente que já exista.
# Considere que podem existir, no máximo, 15 clientes e 30 documentos. Crie um vetor para clientes e outro para documentos.
# Crie um menu para a realização de cada uma das operações especificadas a seguir:

# ** SISTEMA GERENCIADOR DE CLIENTES E DOCUMENTOS **
# Cadastrar clientes
# Relatório de clientes
# Cadastrar documentos
# Relatório de documentos
# Excluir clientes sem documentos
# Excluir documentos individuais pelo número
# Excluir documentos por cliente
# Excluir documentos por período
# Alterar as informações dos clientes
# Mostrar o total de documentos de determinado cliente
# Sair

# Qual opção deseja?

# .................................................................................................
# Para cada item do menu, desenvolva uma função.

# A seguir são apresentados os detalhes de implementação de cada opção do menu:

# Cadastrar clientes — não pode existir mais que um cliente com o mesmo código.
# Relatório de clientes - listar todos os clientes cadastrados.
# Cadastrar documentos — ao cadastrar um documento, se o dia de pagamento for maior que o dia de vencimento, calcular o campo ‘juros’ do registro documentos (5% sobre o valor original do documento).
# Relatório de documentos - listar todos os documentos cadastrados.
# Excluir clientes — um cliente só poderá ser excluído se não existir nenhum documento associado a ele.
# Excluir documentos individuais — por meio de seu número. Caso o documento não exista, o programa deverá mostrar a mensagem "Documento não encontrado".
# Excluir documentos por cliente — o programa deverá informar o código do cliente e excluir todos os seus documentos. Caso o cliente não exista, deverá mostrar a mensagem "Cliente não encontrado".
# Excluir documentos por período — o programa deverá informar o dia inicial e o dia final e excluir todos os documentos que possuam data de vencimento nesse período.
# Alterar as informações sobre os clientes — só NÃO altere o código do cliente.
# Mostrar o total de documentos de determinado cliente.

class classCliente:
    cod_cli = 0
    nome = ''
    fone = 0


class classDocumentos:
    num_doc = 0
    cod_cli = 0
    dia_venc = 0
    dia_pag = 0
    valor = 0
    juros = 0


def menu():
    print(f'\n** SISTEMA GERENCIADOR DE CLIENTES E DOCUMENTOS **\n1. Cadastrar clientes\n2. Relatório de clientes\n3. Cadastrar documentos\n4. Relatório de documentos\n5. Excluir clientes sem documentos\n6. Excluir documentos individuais pelo número\n7. Excluir documentos por cliente\n8. Excluir documentos por período\n9. Alterar as informações dos clientes\n10. Mostrar o total de documentos de determinado cliente\n11. Sair')

    opcao = int(input('\nQual opção deseja? '))

    return opcao

# Cadastros


def cadastrarClientes(arrayClientes):
    cliente = classCliente()
    numero = 0

    while numero == 0:
        numero = int(input('\nDigite o código do cliente: '))

        for i in range(len(arrayClientes)):
            if arrayClientes[i].cod_cli == numero:
                print('\nCódigo de cliente já cadastrado!')
                numero = 0

    cliente.cod_cli = numero
    cliente.nome = input('Digite o nome do cliente: ')
    cliente.fone = input('Digite o telefone do cliente: ')

    arrayClientes.append(cliente)

    return arrayClientes


def cadastrarDocumentos(arrayClientes, arrayDocumentos):
    documento = classDocumentos()
    numero = 0

    while numero == 0:
        numero = int(input('\nDigite o número do documento: '))

        for i in range(len(arrayDocumentos)):
            if arrayDocumentos[i].num_doc == numero:
                print('\nNúmero de documento já cadastrado!')
                numero = 0

    documento.num_doc = numero

    existe = False

    while existe == False:
        numero = int(input('Digite o código do cliente: '))

        for i in range(len(arrayClientes)):
            if arrayClientes[i].cod_cli == numero:
                documento.cod_cli = numero
                existe = True
        
        if existe == False:
            print('Código de cliente não cadastrado!')

    documento.dia_venc = int(
        input('Digite o dia de vencimento do documento: '))
    documento.dia_pag = int(input('Digite o dia de pagamento do documento: '))
    documento.valor = float(input('Digite o valor do documento: '))

    if documento.dia_pag > documento.dia_venc:
        documento.juros = documento.valor * 0.05

    arrayDocumentos.append(documento)

    return arrayDocumentos

# Relatórios


def relatorioClientes(arrayClientes):
    print('\nRelatório de clientes\n')

    for i in range(len(arrayClientes)):
        print(
            f'Código: {arrayClientes[i].cod_cli}\nNome: {arrayClientes[i].nome}\nTelefone: {arrayClientes[i].fone}\n')


def relatorioDocumentos(arrayDocumentos):
    print('\nRelatório de documentos\n')

    for i in range(len(arrayDocumentos)):
        print(f'Número: {arrayDocumentos[i].num_doc}\nCódigo do cliente: {arrayDocumentos[i].cod_cli}\nDia de vencimento: {arrayDocumentos[i].dia_venc}\nDia de pagamento: {arrayDocumentos[i].dia_pag}\nValor: {arrayDocumentos[i].valor}\nJuros: {arrayDocumentos[i].juros}\n')

# Exclusões


def excluirClientes(arrayClientes, arrayDocumentos):
    numero = int(input('\nDigite o código do cliente: '))

    for i in range(len(arrayClientes)):
        if arrayClientes[i].cod_cli == numero:
            for j in range(len(arrayDocumentos)):
                if arrayDocumentos[j].cod_cli == numero:
                    print('\nCliente não pode ser excluído pois possui documento(s)!')
                else:
                    arrayClientes.pop(i)
                    print('\nCliente excluído!')
                    break

    return arrayClientes


def excluirDocumentosIndividuais(arrayDocumentos):
    excluiu = False
    numero = int(input('\nDigite o número do documento: '))

    for i in range(len(arrayDocumentos)):
        if arrayDocumentos[i].num_doc == numero:
            arrayDocumentos.pop(i)
            print('\nDocumento excluído!')
            excluiu = True

    if excluiu == False:
        print('\nDocumento não encontrado!')

    return arrayDocumentos


def excluirDocumentosPorCliente(arrayClientes, arrayDocumentos):
    numero = int(input('\nDigite o código do cliente: '))
    existe = False

    for i in range(len(arrayClientes)):
        if arrayClientes[i].cod_cli == numero:
            existe = True
            
    posicaoDocumentos = []

    if existe == True:
        for i in range(len(arrayDocumentos)):
            if arrayDocumentos[i].cod_cli == numero:
                posicaoDocumentos.append(i)
    else:
        print('\nCliente não encontrado!')
        
    for i in range(len(posicaoDocumentos)):
        arrayDocumentos.pop(posicaoDocumentos[i])
        print('\nDocumento excluído!')

    return arrayDocumentos


def excluirDocumentosPorPeriodo(arrayDocumentos):
    diaInicial = int(input('\nDigite o dia inicial: '))
    diaFinal = int(input('\nDigite o dia final: '))

    for i in range(len(arrayDocumentos)):
        if arrayDocumentos[i].dia_pag >= diaInicial and arrayDocumentos[i].dia_pag <= diaFinal:
            arrayDocumentos.pop(i)
            print('\nDocumento excluído!')

    return arrayDocumentos

# Alterações


def alterarClientes(arrayClientes):
    numero = int(input('\nDigite o código do cliente: '))

    for i in range(len(arrayClientes)):
        if arrayClientes[i].cod_cli == numero:
            option = (input('\nDeseja alterar o nome do cliente? (S/N) '))

            if option == 'S' or option == 's':
                arrayClientes[i].nome = input('\nDigite o nome do cliente: ')

            option = (input('\nDeseja alterar o telefone do cliente? (S/N) '))

            if option == 'S' or option == 's':
                arrayClientes[i].fone = input(
                    '\nDigite o telefone do cliente: ')

            print('\nCliente alterado!')
            
            break

    return arrayClientes

# Totalizadores


def totalizarDocumentos(arrayDocumentos):
    total = 0
    numero = int(input('\nDigite o código do cliente: '))

    for i in range(len(arrayDocumentos)):
        if arrayDocumentos[i].cod_cli == numero:
            total += 1

    print(f'\nTotal de documentos: {total}')


def main():
    arrayClientes = []
    arrayDocumentos = []

    opcao = menu()

    while opcao != 11:
        if opcao == 1:
            if len(arrayClientes) < 15:
                cadastrarClientes(arrayClientes)
            else:
                print('\nNúmero máximo de clientes cadastrados!\n')
        elif opcao == 2:
            relatorioClientes(arrayClientes)
        elif opcao == 3:
            if len(arrayDocumentos) < 30:
                cadastrarDocumentos(arrayClientes, arrayDocumentos)
            else:
                print('\nNúmero máximo de documentos cadastrados!\n')
        elif opcao == 4:
            relatorioDocumentos(arrayDocumentos)
        elif opcao == 5:
            excluirClientes(arrayClientes, arrayDocumentos)
        elif opcao == 6:
            excluirDocumentosIndividuais(arrayDocumentos)
        elif opcao == 7:
            excluirDocumentosPorCliente(arrayClientes, arrayDocumentos)
        elif opcao == 8:
            excluirDocumentosPorPeriodo(arrayDocumentos)
        elif opcao == 9:
            alterarClientes(arrayClientes)
        elif opcao == 10:
            totalizarDocumentos(arrayDocumentos)
        else:
            print('\nOpção inválida!\n')

        opcao = menu()


main()
