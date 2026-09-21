import importlib
import subprocess
import sys

try:
    numpy = importlib.import_module("numpy")
except ModuleNotFoundError:
    print("NumPy is not installed in this environment. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy"])
    numpy = importlib.import_module("numpy")

print(f"NumPy version: {numpy.__version__}")
arr = numpy.array([1, 2, 3, 4, 5])
# print(arr)
#######################
arr = numpy.array([10,20,30,40,50])
print(arr)
print(arr.shape)
print(arr.ndim)
print("\n") # emptyline
arr = numpy.array([[10,20,30,40,50]])
print(arr)
print(arr.shape)
print(arr.ndim)
print("\n")
arr = numpy.array([[[10,20,30,40,50]]])
print(arr)
print(arr.shape)
print(arr.ndim)