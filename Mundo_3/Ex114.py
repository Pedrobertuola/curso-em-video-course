# Solução conforme vídeo

# import urllib  # Import não necessário
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')
    # print(site.read())  # Extra

    # com site.read() é possível pegar o conteúdo HTML do site que acabou de acessar

# Tem um pequeno delay ao executar o código, pois essa biblioteca vai realmente na internet ver
# se a conexão está funcionando.