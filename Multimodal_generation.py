from vertexai.preview.vision_models import ImageGenerationModel
from vertexai.preview.language_models import TextGenerationModel
import vertexai

def generate_bouquet_image(prompt: str):
    vertexai.init(project="qwiklabs-gcp-00-1c386a9205fa", location="us-east4")
    model = ImageGenerationModel.from_pretrained("imagegeneration@002")
    images = model.generate_images(prompt=prompt)

    # Save the first image
    image_path = "/home/student/bouquet.png"
    with open(image_path, "wb") as f:
        f.write(images[0]._image_bytes)  # internal property
    print(f"Image saved to {image_path}")

if __name__ == "__main__":
    generate_bouquet_image("Create an image containing a bouquet of 2 sunflowers and 3 roses")

