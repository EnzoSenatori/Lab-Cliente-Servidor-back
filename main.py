from app.infrastructure.services.qr_code_service_qrcode import QRCodeServiceQRCode
from app.infrastructure.persistence import (LivroRepositoryTXT, ReservaRepositoryTXT)
from app.interface_adapters.controllers import (buscar_livros_controller, detalhar_livro_controller, reservar_livro_controller)
from app.infrastructure.web.flask_app import criar_app


# Infra (dados)
livro_repository = LivroRepositoryTXT("dados/livros.txt")
reserva_repository = ReservaRepositoryTXT("dados/reservas.txt")
qr_code_service = QRCodeServiceQRCode()

# App (injeção) — variável de módulo, exigida pelo Azure
app = criar_app(
    livro_repository,
    reserva_repository,
    qr_code_service,
    buscar_livros_controller,
    detalhar_livro_controller,
    reservar_livro_controller,
)


if __name__ == "__main__":
    # Execução local apenas — o Azure ignora este bloco e usa `app` diretamente
    app.run(host="0.0.0.0", port=5000, debug=True)