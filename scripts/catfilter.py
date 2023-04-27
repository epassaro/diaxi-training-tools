import argparse
import json
import pathlib

def main(infile, outfile, categories):
    in_path = pathlib.Path(infile).absolute()
    out_path = pathlib.Path(outfile).absolute()

    print(f"\nOpening file: '{in_path}'")
    with open(in_path, "r") as f:
        coco_dataset = json.load(f)

    keep_categories = args.categories.split(",")
    new_categories = []
    new_annotations = []

    # Clean `category` key
    for category in coco_dataset["categories"]:
        if category["name"] in keep_categories:
            new_categories.append(category)

    # Clean `annotations` key
    keep_ids = [c["id"] for c in new_categories]
    for ann in coco_dataset["annotations"]:
        if ann["category_id"] in keep_ids:
            new_annotations.append(ann)

    coco_dataset["categories"] = new_categories
    coco_dataset["annotations"] = new_annotations

    print(f"Writing to: '{out_path}'")
    with open(out_path, "w") as f:
        json.dump(coco_dataset, f, indent=2, sort_keys=True)

    print("\nDone.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="catfilter")
    parser.add_argument("-i", "--input", required=True, help="JSON file of a COCO dataset")
    parser.add_argument("-o", "--output", required=True, help="Output JSON filename")
    parser.add_argument("-c", "--categories", required=True, help="Comma separated list of categories")
    args = parser.parse_args()

    main(args.input, args.output, args.categories)
