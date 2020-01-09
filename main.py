from grid import Grid

# Solicitando R, C e N ao usuario
print('Informe o numero de linhas, colunas e os segundos a serem simulados:')
dados_str = raw_input('>> ')

# Separando valores digitados
dados_arr = dados_str.split(' ')
num_linhas = int(dados_arr[0])
num_colunas = int(dados_arr[1])
segundos = int(dados_arr[2])

# Solicitando estado inicial do grid
linhas_arr = []
print('\nInforme agora o conteudo de cada linha, uma por vez. Utilize \'O\' para bombas, \'X\' para obstaculos e \'.\' para espacos vazios.')
for linha in range(0, num_linhas):
  linha = raw_input('>> ')
  linhas_arr.append(list(linha))

# Imprimindo grid
grid = Grid(linhas_arr, segundos)
grid.passar_segundos(segundos)
print("\nApos " + str(segundos) + " segundos, o grid estara da seguinte forma:")
print(grid)
