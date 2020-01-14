"""
Title :
author:YL
date:
"""
import random
import pygame
import sys
from pygame.locals import *

Snakespeed = 17  # 蛇的移动速度
Window_Width = 800
Window_Height = 500
Cell_Size = 20  # 单个单元格的大小

assert Window_Width % Cell_Size == 0, "Window width must be a multiple of cell size."
# 不满足条件则返回提示
# 保证窗口宽度必须是单元格的整数倍.
assert Window_Height % Cell_Size == 0, "Window height must be a multiple of cell size."
# 保证窗口的高度必须是单元格的整数倍
Cell_W = int(Window_Width / Cell_Size)  # 单元格宽度
Cell_H = int(Window_Height / Cell_Size)  # 单元格高度

# 定义颜色
White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)
Green = (0, 255, 0)
DARKGreen = (0, 155, 0)
DARKGRAY = (40, 40, 40)
YELLOW = (255, 255, 0)
Red_DARK = (150, 0, 0)
BLUE = (0, 0, 255)
BLUE_DARK = (0, 0, 150)

BGCOLOR = Black  # 背景颜色

# 定义键盘
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
HEAD = 0


def main():
    global SnakespeedCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    SnakespeedCLOCK = pygame.time.Clock()  # 创建时钟对象 (可以控制游戏循环频率)
    DISPLAYSURF = pygame.display.set_mode((Window_Width, Window_Height))  # 窗口大小
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Snake')

    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()


def runGame():
    # 定义了一个随机的贪吃蛇的坐标
    startx = random.randint(5, Cell_W - 6)
    starty = random.randint(5, Cell_H - 6)
    wormCoords = [{'x': startx, 'y': starty},  # 贪吃蛇坐标
                  {'x': startx - 1, 'y': starty},
                  {'x': startx - 2, 'y': starty}]
    direction = RIGHT

    # 定义苹果起始的随机位置
    apple = getRandomLocation()

    while True:  # 死循环让游戏一直持续下去
        for event in pygame.event.get():  # 事件循环
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate()

                    # 判断snake是否碰撞到墙壁或者碰撞到自己本身
        if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['x'] == Cell_W or wormCoords[HEAD]['y'] == -1 or \
                wormCoords[HEAD]['y'] == Cell_H:
            return  # game over 撞到墙了
        for wormBody in wormCoords[1:]:
            if wormBody['x'] == wormCoords[HEAD]['x'] and wormBody['y'] == wormCoords[HEAD]['y']:
                return  # game over 撞到自己了

        # 判断snake是否吃到了苹果
        if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']:

            apple = getRandomLocation()  # 当苹果被吃了后重新随机一个坐标
        else:
            del wormCoords[-1] #删除尾部

        # 通过在snake的移动方向上增加一个段来移动
        if direction == UP:
            newHead = {'x': wormCoords[HEAD]['x'],
                       'y': wormCoords[HEAD]['y'] - 1}
        elif direction == DOWN:
            newHead = {'x': wormCoords[HEAD]['x'],
                       'y': wormCoords[HEAD]['y'] + 1}
        elif direction == LEFT:
            newHead = {'x': wormCoords[HEAD][
                                'x'] - 1, 'y': wormCoords[HEAD]['y']}
        elif direction == RIGHT:
            newHead = {'x': wormCoords[HEAD][
                                'x'] + 1, 'y': wormCoords[HEAD]['y']}
        wormCoords.insert(0, newHead) # 插入头部
        DISPLAYSURF.fill(BGCOLOR)
        drawGrid()
        drawWorm(wormCoords)
        drawApple(apple)
        drawScore(len(wormCoords) - 3)  # 屏幕上写成绩
        pygame.display.update() #更新屏幕
        SnakespeedCLOCK.tick(Snakespeed)


def drawPressKeyMsg():  # 绘制提示信息的函数
    pressKeySurf = BASICFONT.render('Press a key to play.', True, White)
    pressKeyRect = pressKeySurf.get_rect()  # 获得矩形大小
    pressKeyRect.topleft = (Window_Width - 200, Window_Height - 30)  # 取的是 左上角坐标的值
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)  # 绘制提示开始游戏动画


def checkForKeyPress():  # 键盘事件
    if len(pygame.event.get(QUIT)) > 0:
        terminate()  # 退出游戏
    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:  # 如果按下的是ESC则退出
        terminate()
    return keyUpEvents[0].key


def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    titleSurf1 = titleFont.render('Snake!', True, White, DARKGreen)
    degrees1 = 0
    degrees2 = 0
    while True:
        DISPLAYSURF.fill(BGCOLOR)  # 背景为黑色
        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (Window_Width / 2, Window_Height / 2)
        DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)

        drawPressKeyMsg()

        if checkForKeyPress():
            pygame.event.get()  # clear event queue
            return
        pygame.display.update()
        SnakespeedCLOCK.tick(Snakespeed)
        degrees1 += 3  # rotate by 3 degrees each frame
        degrees2 += 7  # rotate by 7 degrees each frame


def terminate():  # 定义的一个退出函数
    pygame.quit()
    sys.exit()


def getRandomLocation():  # 随机苹果位置
    return {'x': random.randint(0, Cell_W - 1), 'y': random.randint(0, Cell_H - 1)}


def showGameOverScreen():  # 游戏结束界面
    gameOverFont = pygame.font.Font('freesansbold.ttf', 100)
    gameSurf = gameOverFont.render('Game', True, White)
    overSurf = gameOverFont.render('Over', True, White)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (Window_Width / 2, 10)
    overRect.midtop = (Window_Width / 2, gameRect.height + 10 + 25)

    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress()  # 清空事件中所有的按键

    while True:
        if checkForKeyPress():
            pygame.event.get()  # 清空事件队列
            return


def drawScore(score):  # 画分数
    scoreSurf = BASICFONT.render('Score: %s' % (score), True, White)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (Window_Width - 120, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)


def drawWorm(wormCoords):  # 画蛇
    for coord in wormCoords:
        x = coord['x'] * Cell_Size
        y = coord['y'] * Cell_Size
        wormSegmentRect = pygame.Rect(x, y, Cell_Size, Cell_Size)
        pygame.draw.rect(DISPLAYSURF, DARKGreen, wormSegmentRect)
        wormInnerSegmentRect = pygame.Rect(
            x + 4, y + 4, Cell_Size - 8, Cell_Size - 8)
        pygame.draw.rect(DISPLAYSURF, Green, wormInnerSegmentRect)


def drawApple(coord): # 画苹果
    x = coord['x'] * Cell_Size
    y = coord['y'] * Cell_Size
    appleRect = pygame.Rect(x, y, Cell_Size, Cell_Size)  # x,y 坐标位置  Cell_Size 宽高大小
    pygame.draw.rect(DISPLAYSURF, Red, appleRect)  #


def drawGrid():  # 画分割线的函数
    for x in range(0, Window_Width, Cell_Size):  # 画垂直线
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, Window_Height))
    for y in range(0, Window_Height, Cell_Size):  # 画水平线
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (Window_Width, y))


if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
