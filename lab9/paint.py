import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    circle_color = 'red'
    square_color = 'red'
    rhombus_color = 'red'
    rectangle_color = 'red'
    equilateral_triangle_color = 'red'
    right_triangle_color = 'red'
    mode = 'circle'
    points = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    circle_color = 'red'
                    square_color = 'red'
                    rhombus_color = 'red'
                    rectangle_color = 'red'
                    equilateral_triangle_color = 'red'
                    right_triangle_color = 'red'
                elif event.key == pygame.K_g:
                  circle_color = 'green'
                  square_color = 'green'
                  rhombus_color = 'green'
                  rectangle_color = 'green'
                  equilateral_triangle_color = 'green'
                  right_triangle_color = 'green'
                elif event.key == pygame.K_b:
                  circle_color = 'blue'
                  square_color = 'blue'
                  rhombus_color = 'blue'
                  rectangle_color = 'blue'
                  equilateral_triangle_color = 'blue'
                  right_triangle_color = 'blue'
                elif event.key == pygame.K_y:
                  circle_color = 'yellow'
                  square_color = 'yellow'
                  rhombus_color = 'yellow'
                  rectangle_color = 'yellow'
                  equilateral_triangle_color = 'yellow'
                  right_triangle_color = 'yellow'
                elif event.key == pygame.K_d:
                    points = []
                elif event.key == pygame.K_s:
                    mode = 'square'
                elif event.key == pygame.K_r:
                    mode = 'rectangle'
                elif event.key == pygame.K_t:
                    mode = 'right_triangle'
                elif event.key == pygame.K_e:
                    mode = 'equilateral_triangle'
                elif event.key == pygame.K_h:
                    mode = 'rhombus'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    position = event.pos
                    if mode == 'circle':
                        points.append((position, 'circle', circle_color))
                    elif mode == 'rectangle':
                        points.append((position, 'rectangle', square_color))
                    elif mode == 'square':
                        points.append((position, 'square', square_color))
                    elif mode == 'right_triangle':
                        points.append((position, 'right_triangle', square_color))
                    elif mode == 'equilateral_triangle':
                        points.append((position, 'equilateral_triangle', square_color))
                    elif mode == 'rhombus':
                        points.append((position, 'rhombus', square_color))

                elif event.button == 3:  # Right click
                    if mode == 'circle':
                        mode = 'rectangle'
                    elif mode == 'rectangle':
                        mode = 'square'
                    elif mode == 'square':
                        mode = 'right_triangle'
                    elif mode == 'right_triangle':
                        mode = 'equilateral_triangle'
                    elif mode == 'equilateral_triangle':
                        mode = 'rhombus'
                    elif mode == 'rhombus':
                        mode = 'circle'

        screen.fill((0, 0, 0))

        for point, drawing_mode, color in points:
            if drawing_mode == 'circle':
                pygame.draw.circle(screen, getColor(color), point, radius)
            elif drawing_mode == 'rectangle':
                pygame.draw.rect(screen, getColor(color), pygame.Rect(point[0] - radius, point[1] - radius, 2 * radius, 2 * radius))
            elif drawing_mode == 'square':
                pygame.draw.rect(screen, getColor(color), pygame.Rect(point[0] - radius, point[1] - radius, 2 * radius, 2 * radius))
            elif drawing_mode == 'right_triangle':
                pygame.draw.polygon(screen, getColor(color), [(point[0], point[1]), (point[0] + radius, point[1]), (point[0], point[1] + radius)])
            elif drawing_mode == 'equilateral_triangle':
                x1, y1 = point[0], point[1]
                x2, y2 = point[0] + radius, point[1]
                x3, y3 = point[0] + radius / 2, point[1] + math.sqrt(3) * radius / 2
                pygame.draw.polygon(screen, getColor(color), [(x1, y1), (x2, y2), (x3, y3)])
            elif drawing_mode == 'rhombus':
                pygame.draw.polygon(screen, getColor(color), [(point[0], point[1] - radius), (point[0] + radius, point[1]), (point[0], point[1] + radius), (point[0] - radius, point[1])])

        pygame.display.flip()
        clock.tick(60)

def getColor(color_mode):
    if color_mode == 'blue':
        return (0, 0, 255)
    elif color_mode == 'red':
        return (255, 0, 0)
    elif color_mode == 'green':
        return (0, 255, 0)
    elif color_mode == 'yellow':
        return (255, 255, 0)

main()
