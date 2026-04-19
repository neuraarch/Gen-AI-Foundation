from config import client, EMBEDDING_MODEL, VISION_MODEL

def get_text_embedding(text):
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text
    )
    return response.data[0].embedding


def image_to_caption(image_bytes):
    import base64

    base64_image = base64.b64encode(image_bytes).decode("utf-8")

    response = client.responses.create(
        model=VISION_MODEL,
        input=[{
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "Describe this car dashboard warning image clearly"
                },
                {
                    "type": "input_image",
                    "image_url": f"data:image/png;base64,{base64_image}"
                }
            ]
        }]
    )

    return response.output[0].content[0].text


def generate_llm_response(prompt):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output[0].content[0].text