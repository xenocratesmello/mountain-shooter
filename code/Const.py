# C
import pygame

COLOR_ORANGE = (255, 165, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_YELLOW = (255, 255, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_GREEN = (0, 255, 0)
COLOR_CYAN = (0, 255, 255)

# E
ENTITY_DAMAGE = {
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level1Bg7': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level2Bg5': 0,
    'Player1': 1,
    'Player2': 1,
    'Enemy1': 1,
    'Enemy2': 1,
    'Player1Shot': 25,
    'Player2Shot': 25,
    'Enemy1Shot': 20,
    'Enemy2Shot': 15}

ENTITY_HEALTH = {
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level1Bg7': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Level2Bg5': 999,
    'Player1': 300,
    'Player2': 300,
    'Enemy1': 50,
    'Enemy2': 60,
    'Player1Shot': 1,
    'Player2Shot': 1,
    'Enemy1Shot': 1,
    'Enemy2Shot': 1}

ENTITY_SCORE = {
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level1Bg7': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level2Bg5': 0,
    'Player1': 0,
    'Player2': 0,
    'Enemy1': 100,
    'Enemy2': 125,
    'Player1Shot': 0,
    'Player2Shot': 0,
    'Enemy1Shot': 0,
    'Enemy2Shot': 0}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 20,
    'Enemy1': 100,
    'Enemy2': 80}

EVENT_ENEMY = pygame.USEREVENT + 1

EVENT_TIMEOUT = pygame.USEREVENT + 2

# F
FILEPATH = {
    'Level1Bg1': 'craftpix/m2/1',
    'Level1Bg2': 'craftpix/m2/2',
    'Level1Bg3': 'craftpix/m2/3',
    'Level1Bg4': 'craftpix/m2/4',
    'Level1Bg5': 'craftpix/m2/5',
    'Level1Bg6': 'craftpix/m2/6',
    'Level1Bg7': 'craftpix/m2/7',
    'Level2Bg1': 'craftpix/m3/1',
    'Level2Bg2': 'craftpix/m3/2',
    'Level2Bg3': 'craftpix/m3/3',
    'Level2Bg4': 'craftpix/m3/4',
    'Level2Bg5': 'craftpix/m3/5',
    'Player1': 'craftpix/ships/Ship1',
    'Player2': 'craftpix/ships/Ship2',
    'Enemy1': 'craftpix/ships/Ship3',
    'Enemy2': 'craftpix/ships/Ship4',
    'Player1Shot': 'craftpix/shots/shot1_asset',
    'Player2Shot': 'craftpix/shots/shot2_asset',
    'Enemy1Shot': 'craftpix/shots/shot3_asset',
    'Enemy2Shot': 'craftpix/shots/shot4_asset'}
# M
MENU_OPTION = (
    'NEW GAME 1P',
    'NEW GAME 2P - COOPERATIVE',
    'NEW GAME 2P - COMPETITIVE',
    'SCORE',
    'EXIT')

MUSIC_FILE = {
    'Level1': './asset/pixabay/tudo_free-16-bits-music-294095.mp3',
    'Level2': './asset/pixabay/tudo_free-16-bits-musica-294099.mp3'}

# P
PLAYER_KEY_UP = {
    'Player1': pygame.K_UP,
    'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {
    'Player1': pygame.K_DOWN,
    'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {
    'Player1': pygame.K_LEFT,
    'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {
    'Player1': pygame.K_RIGHT,
    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {
    'Player1': pygame.K_RCTRL,
    'Player2': pygame.K_LCTRL}
# S
SPEED = {
    'Level1Bg1': 0,
    'Level1Bg2': 1,
    'Level1Bg3': 2,
    'Level1Bg4': 3,
    'Level1Bg5': 4,
    'Level1Bg6': 5,
    'Level1Bg7': 6,
    'Level2Bg1': 0,
    'Level2Bg2': 1,
    'Level2Bg3': 2,
    'Level2Bg4': 3,
    'Level2Bg5': 4,
    'Player1': 3,
    'Player2': 3,
    'Enemy1': 2,
    'Enemy2': 1,
    "Player1Shot": 5,
    'Player2Shot': 5,
    'Enemy1Shot': 5,
    'Enemy2Shot': 3}

SPAWN_TIME = 3000

# T
TIMEOUT_STEP = 100 # 100ms
TIMEOUT_LEVEL = 20000 # 20s

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
