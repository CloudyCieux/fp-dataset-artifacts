"""Convert predictions into a format that can be parsed by Jia and Liang (2017) script for evaluating squad with adversarial data."""

import argparse
import json
import pandas as pd

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path", type=str, help="Input path of json file with predictions.")
    parser.add_argument("output_path", type=str, help="Output path of json file to put reformatted predictions.")

    args = parser.parse_args()

    predictions = pd.read_json(path_or_buf=args.input_path, lines=True)
    
    pred_dict = dict()
    for id, ans in zip(predictions["id"], predictions["predicted_answer"]):
        pred_dict[id] = ans
    
    with open(args.output_path, "w") as f_out:
        json.dump(pred_dict, f_out)

if __name__ == "__main__":
    main()
