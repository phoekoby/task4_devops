# Task4-5-DEVOPS



Procedure: 
1. Install Lens, minikube
2. Start minikube: `$minikube start;`
3. Create new repo in [docker hub](https://hub.docker.com "Docker hub link")
4. Create image: `docker build -t task4`
5. Push image on [docker hub](https://hub.docker.com "Docker hub link") `docker push <myusername>:task4:latest`
6. Deploy pod: `kubectl run task4 --image=<myusername>/task4:latest --port=5000`
7. Configure ports: `kubectl port-forward task4 8080:5000`

If you have smth like that:
![ScreenShot](/img/task4_1.jpg "ScreenShot-1")
![ScreenShot](/img/task4_2.jpg "ScreenShot-2")
## Congratulations you run your app!
