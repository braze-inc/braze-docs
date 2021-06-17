---
nav_title: Amazon Personalize
alias: /partners/amazon_personalize/

description: "This article outlines a reference architecture for and integration between Braze and Amazon Personalize."
page_type: partner

---

# Amazon Personalize

> Amazon Personalize is like having your very own Amazon.com machine learning recommendation system, 24 hours a day. Based on over 20 years of recommendation experience, Amazon Personalize enables you to improve customer engagement by powering real-time personalized product and content recommendations, and targeted marketing promotions. 

Using machine learning, Amazon Personalize creates higher-quality recommendations for your websites and applications. You can get started without any prior machine learning experience using simple APIs to easily build sophisticated personalization capabilities in just a few clicks. Amazon Personalize will process and examine your data, identify what is meaningful, allow you to pick a machine learning algorithm, and train and optimize a custom model based on your data. 

This article will walk you through the process of configuring Amazon Personalize and integrating it into your Braze environment using Connected Content. This is done using a hands-on workshop that will walk you through all the steps required to deploy and train Amazon Personalize solutions, and then to integrate these solutions into a Braze email campaign using Connected Content. These examples are deployed in a fully-functional example eCommerce site called the Retail Demo Store. The resources and code for this tutorial are published in the [AWS Samples Retail Demo Store](https://github.com/aws-samples/retail-demo-store/). You can use this reference architecture implementation as an outline to implement Amazon Personalize in your own environment.

# Prerequisites

You will need to clone the [Retail Demo Store repo](https://github.com/aws-samples/retail-demo-store/) and follow the steps outlined below to deploy the workshop environment to your AWS account. An AWS account is required to complete the workshop and to run the integration code.

# Integration Architecture

Before you set up Braze to send personalized messages to users, let's review the relevant components required for a typical eCommerce website, using the Retail Demo Store architecture as an example.

![Braze Personalization Architecture][1] 

Braze will send emails to your users based on their behavior or based on attributes of their user profiles. This data can be used to identify users and to build user profiles that can be used to determine when to send a message or email. 

This event data flow will happen in parallel to the same behavioral event data being sent to Amazon Personalize. In this workshop, the demo store uses Amplify to send events to Personalize as shown in the diagram. This data is used to train a recommendations model that can in turn be used by Braze Connected Content to personalize content to users of your mobile and web applications when your Braze campaign runs. 

Braze Connected Content will be able to get these recommendations via a recommendation service running in AWS. The Retail Demo Store workshop shows an example recommendation service deployment. In a deployment scenario in your own infrastructure, you will need to deploy a similar service in order to get items from your own catalog service.

# Setting up the Reference Architecture Workshop

## Step 1: Deploy the Retail Demo Store to your AWS Account

![Choose AWS Region][2]{: style="float:right;max-width:40%;margin-top:15px;margin-bottom:10px;"}

In the following table, choose an **AWS Region** and select **Launch Stack**. This list does not represent all the possible regions where you can deploy the project, only the ones that are currently configured for deployment with the Retail Demo Store.

Accept all the default parameter values for the template. The deployment of all the project resources should take 25-30 minutes.

## Step 2: Build Amazon Personalize Campaigns

Before you can provide personalized product recommendations, you first need to train the machine learning models and provision the inference endpoints that will allow you to get recommendations from Amazon Personalize. The CloudFormation template deployed in Step 1 includes an Amazon SageMaker notebook instance that provides a Jupyter notebook with detailed step-by-step instructions.

1. Sign in to the AWS account where you deployed the AWS CloudFormation template in Step 1.
2. On the Amazon SageMaker console, choose Notebook instances.
3. If you don't see the **RetailDemoStore** notebook instance, make sure you are in the same region where you deployed the project in Step 1.
4. To access the notebook instance, choose **Open Jupyter** or **Open JupyterLab**.
5. When the Jupyter web interface is loaded for the notebook instance, choose the `workshop/1-Personalization/1.1-Personalize.ipynb` notebook. You may have to choose the `workshop` folder to see the notebook subdirectories.
6. When you have the `1.1-Personalize` notebook open, step through the workshop by executing each cell. You can choose **Run** from the Jupyter toolbar to sequentially execute the code in the cells. The notebook takes approximately 2 hours to complete.

## Step 3: Send Personalized Emails from Braze

With the Amazon Personalize solutions and campaigns in place, your instance of the Retail Demo Store is ready to provide recommendations to your email campaigns. In Step 1 you also deployed the environment that contains the Retail Demo Store web application, and all associated services, including the recommendation service that you will need to integrate your email campaigns with Braze using Connected Content (which will use the Amazon Personalize campaigns you deployed in Step 2). 

Similar to the Personalization workshop in Step 2, there is a Braze messaging workshop that steps you through the process of setting up the Braze / Amazon Personalize integration.

1. Sign in to the AWS account where you deployed the AWS CloudFormation template in Step 1.
2. On the Amazon SageMaker console, choose **Notebook Instances**.
3. If you don't see the **RetailDemoStore** notebook instance, make sure you are in the same AWS region where you deployed the project.
4. To access the notebook instance, choose **Open Jupyter** or **Open JupyterLab**.
5. When the Jupyter web interface is loaded for the notebook instance, choose the `workshop/4-Messaging/4.2-Braze.ipynb` notebook. You may have to choose the `workshop` folder to see the notebook subdirectories.
6. When you have the `4.2-Braze` notebook open, step through the workshop by executing each cell. You can choose **Run** from the Jupyter toolbar to sequentially execute the code in the cells. The notebook takes approximately 1 hour to complete. 

## Step 4: Clean up Resources

To avoid incurring future charges, delete the AWS resources the Retail Demo Store project created by deleting the AWS CloudFormation stack you created in Step 1.

[1]: {% image_buster /assets/img/amazon_personalize/braze-personalize-arch.png %}
[2]: {% image_buster /assets/img/amazon_personalize/region.png %}