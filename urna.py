candidato_x = 0
candidato_y = 0
candidato_z = 0
nulo = 0

while True:
    print(' Candidato_X => 889 \n Candidato_Y => 847 \n Candidato_Z => 515 \n Branco => 0')
    voto = int(input('Escolha seu voto: '))
    
    if voto == 889 :
        candidato_x = candidato_x + 1
    elif voto == 847 :
        candidato_y = candidato_y + 1
    elif voto == 515 :
        candidato_z = candidato_z + 1
    else :
        nulo = nulo + 1
    
    fim = input('Deseja finalizar a votação? ')
    if fim == 'sim' :
        break

if candidato_x > candidato_y and candidato_x > candidato_z :
    print('Candidato X venceu')
elif candidato_y > candidato_x and candidato_y > candidato_z :
    print('Candidato Y venceu')
elif candidato_z > candidato_x and candidato_z > candidato_y :
    print('Candidato Z venceu')
else : 
    print('Não teve vencedores')

print('Voto candidato X:', candidato_x)
print('Voto candidato Y:', candidato_y)
print('Voto candidato Z:', candidato_z)
print('Branco:', nulo)