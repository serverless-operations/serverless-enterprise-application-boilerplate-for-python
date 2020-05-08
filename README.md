[![serverless](http://public.serverless.com/badges/v3.svg)](http://www.serverless.com)  [![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE) [![CircleCI](https://circleci.com/gh/serverless-operations/serverless-enterprise-application-boilerplate-for-python/tree/master.svg?style=svg)](https://circleci.com/gh/serverless-operations/serverless-enterprise-application-boilerplate-for-python/tree/master)

# Serverless Enterprise Application Boilerplate For Python
This is a boilerplate to build an AWS serverless enterprise application. In general, a serverless application is composed of some CloudFormation stacks. This repository shows you all the things which build that like how to separate each stack and build a directory structure using Serverless Framework, Python, and CircleCI.

## Deploy image
Deploy this app to AWS using Serverless Framework via CircleCI.

<img src="https://raw.githubusercontent.com/serverless-operations/serverless-enterprise-application-boilerplate-for-python/master/service.png" alt="Architecture" width="50%;">

## Directory Structure

| Directory | Description |
|:---|:---|
|layer |Lambda layers. Put Python external libraries and common libraries that can use each service. |
|lib |Common libraries that can use each service. |
|services/api |API Service which a part of this application. Here is [the architecture](https://github.com/serverless-operations/serverless-enterprise-application-boilerplate-for-python/tree/master/services/api) |
|services/workflow |API Service which a part of this application. Here is [the architecture](https://github.com/serverless-operations/serverless-enterprise-application-boilerplate-for-python/tree/master/services/workflow-service) |
|services/message-service |Message Service which a part of this application. Here is [the architecture](https://github.com/serverless-operations/serverless-enterprise-application-boilerplate-for-python/tree/master/services/message-service) |
|services/stream-service |Stream Service which a part of this application. Here is [the architecture](https://github.com/serverless-operations/serverless-enterprise-application-boilerplate-for-python/tree/master/services/stream-service) |
|tests/unit_tests |Put unit tests. |
|tests/integration_tests |Put E2E tests. |

## Commands

All commands you need to build this application is defined as yarn script.
Here is a part of that.
| Command | Description |
|:---|:---|
| yarn lint | Run lint with flake8. |
| yarn test:unit | Run unit testing. |
| yarn test:workflow | Run E2E testing for workflow service. |
| yarn deploy:workflow | Deploy workflow service. |
| yarn deploy:db | Deploy tables. |

All commands are defined in [package.json](https://github.com/serverless-operations/serverless-enterprise-application-boilerplate-for-python/blob/master/package.json). See that.

## Setup

You can use this boilerplate as a skeleton to build your serverless application. First, check out the code and remove `.git` directory so that you can put it in your repository.

```
$ git clone git@github.com:serverless-operations/serverless-enterprise-application-boilerplate-for-python.git
$ cd serverless-enterprise-application-boilerplate-for-python
$ rm -rf .git
$ yarn install
```

Setup needed environment valiables  via `direnv`.
```
$ cp -pr .envrc.sample .envrc
$ vi .envrc # edit

# allow
$ direnv allow
```

Install Python external libraries to develop into `venv`.
```
$ python3 -m venv venv
$ . venv/bin/activate
$ pip3 install -r requirements-dev.txt
```

Run deploy API to see this setup successfully.
```
$ yarn deploy:api
```

## AWS Account

This boilerplate supposes to use two AWS accounts, which are for production and other than that.
You can switch AWS accounts to deploy using the CircleCI context feature.

<img src="https://raw.githubusercontent.com/serverless-operations/serverless-enterprise-application-boilerplate-for-python/master/accounts.png" alt="Accounts" width="50%;">
