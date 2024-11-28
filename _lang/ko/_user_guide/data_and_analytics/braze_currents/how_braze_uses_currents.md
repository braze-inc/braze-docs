---
nav_title: Braze가 커런츠를 사용하는 방법
article_title: Braze가 커런츠를 사용하는 방법
page_order: 6
page_type: tutorial
description: "이 커런츠 사용 방법 기사에서는 이벤트 데이터에 대한 적절한 수집을 설정하는 기본 프로세스와 이를 데이터베이스 및 BI 도구로 이동하는 방법을 안내합니다."
tool: Currents
 
---

# Braze가 커런츠를 사용하는 방법

> Braze는 커런츠를 사용합니다! 네, Braze는 일부 [당사 파트너]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/)와 함께 사용할 만큼 당사 제품을 좋아합니다.

Braze는 이메일 및 푸시 캠페인에서 데이터를 필터링하여 비즈니스 인사이트 도구인 Looker에 넣지만, 그 과정은 흥미로운 경로를 거칩니다. Braze는 ETL(추출, 변환, 로드) 방법론의 약간 반전된 버전을 사용합니다. 순서를 ELT(추출, 로드, 변환)로 바꾸기만 한 것이죠!

## 1단계: 섭취 및 집계 이벤트 데이터

캠페인 또는 캔버스와 같은 참여 도구를 사용하여 캠페인을 시작한 후, 당사의 시스템과 이메일 파트너의 시스템을 사용하여 이벤트 데이터를 추적합니다. 이 데이터 중 일부는 대시보드에 집계되어 표시되지만, Braze는 더 깊이 파고드는 것에 관심이 있었습니다!

## 2단계: 이벤트 데이터를 데이터 저장 파트너에게 전송

우리는 커런츠를 설정하여 Braze 이벤트 데이터를 Amazon S3로 전송하여 저장 및 추출합니다. 이제 Braze는 [Athena][2]를 사용하여 S3 위에 앉아 쿼리를 실행할 수 있다는 것을 알고 있습니다. 단기적으로 훌륭한 솔루션입니다. 하지만 Braze는 관계형 데이터베이스와 비즈니스 인텔리전스/분석 도구를 사용하는 장기적인 솔루션을 원했고 (그리고 이를 추천합니다).

Braze는 S3를 성의 열쇠로 생각합니다! 이것은 Braze가 데이터를 이동, 피벗 및 분석할 수 있는 수많은 가능성을 열어줍니다. 하지만 Braze는 S3의 데이터를 변환하지 않도록 주의합니다. 데이터에 대해 매우 구체적인 구조를 가지고 있기 때문입니다.

## 3단계: 관계형 데이터베이스로 이벤트 데이터를 변환

S3에서 Braze는 창고([Snowflake 데이터 공유](https://www.snowflake.com/try-the-data-warehouse-built-for-the-cloud/?&utm_medium=search&utm_source=adwords&utm_campaign=NA%20-%20Branded&utm_adgroup=NA%20-%20Branded%20Snowflake%20-%20Data&utm_term=%2Bsnowflake%20%2Bdata&utm_region=NA&gclid=EAIaIQobChMI0vLv6uDA3gIVEFqGCh3aiwMzEAAYASAAEgI72fD_BwE) 또는 Snowflake Reader 계정, Braze의 경우)를 선택합니다. Braze는 그것을 거기서 변환한 다음 Looker로 이동하여 데이터의 구조와 조직을 설정할 블록을 설정합니다.

Snowflake만이 유일한 데이터 웨어하우스 옵션은 아닙니다. 또한 [Redshift](https://aws.amazon.com/redshift/), [Google BigQuery](https://cloud.google.com/bigquery/?utm_source=google&utm_medium=cpc&utm_campaign=na-US-all-en-dr-bkws-all-all-trial-p-dr-1003905&utm_content=text-ad-none-any-DEV_c-CRE_288551384566-ADGP_Hybrid+%7C+AW+SEM+%7C+BKWS+%7C+US+%7C+en+%7C+PHR+~+Big+Data+~+BigQuery+~+google+bigquery-KWID_43700035823403663-kwd-300487425311&utm_term=KW_google%20bigquery-ST_google+bigquery&gclid=EAIaIQobChMIl9OK8uHA3gIVyVmGCh1lFgB-EAAYASAAEgIfWfD_BwE) 등을 선택할 수 있습니다!

### Snowflake 리더 계정

Snowflake Reader Accounts는 사용자에게 Snowflake 계정이나 Snowflake와의 고객 관계를 요구하지 않고도 [Snowflake 데이터 공유]({{site.baseurl}}/partners/snowflake/)와 동일한 데이터 및 기능에 대한 액세스를 제공합니다. 리더 계정을 사용하면 Braze에서 데이터를 생성하여 계정으로 공유하고 로그인하여 데이터에 액세스할 수 있는 자격 증명을 제공합니다. 이로 인해 모든 데이터 공유 및 사용 청구가 Braze에 의해 완전히 처리됩니다. 

자세히 알아보려면 고객 성공 매니저에게 문의하세요.

**추가 자료**<br>
유용한 사용 모니터링 리소스를 위해 Snowflake의 [리소스 모니터](https://docs.snowflake.com/en/user-guide/resource-monitors.html) 및 [웨어하우스 크레딧 사용량 보기](https://docs.snowflake.com/en/user-guide/credits.html#viewing-warehouse-credit-usage-for-your-account) 기사를 확인하세요.

## 4단계: BI 도구를 사용하여 데이터를 조작하십시오

마지막으로, Braze는 BI 도구를 사용하여 데이터를 분석하고, 차트 및 기타 시각적 도구로 변환하며, [Looker 및 Looker Blocks](https://www.marketplace.looker.com/)를 사용하여 커런츠에서 데이터가 이동할 때마다 ETL/ELT를 수행할 필요가 없도록 합니다.

다음 문서를 확인하여 이에 대한 자세한 정보와 데이터베이스를 구축하는 방법을 알아보세요!

- [사용자 행동 차단](https://marketplace.looker.com/marketplace/detail/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)
- [메시지 인게이지먼트 블록](https://marketplace.looker.com/marketplace/detail/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)

[2]: https://aws.amazon.com/athena/
