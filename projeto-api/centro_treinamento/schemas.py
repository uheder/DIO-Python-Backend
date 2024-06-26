from typing import Annotated
from contrib.schemas import BaseSchema
from pydantic import BaseModel, Field


class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='Nome do CT', examples='PedroFit', max_length=20)]
    endereco: Annotated[str, Field(description='Endereço do CT', examples='Rua 1', max_length=60)]
    proprietario: Annotated[str, Field(description='Nome do proprietario do CT', examples='Roberto Guimaraes', max_length=30)]