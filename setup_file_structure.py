import os
import shutil

if __name__ == "__main__":
    shutil.rmtree("TSA-ActionSeg/datasets")
    os.mkdir("TSA-ActionSeg/datasets")
    os.mkdir("TSA-ActionSeg/datasets/breakfast_action")
    os.mkdir("TSA-ActionSeg/datasets/breakfast_action/features")
    os.mkdir("TSA-ActionSeg/datasets/breakfast_action/groundTruth")
    os.mkdir("TSA-ActionSeg/datasets/breakfast_action/mappping")

