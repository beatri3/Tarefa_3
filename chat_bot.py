import os
from datetime import datetime

def obter_resposta(texto: str) -> str:
    comando: str = texto.lower()

    respostas = {
        ('ola', 'boa tarde', 'bom dia'): 'Olá tudo bem!',
        ('bye', 'adeus', 'tchau'): 'Gostei de falar contigo! Até breve...',
        ('quantos planetas no sistema solar', 'planetas no sistema solar'): 'Existem 8 planetas no Sistema Solar.',
        
        'como estas': 'Estou bem, obrigado!',
        'como te chamas': 'O meu nome é: Bot :)',
        'tempo': 'Está um dia de sol!',
        'horas': f'São: {datetime.now():%H:%M} horas',
        'data': f'Hoje é dia: {datetime.now():%d-%m-%Y}',
        'quantos continentes existem': 'De acordo com o Modelo Continental mais comum existem 7 continentes!',
        'diz-me uma curiosidade': 'No Barreiro, em Portugal, o sol põe-se 20 segundos mais cedo do que em qualquer outro lugar do mundo, devido à sua localização geográfica.',
        'quantos anos durou o imperio romano': 'O Império Romano durou cerca de 500 anos, desde 27 a.C. até 476 d.C.',
        'capital de portugal': 'A capital de Portugal é Lisboa.'
    }
    
    if comando in respostas:
        return respostas[comando]

    for chave, resposta in respostas.items():
        if isinstance(chave, tuple) and comando in chave:
            return resposta

    return f'Desculpa, não entendi a questão! {texto}'


def chat() -> None:
    print('Bem-vindo ao ChatBot!')
    print('Escreva "bye" para sair do chat')
    name: str = input('Bot: Como te chamas? ')
    print(f'Bot: Olá, {name}! \n Como te posso ajudar?')

    while True:
        user_input: str = input('Tu: ')
        resposta: str = obter_resposta(user_input)
        print(f'Bot: {resposta}')

        if resposta == 'Gostei de falar contigo! Até breve...':
            break

    print('Chat acabou')
    print()


def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    chat()


if __name__ == '__main__':
    main()
