import requests
from PIL import Image
from io import BytesIO
from skimage.metrics import structural_similarity as ssim

def fetch_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

def compare_images(img1, img2):
    return ssim(img1, img2, multichannel=True)

def find_similar_product_images(main_image_url, other_images_urls):
    main_image = fetch_image(main_image_url)
    similarities = []

    for img_url in other_images_urls:
        other_image = fetch_image(img_url)
        similarity = compare_images(main_image, other_image)
        similarities.append((img_url, similarity))

    return sorted(similarities, key=lambda x: x[1], reverse=True)


#THIS IS SO SLOW???????? I DONT THINK IT WILL WORK??????