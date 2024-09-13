"""hello world"""
import subprocess

def random_array(arr: list[int]):
    """temperarory"""
    shuffled_num = None
    for i,_ in enumerate(arr):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check= True)
        arr[i] = int(shuffled_num.stdout.decode("utf-8").strip())
    return arr

# pyright:strict
