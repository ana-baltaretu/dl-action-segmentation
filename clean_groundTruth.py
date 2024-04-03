import os

if __name__ == "__main__":
    folder_path = "./TSA-ActionSeg/datasets/breakfast_action/groundTruth"
    print(os.listdir(folder_path))

    for file in os.listdir(folder_path):
        if ("cereals" not in file) and (".history" not in file):
            # print(file)
            os.remove(os.path.join(folder_path, file))



