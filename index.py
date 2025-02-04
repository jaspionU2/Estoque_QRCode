from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from controller.Equipamento_controller import router_equipamentos
from controller.Atribuicoes_controller import router_atribuicao
from controller.Emprestimo_controller import router_emprestimo
from controller.Usuarios_controller import router_usuario
from controller.Materia_controller import router_materia
from controller.Serie_controller import router_serie
from controller.Status_controller import router_status_dispositivo
from controller.Categoria_controller import router_categoria
from controller.Conta_controller import router_conta

from schema.Schema_Conta import SchemaConta

app = FastAPI()

app.add_middleware(
   CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials =True,
    allow_methods = ["*"],
    allow_headers= ["*"],
)

app.router.include_router(router_conta, prefix="/conta")
app.router.include_router(router_equipamentos, prefix="/equipamento")
app.router.include_router(router_atribuicao, prefix="/atribuicao")
app.router.include_router(router_emprestimo, prefix="/emprestimo")
app.router.include_router(router_usuario, prefix="/usuario")
app.router.include_router(router_categoria, prefix="/categoria")
app.router.include_router(router_materia, prefix="/materia")
app.router.include_router(router_serie, prefix="/serie")
app.router.include_router(router_status_dispositivo, prefix="/status")

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Estoque_QR API",
        version="1.0.0",
        description="Pindamonhangaba",
        routes=app.routes,
    )
    openapi_schema["paths"]["/conta/addNewConta"] = {
        "post": {
            "summary": "WebSocket connection",
            "description": "Connect to the WebSocket server. Send a message and receive a response.",
            "requestBody": {
                "required": True,
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "properties": {
                                "usuario_conta": {
                                    "type": "string",
                                    "example": "joao123"
                                },
                                "email_conta": {
                                    "type": "string",
                                    "format": "email",
                                    "example": "joao@gmail.com"
                                },
                                "senha_conta": {
                                    "type": "string",
                                    "format": "password",
                                    "example": "********"
                                }
                            },
                            "required": ["usuario_conta", "email_conta", "senha_conta"]
                        }
                    }
                }
            },
            "responses": {
                "201": {
                    "description": "Usuario criado",
                },
                "400": {
                    "description": "Erro no processamento"
                },
                "401": {
                    "description": "Nenhum dado foi enviado"
                },
                "500": {
                    "description": "Erro interno"
                }
            }
        }
    }
    print(openapi_schema)
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=3000)
