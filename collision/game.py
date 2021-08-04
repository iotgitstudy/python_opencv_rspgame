import os
import pygame
##############################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()


# 화면 크기 설정
screen_width = 1200 # 가로 크기
screen_height = 700 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("crash")

# FPS
clock = pygame.time.Clock()

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") # images 폴더 위치 반환
data_path = os.path.join(current_path, "data") # data 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "back2.png"))
background2 = pygame.image.load(os.path.join(image_path, "back2.png"))
background_size = background.get_rect().size
background_width = background_size[0]
background_height = background_size[1]
background_x_pos = 0
background_y_pos = 0
background_speed = 5
background2_size = background2.get_rect().size
background2_width = background2_size[0]
background2_height = background2_size[1]
background2_x_pos = 0
background2_y_pos = 0
background2_speed = 5
#캐릭터 만들기
me = pygame.image.load(os.path.join(image_path, "character.png"))
me_size = me.get_rect().size
me_width = me_size[0]
me_height = me_size[1]
me_x_pos = 0
me_y_pos = (screen_height - me_height)/2
me_speed = 5

running = True
while running: 

    #화면에 그리기

    dt = clock.tick(20)
    screen.blit(background, (background_x_pos, background_y_pos))
    screen.blit(background2, (background2_x_pos, background2_y_pos))
    screen.blit(me, (me_x_pos, me_y_pos))

    if background_x_pos == 0:
        background2_x_pos = background_width
    if background2_x_pos == 0:
        background_x_pos = background2_width

    


    background_x_pos -= background_speed
    background2_x_pos -= background2_speed




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()




    

# 2초 대기
