from fastapi import FastAPI, HTTPException
from veiculo_model import Item
from tinydb import TinyDB, Query

app = FastAPI(
    title="API Veículos",
    description="API para gerenciamento de veículos.",
    version="1.0.0"
)

db = TinyDB('dados.json')

@app.get("/")
def index():
    return {"info": "API Veículos"}

@app.post("/veiculos/", response_model=Item)
def adicionar(item: Item):
    item_dict = item.model_dump()
    item_id = db.insert(item_dict)
    return {"item_id": item_id, **item_dict}

@app.get("/veiculos/", response_model=list[Item])
def listar():
    '''
    Retornar uma lista com todos os veículos
    '''
    return db.all()

@app.get("/veiculos/{item_id}", response_model=Item)
def retornarPorId(item_id: int):
    item = db.get(doc_id=item_id)
    if item is None:
        raise HTTPException(status_code=404,detail='Item não encontrado.')
    return item

@app.put("/veiculos/{item_id}", response_model=Item)
def atualizar(item_id: int, item_atualizado: Item):
    item_dict = item_atualizado.model_dump()
    if not db.update(item_dict,doc_ids=[item_id]):
        raise HTTPException(status_code=404,detail='Item não encontrado.')
    return {"item_id": item_id, **item_dict}

@app.delete("/veiculos/{item_id}", response_model=Item)
def deletar(item_id: int):
    item = db.get(doc_id=item_id)
    if item is None:
        raise HTTPException(status_code=404,detail='Item não encontrado.')
    db.remove(doc_ids=[item_id])
    return item

