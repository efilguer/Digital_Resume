import qrcode
import qrcode.constants
from qrcode.image.styledpil import StyledPilImage

class generateQR:

    def generate(data):

        qr = qrcode.QRCode(
            version= 1,
            error_correction= qrcode.constants.ERROR_CORRECT_H,
            box_size = 10,
            border = 4 
        )

        qr.add_data(data)
        qr.make(fit = True)

        #image from QR
        image = qr.make_image(image_factory=StyledPilImage, embeded_image_path="/home/locutus/Pictures/Screenshots/dogpaw.png")

        #save image
        image.save('/home/locutus/Documents/Tech_Projects/ProjectIAmDog/images/test_generated0113.png')
        print('generating ...')
        print('qr code generated and image saved')
