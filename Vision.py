
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D://MAIN DRIVE//RUN DRIVE//PYTHON//Projects//VisionAPI//cred.json"

def detect_text(path):
    """Detects text in the file."""
    
    from google.cloud import vision
    import io
    
    #instance
    client = vision.ImageAnnotatorClient()

    #file reading
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    #instace
    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    
    #display
    
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    
path = "D://MAIN DRIVE//RUN DRIVE//PYTHON//Projects//VisionAPI//imagem_teste.jpg"        
key="AIzaSyDponSWgIQOot58iPQMSo3DT6E3EF2q4t4" 
detect_text(path)