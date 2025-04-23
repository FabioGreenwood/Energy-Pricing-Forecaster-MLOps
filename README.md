# Project Overview

Personal project to create a **MLOps pipeline** for a home energy price forecaster. Currently the focus of this project is the **data/cloud engineering** and the ML model is a basic placeholder (due to time constraints), though there is a view to expand it going forward.

**CI/CD** pipeline will be deployed in **AWS**, using **code-as-infrastructure (CID)** via **terraform**. The ML model will be deployed via **docker**.

# Model Functionality
The model will forecast home energy prices. It will be trained on historical home energy prices and weather data. Seasonality, the potential for weather forecast error and other factors will also be considered. 

Once trained the model will provide a price forecast based on the recent prices, time-of-year and weather and forecast weather data.

The model will also have various automated features such as **live performance monitoring, periodic retraining, model logging and a A/B champion model system**.

The model will likely be an **RNN** using **keras** and **tensorflow**. However, it should be again noted that the focus of this project currently is the data/cloud engineering and not the actual model itself.

# CI/CD Environments
There will be various environments used for the project:

- feature/
  - No name enforcement
  - these will be branches for the development of features

- offline-testing/
  - Once a feature is complete, it must be committed to the offline testing branch, this will test that the changes from a feature will not cause any offline tests to fail

- live-testing/
  - Once various new features have been implemented into the offline-testing branch, it can be committed up to the live-testing branch
  - This will run additional tests that can only be achieved through deploying a working copy of the new app version to a separate AWS VPC (virtual private cloud).

- prod/
  - This branch will deploy the fully tested new version of the functionality to the cloud
  - Data will remain persistent through this process as default.


# Summary
The project will include the following technologies/techniques:
-	AWS
-	Docker
-	Terraform
-	Code-as-Infrastructure (CID)
-	Continuous Integration and Deployment (CI/CD)
-	RNN, Keras, Tensorflow
-	Spark/PySpark (2nd phase target)


# Project Team
- Fabio Greenwood
- Andrew Rudge
