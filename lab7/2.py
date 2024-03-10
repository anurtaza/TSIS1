import time
import pygame as pg
pg.init()

azazelPath = "/Users/ayaulymnurtaza/Downloads/lab7/Азазель.mp3"
macanPath = "/Users/ayaulymnurtaza/Downloads/lab7/Самый пьяный округ в мире - MACAN.mp3"
janagaPath = "/Users/ayaulymnurtaza/Downloads/lab7/JANAGA - По сути.mp3"
sc = pg.display.set_mode((480, 360))
pg.display.set_caption("Music Player")
clock = pg.time.Clock()
mozzart = pg.mixer.music.load(macanPath)
boom = pg.mixer.music.load(janagaPath)
despacito = pg.mixer.music.load(azazelPath)
musicList = [azazelPath, macanPath, janagaPath]
pg.mixer.music.play(-1)
backgr = pg.image.load("/Users/ayaulymnurtaza/Downloads/lab7/IMG_6639.JPG")

sc.blit(backgr, (0, 0))
flPlay = False
run = True
index = 0
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                flPlay = not flPlay
                if flPlay:
                    pg.mixer.music.pause()
                else:
                    pg.mixer.music.unpause()
            elif event.key == pg.K_RIGHT:
                
                index += 1
                if index == len(musicList):
                    index = 0
                pg.mixer.music.load(musicList[index])
                pg.mixer.music.play()
            elif event.key == pg.K_LEFT:
                index -= 1
                if index == -1:
                    index = len(musicList)-1
                pg.mixer.music.load(musicList[index])
                pg.mixer.music.play()


    pg.display.flip()
    clock.tick(60)