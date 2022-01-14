from pytube import YouTube

link = 'link do video no youtube'
path = 'caminho da pasta onde será salvo'
yt = YouTube(link)

ys = yt.streams.get_highest_resolution()

print('Baixando...')
ys.download(path)
print('download completo')
