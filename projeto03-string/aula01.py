# Vídeo 02 - Iniciando com strings

meuNome = 'Rodrigo'
minhaIdade = 26
sobreMim = 'Meu nome é Rodrigo e minha idade é 26'

print(meuNome)
print(type(meuNome))
print(minhaIdade)
print(type(minhaIdade))
print(sobreMim)
print(type(sobreMim))

# Vídeo 03 - Fatiamento e índices de strings

sobreMim = 'Meu nome é Rodrigo e minha idade é 26'

substring = sobreMim[35:]
print(substring)

argumento = 'moedaorigem=real'
substring = argumento[:11]
print(substring)

# Vídeo 04 - O método find

argumento = 'moedaorigem=real'
index = argumento.find('=')
substring = argumento[index + 1:]
print(substring)

argumento = 'moedaorigem=real'
listaargumentos = argumento.split('=')
print(listaargumentos)