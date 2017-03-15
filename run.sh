rm my_program.fifo
python buttons_with_fifo.py & python webcams_compositing_using_pygame.py | ffmpeg -f rawvideo -pix_fmt rgb24 -s 640x480 -r 30 -i - -an -vf format=pix_fmts=yuyv422 -f v4l2 /dev/video2
