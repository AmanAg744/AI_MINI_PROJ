import pygame
from sys import exit
import configuration
import population

pygame.init()
clock = pygame.time.Clock()
population = population.Population(100)

def generate_pipes():
    configuration.pipes.append(configuration.Pipes(configuration.win_width))

def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def main():
    pipes_spawn_time = 10

    while True:
        quit_game()

        configuration.window.fill((0, 0, 0))

        configuration.ground.draw(configuration.window)

        
        if pipes_spawn_time <= 0:
            generate_pipes()
            pipes_spawn_time = 200
        pipes_spawn_time -= 1

        for p in configuration.pipes:
            p.draw(configuration.window)
            p.update()
            if p.off_screen:
                configuration.pipes.remove(p)

        if not population.extinct():
            population.update_live_players()
        else:
            configuration.pipes.clear()
            population.natural_selection()

        clock.tick(60)
        pygame.display.flip()

main()