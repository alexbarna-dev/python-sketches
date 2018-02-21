import os

FPS = 60.0
CAPTION = "Space Shooter"
WINDOW_SIZE = WIDTH, HEIGHT = 800, 600
FONT_COLOR = (0, 255, 0)
RESOURCES = os.path.dirname(__file__) + os.sep + "resources" + os.sep
SHIP_RESOURCES = RESOURCES + "ships" + os.sep
BEAM_RESOURCES = RESOURCES + "beams" + os.sep
EXPLOSION_RESOURCES = RESOURCES + "explosion" + os.sep
SOUND_RESOURCES = RESOURCES + "sound" + os.sep
SHIP_SIZE = 20, 30
BULLET_SIZE = 10, 15
EXPLOSION_SIZE = 50, 50
PLAYER_DEFAULT_POSITION = WIDTH / 2 - SHIP_SIZE[0] / 2, HEIGHT - SHIP_SIZE[1] - 20
PLAYER_DEFAULT_SPEED = 4, 0
ENEMY_DEFAULT_SPEED = 1, 0
PLAYER_BULLET_SPEED = 0, -5
ENEMY_BULLET_SPEED = 0, 5
