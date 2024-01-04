# Dash Dashboard Demo
This repository contains a sample application built with [Dash](https://plotly.com/dash/), a Python framework for building analytical web applications.

This project is intented to demonstrate how to set up and deploy a Dash application on AWS, and could be used as a basic template to accelerate development. The sample Dash application included is deliberately simple, designed to serve as a starting point. You can extend and modify this basic application to suit your specific requirements, adding more complex features and functionalities as needed.

This application is deployed using AWS Elastic Beanstalk, a fully managed service that makes it easy to deploy and run applications in multiple languages. The AWS infrastructure is created using a combination of terraform and the Elastic Beanstalk CLI.


## Setup Instructions
**Prerequisites**: These instructions are for Unix-like systems. You should have permissions to create and manage resources in AWS.

### AWS CLI
Install [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [configure](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) with your AWS credentials.

You can verify the AWS CLI is installed correctly with this command:
```
aws sts get-caller-identity
```
### Terraform
Install [terraform](https://developer.hashicorp.com/terraform/install) and verify the installation  with:
```
terraform --version
```

### Repository Setup
Clone this repository and navigate into it:
```
git clone git@github.com:JacobNorman/dash-dashboard-demo.git
```
```
cd dash-dashboard-demo/
```
 ### Python Environment
Create virtual environment and activate it: 
```
python -m venv venv
```
```
source venv/bin/activate
```

Install the necessary Python packages:
```
pip install -r requirements.txt
```

### Infrastructure Setup
Initialize Terraform and create the infrastructure:
```
terraform init
```
```
terraform plan
```
```
terraform apply
```

Then, set up the Elastic Beanstalk environment:
```
eb init
```
During the initialization:
* Select your preferred region.
* Enter the application name as shown in the Terraform output.
* When asked `Do you wish to continue with CodeCommit?`, enter `n`.

Next create the Elastic Beanstalk environment:
```
eb create
```
During the creation process:
* Use default Environment Name, DNS CNAME prefix, and load balancer type.
* When asked `Would you like to enable Spot Fleet requests for this environment? (y/N):`, select `N`.

The application should now be running at the URL provided in the terminal logs. You can also find the URL in the AWS Console under the Elastic Beanstalk section.

## Clean up
When you're done, you can destroy the infrastructure to avoid incurring further costs:
```
terraform destroy
```