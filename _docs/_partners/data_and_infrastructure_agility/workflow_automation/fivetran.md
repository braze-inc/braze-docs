---
nav_title: Fivetran
article_title: Fivetran
alias: /partners/fivetran/
description: "This article outlines the partnership between Braze and Fivetran, a workflow automation tool that can assist you in data-backed decision making by delivering ready-to-query data into your cloud warehouse."
page_type: partner
search_tag: Partner

---

# Fivetran

[Fivetran](https://fivetran.com/) is a globally recognized brand whose analyst focused products and fully managed pipelines enable data-backed decisions by delivering ready-to-query data into your cloud warehouse. Now, as Braze's new technology partner, data-backed decision making has been made easier and more efficient than ever before, allowing you to spend more time on the difficult tasks.

## Prerequisites

Requirement   |Source| Notes
--------------|------|-------------
Braze Account    | [Braze](https://dashboard.braze.com/sign_in) | This account should have at least one active subscription and admin privileges. |
Fivetran Account | [Fivetran](https://fivetran.com/login?next=%2Fdashboard)| This Fivetran account should have owner/admin privileges. |
Braze Currents    | [Braze Currents](https://www.braze.com/product/data-agility-management/currents/)  | Currents should be connected to one of the following cloud storage services: <br> **Amazon S3** or **Google Cloud Storage**. |
Braze API URL    | [Braze](https://dashboard.braze.com/sign_in) | Found in your Braze account.
Braze API Key    | [Braze](https://dashboard.braze.com/sign_in) | Found in your Braze account.

## Integration

### Setting up Braze Current

{% tabs %}
{% tab Amazon S3 %}

### Step 1: Locate your external ID

Locate your External ID in the Fivetran setup form for Braze.
![Fivetran Connector setup form]({% image_buster /assets/img/fivetran_braze_setupform_as3.png %})

{% alert note %} 
Note the **External ID** as depicted above. The remaining details required to complete the setup will be retrieved in later steps. 
{% endalert %}

### Step 2: Create a Braze API key for Amazon S3 storage

Next, login to your dashboard [here](https://dashboard.braze.com) or with your [designated dashboard URL]({{site.baseurl}}/api/basics?redirected=true#endpoints) and click **Developer Console** on the bottom left corner of the Braze dashboard.

![Braze Dashboard]({% image_buster /assets/img/fivetran_braze_developer_console.png %})

From here, [create an API Key]({{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys) for Fivetran and enable the following permissions for said key:

* users.export.ids
* users.export.segment
* email.unsubscribe
* email.hard_bounces
* messages.schedule_broadcasts
* campaigns.list
* campaigns.details
* canvas.list
* canvas.details
* segments.list
* segments.details
* purchases.product_list
* events.list
* feed.list
* feed.details
* templates.email.info
* templates.email.list
* subscription.status.get
* subscription.groups.get

Lastly, take note of the created API key before proceeding because it will be required in Step 4.

### Step 3: Give Fivetran access to a specified S3 bucket

#### Creating an IAM policy

Open the [Amazon IAM Console](https://console.aws.amazon.com/iam/home#home) and navigate to **Policies->Create Policy** as shown below.

![Amazon S3 Policies]({% image_buster /assets/img/fivetran_as3_iam.png %})

Then, navigate to the **JSON** tab.

![Amazon S3 Json Policy]({% image_buster /assets/img/fivetran_iam_policy_json.png %})

Copy the policy below, replacing **{your-bucket-name}** with the name of your s3 bucket:

{% raw %}
```json
{
"Version": "2012-10-17",
"Statement": [
    {
      "Effect": "Allow",
      "Action": [
"s3:Get*",
"s3:List*"
      ],
      "Resource": "arn:aws:s3:::{your-bucket-name}/*"
    },
    {
      "Effect": "Allow",
      "Action": [
"s3:Get*",
"s3:List*"
      ],
      "Resource": "arn:aws:s3:::{your-bucket-name}"
    }
  ]
}
```
{% endraw %}

Now, click the **Review Policy** button to make any final changes before setup.

![Amazon S3 Policy Review Button]({% image_buster /assets/img/fivetran_iam_policy_review.png %})

Here, give the policy a unique name (something like "Fivetran-S3-Access") and an optional description before clicking the **Create Policy** button.

![Amazon S3 Policy Review Button]({% image_buster /assets/img/fivetran_iam_policy_meta.png %})

#### Create an IAM role

Navigate to **Roles**, then select **Create New Role**.

![Amazon S3 IAM New Role]({% image_buster /assets/img/fivetran_iam_new_role.png %})

Select **Another AWS Account**, then click the checkbox for **Require external ID**.

![Amazon S3 Require External ID]({% image_buster /assets/img/fivetran_another_aws_account.png %})

Here, enter the Fivetran account ID, ``834469178297``, and the ``External ID`` which was found in the  Fivetran Braze S3 connection setup form during Step 1.

![Amazon S3 Input External ID]({% image_buster /assets/img/fivetran_as3_external_id.png %})

Click **Next: Permissions**, and now select the policy that you created earlier (ie, "Fivetran-S3-Access").

![Amazon S3 Select Policy]({% image_buster /assets/img/fivetran_as3_select_policy.png %})

Lastly, click **Next: Review**, name your new role (i.e., Fivetran), and click **Create Role**.

#### Locating the IAM role ARN

Click on the role you just created, or navigate to **Roles** from your [Amazon IAM Console](https://console.aws.amazon.com/iam/home#home).
![Amazon S3 IAM Role ARN]({% image_buster /assets/img/fivetran_iam_role_arn.png %})

{% alert note %}
You can specify permissions for the Role ARN that you designate for Fivetran. Giving selective permissions to this Role will allow Fivetran to only sync what it has permissions to see.
{% endalert %}

{% endtab %}
{% tab Google Cloud Storage %}

### Step 1: Retrieve your Fivetran email from Google Cloud Storage

Locate your Fivetran email in the Fivetran setup form for Braze by logging into your [Fivetran Dashboard](https://fivetran.com/dashboard), clicking on **+ Connector** selecting **Braze** and selecting **Azure Blob storage** as the ``Cloud Storage`` option.

![Fivetran Connector setup form]({% image_buster /assets/img/fivetran_braze_setupform_gcs.png %})

### Step 2: Create a Braze API key for Google Cloud Storage

Next, login to your Braze account [here](https://dashboard.braze.com) or with your [designated dashboard URL]({{site.baseurl}}/api/basics?redirected=true#endpoints) and click **Developer Console** on the bottom left corner of the Braze dashboard.

![Braze Dashboard]({% image_buster /assets/img/fivetran_braze_developer_console.png %})

From here, [create an API Key]({{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys) for Fivetran and enable the following permissions for said key:

* users.export.ids
* users.export.segment
* email.unsubscribe
* email.hard_bounces
* messages.schedule_broadcasts
* campaigns.list
* campaigns.details
* canvas.list
* canvas.details
* segments.list
* segments.details
* purchases.product_list
* events.list
* feed.list
* feed.details
* templates.email.info
* templates.email.list
* subscription.status.get
* subscription.groups.get

Lastly, take note of the created API key before proceeding because it will be required in Step 4.

### Step 3: Authorization

Navigate to your [Google Storage Console](https://console.cloud.google.com/storage/browser) and select a bucket which you configured Braze Currents with and click on **Edit bucket permissions**.

After clicking **Edit bucket permissions**, grant ``Storage Object Viewer`` access to the email from Step 1 by adding the email as a member.

![Google Storage Bucket Add Member]({% image_buster /assets/img/fivetran_add_members_gcs.png %})

Lastly, navigate to your [Google Cloud Storage Consle](https://console.cloud.google.com/storage?pli=1) and take note of the bucket name as it will be needed in during the final setup steps.

![Google Storage Buckets]({% image_buster /assets/img/fivetran_edit_bucket_permissions_gcs.png %})
{% endtab %} {% endtabs %}

## Final steps

After logging into your [Fivetran Dashboard](https://fivetran.com/dashboard), click on **+ Connector** found at the top right corner of the screen and select the **Braze** connector to launch the setup form. Within the form, fill the given fields with the appropriate values:

{% tabs %}
{% tab Amazon S3 %}

``Destination schema``: Choose a unique schema name.

``API URL``: Your assigned API URL found during the Braze Currents setup process.

``API Key``: The API Key noted during the Braze Currents setup process.

``External ID``: Fixed value. Use this ID to setup IAM role in Step 3 of the Braze Currents setup process.

``Bucket``: Found within your Braze Dashboard by navigating to **Integration > Currents > `your-current-name`**.

``Role ARN``: See Step 3 of the Braze Currents setup process.

{% alert important %}
Ensure **Amazon S3** is selected as the ``Cloud Storage`` choice.
{% endalert %}

{% endtab %}
{% tab Google Cloud Storage %}

``Destination schema``: A unique schema name.

``API URL``: your assigned API URL found in Step 2 of the Braze Currents setup process.

``API Key``: The key you noted in Step 2 of the Braze Currents setup process.

``Bucket name``: Found within your Braze account by navigating to **Integration > Currents > `your-current-name` > `Bucket Name`**.

``Folder``: Found within your Braze account by navigating to **Integration > Currents > `your-current-name` > `Prefix`**

{% alert important %}
Ensure **Google Cloud Storage** is selected as the ``Cloud Storage`` choice.
{% endalert %}

{% endtab %}
{% endtabs %}

Lastly, click **Save & Test** and Fivetran will do the rest by syncing with the data from your Braze account!
