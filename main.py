from app.infrastructure.services.qr_code_service_qrcode import QRCodeServiceQRCode

from app.infrastructure.persistence import (LivroRepositoryTXT, ReservaRepositoryTXT)

from app.interface_adapters.controllers import (buscar_livros_controller, detalhar_livro_controller, reservar_livro_controller)

from app.infrastructure.web.flask_app import criar_app


def main():

    # Infra (dados)
    livro_repository = LivroRepositoryTXT("dados/livros.txt")
    reserva_repository = ReservaRepositoryTXT("dados/reservas.txt")
    qr_code_service = QRCodeServiceQRCode()

    # App (injeção)
    app = criar_app(
        livro_repository,
        reserva_repository,
        qr_code_service,
        buscar_livros_controller,
        detalhar_livro_controller,
        reservar_livro_controller,
    )

    # Run
    app.run(debug=True)


if __name__ == "__main__":
    main()