## DO NOT EDIT! copy this into game.py and edit it there to create new scene


def menu(screen, args):
    # Initialize game variables as the player, enemies and such.
    fps_cap = 30
    items = ['sword', 'armor', 'potion']
    clock = pygame.time.Clock()

    # Game loop.
    while True:

        # Time management.
        clock.tick(fps_cap)

        # Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        # Update the shop (like buttons, money transfers, ...).
        print('Looking at items:', *items)

        # Draw the shop.
        screen.fill((255, 0, 0))  # A red shop.
        pygame.display.update()