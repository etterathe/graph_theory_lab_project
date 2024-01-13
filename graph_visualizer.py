import math
import pygame


class GraphVisualizer:
    def __init__(self, nodes_set, edges_set, value_of_x_max=50, value_of_y_max=50, scale=15):
        self.nodes_set = nodes_set
        self.edges_set = edges_set
        self.value_of_x_max = value_of_x_max
        self.value_of_y_max = value_of_y_max
        self.scale = scale

    def visualize_graph(self):
        pygame.init()
        max_x, max_y = self.value_of_x_max, self.value_of_y_max
        graph_scale = self.scale
        node_name_font_size = 30
        node_name_offset = 30
        axe_name_font_size = 25
        node_icon_size = 5
        color_node_name = (200, 200, 200)
        color_node_icon = (70, 220, 70)
        color_line = (180, 30, 30)
        color_axe_name = (250, 250, 250)

        font_nodes = pygame.font.SysFont('comicsans', node_name_font_size)
        font_axes = pygame.font.SysFont('comicsans', axe_name_font_size)

        surface_size = (max_x * graph_scale + 100, max_y * graph_scale + 100)

        class Node:
            def __init__(self, x, y, name):
                self.x = x
                self.y = y
                self.name = name
                self.size = node_icon_size

            def draw(self, surface):
                yOffsetConst = (self.size * 2) * math.cos(math.radians(30))
                triangleCenter = [(self.x - self.size, self.y + yOffsetConst/3),
                                  (self.x, self.y - yOffsetConst*2/3),
                                  (self.x + self.size, self.y + yOffsetConst/3)]
                pygame.draw.polygon(surface, color_node_icon, triangleCenter, 1)
                text1 = font_nodes.render(str(self.name), 1, color_node_name)
                surface.blit(text1, (self.x, self.y - node_name_offset))

        class Edge:
            def __init__(self, x1, y1, x2, y2):
                self.x1 = x1
                self.y1 = y1
                self.x2 = x2
                self.y2 = y2
                self.thickness = 1

            def draw(self, surface):
                pygame.draw.line(surface, color_line, (self.x1, self.y1), (self.x2, self.y2), 1)

        CLOCK = pygame.time.Clock()
        FPS = 60
        pygame.display.set_caption('Graph generator')

        surface_main = pygame.display.set_mode(surface_size)
        list_of_nodes = []

        for n in self.nodes_set:
            x = 50 + graph_scale * self.nodes_set[n][0]
            y = surface_size[1] - (50 + graph_scale * self.nodes_set[n][1])
            list_of_nodes.append(Node(x, y, n))

        list_of_edges = []

        for e in self.edges_set:
            x1 = 50 + graph_scale * self.nodes_set[e][0]
            y1 = surface_size[1] - (50 + graph_scale * self.nodes_set[e][1])
            edge_value = self.edges_set[e]
            for v in edge_value:
                x2 = 50 + graph_scale * self.nodes_set[v][0]
                y2 = surface_size[1] - (50 + graph_scale * self.nodes_set[v][1])
                list_of_edges.append(Edge(x1, y1, x2, y2))

        def redraw_game_window():
            surface_main.fill((0, 0, 0))

            for e in list_of_edges:
                e.draw(surface_main)

            for n in list_of_nodes:
                n.draw(surface_main)

            pygame.draw.line(surface_main, (250, 250, 250), (50, 50 + max_y * graph_scale), (50, 50), 1)
            text_axe_y = font_axes.render('Y', 1, color_axe_name)
            surface_main.blit(text_axe_y, (30, 50))
            pygame.draw.line(surface_main, (250, 250, 250), (50, 50 + max_y * graph_scale), (50 + max_y * graph_scale, 50 + max_y * graph_scale), 1)
            text_axe_x = font_axes.render('X', 1, color_axe_name)
            surface_main.blit(text_axe_x, (40 + max_y * graph_scale, 60 + max_y * graph_scale))
            pygame.display.update()

        run = True
        while run:
            CLOCK.tick(FPS)

            keys = pygame.key.get_pressed()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    run = False
            if keys[pygame.K_ESCAPE]:
                run = False
            redraw_game_window()
        pygame.quit()