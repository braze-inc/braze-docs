---
nav_title: Microsoft Azure Blob Storage
article_title: Microsoft Azure Blob Storage
alias: /partners/microsoft_azure_blob_storage_for_currents/
description: "This reference article outlines the partnership between Braze Currents and Microsoft Azure Blog Storage, a massively scalable object storage for unstructured data."
page_type: partner
tool: Currents
search_tag: Partner

---

# Microsoft Azure Blob Storage

> [Microsoft Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/) is a massively scalable object storage for unstructured data offered by Microsoft as part of the Azure product suite.

{% alert important %}
클라우드 스토리지 제공업체 간에 전환하는 경우, 새로운 통합을 설정하고 검증하는 데 대한 추가 지원을 받으려면 Braze 고객 성공 매니저에게 문의하세요.
{% endalert %}

The Braze and Microsoft Azure Blob Storage integration allows you to export data back to Azure and stream Currents data. Later, you can use an ETL process (Extract, Transform, Load) to transfer your data to other locations.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Microsoft Azure and Azure storage account | A Microsoft Azure and Azure storage account are required to take advantage of this partnership. |
| Currents | To export data to Currents, you must have [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) set up for your account. 메시지 보관만 설정하는 경우에는 커런츠가 필요하지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

To integrate with Microsoft Azure Blob Storage, you must have a storage account and a connection string to allow Braze to either export data back to Azure or stream Currents data.

### Step 1: Create a storage account

In Microsoft Azure, navigate to **Storage Accounts** in the sidebar and click **\+ Add** to create a new storage account. Next, provide a storage account name. Other default settings will not need to be updated. Lastly, select **Review + create**. 

Even if you already have a storage account, we recommend creating a new one specifically for your Braze data.

![]({% image_buster /assets/img/azure-currents-step-1.png %})

### 2단계: Get the connection string

Once the storage account is deployed, navigate to the **Access Keys** menu from the storage account and take note of the connection string.

Microsoft provides two access keys to maintain connections using one key while regenerating the other. You only need the connection string from one of them.

{% alert note %}
Braze uses the connection string from this menu, not the key.
{% endalert %}

![]({% image_buster /assets/img/azure-currents-step-2.png %})

### 3단계: Create a blob service container

Navigate to the **Blobs** menu under the **Blob Service** section of your storage account. Create a Blob Service Container within that storage account you created earlier. 

Provide a name for your Blob Service Container. Other default settings will not need to be updated.

![]({% image_buster /assets/img/azure-currents-step-3.png %})

### 4단계: Set up Currents

In Braze, navigate to **Currents > + Create Current > Azure Blob Data Export** and provide your integration name and contact email.

Next, provide your connection string, container name, and BlobStorage prefix (optional).

![The Microsoft Azure Blob storage Currents page in Braze. 이 페이지에는 통합 이름, 연락처 이메일, 연결 문자열, 컨테이너 이름 및 접두사 필드가 있습니다.]({% image_buster /assets/img/maz.png %})

Finally, scroll to the bottom of the page and select which message engagement events or customer behavior events you would like to export. When completed, launch your Current.

### Step 5: Set up Azure data export

The following configures credentials that are used for:
1. Segment exports through the API
2. CSV exports (campaign, segment, Canvas user data export via the dashboard)
3. Engagement reports

In Braze, navigate to **Partner Integrations** > **Technology Partners** > **Microsoft Azure** and provide your connection string, Azure storage container name, and Azure storage prefix.

Next, make sure the **Make this the default data export destination** box is checked, this will make sure your exported data is sent to Azure. When completed, save your integration.

![The Microsoft Azure data export page in Braze. 이 페이지에는 연결 문자열, 컨테이너 이름 및 접두사 필드가 있습니다.]({% image_buster /assets/img/azure_data_export.png %})

{% alert important %}
It's important to keep your connection string up to date; if your connector's credentials expire, the connector will stop sending events. If this persists for more than **48 hours**, the connector's events will be dropped, and data will be permanently lost.
{% endalert %}

## Export behavior

Users that have integrated a cloud data storage solution, and are trying to export APIs, dashboard reports, or CSV reports will experience the following:

- All API exports will not return a download URL in the response body and must be retrieved through data storage.
- All dashboard reports and CSV reports will be sent to the user's email for download (no storage permissions required) and backed up on data storage.

{% alert important %}
**JSON 형식 요구 사항**: JSON 내보내기의 경우 Braze는 각 줄에 별도의 JSON 개체가 포함되는 JSONL(줄 바꿈으로 구분된 JSON) 형식을 사용합니다. 이 형식은 단일 JSON 배열 또는 오브젝트인 표준 JSON과 다릅니다. 내보낸 파일의 각 줄은 유효한 JSON 객체이지만 파일 전체가 하나의 유효한 JSON 설명서가 아닙니다. 이러한 파일을 처리할 때는 전체 파일을 하나의 JSON 설명서로 구문 분석하지 말고 각 줄을 별도의 JSON 객체로 개별적으로 구문 분석하세요.

커런츠 내보내기는 JSON이 아닌 Apache Avro 형식(`.avro` 파일)을 사용합니다. 이 JSON 형식 요구 사항은 JSON 형식을 사용하는 대시보드 데이터 내보내기 및 API 내보내기에 적용됩니다.
{% endalert %}
