---
nav_title: CDI 세그먼트
article_title: CDI 세그먼트
page_order: 0
page_type: reference
tool: 
- Segments
description: "이 방법 안내 기사는 위치 타겟팅 설정 방법을 안내하여 사용자를 위치별로 세그먼트할 수 있도록 합니다."

---

# CDI 세그먼트

> With Braze [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/overview/) (CDI), you can set up a direct connection from your data warehouse or file storage system to Braze to sync relevant user or catalog data on a recurring basis.

{% alert warning %}
이 기능은 데이터 웨어하우스에 직접 쿼리하기 때문에 데이터 웨어하우스에서 이러한 쿼리를 실행하는 것과 관련된 모든 비용은 사용자가 부담합니다. CDI 세그먼트는 [SQL 세그먼트 크레딧]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#monitoring-your-sql-segments-usage)을 사용하지 않으며, 세그먼트 확장 한도에 포함되지 않고, 데이터 포인트를 사용하지 않습니다.
{% endalert %}

## 필수 조건

To use your data warehouse data for segmentation within your Braze workspace, you'll need to create a [connected source]({{site.baseurl}}/user_guide/data/cloud_ingestion/connected_sources/), then create a CDI segment within your [Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/). CDI 세그먼트를 사용하면 CDI 연결을 통해 제공된 데이터를 사용하여 자체 데이터 웨어하우스를 직접 쿼리하는 SQL을 작성하고 Braze 내에서 타겟팅할 수 있는 사용자 그룹을 생성할 수 있습니다.

## 세그먼트 생성

### 1단계: 소스 설정

Before creating your first CDI Segment, set up a new Connected Source with your data warehouse by following the steps in [Connected Sources]({{site.baseurl}}/user_guide/data/cloud_ingestion/connected_sources/).

### 2단계: 세그먼트를 생성

먼저 새 [세그먼트 확장]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)을 만든 다음 **전체 새로고침**을 선택합니다.

![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:60%;"}

데이터 소스로 **CDI 데이터 테이블**을 선택하십시오.

![]({% image_buster /assets/img/segment/cdi_data_tables.png %}){: style="max-width:60%;"}

CDI 설정의 일부로, CDI 세그먼트에서 사용할 다양한 연결을 선택할 수 있습니다. 각 연결에는 특정 데이터 테이블 세트가 있습니다. 개발 팀은 CDI 설정 중에 연결 및 데이터 테이블을 구성할 수 있습니다.

사용 가능한 데이터 테이블을 보려면 **참조**을 선택하십시오. 준비가 되면 연결을 선택하세요.

![]({% image_buster /assets/img/segment/connection_schema.png %}){: style="max-width:100%;"}

다음으로, [Braze SQL 구문]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#writing-sql)을 사용하여 세그먼트를 위한 SQL을 작성하십시오.

명심하세요, 모든 CDI 세그먼트는 선택된 열로 `external_user_id`를 사용해야 하며, `external_user_id`는 Braze에 설정된 사용자와 일치해야 합니다. 쿼리 결과에 Braze에 존재하지 않는 사용자가 포함된 경우, 해당 사용자는 무시됩니다. Braze는 귀하의 CDI 세그먼트의 출력에 따라 새로운 사용자를 생성하지 않습니다.

{% alert tip %}
세그먼트를 미리 보는 방법, 세그먼트를 관리하는 방법 및 자동 멤버십 새로 고침을 실행하는 방법을 알아보려면 [SQL 세그먼트 확장]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/)을 참조하십시오.
{% endalert %}

마침내, [이 세그먼트 확장]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#step-5-use-your-extension-in-a-segment)을 Braze 세그먼트 내에서 사용하여 이 오디언스에게 캠페인 또는 캔버스를 보낼 수 있습니다.

## 고려사항

- 세그먼트 확장은 여러 연결이 아닌 하나의 연결에서만 데이터를 참조할 수 있습니다.    
- 세그먼트 확장은 데이터 소스로 다음 중 하나를 사용할 수 있습니다: CDI 데이터 또는 Braze Snowflake (커런츠) 데이터. 세그먼트 확장 내에서 데이터 소스를 혼합할 수는 없지만, 세그먼트 내에서 함께 참조할 수 있도록 여러 세그먼트 확장을 만들 수 있습니다.

## 문제 해결

- 쿼리가 최대 런타임에 도달하면 타임아웃될 수 있으며, 이는 **클라우드 데이터 수집** 페이지에서 각 연결 동기화에 대해 설정됩니다. 최대 실행 시간은 60분입니다.
- 데이터 웨어하우스를 위한 적절한 구문을 사용하여 SQL을 작성하세요. 
