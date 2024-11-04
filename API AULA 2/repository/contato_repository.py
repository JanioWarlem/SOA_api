from __future__ import annotations
from sqlalchemy.orm import Session
from models.models import Contato

class ContatoRepository:

    #
    # Retornar todos os contatos
    #
    @staticmethod
    def get_all(db:Session) -> list[Contato]:
        return db.query(Contato).all()
    
    #
    # Salvar um contato na tabela
    #
    @staticmethod
    def salvar(db:Session, Contato: Contato) -> Contato:
        if (Contato.id):
            db.merge(Contato)
        else:
            db.add(Contato)
        db.commit()
        return Contato

    #
    # Retornar um contato a partir do Id
    #
    @staticmethod
    def get_by_id(db:Session, id: int) -> Contato:
        return db.query(Contato).filter(Contato.id == id).first()
    
    #
    # Verificar se um contato existe a partir do Id
    #
    @staticmethod
    def exists_by_id(db:Session, id: int) -> bool:
        return db.query(Contato).filter(Contato.id == id).first() is not None
    
    #
    # Apagar um contator a partir do Id
    #
    @staticmethod
    def deletar(db:Session, id: int) -> bool:
        contato = db.query(Contato).filter(Contato.id == id).first()
        if contato is not None:
            db.delete(contato)
            db.commit()
            return True
        return False

    #
    # Retornar todos os contatos ordenado por nome
    #
    @staticmethod
    def get_sort(db:Session) -> list[Contato]:
        return db.query(Contato).all().sort()