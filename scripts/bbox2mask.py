import argparse
import json
import pathlib

def main(infile, outfile):
    in_path = pathlib.Path(infile).absolute()
    out_path = pathlib.Path(outfile).absolute()

    print(f"\nOpening file: '{in_path}'")
    with open(in_path, "r") as f:
        coco_dataset = json.load(f)

    new_annotations = []
    for ann in coco_dataset["annotations"]:
        x, y, w, h = [int(i) for i in ann["bbox"]]
        ann["segmentation"] = [[x, y, x+w, y, x+w, y+h, x, y+h]]
        new_annotations.append(ann)

    coco_dataset["annotations"] = new_annotations

    print(f"Writing to: '{out_path}'")
    with open(out_path, "w") as f:
        json.dump(coco_dataset, f, indent=2, sort_keys=True)

    print("\nDone.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="bbox2mask")
    parser.add_argument("-i", "--input", required=True, help="JSON file of a COCO dataset")
    parser.add_argument("-o", "--output", required=True, help="Output JSON filename")
    args = parser.parse_args()

    main(args.input, args.output)
