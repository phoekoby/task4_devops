Task4-5-DEVOPS
Procedure:

Install Lens, minikube
Start minikube: $minikube start;
Create new repo in docker hub
Create image: docker build -t task4
Push image on docker hub docker push <myusername>:task4:latest
Deploy pod: kubectl run task4 --image=<myusername>/task4:latest --port=5000
Configure ports: kubectl port-forward task4 8080:5000
If you have smth like that: ScreenShot ScreenShot

Congratulations you run your app!
