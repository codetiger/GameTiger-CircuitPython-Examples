import time
import board
from digitalio import DigitalInOut, Pull
import displayio
from adafruit_display_shapes.circle import Circle

display = board.DISPLAY
frame = displayio.Group()
display.root_group = frame
display.auto_refresh = False

bitmap = displayio.Bitmap(display.width, display.height, 2)
colors = [0xDFFF00, 0xFFBF00, 0xFF7F50, 0xDE3163, 0x9FE2BF, 0x40E0D0, 0x6495ED, 0xCCCCFF]

foreground_color = 1
background_color = 3

color_bitmap = displayio.Bitmap(320, 240, 1)
color_palette = displayio.Palette(8)

ball_position_x = 100
ball_position_y = 100

button_up = DigitalInOut(board.KB_UP)
button_up.switch_to_input(pull=Pull.UP)

button_down = DigitalInOut(board.KB_DOWN)
button_down.switch_to_input(pull=Pull.UP)

button_right = DigitalInOut(board.KB_RIGHT)
button_right.switch_to_input(pull=Pull.UP)

button_left = DigitalInOut(board.KB_LEFT)
button_left.switch_to_input(pull=Pull.UP)

button_A = DigitalInOut(board.KB_A)
button_A.switch_to_input(pull=Pull.UP)

button_B = DigitalInOut(board.KB_B)
button_B.switch_to_input(pull=Pull.UP)

button_select = DigitalInOut(board.KB_SELECT)
button_select.switch_to_input(pull=Pull.UP)

button_start = DigitalInOut(board.KB_START)
button_start.switch_to_input(pull=Pull.UP)

needs_display_update = True

while True:
    if not button_up.value:
        ball_position_y -= 5
        needs_display_update = True
        print("Button UP pressed")

    if not button_down.value:
        ball_position_y += 5
        needs_display_update = True
        print("Button DOWN pressed")

    if not button_right.value:
        ball_position_x += 5
        needs_display_update = True
        print("Button RIGHT pressed")

    if not button_left.value:
        ball_position_x -= 5
        needs_display_update = True
        print("Button LEFT pressed")

    if not button_A.value:
        foreground_color += 1
        needs_display_update = True
        print("Button A pressed")

    if not button_B.value:
        foreground_color -= 1
        needs_display_update = True
        print("Button B pressed")

    if not button_select.value:
        background_color += 1
        needs_display_update = True
        print("Button Select pressed")

    if not button_start.value:
        background_color -= 1
        needs_display_update = True
        print("Button Start pressed")

    if foreground_color >= len(colors):
        foreground_color = len(colors) - 1
    elif foreground_color < 0:
        foreground_color = 0

    if background_color >= len(colors):
        background_color = len(colors) - 1
    elif background_color < 0:
        background_color = 0

    if needs_display_update:
        needs_display_update = False
        color_palette[0] = colors[background_color]
        bg_sprite = displayio.TileGrid(color_bitmap, x=0, y=0, pixel_shader=color_palette)
        frame.append(bg_sprite)

        ball = Circle(ball_position_x, ball_position_y, 20, fill=colors[foreground_color])
        frame.append(ball)
        display.refresh()

    time.sleep(0.01)