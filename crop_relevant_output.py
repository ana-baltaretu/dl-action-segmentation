import os
import shutil
import cv2


def show_stuff():
    cv2.imshow('Resized Image', resized_image)
    cv2.imshow('Cropped Image', cropped_image)
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def write_stuff():
    destination_path_gt = os.path.join("cropped_output", "_groundTruth.png")
    cv2.imwrite(destination_path_gt, cropped_image_gt)

    destination_path_features = os.path.join("cropped_output", f"_{mode}_initialFeatures.png")
    cv2.imwrite(destination_path_features, cropped_image_features)

    combined_base = cv2.vconcat([cropped_image_gt, cropped_image_features])
    current_combined_image = combined_images.get(mode, combined_base)

    destination_path_result = os.path.join("cropped_output", experiment_name, f"{mode}_result_Pw{window_size}.png")
    cv2.imwrite(destination_path_result, cropped_image)

    combined_images[mode] = cv2.vconcat([current_combined_image, cropped_image])
    final_destination_path_result = os.path.join("cropped_output", f"__final_{mode}_result.png")

    line_h = 550
    start_point = (0, line_h)
    end_point = (6000, line_h)
    color_black = (0, 0, 0)
    thickness = 5
    cv2.line(combined_images[mode], start_point, end_point, color_black, thickness)

    cv2.imwrite(final_destination_path_result, combined_images[mode])


if __name__ == '__main__':

    shutil.rmtree("cropped_output")
    if not os.path.exists("cropped_output"):
        os.mkdir("cropped_output")
    window_sizes = [5, 10, 50, 100, 120, 250]
    video_name = "P03_cam01_P03_cereals"

    combined_images = dict()

    for window_size in window_sizes:
        experiment_name = "breakfast_action_experiment_6_Pw" + str(window_size)
        destination_experiment_path = os.path.join("cropped_output", experiment_name)
        if not os.path.exists(destination_experiment_path):
            os.mkdir(destination_experiment_path)

        modes = ["finch", "kmeans", "spectral", "twfinch"]
        for mode in modes:
            file_name = video_name + ".segmentation_" + mode + ".png"
            source_path = os.path.join("TSA-ActionSeg", "output", experiment_name, video_name, file_name)
            image = cv2.imread(source_path)

            left = 500
            right = 5500

            top_gt = 50
            bottom_gt = 349
            cropped_image_gt = image[top_gt:bottom_gt, left:right]

            top_features = 325
            bottom_features = 580
            cropped_image_features = image[top_features:bottom_features, left:right]

            top_result = 570
            bottom_result = 830
            cropped_image = image[top_result:bottom_result, left:right]

            # white_image = cropped_image.copy()
            cropped_image[0:250, 0:250] = (255, 255, 255)

            text_org = (130 - (2+len(str(window_size))) * 20, 150)
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 2
            color = (0, 0, 0)
            line_type = 8
            cv2.putText(cropped_image, "L=" + str(window_size), text_org, font, font_scale, color, line_type)

            scale_width = 0.1  # 50% of the original size
            scale_height = 0.1  # 50% of the original size
            new_size = (int(cropped_image.shape[1] * scale_width), int(cropped_image.shape[0] * scale_height))
            resized_image = cv2.resize(cropped_image, new_size)

            write_stuff()

