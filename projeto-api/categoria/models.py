from sqlalchemy import ForeignKey, Integer, String
from contrib.models import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship


class CategoriaModel(BaseModel):
    __tablename__ = 'categorias'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(10), nullable=False)
    atleta: Mapped['AtletaModel'] = relationship(back_populates='categoria')
    atleta_id = Mapped[int] = mapped_column(ForeignKey('atletas.pk_id'))
