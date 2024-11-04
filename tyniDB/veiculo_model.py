from pydantic import BaseModel

class Item(BaseModel):
    marca: str
    model: str = None
    ano_fabricacao: float
    preco: float = None
    