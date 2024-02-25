import sys
class MediaPlayer():
    def open(self, file):
        MediaPlayer.filename = file
    def play(self):
        print(f'Воспроизведение {MediaPlayer.filename}')
def main():
    media1 = MediaPlayer()
    media1.open('filemedia1')
    media1.play()

    media2 = MediaPlayer()
    media2.open('filemedia2')
    media2.play()
    
if __name__ == '__main__':
    main()

