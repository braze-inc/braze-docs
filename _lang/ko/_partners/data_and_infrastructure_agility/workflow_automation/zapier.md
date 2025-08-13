---
nav_title: Zapier
article_title: Zapier
alias: /partners/zapier/
description: "이 참조 문서에서는는 웹 앱 간에 데이터를 공유하고 해당 정보를 사용하여 작업을 자동화할 수 있는 자동화 웹 툴인 Zapier와 Braze 간의 파트너십을 간략히 설명합니다."
page_type: partner
search_tag: Partner

---
# Zapier 통합

> [Zapier][1]는 웹 앱 간에 데이터를 공유한 다음 해당 정보를 사용하여 작업을 자동화할 수 있는 자동화 웹 도구입니다. 

Braze와 Zapier의 파트너십을 통해 Braze API와 Braze [웹훅][3]을 활용하여 Google Workplace, Slack, Salesforce, WordPress 등과 같은 서드파티 애플리케이션과 연결하여 다양한 작업을 자동화합니다.

## 전제 조건

| 요구 사항 | 설명 |
|---|---|
| Zapier 계정 | 이 파트너십을 활용하려면 Zapier 계정이 필요합니다. |
| Braze REST 엔드포인트 | REST 엔드포인트 URL. 엔드포인트는 [인스턴스의 Braze URL에][0] 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

다음 Zapier 예제에서는 POST 웹훅을 사용하여 WordPress에서 Braze로 정보를 전송합니다. 이 정보는 Braze 캔버스를 생성하는 데 사용할 수 있습니다.

### 1단계: Zapier 트리거 생성

Zapier의 용어를 사용하면 "zap"은(는) 앱과 서비스를 연결하는 자동화된 워크플로우입니다. 모든 zap의 첫 번째 부분은 트리거를 지정하는 것입니다. zap이 활성화되면 Zapier는 트리거가 감지될 때마다 자동으로 해당 작업을 수행합니다.

WordPress 예제를 사용하여 Zapier 플랫폼에서 새로운 WordPress 게시물이 추가될 때 트리거할 zap을 설정하고 **게시물 상태** 및 **게시물 유형**으로 **게시됨** 및 **게시물**을 선택합니다. 

![Zapier 플랫폼의 zap 내에서 트리거를 '새 댓글', '모든 웹훅' 또는 '새 게시물'로 선택합니다. 이 예에서는 "새 게시물"이 선택됩니다. ] [5]

![Zapier 플랫폼의 zap 내에서 원하는 게시물 상태 및 게시물 유형을 선택하여 트리거를 구성합니다. 이 예제에서는 '게시됨' 및 '게시물;이 선택되었습니다.] [6]

### 2단계: 작업 웹훅 추가

다음으로, zap 작업을 정의합니다. zap이 활성화되고 트리거가 감지되면, 작업이 자동으로 수행됩니다.

예제를 계속 진행하여, Braze 엔드포인트에 POST 요청을 JSON으로 전송하려고 합니다. 이 작업은 **앱** 아래에서 **웹훅** 옵션을 선택하여 수행할 수 있습니다.

![][7]

### 3단계: Braze POST 설정

웹훅을 설정할 때 다음 설정을 사용하고 웹훅 URL에 Braze REST 엔드포인트를 제공하십시오. 완료되면 **게시**를 선택하십시오.

- **방법** : POST
- **웹훅 URL**: `https://rest.iad-01.braze.com/canvas/trigger/send`
- **데이터 패스스루**: False
- **미전개**: 아니요
- **요청 헤더**:
  - **Content-Type**: application/json
  - **권한 부여**: Bearer YOUR-API-KEY
- **데이터**: 

```json
{
  "canvas_id": "your_canvas_identifier",
  "recipients": [
    {
      "external_user_id": "external_user_identifier",
      "canvas_entry_properties":{
        "string_property": "Your example string",
        "example_integer_property": 1
      }
    }
  ]
}
```

![][4]{: style="max-width:70%;"}

### 4단계: Braze 캠페인을 생성합니다

일단 zap을 성공적으로 설정하면 Liquid 형식을 사용하여 메시지에 정보를 표시함으로써 WordPress 데이터로 Braze 캠페인 또는 캔버스를 사용자 지정할 수 있습니다.

[0]: {{site.baseurl}}/api/basics/#api-definitions
[1]: https://zapier.com/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#creating-a-webhook
[4]:{% image_buster /assets/img/zapier.png %}
[5]:{% image_buster /assets/img_archive/zapier1.png %}
[6]:{% image_buster /assets/img_archive/zapier2.png %}
[7]:{% image_buster /assets/img_archive/zapier3.png %}
[8]:{% image_buster /assets/img_archive/zapier4.png %}
[10]:{% image_buster /assets/img_archive/zapier5.png %}
[12]:{% image_buster /assets/img_archive/zapier6.png %}