---
nav_title: FAQ
article_title: 전류 FAQ
page_order: 9
page_type: reference
description: "이 글에서는 브레이즈 커런트를 설정할 때 가장 자주 발생하는 몇 가지 질문에 대해 설명합니다."
tool: Currents
---

# Frequently asked questions

> 이 페이지에서는 커런츠에 대해 자주 묻는 질문에 대한 답변을 제공합니다.

### 기록 데이터는 어떻게 얻나요?

커런츠는 실시간 라이브 데이터 스트림이므로 이벤트를 다시 재생할 수 없습니다. 하지만 [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) 또는 [Microsoft Azure Blob Storage와]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/) 같은 데이터 웨어하우스에 Currents 데이터를 저장할 수 있으므로 과거 이벤트에 대해 적절하게 조치를 취할 수 있습니다. 데이터는 30일 동안 보관되지만, 더 많은 과거 데이터를 보려면 [눈송이를]({{site.baseurl}}/user_guide/data/braze_currents/s3_to_snowflake/) 쿼리할 수 있습니다.

### Currents가 JSON이 아닌 Avro 형식으로 데이터를 출력하는 이유는 무엇인가요?

Avro는 스키마가 없는 JSON과 달리 스키마 진화를 기본적으로 지원합니다. 또한 Avro는 압축률이 높기 때문에 대역폭을 줄이고 저장 공간을 절약하면서 Avro 파일을 전송할 수 있는 이점을 누릴 수 있습니다.

### Braze는 파일 오버헤드를 어떻게 처리하나요?

한 데이터베이스에서 대량의 데이터를 가져와 다른 데이터베이스에 저장할 수 있는 추출, 변환, 로드(ETL) 프로세스를 구축합니다.

### 쿼리를 위해 이 데이터를 어디에 저장해야 하나요?

Braze는 쿼리를 위해 데이터를 저장할 수 있는 여러 데이터 웨어하우스와 제휴하고 있습니다. 사용을 권장합니다:
- [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)
- [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/)
- [Google 클라우드 스토리지]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/).