def run():
    dia1 = int(input().split()[1])
    hora_dia1, minuto_dia1, segundo_dia1 = list(map(int, input().split(' : ')))

    dia2 = int(input().split()[1])
    hora_dia2, minuto_dia2, segundo_dia2 = list(map(int, input().split(' : ')))

    segundos_inicial = segundo_dia1 +\
                        minuto_dia1*60 +\
                        hora_dia1*60*60 +\
                        dia1*24*60*60

    segundos_final = segundo_dia2 +\
                        minuto_dia2*60 +\
                        hora_dia2*60*60 +\
                        dia2*24*60*60

    duracao_em_segundo = segundos_final - segundos_inicial

    dias = duracao_em_segundo // (24*60*60) # -> divisao inteira
    resto = duracao_em_segundo % 2 # -> resto da divisao inteira

    horas, duracao_em_segundo = divmod(duracao_em_segundo, 60*60)

    minutos, duracao_em_segundo = divmod(duracao_em_segundo, 60)

    segundos = duracao_em_segundo

    print(f"""{dias} dia(s)
{horas} hora(s)
{minutos} minuto(s)
{segundos} segundo(s)""")

run()

try:
    while True:
        run()
except EOFError:
    pass
