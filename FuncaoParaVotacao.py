def voto(ano):
    from datetime import date
    atual = date.today().year    
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos. Voto NEGADO.'
    elif idade >= 16 and idade < 18 or idade > 65:
        return f'Com {idade} anos. Voto OPCIONAL.'
    else:
        return f'Com {idade} anos. Voto OBRIGATORIO.'
    
print('='*30)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
