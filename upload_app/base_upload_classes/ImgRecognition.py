from imageai.Prediction import ImagePrediction


class ImgRecognition:
    MODEL_PATH = "/home/imgrecognitionteam3/img-recognition-dataset/resnet50_model.h5"

    def __init__(self):
        self.prediction = ImagePrediction()

        # set model type as ResNet
        self.prediction.setModelTypeAsResNet()
        self.prediction.setModelPath(self.MODEL_PATH)
        self.prediction.loadModel()

    # Recognize image function
    # @param img_file -> img file to recognize
    # @return -> string img prediction
    def recognize_image(self, img_file):
        try:
            prediction = self.prediction.predictImage(img_file, result_count=1)
            return prediction[0]

        except Exception as ex:
            # if there is any error, raise a ValueError
            raise ValueError(ex.args)


