import math
import os.path
import torch
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')


def plot_weight_function(positive_window):
    beta = -2 * math.log(0.5) / positive_window
    print("positive_window = ", positive_window, "--|||--", "beta = ", beta)

    # temp_x = list(range(positive_window))
    temp_x = list(range(max(positive_window, 2)))
    temporal = -1 + 2 * torch.exp(
        -beta * torch.abs(torch.transpose(torch.tensor([temp_x]), 1, 0) - torch.tensor([temp_x] * positive_window)))

    # print(temporal)

    plt.plot(temp_x, temporal.numpy())
    plt.xlabel('Temporal Distance')
    plt.ylabel('Weight')
    plt.title('Weight Function for Positive Window = {}'.format(positive_window))
    plt.grid(True)

    # plt.xlim(0, 2)

    plt.savefig(f"positive_window_plots/window_{window}")
    # plt.clf()  # Clear the plot after saving
    # plt.show()


if __name__ == '__main__':
    if not os.path.isdir("positive_window_plots"):
        os.makedirs("positive_window_plots")

    # Plot the weight function for different positive window values
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 25, 50, 100, 200]
    positive_window_values = [4, 5, 6, 7, 8, 9, 10]  # Example values for positive window
    for window in positive_window_values:
        plot_weight_function(window)

