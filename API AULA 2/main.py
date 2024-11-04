from __future__ import annotations
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from models.models import Contato, ContatoResponse, ContatoRequest
from data.config import engine, Base, get_db
from repository.contato_repository import ContatoRepository

#
# INICIALIZAÇÃO
#
Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="API Contatos",
    description="Esta API fornece operações gerenciamento de contatos.",
    version="1.0.0"
)

#
# ROTAS
#
@app.post("/api/contatos", response_model=ContatoResponse, status_code=status.HTTP_201_CREATED, tags=["Operações"])
def inserir(request: ContatoRequest, db:Session = Depends(get_db)):
    return ContatoRepository.salvar(db,Contato(**request.model_dump()))

@app.get("/api/contatos", response_model=list[ContatoResponse], tags=["Operações"])
def listar(db:Session = Depends(get_db)):
    return ContatoRepository.get_all(db)

@app.get("/api/contatos/{id}", response_model=ContatoResponse, tags=["Operações"])
def get_by_id(id: int, db:Session = Depends(get_db)):
    contato = ContatoRepository.get_by_id(db,id)
    if (not contato):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Contato não encontrado.')
    return contato

@app.delete("/api/contatos/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Operações"])
def deletar(id: int, db:Session = Depends(get_db)):
    if not ContatoRepository.exists_by_id(db,id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Contato não encontrado.')
    
    if ContatoRepository.deletar(db,id):
        raise HTTPException(status_code=status.HTTP_200_OK,detail='Operação realizada com sucesso!')
    else:
        raise HTTPException(status_code=status.HTTP_200_OK,detail='Não foi possível realizar a operação.')

@app.put("/api/contatos/{id}", response_model=ContatoResponse, tags=["Operações"])
def atualizar(id: int, request: ContatoRequest, db:Session = Depends(get_db)):
    if not ContatoRepository.exists_by_id(db,id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Contato não encontrado.')
    
    return ContatoRepository.salvar(db, Contato(id=id,**request.model_dump()))



@app.get("/api/contatos/sort", response_model=ContatoResponse, tags=["Operações"])
def listar_por_nome(db:Session = Depends(get_db)):
    contato = ContatoRepository.get_sort(db)
    if (not contato):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Banco de dados Vazio')
    return contato