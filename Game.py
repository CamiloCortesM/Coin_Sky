from modules import *
import os
import pygame
import cfg
import sys
import random


def initGame():
    pygame.init()
    screen = pygame.display.set_mode(cfg.SCREENSIZE)
    pygame.display.set_caption("catch coins")
    
    game_images={}
    
    for key, value in cfg.IMAGE_PATHS.items():
        if isinstance(value, list):
            images = []
            for item in value: images.append(pygame.image.load(item))
            game_images[key] = images
        else:
            game_images[key] = pygame.image.load(value)
    game_sounds ={} 
    for key, value in cfg.AUDIO_PATHS.items():
        if key == 'bgm': continue
        game_sounds[key]= pygame.mixer.Sound(value)
    
    return screen, game_images, game_sounds


def main():
    screen, game_images, game_sounds = initGame()
    
    pygame.mixer.music.load(cfg.AUDIO_PATHS['bgm'])
    pygame.mixer.music.play(-1, 0.0)
    
    font = pygame.font.Font(cfg.FONT_PATH, 40)
    
    hero = Hero(game_images['hero'], position=(375,520))
    
    food_sprites_group = pygame.sprite.Group()
    generate_food_freq = random.randint(10,20)
    generate_font_count = 0
    
    score = 0
    highest_score = 0 if not os.path.exists(cfg.HIGHEST_SCORE_RECORD_FILEPATH) else int(open(cfg.HIGHEST_SCORE_RECORD_FILEPATH).read())
    clock = pygame.time.Clock()


if __name__ == "__main__":
    initGame()