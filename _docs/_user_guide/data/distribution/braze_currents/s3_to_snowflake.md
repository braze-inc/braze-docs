---
nav_title: Transferring data from Amazon S3 to Snowflake
article_title: Transferring Data from Amazon S3 to Snowflake
page_order: 7
page_type: tutorial
description: "This how-to article will walk you through transferring data from cloud storage (like Amazon S3) to a warehouse (like Snowflake) using the Extract, Transform, Load (ETL) process."
tool: Currents

---

# Transferring data from Amazon S3 to Snowflake

> If your data currently sits in Amazon S3, you can transfer it to Snowflake or another relational data warehouse using the Extract, Load, Transform (ELT) process. This page covers how to do so.

{% alert note %}
If you have more specific use cases and would like Braze to service your Currents instance, contact your Braze account manager and ask them about Braze Data Professional Services.
{% endalert %}

## How it works

The Extract, Load, Transform (ELT) process is an automated process that moves data into [Snowflake](https://www.snowflake.com/), which will allow you to use the [Braze Looker Blocks](https://marketplace.looker.com/marketplace/directory) to visualize that data in Looker to help drive insights and feedback into your campaigns, Canvases, and segments.

After you have a Currents to S3 export set up and are receiving live events data, you can configure your live ELT pipeline in Snowflake by configuring the following components:

-   [AWS SQS queues](#aws-sqs-queues)
-   [Auto-Ingest Snowpipes](#auto-ingest-snowpipes)

## Configuring AWS SQS queues

**Auto-ingest Snowpipes** rely on SQS queues for sending notification from S3 to Snowpipe. This process is managed by Snowflake after configuring SQS.

### Step 1: Configure the external S3 stage

{% alert note %}
Tables in your database are created in this stage.
{% endalert %}

1. When you set up Currents in Braze, specify a folder path for your Currents files to follow into your S3 bucket. Here we use ```currents```, the default folder path.

2. Create the following in the listed order:
  2.1 In AWS, create a new **public-private key pair** for the desired S3 bucket, with grants according to your organization's security requirements.
  2.2. In Snowflake, create a database and schema of your choice (named ```currents``` and ```public``` in the following example).
  2.3. Create a Snowflake S3 Stage (called `braze_data`):

```sql
CREATE OR REPLACE STAGE
    currents.public.braze_data
    url='s3://snowpipe-demo/'
    credentials = (AWS_KEY_ID = '...' AWS_SECRET_KEY = '...' );
show stages;
```

{: start="3"}
3. Define the AVRO file format for your stage.

```sql
CREATE FILE FORMAT
    currents.public.currents_avro
    type = 'avro'
    compression = 'auto';
```

```sql
ALTER STAGE
    currents.public.braze_data
SET
    file_format = currents.public.currents_avro;
```

```sql
CREATE OR REPLACE PIPE
  pipe_users_messages_pushnotification_open
    auto_ingest=true AS

COPY INTO
  users_messages_pushnotification_open
          FROM
           (SELECT
             $1:id::STRING,
             $1:user_id::STRING,
             $1:external_user_id::STRING,
              $1:time::INT,
              $1:timezone::STRING,
              $1:app_id::STRING,
              $1:campaign_id::STRING,
              $1:campaign_name::STRING,
              $1:message_variation_id::STRING,
              $1:canvas_id::STRING,
              $1:canvas_name::STRING,
              $1:canvas_variation_id::STRING,
              $1:canvas_step_id::STRING,
              $1:canvas_step_message_variation_id::STRING,
              $1:platform::STRING,
              $1:os_version::STRING,
              $1:device_model::STRING,
              $1:send_id::STRING,
              $1:device_id::STRING,
              $1:button_action_type::STRING,
              $1:button_string::STRING

              FROM
@currents.public.braze_data/currents/dataexport.prod-01.S3.integration.INTEGRATION_ID_GOES_HERE/event_type=users.messages.pushnotification.Open/);
```

{: start="4"}
4. Finally, use the `show pipes;` command to show your SQS information. The name of the SQS queue will be visible in a new column called `NOTIFICATION_CHANNEL` because this pipe was created as an auto-ingest pipe.

### Step 2: Create bucket events

1. In AWS, navigate to the corresponding bucket of the new Snowflake stage. Then, under the **Properties** tab, go to **Events**.

![AWS Properties tab]({% image_buster /assets/img/aws-properties.png %}){: height="50%" width="50%"}

{: start="2"}
2. Create new events for each set of Currents Data, as needed ([Messaging]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/), [User Behavior]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/)), or both.

![Creating a new event in AWS]({% image_buster /assets/img/aws-events.png %}){: height="50%" width="50%"}

{: start="3"}
3. Check the appropriate box for the object create notifications, as well as the ARN on the bottom of the form (from the notification channel column in Snowflake).

## Configuring auto-ingest Snowpipes {#auto-ingest-snowpipes}

For the AWS SQS configuration to produce the correct tables, you must define the structure of the incoming data properly by using the following examples and schemas determined in our Currents documentation for [Message Engagement or Messaging Events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/), [User or Customer Behavior Events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/), or both.

It is critical to structure your tables in accordance with the Braze Currents schemas, as Braze Currents will continuously load data into them through specific fields with specific data types. For example, a `user_id` will be loaded as a string and called a `user_id` in Currents data.

{% alert note %}
  Depending on your Currents integration, you may have different events you must set up (such as [Message Engagement or Messaging Events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) and [User or Customer Behavior Events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/)). You can also write a script for some or all of this process.
{% endalert %}

{% tabs %}
  {% tab User Behavior Events %}

1. Create a table `INTO` which we will continuously load using the following structure from the Currents schema:

```sql
CREATE TABLE
  users_behaviors_app_firstsession (
        id               STRING,
        user_id          STRING,
        external_user_id STRING,
        app_id           STRING,
        time             INT,
        session_id       STRING,
        gender           STRING,
        country          STRING,
        timezone         STRING,
        language         STRING,
        device_id        STRING,
        sdk_version      STRING,
        platform         STRING,
        os_version       STRING,
        device_model     STRING
    );
```

{: start="2"}
2. Create the `auto_ingest` pipe and specify:
  2.1. Which table to load
  2.2 How to load the following table

```sql
CREATE OR REPLACE PIPE
  pipe_users_behaviors_app_firstsession
    auto_ingest=true AS

COPY INTO
  users_behaviors_app_firstsession
          FROM
            (SELECT
              $1:id::STRING,
              $1:user_id::STRING,
              $1:external_user_id::STRING,
              $1:app_id::STRING,
              $1:time::INT,
              $1:session_id::STRING,
              $1:gender::STRING,
              $1:country::STRING,
              $1:timezone::STRING,
              $1:language::STRING,
              $1:device_id::STRING,
              $1:sdk_version::STRING,
              $1:platform::STRING,
              $1:os_version::STRING,
              $1:device_model::STRING

              FROM
@currents.public.braze_data/currents/dataexport.prod-01.S3.integration.INTEGRATION_ID_GOES_HERE/event_type=users.behaviors.app.FirstSession/);
```

{% alert warning %}
You must repeat the `CREATE TABLE` and `CREATE PIPE` commands for every event type.
{% endalert %}

 {% endtab %}
 {% tab Messaging Events %}

1. Create a table `INTO` which we will continuously load using the following structure from the Currents schema:

```sql
CREATE TABLE
    public_users_messages_pushnotification_open (
        id STRING,
        user_id STRING,
        external_user_id STRING,
        time INT,
        timezone STRING,
        app_id STRING,
        campaign_id STRING,
        campaign_name STRING,
        message_variation_id STRING,
        canvas_id STRING,
        canvas_name STRING,
        canvas_variation_id STRING,
        canvas_step_id STRING,
        canvas_step_message_variation_id STRING,
        platform STRING,
        os_version STRING,
        device_model STRING,
        send_id STRING,
        device_id STRING,
        button_action_type STRING,
        button_string STRING
        );
```

{: start="2"}
2. Create the AUTO continuous load pipe and specify:
  2.1. Which table to load
  2.2 How to load the following table

```sql
CREATE OR REPLACE PIPE
  pipe_users_messages_pushnotification_open
    auto_ingest=true AS

COPY INTO
  users_messages_pushnotification_open
          FROM
           (SELECT
             $1:id::STRING,
             $1:user_id::STRING,
             $1:external_user_id::STRING,
              $1:time::INT,
              $1:timezone::STRING,
              $1:app_id::STRING,
              $1:campaign_id::STRING,
              $1:campaign_name::STRING,
              $1:message_variation_id::STRING,
              $1:canvas_id::STRING,
              $1:canvas_name::STRING,
              $1:canvas_variation_id::STRING,
              $1:canvas_step_id::STRING,
              $1:canvas_step_message_variation_id::STRING,
              $1:platform::STRING,
              $1:os_version::STRING,
              $1:device_model::STRING,
              $1:send_id::STRING,
              $1:device_id::STRING,
              $1:button_action_type::STRING,
              $1:button_string::STRING

              FROM
@currents.public.braze_data/currents/dataexport.prod-01.S3.integration.INTEGRATION_ID_GOES_HERE/event_type=users.messages.pushnotification.Open/);
```

{% alert warning %}
You must repeat the `CREATE TABLE` and `CREATE PIPE` commands for every event type.
{% endalert %}

  {% endtab %}
{% endtabs %}

To see the types of analytics you can perform using Braze Currents, consult our [Looker Blocks](https://github.com/llooker?q=braze).

{% alert note %}
Contact your Braze account manager if you have any questions or if you're interested in having Braze guide you through this process.
{% endalert %}

