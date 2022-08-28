# Layer 4 Load balancing using mysql flask and nginx

This project is a demonstration of using nginx as a layer 4 load balancer for a python based web app and mysql. This project is created using docker compose. 

There are 3 folders `mysql`, `python-webserver` and `nginx-load-balancer` that contains the necessary compose files. We'll see details of these files later on.

## Steps 

- Create 3 vpc
- Create vpc peering between 
    - VPC Nginx and VPC Webapp
    - VPC Nginx and VPC Database
- Create 1 vm instance in each vpc
- Create firewall rules for each instance 
- Install necessary packages in each instance
- Clone this repository in all 3 instances 
- Run `mysql`, `python-webserver` and `nginx-load-balancer` in each instance using `docker-compose`
- Test the setup

## Component Diagram

![component diagram](assets/load-balancer-diagram.png)
