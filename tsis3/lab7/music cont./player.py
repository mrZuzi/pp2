import pygame


pygame.init()
window_size = (230,225)
screen = pygame.display.set_mode(window_size)
bg = pygame.image.load('music/images.png')


tracks = [
    'music/tracks/track1.mp3',
    'music/tracks/track2.mp3',
    'music/tracks/track3.mp3',
]

# Load the first track
current_track_index = 0
pygame.mixer.music.load(tracks[current_track_index])

# Run the music player
playing = False
while True:
    
    screen.blit(bg,(0,0))
    # Handle events  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Toggle play/pause
                if playing:
                    pygame.mixer.music.pause()
                    playing = False
                else:
                    pygame.mixer.music.unpause()
                    playing = True
            elif event.key == pygame.K_n:
                # Play next track
                current_track_index = (current_track_index + 1) % len(tracks)
                pygame.mixer.music.load(tracks[current_track_index])
                pygame.mixer.music.play()
                playing = True
            elif event.key == pygame.K_p:
                # Play previous track
                current_track_index = (current_track_index - 1) % len(tracks)
                pygame.mixer.music.load(tracks[current_track_index])
                pygame.mixer.music.play()
                playing = True

    # Update the screen (not actually used in this example)
    pygame.display.update()

    # Wait for 1/60th of a second (60 fps)
    pygame.time.wait(16)

