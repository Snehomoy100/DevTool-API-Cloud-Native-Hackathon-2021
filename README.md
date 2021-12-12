# _CloudNativeHackathon2021_

### About the project⭐
Using Kubernetes production best policies to run the k8s manifest files through [Datree.io](https://github.com/datreeio/datree) to prevent Kubernetes misconfigurations from ever reaching production.

Reference: [Kubernetes production best policies](https://github.com/learnk8s/kubernetes-production-best-practices)

**Added next custom policies recommended for production environment✅:**

- CUSTOM_CONTAINERS_PODS_MISSING_OWNERS
- CUSTOM_CONTAINERS_MISSING_LIVENESSPROBE
- CUSTOM_CONTAINERS_MISSING_READINESSPROBE
- CUSTOM_CONTAINERS_MISSING_IMAGE_TAG
- CUSTOM_CONTAINERS_MIN_REPLICAS
- CUSTOM_CONTAINERS_MISSING_PODANTIAFFINITY
- CUSTOM_CONTAINERS_RESOURCES_REQUESTS_AND_LIMITS
- CUSTOM_CONTAINERS_RESOURCES_REQUESTS_CPU_BELOW_1000M
- CUSTOM_CONTAINERS_TECHNICAL_LABELS
- CUSTOM_CONTAINERS_BUSINESS_LABELS
- CUSTOM_CONTAINERS_SECURITY_LABELS
- CUSTOM_CONTAINERS_RESTRICT_ALPHA_BETA

**Policy type: Containers**

### Setup Process📝
1. Clone the project: ```https://github.com/Snehomoy100/Cloud-Native-Hackathon-2021.git```
2. Then go to ```cd Cloud-Native-Hackathon-2021``` ->```cd api```
3. Set up the virtual environment using ```source env/bin/activate```
4. Install the required modules ```pip install -r requirements.txt```

### Docker🐋
By default, the Docker will expose port 5000, so change this within the
Dockerfile if necessary. When ready, simply use the Dockerfile to
build the image.
```sh
cd api
docker build -t imageonhack .
```

### Workflow of our project
![Workflow](https://user-images.githubusercontent.com/57084217/145702783-aec4a53c-3a07-407d-bd72-f7b097948d2b.PNG)
