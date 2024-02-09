import argparse

from pipe.training_pipeline import training_pipeline
from pipe.predict_pipeline import insurance_charges_prediction_pipeline

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run training or prediction pipeline based on input data.")
    subparsers = parser.add_subparsers(dest='command', help='sub-command help')

    train_parser = subparsers.add_parser('train', help='Run the training pipeline')
    train_parser.add_argument('csv_file', help="CSV file for training data")

    predict_parser = subparsers.add_parser('predict', help='Run the prediction pipeline')
    predict_parser.add_argument('age', type=int, help='Age of the individual')
    predict_parser.add_argument('sex', choices=['male', 'female'], help='Sex of the individual')
    predict_parser.add_argument('bmi', type=float, help='BMI of the individual')
    predict_parser.add_argument('children', type=int, help='Number of children')
    predict_parser.add_argument('smoker', choices=['yes', 'no'], help='Smoker status')
    predict_parser.add_argument('region', help='Region of the individual')

    args = parser.parse_args()

    if args.command == 'train':
        training_pipeline(args.csv_file)
    elif args.command == 'predict':
        insurance_charges_prediction_pipeline(args.age, args.sex, args.bmi, args.children, args.smoker, args.region)
    else:
        parser.print_help()
