import io
from PIL import Image
import segno


def simple_embed_center(qr_code_text, embedded_logo_path, output_qr_code):
    out = io.BytesIO()
    segno.make(qr_code_text, error='h').save(out, scale=5, kind='png')
    out.seek(0)

    img = Image.open(out)
    img = img.convert('RGB')
    img_width, img_height = img.size
    logo_max_size = img_height // 3
    logo_img = Image.open(embedded_logo_path)
    logo_img.thumbnail((logo_max_size, logo_max_size), Image.Resampling.LANCZOS)
    box = ((img_width - logo_img.size[0]) // 2, (img_height - logo_img.size[1]) // 2)
    img.paste(logo_img, box)
    img.save(output_qr_code)


if __name__ == "__main__" :
    qr_code_text = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    embedded_logo_path = 'data/test-cat.png'
    output_qr_code = 'data/qr_code.png'
    simple_embed_center(qr_code_text, embedded_logo_path, output_qr_code)