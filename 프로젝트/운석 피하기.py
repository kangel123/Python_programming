import pygame
import random

# 초기화
pygame.init()

# FPS 설정
clock = pygame.time.Clock()

# 화면 크기
screen_width = 1280  # 가로 크기
screen_height = 720  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("운석 피하기")

# 배경
background = pygame.image.load("./back.jpg")

# 캐릭터 설정
character = pygame.image.load("./my_character.png")
character = pygame.transform.scale(character, (100, 110))   # 크기 재조정
character_size = character.get_rect().size  # 캐릭터 사이즈 구하기
character_width = character_size[0]         # 캐릭터 가로 크기
character_height = character_size[1]        # 캐릭터 세로 크기

# 캐릭 위치 맞추기
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height-55

# 캐릭 이동 정보
toX = 0
characterSpeed = 0.6

# 운석 설정
meteor1 = pygame.image.load("meteor1.gif")
meteor1 = pygame.transform.scale(meteor1, (100, 100))
meteor2 = pygame.image.load("meteor2.gif")
meteor2 = pygame.transform.scale(meteor2, (100, 100))
meteor3 = pygame.image.load("meteor3.gif")
meteor3 = pygame.transform.scale(meteor3, (100, 100))

meteors = []
for i in range(5):    # 운석 개수
    rect = pygame.Rect(meteor1.get_rect())
    rect.left = random.randint(0, screen_width)     # 운석 x좌표
    rect.top = -100     # 운석 y좌표(화면 위)
    meteor_type = random.randint(1, 3)     # 종류 : 1,2,3 랜덤
    dy = random.randint(10, 20)     # 속도 : 10부터 20 중에 랜덤
    meteors.append({'type': meteor_type, 'rect': rect, 'dy': dy})      # dictionary를 이용하여 추가

# 이벤트 시작
running = True
while running:
    dt = clock.tick(20)
    for event in pygame.event.get():     # 이벤트 발생 판단
        if event.type == pygame.QUIT:   # 종료 조건
            running = False
            break
        elif event.type == pygame.KEYDOWN:  # 키보드 입력 시
            if event.key == pygame.K_LEFT:  # 왼쪽 입력 시
                toX = -characterSpeed
            elif event.key == pygame.K_RIGHT:   # 오른쪽 입력 시
                toX = characterSpeed
        elif event.type == pygame.KEYUP:    # 키보드 입력 없을 시 toX 초기화
            if event.key == pygame.K_LEFT:
                toX = 0
            elif event.key == pygame.K_RIGHT:
                toX = 0
    # 캐릭터 이동
    character_x_pos += toX * dt

    # 경계 설정
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 충돌 설정(캐릭터)
    characterRect = character.get_rect()
    characterRect.left = character_x_pos
    characterRect.top = character_y_pos

    # 충돌 설정(운석)
    randomNumber = random.randrange(1, 200)
    randomNumber2 = random.randrange(1, 440)
    for meteor in meteors:
        meteor['rect'].top += meteor['dy']  # 속도 조절
        if meteor['rect'].top > screen_height:    # 운석이 사라지면
            meteors.remove(meteor)
            rect = pygame.Rect(meteor1.get_rect())
            rect.left = random.randint(0, screen_width)
            rect.top = -100
            meteor_type = random.randint(1, 3)
            dy = random.randint(10, 20)
            meteors.append({'type': meteor_type, 'rect': rect, 'dy': dy})    # 새 운석 추가

    screen.blit(background, (0, 0))  # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭 그리기

    for meteor in meteors:
        if meteor['rect'].colliderect(characterRect):   # 충돌 시 종료
            running = False
        # 운석 그리기
        if meteor['type'] == 1:
            screen.blit(meteor1, meteor['rect'])
        elif meteor['type'] == 2:
            screen.blit(meteor2, meteor['rect'])
        else:
            screen.blit(meteor3, meteor['rect'])
    pygame.display.update()

# 종료
pygame.quit()
