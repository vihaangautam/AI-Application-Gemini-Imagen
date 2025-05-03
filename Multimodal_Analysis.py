import vertexai
from vertexai.preview.vision_models import Image as VertexImage
from vertexai.preview.vision_models import ImageCaptioningModel

def analyze_bouquet_image(image_path: str):
    vertexai.init(project="qwiklabs-gcp-00-1c386a9205fa", location="us-east4")

    image = VertexImage.load_from_file(image_path)
    model = ImageCaptioningModel.from_pretrained("imagetext@001")

    captions = model.get_captions(image)
    print("Generated caption:")
    for caption in captions:
        print(caption.text)

if __name__ == "__main__":
    analyze_bouquet_image("/home/student/bouquet.png")

