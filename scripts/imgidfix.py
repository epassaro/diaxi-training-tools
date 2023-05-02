import argparse
import json
import pathlib

def main(infile, outfile):
    in_path = pathlib.Path(infile).absolute()
    out_path = pathlib.Path(outfile).absolute()

    print(f"\nOpening file: '{in_path}'")
    with open(in_path, "r") as f:
        coco_dataset = json.load(f)

    new_images = []
    new_annotations = []

    images = coco_dataset["images"]
    ids = [i["id"] for i in  images]
    new_ids = range(len(images))
    map_ids = dict(zip(ids, new_ids))
    
    for img in images:
        img["id"] = map_ids[img["id"]]
        new_images.append(img)

    for ann in coco_dataset["annotations"]:
        try:
            ann["image_id"] = map_ids[ann["image_id"]]
            new_annotations.append(ann)

        except KeyError:
            continue

    coco_dataset["images"] = new_images
    coco_dataset["annotations"] = new_annotations

    print(f"Writing to: '{out_path}'")
    with open(out_path, "w") as f:
        json.dump(coco_dataset, f, indent=2, sort_keys=True)

    print("\nDone.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="imgidfix")
    parser.add_argument("-i", "--input", required=True, help="JSON file of a COCO dataset")
    parser.add_argument("-o", "--output", required=True, help="Output JSON filename")
    args = parser.parse_args()

    main(args.input, args.output)
