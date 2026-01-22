---
nav_title: Braze 커런츠 사용 방법
article_title: Braze 커런츠 사용 방법
page_order: 6
page_type: tutorial
description: "이 커런츠 사용법 문서에서는 이벤트 데이터에 대한 적절한 인입을 설정하고 데이터베이스 및 비즈니스 인텔리전스(BI) 도구로 데이터를 이동하는 기본 프로세스를 안내합니다."
tool: Currents
 
---

# Braze 커런츠 사용 방법

> Braze는 커런츠를 사용합니다! 네, 저희는 몇몇 [파트너와]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) 함께 사용할 만큼 자체 제품에 만족하고 있습니다.

이메일에서 데이터를 필터링하여 비즈니스 인사이트 도구인 Looker로 캠페인을 푸시하지만, 여기까지 도달하는 데는 흥미로운 경로가 필요합니다. 우리는 추출, 변환, 로드(ETL) 방법론을 약간 뒤집은 버전인 추출, 로드, 변환(ELT)으로 순서를 바꾸어 사용합니다!

## 1단계: 이벤트 데이터 수집 및 집계

캠페인이나 캔버스와 같은 참여 툴을 사용하여 캠페인을 시작한 후에는 자체 시스템과 이메일 파트너의 시스템을 사용하여 이벤트 데이터를 추적합니다. 이 데이터 중 일부는 집계되어 대시보드에 표시되지만, 더 자세히 살펴보고 싶습니다!

## 2단계: 데이터 스토리지 파트너에게 이벤트 데이터 보내기

우리는 저장 및 추출을 위해 Braze 이벤트 데이터를 Amazon S3로 전송하도록 커런츠를 설정했습니다. 이제 [Athena를](https://aws.amazon.com/athena/) 사용하여 S3 위에 앉아 쿼리를 실행할 수 있다는 것을 알고 있습니다. 단기적으로 훌륭한 솔루션입니다. 하지만 저희는 관계형 데이터베이스와 비즈니스 인텔리전스/분석 도구를 사용하는 장기적인 솔루션을 원했습니다. (여러분에게도 동일한 방법을 권장합니다.)

저희는 S3를 성의 열쇠라고 생각합니다! 데이터를 필요한 곳으로 전송하여 데이터를 이동, 전환, 분석할 수 있는 수많은 가능성을 열어줍니다. 하지만 데이터에 대한 매우 구체적인 구조를 가지고 있기 때문에 S3에서 데이터를 변환하지 않도록 주의하고 있습니다.

## 3단계: 관계형 데이터베이스로 이벤트 데이터 변환하기

S3에서 데이터 웨어하우스[(](https://www.snowflake.com/try-the-data-warehouse-built-for-the-cloud/?&utm_medium=search&utm_source=adwords&utm_campaign=NA%20-%20Branded&utm_adgroup=NA%20-%20Branded%20Snowflake%20-%20Data&utm_term=%2Bsnowflake%20%2Bdata&utm_region=NA&gclid=EAIaIQobChMI0vLv6uDA3gIVEFqGCh3aiwMzEAAYASAAEgI72fD_BwE) 저희의 경우[Snowflake 데이터 공유](https://www.snowflake.com/try-the-data-warehouse-built-for-the-cloud/?&utm_medium=search&utm_source=adwords&utm_campaign=NA%20-%20Branded&utm_adgroup=NA%20-%20Branded%20Snowflake%20-%20Data&utm_term=%2Bsnowflake%20%2Bdata&utm_region=NA&gclid=EAIaIQobChMI0vLv6uDA3gIVEFqGCh3aiwMzEAAYASAAEgI72fD_BwE) 또는 Snowflake 리더 계정)를 선택합니다. 거기서 변환한 다음 데이터를 구조화하고 구성할 블록을 설정한 후 Looker로 옮깁니다.

Snowflake만이 유일한 창고 옵션은 아닙니다. 다른 옵션으로는 [Redshift](https://aws.amazon.com/redshift/), [Google BigQuery](https://cloud.google.com/bigquery/?utm_source=google&utm_medium=cpc&utm_campaign=na-US-all-en-dr-bkws-all-all-trial-p-dr-1003905&utm_content=text-ad-none-any-DEV_c-CRE_288551384566-ADGP_Hybrid+%7C+AW+SEM+%7C+BKWS+%7C+US+%7C+en+%7C+PHR+~+Big+Data+~+BigQuery+~+google+bigquery-KWID_43700035823403663-kwd-300487425311&utm_term=KW_google%20bigquery-ST_google+bigquery&gclid=EAIaIQobChMIl9OK8uHA3gIVyVmGCh1lFgB-EAAYASAAEgIfWfD_BwE) 등이 있습니다!

### Snowflake 리더 계정

스노우플레이크 리더 계정은 스노우플레이크 계정이나 스노우플레이크와의 고객 관계 없이도 스노우플레이크 [데이터 공유와]({{site.baseurl}}/partners/snowflake/) 동일한 데이터 및 기능에 액세스할 수 있도록 합니다. 독자 계정을 사용하면 Braze는 데이터를 계정으로 생성 및 공유하고 로그인 및 데이터 액세스를 위한 자격 증명을 제공합니다. 이렇게 하면 모든 데이터 공유 및 사용량 청구는 Braze에서 전적으로 처리하게 됩니다. 

자세한 내용은 고객 성공 매니저에게 문의하세요.

#### 추가 리소스
사용량 모니터링에 도움이 되는 [리소스는](https://docs.snowflake.com/en/user-guide/resource-monitors.html) Snowflake의 [리소스 모니터](https://docs.snowflake.com/en/user-guide/resource-monitors.html) 및 [창고 크레딧 사용량 보기](https://docs.snowflake.com/en/user-guide/credits.html#viewing-warehouse-credit-usage-for-your-account) 문서를 참조하세요.

## 4단계: 비즈니스 인텔리전스(BI) 도구를 사용하여 데이터 조작하기

마지막으로, 커런츠에서 데이터를 이동할 때마다 ETL이나 ELT를 할 필요가 없도록 [Looker 및 Looker 블록을](https://www.marketplace.looker.com/) 사용하여 데이터를 분석하고 차트 및 기타 시각적 도구로 변환하는 등의 작업을 BI 도구로 수행합니다.

같은 일을 하고 싶으신가요? 다음 문서를 확인하여 이에 대한 자세한 정보와 데이터베이스를 구축하는 방법을 알아보세요!

- [사용자 행동 블록](https://marketplace.looker.com/marketplace/detail/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)
- [메시지 참여 블록](https://marketplace.looker.com/marketplace/detail/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)

