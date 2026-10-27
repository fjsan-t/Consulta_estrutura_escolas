from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

@app.get("/", response_class=FileResponse)
def serve_index():
    return FileResponse("index.html")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def carregar_dados():
    df = pd.read_csv("dados_escola_mvp.csv")
    df['Tem_Informatica'] = df['IN_LABORATORIO_INFORMATICA'] == 1.0
    return df

@app.get("/api/municipios")
def obter_municipios():
    df = carregar_dados()
    return sorted(df['NO_MUNICIPIO'].dropna().unique().tolist())

@app.get("/api/escolas")
def filtrar_escolas(
    municipio: str = Query(None),
    dependencia: int = Query(None),
    tem_lab: int = Query(None),
    nome: str = Query(None)
):
    df = carregar_dados()
    if municipio:
        df = df[df['NO_MUNICIPIO'].str.lower() == municipio.lower()]
    
    if dependencia:
        df = df[df['TP_DEPENDENCIA'] == dependencia]
        
    if tem_lab is not None:
        df = df[df['IN_LABORATORIO_INFORMATICA'] == tem_lab]
        
    if nome:
        df = df[df['NO_ENTIDADE'].str.contains(nome, case=False, na=False)]
      
    return {
        "total": len(df),
        "escolas": df[['CO_ENTIDADE', 'NO_ENTIDADE', 'NO_MUNICIPIO', 'TP_DEPENDENCIA', 'Tem_Informatica']].to_dict(orient="records")
    }
