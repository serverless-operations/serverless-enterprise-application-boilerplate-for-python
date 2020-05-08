# Serverless Enterprise Application Boilerplate For Python
This is a boilerplate to build an AWS serverless enterprise application. In general, a serverless application is composed of some CloudFormation stacks. This repository shows you all the things which build that like how to separate each stack and build a directory structure with using Serverless Framework, Python and CircleCI.

## Deploy image
Deploy apps to AWS with using Serverless Framework via CircleCI.

<img src="https://raw.githubusercontent.com/serverless-operations/serverless-enterprise-application-boilerplate-for-python/master/service.png" alt="Architecture" width="50%;">

## Directory Structure

| Directory | Description |
|:---|:---|
|layer |Lambda layers. Put Python external libraries and common libraries which can use each service. |
|lib |Common libraries which can use each service. |
|services/api |API Service which a part of this application. Here is [the architecture](https://github.com/serverless-operations/serverless-enterprise-application-boilerplate-for-python/tree/master/services/api) |
|services/workflow |API Service which a part of this application. Here is [the architecture](https://github.com/serverless-operations/serverless-enterprise-application-boilerplate-for-python/tree/master/services/workflow-service) |
|services/message-service |Message Service which a part of this application. Here is [the architecture](https://github.com/serverless-operations/serverless-enterprise-application-boilerplate-for-python/tree/master/services/message-service) |
|services/stream-service |Stream Service which a part of this application. Here is [the architecture](https://github.com/serverless-operations/serverless-enterprise-application-boilerplate-for-python/tree/master/services/stream-service) |
|tests/unit_tests |Put unit tests. |
|tests/integration_tests |Put E2E tests. |



## Setup
