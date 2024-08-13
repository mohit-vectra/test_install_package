import os
import subprocess
import urllib.request

# Define URLs for the wheel files
wheel_urls = [

    "https://github.com/mohitVec/test_install_package/blob/main/wheel/my_package-0.1.0-py3-none-any.whl",
    "https://github.com/mohitVec/test_install_package/blob/main/wheel/numpy-1.26.1-cp312-cp312-win_amd64.whl",
    "https://github.com/mohitVec/test_install_package/blob/main/wheel/scikit_learn-1.3.2-cp312-cp312-win_amd64.whl"
]

# Download and install each wheel file
for url in wheel_urls:
    filename = url.split("/")[-1]
    urllib.request.urlretrieve(url, filename)
    subprocess.run(["pip", "install", filename], check=True)
