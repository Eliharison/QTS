from fastapi import FastAPI, HTTPException, status

app = FastAPI(title="Fatec299")

estudantes = {
    1: {"id": 1, "nome": "Eliharison", "idade": 20},
    2: {"id": 2, "nome": "Rodrigo", "idade": 20},
}


@app.get("/estudante/{estudante_id}")
def buscar_estudante_por_id(estudante_id: int):
    estudante = estudantes.get(estudante_id)
    if estudante:
        return estudante
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"mensagem": "Estudante não encontrado"},
        )
