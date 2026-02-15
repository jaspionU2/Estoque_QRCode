from sqlalchemy.orm import Session
from configs.register import engine
from model.Model_Conta import Conta
from configs.security import get_password_hash
from sqlalchemy import select

def seed():
    with Session(engine) as session:
        # Verificar se já existe um admin
        admin_exists = session.execute(
            select(Conta).where(Conta.email_conta == 'admin@idevs.com')
        ).scalars().first()

        if not admin_exists:
            admin = Conta(
                usuario_conta='admin',
                email_conta='admin@idevs.com',
                senha_conta=get_password_hash('admin123')
            )
            session.add(admin)
            session.commit()
            print("👤 Usuário admin criado com sucesso!")
            print("Email: admin@idevs.com")
            print("Senha: admin123")
        else:
            print("⚠️ Usuário admin já existe.")

if __name__ == "__main__":
    seed()
