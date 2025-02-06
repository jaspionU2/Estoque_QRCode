from fastapi import HTTPException, status

NOT_DATA = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Nenhum dado foi enviado"
)
NOT_SUCCESS = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Erro no processamento"    
)
NOT_FOUND = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Dados não encontrados"
)

internal_server_error = HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail="Erro interno do servidor"
)

