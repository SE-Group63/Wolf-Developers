import subprocess

def random_array(arr: list[int]):
    shuffled_num = None
    for i in range(len(arr)):
        shuffled_num = subprocess.run(["shuf", "-i1-20", "-n1"], capture_output=True)
        arr[i] = int(shuffled_num.stdout.decode("utf-8").strip())
    return arr

#pyright:strict