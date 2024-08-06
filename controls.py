import pygame

class Controls:
    def __init__(self, FISH_EYE_EFFECT, SHADING_EFFECT, SHADING_DISTANCE) -> None:
        self.fish_eye_effect = FISH_EYE_EFFECT
        self.shading_effect = SHADING_EFFECT
        self.shading_distance = SHADING_DISTANCE
    
    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_F1]:
            self.fish_eye_effect = not self.fish_eye_effect
        if keys[pygame.K_F2]:
            self.shading_effect = not self.shading_effect
        if keys[pygame.K_PAGEUP]:
            self.shading_distance += 10
        if keys[pygame.K_PAGEDOWN]:
            self.shading_distance -= 10