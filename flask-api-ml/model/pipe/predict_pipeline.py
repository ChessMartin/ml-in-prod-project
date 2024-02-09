from zenml.pipelines import pipeline
from steps.predictor import predict_from_json


@pipeline
def prediction_pipeline(predict_step):
    predict_step()

    results = predict()
