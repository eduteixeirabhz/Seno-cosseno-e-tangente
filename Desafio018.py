from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo desejado: '))
se = sin(radians(ang))
print('O Seno para o ângulo de {} graus é: {:.2f}'.format(ang, se))
co = cos(radians(ang))
print('O Cosseno para o ângulo de {}  graus é: {:.2f}'.format(ang, co))
ta = tan(radians(ang))
print('A Tangente para o ângulo de {} graus é: {:.2f}'.format(ang, ta))
##print('O Ângulo digitado foi: {:.2f} o valor do Seno é: {:.2f}, o valor do Cosceno é {:.2f} e o valor da Tangente é: {:.2f}'.format(ang, se, co, ta))