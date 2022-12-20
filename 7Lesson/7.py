class Button:
    """Класс Button"""
    color = 'white'
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
        cls.color = new_color

    def press(self):
        self.is_pressed = True

    def __str__(self):
        return f'{self.text}'

    # def to_dict(self):
    #     dict = {
    #     self.widht: widht,
    #     self.heiht: heiht,
    #     self.text: text
    #     }

enter = Button(widht=12, height=5, text='enter')
Button.change_color('red')
print(Button.color)

print(enter.press)
print(enter.text)







