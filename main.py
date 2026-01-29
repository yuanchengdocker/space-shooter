#!/usr/bin/env python3
"""
🚀 Space Shooter - 太空射击游戏
一个功能完整的打飞机游戏
"""

import pygame
import random
import sys
import os
from enum import Enum
import math

# 初始化 Pygame
pygame.init()
pygame.mixer.init()

# 游戏常量
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (10, 10, 30)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
BLUE = (50, 150, 255)
YELLOW = (255, 255, 50)
PURPLE = (200, 50, 255)
ORANGE = (255, 150, 50)

# 游戏状态
class GameState(Enum):
    MENU = 1
    PLAYING = 2
    PAUSED = 3
    GAME_OVER = 4

class Player(pygame.sprite.Sprite):
    """玩家飞船类"""
    def __init__(self):
        super().__init__()
        self.width = 50
        self.height = 40
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.draw_ship()
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 20
        self.speed_x = 0
        self.speed = 6
        self.health = 100
        self.max_health = 100
        self.score = 0
        self.level = 1
        self.power_level = 1
        self.last_shot = pygame.time.get_ticks()
        self.shoot_delay = 250
        self.invincible = False
        self.invincible_timer = 0
        self.invincible_duration = 2000

    def draw_ship(self):
        """绘制玩家飞船"""
        # 主体
        pygame.draw.polygon(self.image, BLUE, [
            (25, 0),
            (0, 40),
            (50, 40)
        ])
        # 驾驶舱
        pygame.draw.ellipse(self.image, (100, 200, 255), (15, 10, 20, 15))
        # 引擎火焰
        pygame.draw.polygon(self.image, ORANGE, [
            (10, 40),
            (25, 55),
            (40, 40)
        ])
        # 装饰线
        pygame.draw.line(self.image, WHITE, (25, 0), (25, 40), 2)

    def update(self):
        """更新玩家状态"""
        # 移动
        self.rect.x += self.speed_x
        
        # 边界检查
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        
        # 无敌时间
        if self.invincible:
            current_time = pygame.time.get_ticks()
            if current_time - self.invincible_timer > self.invincible_duration:
                self.invincible = False

    def move_left(self):
        """向左移动"""
        self.speed_x = -self.speed

    def move_right(self):
        """向右移动"""
        self.speed_x = self.speed

    def stop_move(self):
        """停止移动"""
        self.speed_x = 0

    def shoot(self):
        """发射子弹"""
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot > self.shoot_delay:
            self.last_shot = current_time
            bullets = []
            
            if self.power_level == 1:
                bullets.append(Bullet(self.rect.centerx, self.rect.top))
            elif self.power_level == 2:
                bullets.append(Bullet(self.rect.left, self.rect.top))
                bullets.append(Bullet(self.rect.right, self.rect.top))
            else:
                bullets.append(Bullet(self.rect.centerx, self.rect.top))
                bullets.append(Bullet(self.rect.left, self.rect.centery))
                bullets.append(Bullet(self.rect.right, self.rect.centery))
            
            return bullets
        return []

    def power_up(self):
        """升级武器"""
        self.power_level = min(self.power_level + 1, 3)

    def take_damage(self, damage):
        """受到伤害"""
        if not self.invincible:
            self.health -= damage
            self.invincible = True
            self.invincible_timer = pygame.time.get_ticks()
            if self.health <= 0:
                return True
        return False

class Enemy(pygame.sprite.Sprite):
    """敌机类"""
    def __init__(self, difficulty=1):
        super().__init__()
        self.type = random.choice(['basic', 'fast', 'tank'])
        
        if self.type == 'basic':
            self.width = 40
            self.height = 35
            self.speed = random.uniform(2, 3)
            self.health = 1
            self.score = 10
            color = RED
        elif self.type == 'fast':
            self.width = 35
            self.height = 30
            self.speed = random.uniform(4, 6)
            self.health = 1
            self.score = 15
            color = PURPLE
        else:  # tank
            self.width = 50
            self.height = 45
            self.speed = random.uniform(1, 2)
            self.health = 3
            self.score = 25
            color = ORANGE
        
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.draw_enemy(color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.width)
        self.rect.y = random.randint(-100, -40)
        self.difficulty = difficulty

    def draw_enemy(self, color):
        """绘制敌机"""
        if self.type == 'basic':
            pygame.draw.polygon(self.image, color, [
                (self.width//2, self.height),
                (0, 0),
                (self.width, 0)
            ])
            pygame.draw.circle(self.image, (255, 200, 200), 
                            (self.width//2, self.height//3), 5)
        elif self.type == 'fast':
            pygame.draw.polygon(self.image, color, [
                (self.width//2, self.height),
                (0, 5),
                (self.width, 5)
            ])
            pygame.draw.line(self.image, WHITE, (0, 5), (self.width, 5), 2)
        else:  # tank
            pygame.draw.rect(self.image, color, (0, 0, self.width, self.height))
            pygame.draw.rect(self.image, (color[0]+30, color[1]+30, color[2]+30), 
                           (5, 5, self.width-10, self.height-10))
            pygame.draw.circle(self.image, BLACK, 
                             (self.width//2, self.height//2), 8)

    def update(self):
        """更新敌机位置"""
        self.rect.y += self.speed * (1 + self.difficulty * 0.1)
        
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

    def hit(self):
        """被击中"""
        self.health -= 1
        return self.health <= 0

class Bullet(pygame.sprite.Sprite):
    """子弹类"""
    def __init__(self, x, y, is_enemy=False):
        super().__init__()
        self.width = 4
        self.height = 15
        self.is_enemy = is_enemy
        
        if is_enemy:
            color = RED
            self.speed = 5
        else:
            color = YELLOW
            self.speed = -10
        
        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.ellipse(self.image, color, (0, 0, self.width, self.height))
        pygame.draw.ellipse(self.image, WHITE, (1, 1, self.width-2, self.height-2))
        
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y if not is_enemy else y

    def update(self):
        """更新子弹位置"""
        self.rect.y += self.speed
        
        if self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT:
            self.kill()

class PowerUp(pygame.sprite.Sprite):
    """道具类"""
    def __init__(self, x, y):
        super().__init__()
        self.type = random.choice(['health', 'power', 'score'])
        self.size = 25
        
        if self.type == 'health':
            self.color = GREEN
            self.symbol = '+'
        elif self.type == 'power':
            self.color = PURPLE
            self.symbol = 'P'
        else:
            self.color = YELLOW
            self.symbol = '$'
        
        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.size//2, self.size//2), self.size//2)
        pygame.draw.circle(self.image, WHITE, (self.size//2, self.size//2), self.size//2-3)
        
        font = pygame.font.Font(None, 20)
        text = font.render(self.symbol, True, self.color)
        text_rect = text.get_rect(center=(self.size//2, self.size//2))
        self.image.blit(text, text_rect)
        
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = 2

    def update(self):
        """更新道具位置"""
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

class Star:
    """背景星星类"""
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.speed = random.uniform(0.5, 2)
        self.size = random.randint(1, 2)
        self.brightness = random.randint(100, 255)

    def update(self):
        """更新星星位置"""
        self.y += self.speed
        if self.y > SCREEN_HEIGHT:
            self.y = 0
            self.x = random.randint(0, SCREEN_WIDTH)

    def draw(self, surface):
        """绘制星星"""
        color = (self.brightness, self.brightness, self.brightness)
        pygame.draw.circle(surface, color, (int(self.x), int(self.y)), self.size)

class Explosion(pygame.sprite.Sprite):
    """爆炸效果类"""
    def __init__(self, x, y, size=50):
        super().__init__()
        self.size = size
        self.max_size = size
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.frame = 0
        self.max_frames = 20

    def update(self):
        """更新爆炸动画"""
        self.frame += 1
        if self.frame >= self.max_frames:
            self.kill()
        else:
            progress = self.frame / self.max_frames
            alpha = int(255 * (1 - progress))
            current_size = int(self.max_size * (1 + progress * 0.5))
            
            self.image = pygame.Surface((current_size, current_size), pygame.SRCALPHA)
            colors = [ORANGE, YELLOW, RED]
            color = colors[self.frame % len(colors)]
            
            pygame.draw.circle(self.image, (*color, alpha), 
                             (current_size//2, current_size//2), 
                             int(current_size//2 * (1 - progress * 0.3)))
            
            self.rect = self.image.get_rect()
            self.rect.centerx = self.rect.centerx
            self.rect.centery = self.rect.centery

class Game:
    """游戏主类"""
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("🚀 Space Shooter - 太空射击游戏")
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = GameState.MENU
        
        # 字体
        self.font_title = pygame.font.Font(None, 72)
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 24)
        
        # 游戏对象
        self.player = None
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.power_ups = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.stars = [Star() for _ in range(100)]
        
        # 游戏数据
        self.score = 0
        self.high_score = 0
        self.level = 1
        self.difficulty = 1
        
        # 敌机生成
        self.enemy_spawn_timer = 0
        self.enemy_spawn_delay = 60
        
        # 加载高分
        self.load_high_score()

    def load_high_score(self):
        """加载高分记录"""
        try:
            if os.path.exists('highscore.txt'):
                with open('highscore.txt', 'r') as f:
                    self.high_score = int(f.read())
        except:
            self.high_score = 0

    def save_high_score(self):
        """保存高分记录"""
        try:
            with open('highscore.txt', 'w') as f:
                f.write(str(self.high_score))
        except:
            pass

    def reset_game(self):
        """重置游戏"""
        self.player = Player()
        self.enemies.empty()
        self.bullets.empty()
        self.enemy_bullets.empty()
        self.power_ups.empty()
        self.explosions.empty()
        self.score = 0
        self.level = 1
        self.difficulty = 1
        self.enemy_spawn_delay = 60

    def handle_events(self):
        """处理事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                if self.state == GameState.MENU:
                    if event.key == pygame.K_SPACE:
                        self.reset_game()
                        self.state = GameState.PLAYING
                    elif event.key == pygame.K_q:
                        self.running = False
                
                elif self.state == GameState.PLAYING:
                    if event.key == pygame.K_SPACE:
                        new_bullets = self.player.shoot()
                        self.bullets.add(new_bullets)
                    elif event.key == pygame.K_p:
                        self.state = GameState.PAUSED
                    elif event.key == pygame.K_ESCAPE:
                        self.state = GameState.MENU
                
                elif self.state == GameState.PAUSED:
                    if event.key == pygame.K_p:
                        self.state = GameState.PLAYING
                    elif event.key == pygame.K_ESCAPE:
                        self.state = GameState.MENU
                
                elif self.state == GameState.GAME_OVER:
                    if event.key == pygame.K_SPACE:
                        self.reset_game()
                        self.state = GameState.PLAYING
                    elif event.key == pygame.K_ESCAPE:
                        self.state = GameState.MENU

        # 持续按键处理
        if self.state == GameState.PLAYING:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.player.move_left()
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.player.move_right()
            else:
                self.player.stop_move()

    def update(self):
        """更新游戏状态"""
        if self.state == GameState.PLAYING:
            # 更新星星
            for star in self.stars:
                star.update()
            
            # 更新玩家
            self.player.update()
            
            # 更新子弹
            self.bullets.update()
            self.enemy_bullets.update()
            
            # 更新敌机
            self.enemies.update()
            
            # 更新道具
            self.power_ups.update()
            
            # 更新爆炸效果
            self.explosions.update()
            
            # 生成敌机
            self.enemy_spawn_timer += 1
            if self.enemy_spawn_timer >= self.enemy_spawn_delay:
                self.enemy_spawn_timer = 0
                enemy = Enemy(self.difficulty)
                self.enemies.add(enemy)
            
            # 碰撞检测：子弹与敌机
            hits = pygame.sprite.groupcollide(self.enemies, self.bullets, False, True)
            for enemy, bullets in hits.items():
                for bullet in bullets:
                    if enemy.hit():
                        explosion = Explosion(enemy.rect.centerx, enemy.rect.centery)
                        self.explosions.add(explosion)
                        self.score += enemy.score
                        enemy.kill()
                        
                        # 随机掉落道具
                        if random.random() < 0.15:
                            power_up = PowerUp(enemy.rect.centerx, enemy.rect.centery)
                            self.power_ups.add(power_up)
            
            # 碰撞检测：玩家与敌机
            hits = pygame.sprite.spritecollide(self.player, self.enemies, True)
            for hit in hits:
                if self.player.take_damage(20):
                    self.game_over()
                explosion = Explosion(hit.rect.centerx, hit.rect.centery, 60)
                self.explosions.add(explosion)
            
            # 碰撞检测：玩家与道具
            hits = pygame.sprite.spritecollide(self.player, self.power_ups, True)
            for hit in hits:
                if hit.type == 'health':
                    self.player.health = min(self.player.health + 20, self.player.max_health)
                elif hit.type == 'power':
                    self.player.power_up()
                elif hit.type == 'score':
                    self.score += 50
            
            # 更新难度
            if self.score > self.level * 500:
                self.level += 1
                self.difficulty = 1 + (self.level - 1) * 0.2
                self.enemy_spawn_delay = max(20, 60 - self.level * 5)

    def game_over(self):
        """游戏结束"""
        self.state = GameState.GAME_OVER
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()

    def draw_text(self, text, font, color, x, y, align='center'):
        """绘制文本"""
        surface = font.render(text, True, color)
        rect = surface.get_rect()
        if align == 'center':
            rect.centerx = x
            rect.centery = y
        elif align == 'left':
            rect.x = x
            rect.y = y
        elif align == 'right':
            rect.right = x
            rect.y = y
        self.screen.blit(surface, rect)

    def draw_health_bar(self, x, y, health, max_health):
        """绘制血条"""
        bar_width = 150
        bar_height = 15
        
        # 背景
        pygame.draw.rect(self.screen, (50, 50, 50), (x, y, bar_width, bar_height))
        
        # 血量
        health_width = int(bar_width * (health / max_health))
        color = GREEN if health > 50 else (YELLOW if health > 25 else RED)
        pygame.draw.rect(self.screen, color, (x, y, health_width, bar_height))
        
        # 边框
        pygame.draw.rect(self.screen, WHITE, (x, y, bar_width, bar_height), 2)

    def draw_menu(self):
        """绘制菜单"""
        # 绘制星星背景
        for star in self.stars:
            star.draw(self.screen)
        
        # 标题
        self.draw_text("🚀 SPACE SHOOTER", self.font_title, WHITE, 
                      SCREEN_WIDTH//2, SCREEN_HEIGHT//3)
        
        self.draw_text("太空射击游戏", self.font_large, YELLOW, 
                      SCREEN_WIDTH//2, SCREEN_HEIGHT//3 + 70)
        
        # 选项
        self.draw_text("按 [SPACE] 开始游戏", self.font_medium, GREEN, 
                      SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 50)
        
        self.draw_text("按 [Q] 退出", self.font_medium, RED, 
                      SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 100)
        
        # 说明
        instructions = [
            "操作说明:",
            "← → 或 A D 移动",
            "SPACE 射击",
            "P 暂停游戏"
        ]
        
        for i, text in enumerate(instructions):
            self.draw_text(text, self.font_small, WHITE, 
                          SCREEN_WIDTH//2, SCREEN_HEIGHT - 150 + i * 30)
        
        # 高分
        self.draw_text(f"最高分: {self.high_score}", self.font_medium, PURPLE, 
                      SCREEN_WIDTH//2, SCREEN_HEIGHT - 50)

    def draw_game(self):
        """绘制游戏画面"""
        # 绘制星星背景
        for star in self.stars:
            star.draw(self.screen)
        
        # 绘制游戏对象
        self.power_ups.draw(self.screen)
        self.enemies.draw(self.screen)
        self.bullets.draw(self.screen)
        self.enemy_bullets.draw(self.screen)
        
        # 绘制玩家（无敌时闪烁）
        if not self.player.invincible or pygame.time.get_ticks() % 200 < 100:
            self.screen.blit(self.player.image, self.player.rect)
        
        self.explosions.draw(self.screen)
        
        # 绘制UI
        self.draw_health_bar(20, 20, self.player.health, self.player.max_health)
        self.draw_text(f"分数: {self.score}", self.font_medium, WHITE, 20, 45, 'left')
        self.draw_text(f"等级: {self.level}", self.font_medium, WHITE, 20, 80, 'left')
        self.draw_text(f"武器: {self.player.power_level}", self.font_small, PURPLE, 
                      20, 115, 'left')

    def draw_paused(self):
        """绘制暂停画面"""
        # 绘制游戏画面（半透明）
        self.draw_game()
        
        # 半透明遮罩
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))
        self.screen.blit(overlay, (0, 0))
        
        # 暂停文本
        self.draw_text("游戏暂停", self.font_title, YELLOW, 
                      SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 50)
        
        self.draw_text("按 [P] 继续游戏", self.font_large, GREEN, 
                      SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 30)
        
        self.draw_text("按 [ESC] 返回菜单", self.font_medium, WHITE, 
                      SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 90)

    def draw_game_over(self):
        """绘制游戏结束画面"""
        # 绘制星星背景
        for star in self.stars:
            star.draw(self.screen)
        
        # 游戏结束文本
        self.draw_text("游戏结束", self.font_title, RED, 
                      SCREEN_WIDTH//2, SCREEN_HEIGHT//3)
        
        self.draw_text(f"最终分数: {self.score}", self.font_large, WHITE, 
                      SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 30)
        
        self.draw_text(f"达到等级: {self.level}", self.font_medium, YELLOW, 
                      SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 20)
        
        if self.score >= self.high_score:
            self.draw_text("🎉 新纪录！🎉", self.font_large, GREEN, 
                          SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 70)
        
        self.draw_text("按 [SPACE] 重新开始", self.font_medium, GREEN, 
                      SCREEN_WIDTH//2, SCREEN_HEIGHT - 100)
        
        self.draw_text("按 [ESC] 返回菜单", self.font_medium, WHITE, 
                      SCREEN_WIDTH//2, SCREEN_HEIGHT - 50)

    def draw(self):
        """绘制画面"""
        if self.state == GameState.MENU:
            self.draw_menu()
        elif self.state == GameState.PLAYING:
            self.draw_game()
        elif self.state == GameState.PAUSED:
            self.draw_paused()
        elif self.state == GameState.GAME_OVER:
            self.draw_game_over()

    def run(self):
        """运行游戏"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            
            pygame.display.flip()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
