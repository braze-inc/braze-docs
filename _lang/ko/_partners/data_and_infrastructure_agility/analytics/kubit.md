---
nav_title: Kubit
article_title: Kubit
description: "이 참조 문서에서는 즉각적인 제품 인사이트를 제공하는 코드 없는 셀프 서비스 분석 플랫폼인 Braze와 Kubit의 파트너십에 대해 설명하며, 이를 통해 Kubit 사용자 코호트를 가져와서 Braze 메시징에서 타겟팅할 수 있습니다."
alias: /partners/kubit/
page_type: partner
search_tag: Partner

---

# Kubit

> [Kubit](https://kubit.ai/)은 코드가 필요 없는 셀프 서비스 분석 플랫폼으로, 즉각적인 제품 인사이트를 제공합니다. 

Braze와 Kubit의 통합을 통해 [Kubit 사용자 코호트를 가져와서]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/kubit/) Braze 메시징에서 타겟팅할 수 있습니다. 또한, [스노우플레이크 보안 데이터 공유를]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/) 사용하면 Braze의 원시 캠페인 및 노출 데이터를 Kubit 제품 분석과 통합하여 이러한 캠페인의 효과를 실시간으로 측정할 수 있습니다. 이 접근 방식은 엔지니어링 작업 없이도 사용자의 전체 라이프사이클에 대한 인사이트를 제공합니다.

## 필수 조건

| 요구 사항 | 설명 |
|---|---|
|Kubit 엔터프라이즈 계정 | 이 파트너십을 이용하려면 Kubit 기업 계정이 필요합니다. |
| 사용자 ID 일치 | Kubit과 Braze의 고객 데이터는 두 플랫폼에서 일치하는 사용자 ID를 가져야 합니다. 여기에는 익명 UUID도 포함됩니다. Braze에서 사용자 ID를 설정하는 방법에 대한 [설명서를]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=android) 읽어보세요. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## Kubit에서 Braze 데이터 분석하기

[Snowflake 보안 데이터 공유를]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/) 활용하여 Braze 로우 캠페인 및 노출 데이터를 Kubit과 공유하여 Kubit의 셀프 서비스 분석에 통합함으로써 사용자의 라이프사이클을 전체적으로 파악할 수 있습니다.

참고로, 다음은 Kubit 분석에 통합할 수 있는 모든 [Braze 필드입니다]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt?ed79384e6ac6a97fe3b3d9f76852b7c2). 이 단계의 세부 사항은 매우 고객별이며 특별한 구성이 필요합니다. 자세한 내용은 Kubit 계정 관리자 또는 [지원팀(kubit.ai )](support@kubit.ai) 에 문의하세요.