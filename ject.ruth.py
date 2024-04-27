from time import sleep
def criar_link_email(email, texto='Enviar e-mail'):
    link = f'mailto:{email}'
    return link
email = 'ruthgabriellesf@gmail.com'
link_email = criar_link_email(email)

print('-' * 45)
print('\033[40:35:7:1m{:^45}\033[m'.format('CONSULTORIA RUTH GABRIELLE:'))
print('-' * 45)

servicos = {
    1: ('[1]CONSELHO PRA VIDA', 50.00),
    2: ('[2]FORMATAR SEU PC', 60.00),
    3: ('[3]ME CONTRATAR PRA SUA EMPRESA', 1600)}

for servico, (descricao, preco) in servicos.items():
    print(f'{descricao:-<35}', end='')
    print(f'R${preco:>5.2f}\033[m')

print('-' * 45)
total_servicos = 0
total_valor = 0
preco = [50,60,1600]
while True:
    escolha = int(input('Escolha um serviço: '))
    if escolha == 1:
        total_servicos += 1
        total_valor += preco[0]
        print(f'Você escolheu: conselho pra vida!')
        print('Deixe me pensar...')
        sleep(4)
        print('\033[40:32:7:1mAceite suas limitações e trabalhe suas competências!\033[m')

    if escolha == 2:
        total_servicos += 1
        total_valor += preco[1]
        print('Você escolheu: formatar PC!')
        print('\033[40:33:7:1m{:^52}\033[m'.format('Aguarde!'))
        sleep(4)
        print('\033[40:32:7:1m{:^52}\033[m'.format('Formatado com sucesso!'))

    if escolha == 3:
        total_servicos += 1
        total_valor += preco[2]
        print('\033[40:32:7:1mEssa foi uma bela escolha!\033[m')
        print(f'Entre em contato comigo:\n📩 {link_email}\033[m')
    print('-' * 45)
    adc = (input('Adicionar mais serviços? [S/N]: ')).strip().upper()[0]
    if adc == 'S':
        adc = escolha
    elif adc == 'N':
        break
    else:
        print('Opção inválida. Tente novamente.')
print(f'Você escolheu {total_servicos} serviço(s), somando um total de \033[32mR${total_valor:.2f}\033[m')
print('\033[40:35:7:1m{:^52}\033[m'.format('--->OBRIGADA<---'))

