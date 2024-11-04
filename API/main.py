from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="API Manipulação de Strings",
    description="Esta API fornece operações de manipulação de strings.",
    version="1.0.0"
)

@app.get("/inverter", tags=["Operações"])
def inverter_string(texto : str):
    """
    Inverter uma string fornecida pelo usuário

    - **texto**: A string que será invertida
    - **Retorno**: A string invertida
    """

    if not texto:
        raise HTTPException(
            status_code=400, 
            detail="O texto não pode ser vazio."
        )

    resultado = texto[::-1]
    return {"resultado" : resultado}

@app.get("/contar", tags=["Operações"])
def contar_caracteres(texto : str):
    """
    Contar o número de caracteres de uma string

    - **texto**: A string cujo número de caracteres será contado
    - **Retorno**: O número de caracteres da string
    """

    if not texto:
        raise HTTPException(
            status_code=400, 
            detail="O texto não pode ser vazio."
        )

    resultado = len(texto)
    return {"resultado" : resultado}

@app.get("/palindromo", tags=["Operações"])
def verificar_palindromo(texto : str):
    """
    Verificar se a string fornecida pelo usuário é um palíndromo

    - **texto**: A string a ser verificada
    - **Retorno**: 'True' se a string é um palíndromo, ou 'False', caso contrário.
    """

    if not texto:
        raise HTTPException(
            status_code=400, 
            detail="O texto não pode ser vazio."
        )

    resultado = (texto == texto[::-1])
    return {"resultado" : resultado}


@app.get("/maiusculo", tags=["Operações"])
def transformar_maiusculo(texto : str):
    """
    Transforma todos os caracteres da string em maiúsculo

    - **texto**: A string a ser transformada
    - **Retorno**: A string com todos os caracteres em maiúsculo
    """

    if not texto:
        raise HTTPException(
            status_code=400, 
            detail="O texto não pode ser vazio."
        )

    resultado = texto.upper()
    return {"resultado" : resultado}

@app.get("/minusculo", tags=["Operações"])
def transformar_minusculo(texto : str):
    """
    Transforma todos os caracteres da string em minúsculo

    - **texto**: A string a ser transformada
    - **Retorno**: A string com todos os caracteres em minúsculo
    """

    if not texto:
        raise HTTPException(
            status_code=400, 
            detail="O texto não pode ser vazio."
        )

    resultado = texto.lower()
    return {"resultado" : resultado}