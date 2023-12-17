class Color:
    grey = (26, 31, 40)
    light_blue = (0, 230, 253)
    dark_blue = (24, 1, 255)
    orange = (255, 115, 9)
    yellow = (255, 222, 2)
    green = (102, 253, 2)
    red = (254, 17, 60)
    magenta = (185, 3, 253)
    white = (255,255,255)
    black = (0,0,0)

    @classmethod
    def get_color_pieces(cls):
        
        return [cls.grey, cls.light_blue, cls.dark_blue, cls.orange, cls.yellow, cls.green, cls.red, cls.magenta]