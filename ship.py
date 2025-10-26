import os
import pygame

class Ship:
    def __init__(self, screen, width=50):
        self.screen = screen
        self.target_width = width

        # load and scale all images from the ship_images directory
        images_dir = os.path.join(os.path.dirname(__file__), "ship_images")
        self.images = []
        if os.path.isdir(images_dir):
            for fname in sorted(os.listdir(images_dir)):
                if fname.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
                    path = os.path.join(images_dir, fname)
                    try:
                        img = pygame.image.load(path).convert_alpha()
                    except Exception:
                        img = pygame.image.load(path)

                    # scale to target width while preserving aspect ratio
                    if img.get_width() != self.target_width:
                        scale_factor = self.target_width / img.get_width()
                        new_size = (self.target_width, max(1, int(img.get_height() * scale_factor)))
                        try:
                            img = pygame.transform.smoothscale(img, new_size)
                        except Exception:
                            img = pygame.transform.scale(img, new_size)

                    self.images.append(img)

        # fallback to single ship.png if no images found in ship_images
        if not self.images:
            fallback = os.path.join(os.path.dirname(__file__), "ship.png")
            img = pygame.image.load(fallback).convert_alpha()
            if img.get_width() != self.target_width:
                scale_factor = self.target_width / img.get_width()
                new_size = (self.target_width, max(1, int(img.get_height() * scale_factor)))
                try:
                    img = pygame.transform.smoothscale(img, new_size)
                except Exception:
                    img = pygame.transform.scale(img, new_size)
            self.images = [img]

        # animation state
        self.image_index = 0.0
        self.anim_speed = 0.3
        self.image = self.images[int(self.image_index)]
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 1

        # advance animation on every update (so ship is animated even when idle)
        if len(self.images) > 1:
            self._advance_image()

    def _advance_image(self):
        # advance a fractional index to allow smooth animation speed control
        self.image_index = (self.image_index + self.anim_speed) % len(self.images)
        old_centerx = self.rect.centerx
        old_bottom = self.rect.bottom
        self.image = self.images[int(self.image_index)]
        self.rect = self.image.get_rect()
        self.rect.centerx = old_centerx
        self.rect.bottom = old_bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)