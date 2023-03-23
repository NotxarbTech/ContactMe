import qrcode
from django.urls import reverse
from urllib.parse import urljoin

def generate_qr_code(request, id):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(urljoin(request.build_absolute_uri('/'), reverse('view_contact', args=[id])))
    qr.make(fit=True)

    return qr.make_image(fill_color="black", back_color="white")