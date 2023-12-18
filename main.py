import pygame, sys
from game import Game
from colors import Color

pygame.init()

#Text font
title_font = pygame.font.Font(None, 30)
title_level = pygame.font.Font(None, 60)

#Text
next_piece = title_font.render("Next:", True, Color.white)
stored_piece = title_font.render("Stored:", True, Color.white)



pieces_rect = pygame.Rect(510, 50, 180, 550)
piece_stored_rect = pygame.Rect(20, 480, 150, 160)

screen = pygame.display.set_mode((700,650))
pygame.display.set_caption("Tetris")
screen.blit(stored_piece, (20, 450, 20, 50))
screen.blit(next_piece, (580, 20, 20, 50))
pygame.draw.rect(screen, Color.dark_blue ,pieces_rect, 2, 10)
pygame.draw.rect(screen, Color.dark_blue ,piece_stored_rect, 2, 10)

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
intervalo_tiempo = 0
pygame.mixer.music.load("Sounds/music.mp3")
pygame.mixer.music.play(-1)

while True:
    for event in pygame.event.get():
        intervalo_tiempo = int(((0.8 - ((game.level - 1) * 0.007))**(game.level-1))*1000)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game.game_over == True:
                pygame.mixer.music.stop()
                game_over_text = title_level.render(f"Game \n Over", True, Color.white)
                screen.blit(game_over_text, (30, 280, 20, 50))
                game.save_score_record()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    level_rect = pygame.Rect(30, 280, 120, 95)
                    pygame.draw.rect(screen, Color.black ,level_rect)
                    pygame.draw.rect(screen, Color.black ,pieces_rect)
                    pygame.draw.rect(screen, Color.black ,piece_stored_rect)
                    pygame.draw.rect(screen, Color.dark_blue ,pieces_rect, 2, 10)
                    pygame.draw.rect(screen, Color.dark_blue ,piece_stored_rect, 2, 10)
                    game.game_over = False
                    game.reset()
                    pygame.mixer.music.play(-1)
        
        if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_c or event.key == pygame.K_LSHIFT: 
                    game.set_retained_piece(screen)
                if event.key == pygame.K_LEFT and game.game_over == False:
                    game.move_left()
                    game.move_left_ghost()
                if event.key == pygame.K_RIGHT and game.game_over == False:
                    game.move_right()
                    game.move_right_ghost()
                if event.key == pygame.K_DOWN and game.game_over == False:
                    game.move_down()
                if event.key == pygame.K_UP and game.game_over == False:
                    game.hourly_rotation()
                    game.hourly_rotation_ghost()
                if (event.key == pygame.K_z or event.key == pygame.K_LCTRL) and game.game_over == False:
                    game.antihourly_rotation()
                    game.antihourly_rotation_ghost()
                if event.key == pygame.K_SPACE and game.game_over == False:
                    game.move_hard_drop()
        
        pygame.time.set_timer(GAME_UPDATE, intervalo_tiempo)
        #intervalo_tiempo-=10

        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()

    #Drawing window
    score_surface = title_font.render(f"Score: \n{game.score}", True, Color.white)
    level_text = title_level.render(f"Level: \n    {game.level}", True, Color.white)
    line_text = title_font.render(f"Lines: {game.line_completed}", True, Color.white)
    score_record_text = title_font.render(f"Score Record: \n{game.score_record}", True, Color.white)
    level_rect = pygame.Rect(20, 20, 120, 95)
    pygame.draw.rect(screen, Color.black ,level_rect)
    score_rect = pygame.Rect(20, 120, 130, 95)
    pygame.draw.rect(screen, Color.black ,score_rect)
    record = pygame.Rect(20, 180, 120, 95)
    pygame.draw.rect(screen, Color.black ,record)
    screen.blit(level_text, (20, 20, 20, 50))
    screen.blit(score_surface, (20, 120, 20, 50))
    screen.blit(score_record_text, (20, 200, 20, 50))
    screen.blit(line_text, (20, 170, 20, 50))
    game.draw(screen)
    pygame.display.update()
    clock.tick(60)

