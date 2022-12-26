class Button:
    """Класс Button"""
    color = 'white'
    colors = ('white','black','red')
    '''атрибут класса'''

    def __init__(self, widht: int, height: int, text: str) -> None:
        '''конструктор класса'''
        '''Проверка'''
        if not isinstance(widht,int):
            raise TypeError ('Only Int')
        if not isinstance(height, int):
            raise TypeError ('Only Int')
        if not isinstance(text, str):
            raise TypeError

        self.widht = widht
        self.heiht = height
        self.text = text
        self.is_pressed = False

    @classmethod
    def change_color(cls, new_color):
        if not isinstance(new_color, str):
            raise TypeError
        if new_color not in cls.colors:
            raise ValueError
        cls.color = new_color

    def press(self):
        self.is_pressed = not self.is_pressed

    def __str__(self):
        return self.text

    def to_dict(self):
        return {
        'widht': self.widht,
        'heiht': self.heiht,
        'text': self.text
        }

    @classmethod
    def from_dict(cls, data: dict):
        return Button(**data)




enter = Button(widht=12, height=5, text='enter')
Button.change_color('red')
print(Button.color)

print(enter.press)
print(enter.text)







