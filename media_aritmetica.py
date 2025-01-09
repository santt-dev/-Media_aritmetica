primeira_avaliação = float (input('Primeira nota: \n'))
Segunda_avaliação = float (input('Segunda nota: \n'))
Terceira_avaliação = float (input(' Terceira nota: \n'))
Quarta_avaliação = float (input('Quarta nota: \n'))

media_anual = ((primeira_avaliação + Segunda_avaliação + Terceira_avaliação + Quarta_avaliação ) / 2)
if media_anual >= 7:
    print(f'aluno aprovado media é : {media_anual, :.2f}')
    
elif media_anual <= 6 and media_anual >= 5:
    print(f'Recuperação coitado, sua media: {media_anual}')


else:
    if media_anual < 5:
        print(f'{media_anual} Se lascou')