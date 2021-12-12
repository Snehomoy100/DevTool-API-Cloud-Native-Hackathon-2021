# _CloudNativeHackathon2021_

**NAME OF THE PROJECT:** DEVTOOL API

**Video Demo of the project**
[![Watch the video](https://i9.ytimg.com/vi/DNmgIxrbZkA/mq2.jpg?sqp=CNS22I0G&rs=AOn4CLBjzG64OkmN5FVHOhh0FePgaOrsiQ)](https://youtu.be/DNmgIxrbZkA)

![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## **Programming languages & Tools used**: 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/githubactions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

## Sponsor Tools used:
[Datree.io](https://github.com/datreeio/datree)

[Devtron](https://github.com/devtron-labs/devtron)

[Civo](https://www.civo.com/docs)

### About the project⭐
Using Kubernetes production best policies to run the k8s manifest files through [Datree.io](https://github.com/datreeio/datree) to prevent Kubernetes misconfigurations from ever reaching production.
- Clusters are created using Kubernetes in Civo
- DevOps(Configurations, etc)
- Flask API integration
- Python runs Datree commands and POST request to API
- Metrics and logs of the configurations are checked using Grafana (Devtron)
- Notification to the user using Twilio

**Pull request to Datree**: [PRtoDatree](https://github.com/datreeio/datree/pull/332)

**Reference**: [Kubernetes production best policies](https://github.com/learnk8s/kubernetes-production-best-practices)

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
5. **Directory** will look as follows: 

![directory](https://user-images.githubusercontent.com/57084217/145708872-9e2e8c85-cbf8-40fc-b2b2-690dfc5b4e48.PNG)


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
