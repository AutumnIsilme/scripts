import requests
import io
import tarfile


VECTORS_TAR_GZ = "https://filesender.open-science-cloud.ec.europa.eu/download.php?token=63a7235c-0265-4fac-bec7-4e4c6caa4c85&files_ids=2174933"
IMAGES_TAR_GZ  = "https://filesender.open-science-cloud.ec.europa.eu/download.php?token=12c6c6c4-4efe-4897-bb25-222345f135cf&files_ids=2174940"

vectors = requests.get(VECTORS_TAR_GZ)
images = requests.get(IMAGES_TAR_GZ)

if vectors.status_code != 200:
    print(f"Error: Vectors failed to download with code {vectors.status_code}")
    exit(1)
if images.status_code != 200:
    print(f"Error: Images failed to download with code {images.status_code}")
    exit(1)

vectors = io.BytesIO(vectors.content)
images = io.BytesIO(images.content)

vectors = tarfile.open(mode='r:gz', fileobj=vectors)
images = tarfile.open(mode='r:gz', fileobj=images)

vectors.extractall(path='/wise/projects')
images.extractall(path='/wise/data')

print("Successfully extracted.")
