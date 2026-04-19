from connector import image_to_caption

def ingest_image(path):
    with open(path, "rb") as f:
        image_bytes = f.read()

    caption = image_to_caption(image_bytes)
    return caption