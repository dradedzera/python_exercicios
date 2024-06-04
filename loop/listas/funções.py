def exibirMensagem(nome, mensagem="Seja bem vindo"):
    print(f"{mensagem} {nome}")
    return f"Usuário logado: {nome}"

nome_usuario = input('Digite o nome de usuário: ')
msg = input('Digite umamensagem: ')
usuario = exibirMensagem(nome_usuario, msg)
print(usuario)

print(50 * '-')

nome_usuario = input('Digite o nome de usuário: ')
msg = input('Digite umamensagem: ')
usuario = exibirMensagem(nome_usuario, msg)
print(usuario)