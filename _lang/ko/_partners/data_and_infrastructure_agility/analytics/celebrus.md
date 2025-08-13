---
nav_title: Celebrus
article_title: Celebrus 통합
description: "Braze와 Celebrus 통합."
---

# Celebrus

> Celebrus는 웹 및 모바일 앱 채널 전반에서 Braze SDK와 원활하게 통합되어 채널 활동 데이터로 Braze의 인구를 늘리는 데 도움이 됩니다. 여기에는 지정된 기간 동안 디지털 자산 전반의 방문자 트래픽에 대한 포괄적인 인사이트가 포함됩니다. <br><br>또한 Celebrus는 각 개별 고객에 대한 풍부한 프로필 데이터를 캡처하여 Braze와 동기화할 수 있습니다. 이를 통해 포괄적이고 정확하며 상세한 퍼스트 파티 데이터를 기반으로 효과적인 Braze 분석 및 커뮤니케이션 전략을 수립할 수 있습니다. 이 기능은 Celebrus의 머신 러닝 기반 신호를 통해 더욱 강화되어 광범위한 태그 지정 없이도 번거로움 없이 데이터를 캡처할 수 있습니다. 강력한 퍼스트파티 ID 그래프가 구축되어 있으면 모든 데이터에 즉시 액세스하여 즉시 사용할 수 있습니다. 

_This integration is maintained by Celebrus._

## 전제 조건

| 요구 사항 | 설명 |
|---|---|
| Celebrus 계정 | 이 파트너십을 활용하려면 Celebrus 계정이 필요합니다. |
| 데이터 웨어하우스(선택 사항) | Braze 커스텀 속성에 Celebrus 커넥터를 사용하는 경우, Braze 클라우드 데이터 수집(CDI) 통합에서 지원하는 데이터 웨어하우스가 있어야 하며, Braze 대시보드에서 CDI를 구성해야 합니다. |
| Braze SDK 구성 설정(선택 사항) | Braze SDK용 Celebrus 커넥터를 사용할 때는 SDK 엔드포인트와 SDK API 키를 전달해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 구현
Celebrus 구현을 설치한 후, Braze용 Celebrus 커넥터를 사용하여 Celebrus 데이터를 Braze에 통합합니다. Braze용 Celebrus 통합에는 Braze SDK와 Braze 커스텀 속성과 같은 두 가지 요소가 있습니다. Braze를 사용하는 방법과 필요한 사용 사례에 따라 둘 중 하나 또는 둘 다 배포할 수 있습니다.

웹 채널에 아직 Braze SDK가 구현되어 있지 않은 경우 Celebrus를 사용하여 Braze SDK를 배포할 수 있습니다. Celebrus는 웹 페이지에 Braze SDK를 추가하고 Celebrus ID 그래프를 사용하여 웹 방문자에 대한 Braze ID를 설정합니다. 고객 속성은 클라우드 데이터 수집(CDI)을 통해 Braze와 동기화할 수 있습니다. 이를 위해서는 Braze CDI가 지원하는 데이터 웨어하우스가 필요하며, Braze에서 CDI를 구성해야 합니다.

### Braze SDK용 Celebrus 커넥터

Braze SDK용 Celebrus 커넥터는 Braze를 위한 높은 수준의 웹 및 모바일 앱 채널 데이터를 제공합니다. Braze SDK에서는 Celebrus ID 그래프의 Celebrus `System Identity`가 Braze 통합을 위한 식별자로 사용됩니다. Braze 커스텀 속성 Celebrus 커넥터를 통해 커스텀 속성을 동기화하는 데 다른 식별자가 지원됩니다.

커넥터는 채널에서 Braze SDK를 배포하고 구성하므로 Braze SDK 데이터 스트림에서 몇 가지 설정을 구성하고 다음 세 가지 설정에 대한 값을 제공해야 합니다.

```
    response.addParameter("sdk_endpoint", "sdk.xxxxxx.braze.com");
    response.addParameter("api_key", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx");
    response.addParameter("app_id", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx");
```

{% alert important %}
SDK용 Celebrus 커넥터는 사용자를 식별하기 위해 Braze SDK를 삽입하고 초기화하며 Celebrus의 ID 그래프에 식별자를 추가합니다. 이 커넥터는 고객 프로필에 데이터를 기록하거나 다른 Braze SDK 메서드를 트리거하지 않습니다. <br><br>코드베이스 내에서 원하는 메서드를 직접 호출하여 [Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web)를 통해 데이터를 기록하거나 다른 Braze SDK 지원 기능을 활용할 수 있습니다.
{% endalert%}

### Braze 커스텀 속성을 위한 Celebrus 커넥터

#### 1단계: Celebrus에서 연결된 세부 정보 구성 

Braze 커스텀 속성을 위한 Celebrus 커넥터는 Braze가 예상하는 방식으로 미리 형식을 지정하여 커스텀 속성을 중간 데이터베이스로 전송합니다. Celebrus에서는 데이터베이스에 대한 연결 세부 정보를 구성합니다. 이는 사용 중인 데이터베이스 유형(예: Snowflake 또는 Redshift)에 따라 달라집니다. 

#### 2단계: Braze 대시보드에서 클라우드 데이터 수집 구성

이 통합에서는 Braze 클라우드 데이터 수집을 사용합니다. [데이터 웨어하우스 통합]({{site.baseurl}}/user_guide/data/cloud_ingestion/integrations/) 지침을 수행하여 사용 중인 웨어하우스 유형에 따라 [클라우드 데이터 수집 설정]({{site.baseurl}}/user_guide/data/cloud_ingestion/overview/)을 설정하고 구성합니다. 

#### 3단계: Celebrus에서 Braze로 데이터 동기화

Celebrus는 이메일, 전화, `external_id` 또는 사용자 별칭과 같은 고유 식별자를 캡처하여 개인에게 할당하고 CDI를 통해 Braze로 전송합니다. 이를 통해 동일한 개인에 대한 데이터를 Braze에 동기화할 수 있습니다.

Celebrus는 정의된 식별자를 사용하여 Celebrus 프로필 빌더에 정의된 고객 속성을 전송하지만, 속성 값이 변경된 경우에만 전송합니다. Note that the attribute names defined in the Celebrus profile builder will be used in Braze by default. So be sure you update these names to adhere to [Braze naming conventions]({{site.baseurl}}/api/objects_filters/user_attributes_object/).

{% alert important %}
현재 이 릴리스에서는 이벤트와 구매가 지원되지 않습니다.<br><br> 이 통합은 속성을 문자열 값으로 전송하므로 일부 속성은 목록(예: 신호)입니다. 현재로서는 목록을 배열로 변환할 수 없습니다. 중첩된 속성이 없습니다.
{% endalert%}

