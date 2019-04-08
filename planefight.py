import pygame
import sys
from settings import Settings

#设置背景色
bg_color =(110,123,23)

def run_game():
    pygame.init() #初始化游戏
    screen = pygame.display.set_mode((800,800))#创建一个屏幕对象 大小
    pygame.display.set_caption("飞机大战")#标题
    while True:
        #监控键盘与鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#判断是否出退出
                sys.exit()

        #绘制屏幕
        screen.fill(bg_color)
        #让绘制的屏幕可见
        pygame.display.flip()


run_game()
