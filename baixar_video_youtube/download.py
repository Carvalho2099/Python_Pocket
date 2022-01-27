from pytube import YouTube

link = 'https://www.youtube.com/watch?v=8Y4NXE7_yWM&ab_channel=JornadaRPA'
path = r'C:\Users\carva\Downloads'
yt = YouTube(link)

ys = yt.streams.get_highest_resolution()

print('Baixando...')
ys.download(path)
print('download completo')
