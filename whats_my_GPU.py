import torch

i_have_GPU = torch.cuda.is_available()

if i_have_GPU:
    print("YEY, you have at least one GPU!")
    num_gpus = torch.cuda.device_count()
    print(f"Found {num_gpus} CUDA-enabled GPU(s).")
    for i in range(num_gpus):
        print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
else:
    print("Oh no, you don't have a GPU.\n\t\t\t OR \nYour GPU is not set-up properly.")

