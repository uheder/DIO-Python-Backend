from typing import Annotated
from pydantic import BaseModel, Field, PositiveFloat


class Atleta(BaseModel):
    nome: Annotated[str, Field(description='Nome do Atleta', examples='Pedro Alvaro', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do Atleta', examples='12345678910', max_length=11)]
    idade: Annotated[int, Field(description='Idade do Atleta', examples='20', min_length=2, max_length=3)]
    peso: Annotated[PositiveFloat, Field(description='Peso do Atleta', examples='80.2')]
    sexo: Annotated[str, Field(description='Sexo do Atleta', examples='M', max_length=1)]

    
    