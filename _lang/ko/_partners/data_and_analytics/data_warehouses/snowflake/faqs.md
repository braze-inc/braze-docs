---
nav_title: FAQs
article_title: Snowflake Data Sharing FAQs
page_order: 50
page_type: FAQ
description: "This article answers frequently asked questions about Snowflake data sharing."

---

# Frequently asked questions

### Is it possible to obfuscate PII data via Snowflake data sharing?
No, as of now that is not supported.

### Do I need data share for the same region or cross region?
Use data sharing for the same region in the following scenarios:
- Your Snowflake account is in US-EAST-1 (AWS) and your Braze dashboard region is in the US.
- Your Snowflake region is in EU-CENTRAL-1 and your Braze dashboard region is in the EU.
- Snowflake 지역은 AP-Southeast-2(AWS)에 있고 Braze 대시보드 지역은 호주에 있습니다.
- Snowflake 지역은 AP-Southeast-3(AWS)에 있고 Braze 대시보드 지역은 인도네시아에 있습니다.

Otherwise, use data sharing for cross region. 

### What should I do with my data share when I switch to a new Snowflake account?
You can delete the old data share associated with your old Snowflake account and then create a new share for the new account. All historical data will be available in the new share. 

### Why don't I see data in my data share?
You might have used the wrong Snowflake account ID when creating your data share. The account ID on the data sharing dashboard must match the output of `CURRENT_ACCOUNT()` from your Snowflake account.

If your share is cross region, the data might not be immediately available. Depending on your data volume, it could take a few hours for data to sync to your region.

### Why am I receiving a HIPAA compliance error when creating a data share?

The specified account is either not HIPAA-compliant or on [Snowflake Editions](https://docs.snowflake.com/en/user-guide/intro-editions) lower than Business Critical. Your Snowflake account must be upgraded to the Business Critical Edition to be HIPAA-compliant for data sharing. Contact Snowflake support for further assistance with upgrading your account.

### Why can't I recreate a data share after deleting one?

The system may still be processing the deletion of your previous data share. Wait a few minutes for the deprovisioning process to complete, then try creating the new data share again.

### 여러 워크스페이스가 동일한 Snowflake 계정으로 데이터를 공유하는 경우 `CREATE DATABASE` 을 몇 번 실행해야 하나요?

`CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` 을 한 번만 실행하면 됩니다. 서로 다른 Braze 작업 공간의 여러 데이터 공유를 동일한 Snowflake 계정으로 공유하면 자동으로 동일한 공유로 합쳐집니다. 초기 데이터베이스를 만들면 추가 공유 요청이나 데이터베이스 생성 단계 없이도 추가 작업 공간의 데이터가 기존 데이터베이스에 자동으로 추가됩니다.

예를 들어, 작업 공간 A에서 Snowflake 계정 123으로 데이터 공유를 만들면 공유 요청을 수락하고 데이터베이스를 만들게 됩니다. 나중에 작업 공간 B에서 동일한 Snowflake 계정 123으로 데이터 공유를 만들면 새 공유 요청이 전송되지 않고 데이터가 기존 공유에 즉시 추가되어 이전에 만든 데이터베이스에서 사용할 수 있게 됩니다.

### 작업 공간이 여러 개 있는 경우 단일 데이터베이스에 모든 작업 공간의 데이터가 포함되나요?

예. 여러 Braze 작업 공간의 데이터를 동일한 Snowflake 계정으로 공유하면 모든 데이터가 하나의 공유로 통합되어 동일한 데이터베이스에서 사용할 수 있습니다. `app_group_id` 으로 데이터를 필터링하여 워크스페이스를 구분할 수 있습니다.

모범 사례로, 쿼리에서 항상 `app_group_id` 으로 필터링하여 향후에 대비하세요. 이렇게 하면 나중에 작업 공간을 추가하더라도 대시보드와 보고서의 정확성을 유지할 수 있습니다. 이 필터가 없으면 측정기준에 새로 추가된 워크스페이스의 데이터가 예기치 않게 포함될 수 있습니다.

### Snowflake에서 여러 워크스페이스의 데이터를 관리하는 데 권장되는 접근 방식은 무엇인가요?

모든 Braze 데이터를 동일한 데이터베이스로 전송하고 `app_group_id` 으로 필터링하여 작업 공간을 구분하세요. 이 접근 방식은 데이터 관리를 간소화하고 조직 전체에서 일관된 보고를 보장합니다.

### 여러 개의 작업 공간에 몇 개의 Snowflake 데이터 공유 커넥터가 필요하나요?

필요한 커넥터 수는 특정 구성 및 자격에 따라 다릅니다. 사용 사례에 적합한 자격에 대해 자세히 알아보려면 Braze 계정 팀에 문의하세요.


