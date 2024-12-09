from fastapi import FastAPI

from controller.Equipamento_controller import router_equipamentos
from controller.Atribuicoes_controller import router_atribuicao
from controller.Emprestimo_controller import router_emprestimo
from controller.Usuarios_controller import router_usuario
from controller.Materia_controller import router_materia
from controller.Serie_controller import router_serie
from controller.Status_controller import router_status_dispositivo
from controller.Categoria_controller import router_categoria

app = FastAPI()

app.router.include_router(router_equipamentos, prefix="/equipamento")
app.router.include_router(router_atribuicao, prefix="/atribuicao")
app.router.include_router(router_emprestimo, prefix="/emprestimo")
app.router.include_router(router_usuario, prefix="/usuario")
app.router.include_router(router_categoria, prefix="/categoria")
app.router.include_router(router_materia, prefix="/materia")
app.router.include_router(router_serie, prefix="/serie")
app.router.include_router(router_status_dispositivo, prefix="/status")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
