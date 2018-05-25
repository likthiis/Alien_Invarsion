# coding=gbk
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # ��ʼ����Ϸ������һ����Ļ����
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # ����Play��ť
    play_button = Button(ai_settings, screen, "Play")

    # ����һ�����ڴ洢��Ϸͳ����Ϣ��ʵ�����������Ƿ���
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # ����һ�ҷɴ���һ���ӵ������һ�������˱���
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # ����������Ⱥ
    gf.create_fleet(ai_settings,screen,ship,aliens)

    # ��ʼ��Ϸ����ѭ��
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
            play_button)


run_game()
