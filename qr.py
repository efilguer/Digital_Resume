import qrcode
import qrcode.constants

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
    image = qr.make_image()

    #save image
    image.save('/path/here/name.png')
    print('generating ...')
    print('qr code generated and image saved')


generate('working_website_url_here')