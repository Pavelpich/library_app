
class Book:
    id:int # (уникальный идентификатор, генерируется автоматически)
    title:str # (название книги)
    author:str # (автор книги)
    year:str # (год издания)
    status:str # (статус книги: “в наличии”, “выдана”)

class Library:
    books:list[Book]

    