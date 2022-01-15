import speedtest

test = speedtest.Speedtest()

# faz o teste de download e convert em mb/s
dow = test.download()
rs_down = round(dow)
f_dow = int(rs_down/ 1e+6)

# faz o teste de upload e convert em mb/s
up = test.upload()
rs_up = round(up)
f_up = int(rs_up/ 1e+6)

print(f'Sua velocidade de download é: {f_dow} mb/s')
print(f'Sua velocidade de upload é: {f_up} mb/s')