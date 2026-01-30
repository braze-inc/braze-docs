---
nav_title: Amazon S3
article_title: Amazon S3
alias: /partners/amazon_s3/
description: "This reference article outlines the partnership between Braze and Amazon S3, a highly scalable storage system offered by Amazon Web Services."
page_type: partner
search_tag: Partner

---

# Amazon S3

> [Amazon S3](https://aws.amazon.com/s3/) is a highly scalable storage system offered by Amazon Web Services.

{% alert important %}
클라우드 스토리지 제공업체 간에 전환하는 경우, 새로운 통합을 설정하고 검증하는 데 대한 추가 지원을 받으려면 Braze 고객 성공 매니저에게 문의하세요.
{% endalert %}

The Braze and Amazon S3 integration features two integration strategies:

- Leverage [Currents]({{site.baseurl}}/user_guide/data/braze_currents/), enabling you to store data there until you want to connect it to other platforms, tools, and locations.
- Use dashboard data exports (such as CSV exports and engagement reports).

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Amazon S3 account | 이 파트너십을 이용하려면 Amazon S3 계정이 필요합니다. |
| Dedicated S3 bucket | Before integrating with Amazon S3, you must create an S3 bucket for your app.<br><br>If you already have an S3 bucket, we still recommend creating a new bucket specifically for Braze so you can limit permissions. Refer to the following instructions on how to create a new bucket. |
| Currents | 데이터를 Amazon S3로 다시 내보내려면 계정에 [Braze 커런츠가]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) 설정되어 있어야 합니다. 메시지 보관만 설정하는 경우에는 커런츠가 필요하지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Creating a new S3 bucket

To create a bucket for your app, do the following:

1. Open the [Amazon S3 console](https://console.aws.amazon.com/s3/) and follow the instructions to **Sign in** or **Create an Account with AWS**. 
2. 로그인한 후 **스토리지 & 콘텐츠 전달** 카테고리에서 **S3를** 선택합니다. 
3. Select **Create Bucket** on the next screen. 
4. 버킷을 만들고 지역을 선택하라는 메시지가 표시됩니다.

{% alert note %}
Currents does not support buckets with [Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) configured.
{% endalert %}

## Integration

Braze has two different integration strategies with Amazon S3—one for [Braze Currents]({{site.baseurl}}/user_guide/data/braze_currents/) and one for all dashboard data exports (such as CSV exports or engagement reports). Both integrations support two different authentication or authorization methods:

- [AWS secret access key method](#aws-secret-key-auth-method)
- [AWS role ARN method](#aws-role-arn-auth-method)

## AWS secret key auth method

This authentication method generates a secret key and an access key ID that enables Braze to authenticate as a user on your AWS account to write data to your bucket.

### Step 1: Create user {#secret-key-1}

{% alert note %}
메시지 보관만 설정하는 경우에는 **대시보드 데이터 내보내기** 탭의 단계를 따르세요.
{% endalert %}

액세스 키 ID와 비밀 액세스 키를 검색하려면 [AWS에서 IAM 사용자 및 관리자 그룹을 만드세요](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html).

### 2단계: Get credentials {#secret-key-2}

After creating a new user, select **Show User Security Credentials** to reveal your access key ID and secret access key. 그런 다음 자격 증명을 어딘가에 기록해 두거나 나중에 Braze 대시보드에 입력해야 하므로 **자격 증명 다운로드** 버튼을 선택합니다.

![]({% image_buster /assets/img_archive/S3_Credentials.png %})

### 3단계: Create policy {#secret-key-3}

Navigate to **Policies** > **Get Started** > **Create Policy** to add permissions for your user. Next, select **Create Your Own Policy**. 이 권한은 제한된 권한을 부여하므로 Braze는 지정된 버킷에만 액세스할 수 있습니다. 

![]({% image_buster /assets/img_archive/S3_CreatePolicy.png %})

{% alert note %}
Different policies are required for Currents and Dashboard Data Export. `s3:GetObject` is required to allow the Braze backend to perform error handling.
{% endalert %}

Specify a policy name of your choice, and input the following code snippet into the **Policy Document** section. Be sure to replace `INSERTBUCKETNAME` with your bucket name. 이러한 권한이 없으면 통합이 자격 증명 확인에 실패하여 생성되지 않습니다.

{% alert note %}
메시지 보관만 설정하는 경우에는 **대시보드 데이터 내보내기** 탭의 코드 스니펫을 사용하세요.
{% endalert %}

{% tabs %}
{% tab Braze Currents %}
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```
{% endtab %}
{% tab Dashboard Data Export %}
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME*", "arn:aws:s3:::INSERTBUCKETNAME/", "arn:aws:s3:::INSERTBUCKETNAME"]
        }
    ]
}
```
{% endtab %}
{% endtabs %}

### Step 4: Attach policy {#secret-key-4}

After creating a new policy, go to **Users** and select into your specific user. In the **Permissions** tab, select **Attach Policy**, and select the new policy you created. Now, you're ready to link your AWS credentials to your Braze account.

![]({% image_buster /assets/img_archive/S3_AttachPolicy.png %})

### 5단계: Link Braze to AWS {#secret-key-5}

{% alert note %}
메시지 보관만 설정하는 경우에는 **대시보드 데이터 내보내기** 탭의 단계를 따르세요.
{% endalert %}

{% tabs %}
{% tab Braze Currents %}

In Braze, go to **Partner Integrations** > **Data Export**.

Next, select **Create Current** then **Amazon S3 Data Export**.

Name your Current. In the **Credentials** section, make sure **AWS Secret Access Key** is selected, then input your S3 access ID, AWS secret access key, and AWS S3 bucket name in the designated fields.

![]({{site.baseurl}}/assets/img/currents-s3-example.png)

{% alert warning %}
Keep your AWS access key ID and secret access key up to date. 커넥터의 자격 증명이 만료되면 커넥터는 이벤트 전송을 중지합니다. 이 상태가 **5일** 이상 지속되면 커넥터의 이벤트가 삭제되고 데이터가 영구적으로 손실됩니다.
{% endalert %}

You can also add the following customization based on your needs:

- **Folder Path:** Defaults to `currents`. 이 폴더가 없는 경우 Braze에서 자동으로 폴더를 생성합니다. 
- **Server-Side, At-Rest AES-256 Encryption:** Defaults to OFF and includes the `x-amz-server-side-encryption` header.

Select **Launch Current** to continue.

알림을 통해 자격 증명이 성공적으로 확인되었는지 여부를 알 수 있습니다. 이제 AWS S3가 Braze 커런츠를 위해 설정되었습니다.

{% endtab %}
{% tab Dashboard Data Export %}

In Braze, go to **Partner Integrations** > **Technology Partners** and select **Amazon S3**.

On the **AWS Credentials** page, make sure **AWS Secret Access Key** is selected, then input your AWS access ID, AWS secret access key, and AWS S3 bucket name in the designated fields. When inputting your secret key, select **Test Credentials** first to ensure your credentials work, then select **Save** when successful.

![]({{site.baseurl}}/assets/img/s3_tech_partners.png)

{% alert tip %}
You can always retrieve new credentials by navigating to your user, and selecting **Create Access Key** in the **Security Credentials** tab within the AWS Console.
{% endalert %}

알림을 통해 자격 증명이 성공적으로 확인되었는지 여부를 알 수 있습니다. 이제 AWS S3가 Braze 계정에 통합되었습니다.

{% endtab %}
{% endtabs %}

## AWS role ARN auth method

This authentication method generates a role Amazon Resource Name (ARN) that enables the Braze Amazon account to authenticate as a member of the role you created to write data to your bucket.

### Step 1: Create policy {#role-arn-1}

To get started, sign in to the AWS management console as an account administrator. Navigate to the IAM section of the AWS Console, select **Policies** in the navigation bar, and select **Create Policy**.

![]({{site.baseurl}}/assets/img/create_policy_1_list.png)

{% alert note %}
Different policies are required for Currents and Dashboard Data Export. `s3:GetObject` is required to allow the Braze backend to perform error handling.
{% endalert %}

Open the **JSON** tab and input the following code snippet into the **Policy Document** section. Be sure to replace `INSERTBUCKETNAME` with your bucket name. Select **Review Policy** when you're finished.

{% alert note %}
메시지 보관만 설정하는 경우에는 **대시보드 데이터 내보내기** 탭의 코드 스니펫을 사용하세요.
{% endalert %}

{% tabs %}
{% tab Braze Currents %}

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```

{% endtab %}
{% tab Dashboard Data Export %}

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject","s3:DeleteObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```

{% endtab %}
{% endtabs %}

Next, give the policy a name and a description and select **Create Policy**.

![]({{site.baseurl}}/assets/img/create_policy_3_name.png)

![]({{site.baseurl}}/assets/img/create_policy_4_created.png)

### Step 2: Create role {#role-arn-2}

Within the same IAM section of the console, select **Roles** > **Create Role**.

![]({{site.baseurl}}/assets/img/create_role_1_list.png)

Retrieve your Braze account ID and external ID from your Braze account:
- **Currents**: In Braze, go to **Partner Integrations** > **Data Export**. Next, select **Create Current** then **Amazon S3 Data Export**. Here you'll find the identifiers needed to create your role.
- **Dashboard data export**: In Braze, go to **Partner Integrations** > **Technology Partners** and select **Amazon S3**. Here you'll find the identifiers needed to create your role. (메시지 보관만 설정하는 경우에는 여기에서 역할을 만드세요.)

Back on the AWS Console, select **Another AWS Account** as the trusted entity selector type. Provide your Braze account ID, check the **Require external ID** box, and enter the Braze external ID. Select **Next** when complete.

![The S3 "Create Role" page. This page has fields for role name, role description, trusted entities, policies, and permissions boundary.]({{site.baseurl}}/assets/img/create_role_2_another.png)

### Step 3: Attach policy {#role-arn-3}

Next, attach the policy you created earlier to the role. Search for the policy in the search bar, and place a checkmark next to the policy to attach it. Select **Next** when complete.

![Role ARN]({{site.baseurl}}/assets/img/create_role_3_attach.png)

Give the role a name and a description, and select **Create Role**.

![Role ARN]({{site.baseurl}}/assets/img/create_role_4_name.png)

이제 목록에 새로 만든 역할이 표시됩니다.

### 4단계: Link to Braze AWS {#role-arn-4}

In the AWS Console, find your newly created role in the list. Select the name to open up the details of that role.

![]({{site.baseurl}}/assets/img/create_role_5_created.png)

Take note of the **Role ARN** at the top of the Role summary page.

![]({{site.baseurl}}/assets/img/create_role_6_summary.png)

Return to your Braze account and copy the role ARN into the field provided.

{% alert note %}
메시지 보관만 설정하는 경우에는 **대시보드 데이터 내보내기** 탭의 단계를 따르세요.
{% endalert %}

{% tabs %}
{% tab Braze Currents %}

In Braze, go to the **Currents** page under **Integrations**. Next, select **Create Current** and select **Amazon S3 Data Export**

![]({{site.baseurl}}/assets/img/currents-role-arn.png)

Give your Current a name. Then, in the **Credentials** section, make sure **AWS Role ARN** is selected, then provide your role ARN and AWS S3 bucket name in the designated fields.

You can also add the following customization based on your needs:

- Folder Path (defaults to `currents`)
- Server-Side, At-Rest AES-256 Encryption (defaults to OFF) - Includes the `x-amz-server-side-encryption` header

Select **Launch Current** to continue. 알림은 자격 증명이 성공적으로 확인되었는지 여부를 나타냅니다. 이제 AWS S3가 Braze 커런츠를 위해 설정되었습니다.

{% alert important %}
If you receive an "S3 credentials are invalid" error, this may be due to integrating too quickly after creating a role in AWS. Wait and try again.
{% endalert %}

{% endtab %}
{% tab Dashboard Data Export %}

In Braze, go to the **Technology Partners** page under **Integrations** and select **Amazon S3**.

![]({{site.baseurl}}/assets/img/data-export-role-arn.png)

On the **AWS Credentials** page, make sure the **AWS Role ARN** radio button is selected, then input your role ARN and AWS S3 bucket name in the designated fields. Select **Test Credentials** first to confirm your credentials work properly, then select **Save** when successful.

{% alert tip %}
You can always retrieve new credentials by navigating to your user, and selecting **Create Access Key** on the **Security Credentials** tab within the AWS Console.
{% endalert %}

알림을 통해 자격 증명이 성공적으로 확인되었는지 여부를 알 수 있습니다. 이제 AWS S3가 Braze 계정에 통합되었습니다.

{% endtab %}
{% endtabs %}

## Export behavior

클라우드 데이터 스토리지 솔루션을 통합하고 API, 대시보드 보고서 또는 CSV 보고서를 내보내는 사용자는 다음과 같은 경험을 하게 됩니다:

- 모든 API 내보내기는 응답 본문에서 다운로드 URL을 반환하지 않으며 데이터 저장소를 통해 검색해야 합니다.
- 모든 대시보드 보고서와 CSV 보고서는 다운로드할 수 있도록 사용자의 이메일로 전송되며(저장 권한 필요 없음), 데이터 스토리지에 백업됩니다.

{% alert important %}
**JSON 형식 요구 사항**: JSON 내보내기의 경우 Braze는 각 줄에 별도의 JSON 개체가 포함되는 JSONL(줄 바꿈으로 구분된 JSON) 형식을 사용합니다. 이 형식은 단일 JSON 배열 또는 오브젝트인 표준 JSON과 다릅니다. 내보낸 파일의 각 줄은 유효한 JSON 객체이지만 파일 전체가 하나의 유효한 JSON 설명서가 아닙니다. 이러한 파일을 처리할 때는 전체 파일을 하나의 JSON 설명서로 구문 분석하지 말고 각 줄을 별도의 JSON 객체로 개별적으로 구문 분석하세요.

커런츠 내보내기는 JSON이 아닌 Apache Avro 형식(`.avro` 파일)을 사용합니다. 이 JSON 형식 요구 사항은 대시보드 데이터 내보내기 및 API 내보내기에 적용됩니다.
{% endalert %}

## Multiple connectors

S3 버킷으로 보낼 커런츠 커넥터를 두 개 이상 만들려는 경우 동일한 자격 증명을 사용할 수 있지만 각각에 대해 다른 폴더 경로를 지정해야 합니다. 동일한 작업 공간에서 만들거나 여러 작업 공간에서 분할하여 만들 수 있습니다. 각 통합에 대해 단일 정책을 만들거나 두 통합을 모두 포함하는 하나의 정책을 만들 수도 있습니다. 

커런츠와 데이터 내보내기 모두에 동일한 S3 버킷을 사용하려는 경우, 각 통합에 서로 다른 권한이 필요하므로 두 개의 별도 정책을 만들어야 합니다.


