from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def f_index():
    return {"ФИО": "Ломакин С.А."}

@app.get('/users')
async def f_indexU():
    return {"№ телефона": "+7(913)095-**-**"}

@app.get('/tools')
async def f_indexT():
    return {"О себе": "Студент АлтГУ, Программа обучения: Прикладная информатика"}