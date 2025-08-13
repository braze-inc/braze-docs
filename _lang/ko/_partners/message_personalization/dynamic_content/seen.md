---
nav_title: 본
article_title: 본
description: "이 참고 문서에서는 고객 여정 전반에 걸쳐 참여도를 높이기 위해 개인화된 동영상을 디자인하는 플랫폼인 Braze와 SEEN의 파트너십에 대해 설명합니다."
alias: /partners/seen/
page_type: partner
search_tag: Partner
---

# 본

> [SEEN은](https://seen.io/) 기업이 고객을 중심으로 동영상을 제작하고 구축하여 더욱 매력적인 경험을 제공할 수 있도록 지원하는 개인화 동영상 플랫폼입니다. SEEN을 사용하면 데이터를 중심으로 동영상을 디자인하고 클라우드에서 규모에 맞게 개인화한 다음 가장 적합한 곳에 배포할 수 있습니다.

## 사용 사례

SEEN은 전체 고객 여정에서 자동화된 비디오 개인화 기능을 제공합니다. 일반적으로 온보딩, 로열티, 가입 및 전환, 윈백 및 이탈 방지 등의 용도로 사용됩니다.

## 필수 조건

시작하기 전에 다음이 필요합니다:

| 전제 조건          | 설명                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| SEEN 캠페인   | 이 파트너십을 이용하려면 SEEN 캠페인이 필요합니다.                                                                     |
| 데이터 소스   | 동영상을 맞춤 설정하려면 SEEN에 데이터를 전송해야 합니다. Braze에서 모든 관련 데이터를 사용할 수 있는지, 그리고 식별자로 **braze_id를** 사용하여 데이터를 전달하는지 확인하세요. |
| Braze 데이터 변환 웹훅 URL   | Braze 데이터 변환은 SEEN에서 들어오는 데이터를 Braze의 /사용자/트랙 엔드포인트에서 받아들일 수 있도록 형식을 다시 지정하는 데 사용됩니다. |

## 사용량 제한

SEEN API는 현재 시간당 1,000건의 호출을 처리하고 있습니다.

## SEEN과 Braze 통합

다음 예시에서는 동영상 생성을 위해 사용자의 데이터를 SEEN으로 전송하고, 고유한 랜딩 페이지 링크와 개인화된 고유 썸네일을 다시 Braze로 전송하여 배포합니다. 이 예에서는 POST 웹훅을 사용하여 데이터를 SEEN으로 전송하고 데이터 변환을 통해 데이터를 Braze로 다시 수신합니다. SEEN을 사용하는 동영상 캠페인이 여러 개 있는 경우, 이 과정을 반복하여 모든 동영상 캠페인에 Braze를 연결합니다.

{% alert tip %}
문제가 발생하면 SEEN 고객 성공 관리자에게 문의하여 도움을 받으세요.
{% endalert %}

### 1단계: 웹훅 캠페인 생성

Braze에서 새 [웹훅 캠페인을]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks) 만듭니다. 캠페인에 이름을 지정한 다음 다음 표를 참조하여 웹훅을 작성하세요:

{% raw %}
<table>
  <thead>
    <tr>
      <th><strong>필드</strong></th>
      <th><strong>세부 정보</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>웹훅 URL</strong></td>
      <td>다음 웹훅 URL을 사용합니다. 귀하는 다음을 받게 됩니다. <code>campaign_slug</code> 를 눌러 올바른 엔드포인트를 호출하세요.<br><br><code>https://api.seen.io/v1/campaigns/{campaign_slug}/receivers/</code></td>
    </tr>
    <tr>
      <td><strong>HTTP 메서드</strong></td>
      <td>사용 <code>POST</code> 메서드를 사용합니다.</td>
    </tr>
    <tr>
      <td><strong>요청 본문</strong></td>
      <td>요청 본문을 다음과 유사한 원시 텍스트로 입력합니다.<br><br><pre><code>[
    {
    "first_name":"{{${first_name}}}",
    "last_name":"{{${last_name}}}",
    "email":"{{${email_address}}}",
    "customer_id":"{{${braze_id}}}"
    }
]</code></pre><br>자세한 내용은 <a href="https://docs.seen.io/api-documentation/ntRoJJ3rXoHzFXhA94JiHB/overview/tvy2F5tS3JRM7DfcHwz5fK#request-content">SEEN API를</a> 참조하세요.</td>
    </tr>
    <tr>
      <td><strong>요청 헤더</strong></td>
      <td>다음 정보를 사용하여 요청 헤더를 작성하세요:<br>- <strong>권한 부여:</strong> <code>Token {token}</code><br>- <strong>콘텐츠 유형:</strong> <code>application/json</code><br><br>SEEN에서 인증 토큰을 받게 됩니다.</td>
    </tr>
  </tbody>
</table>
{% endraw %}
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

이제 **테스트** 탭으로 전환하여 사용자와 함께 웹훅을 테스트할 수 있습니다.

모든 것이 의도한 대로 작동하면 Braze로 이동한 다음 캠페인이 전송하는 속도를 **분당 10개의 메시지로** 설정합니다. 이렇게 하면 SEEN의 시간당 통화 한도인 1,000건을 초과하지 않습니다.

### 2단계: 데이터 변환 생성

1. `landing_page_url` 및 `email_thumbnail_url` 에 대한 새 [사용자 지정 속성]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) 필드를 만듭니다. 이 예제에서 사용할 두 가지 속성은 다음과 같습니다.
2. **데이터 설정에서** [데이터 변환을]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/creating_a_transformation/#prerequisites) 열고 **변환 만들기를** 선택합니다.
3. 변환에 이름을 지정한 다음 **처음부터 시작을** 선택하고 **대상을** **POST로 설정합니다: 사용자 추적**.
4. **SEEN과 웹훅 URL 공유를** 선택합니다.
5. 아래 코드를 변환의 시작점으로 사용할 수 있습니다:

```javascript
let brazecall = {
  "attributes": [
    {
      "braze_id": payload.customer_id,
      "_update_existing_only": true,
      "landing_page_url": payload.landing_page_url,
      "email_thumbnail_url": payload.email_thumbnail_url
    }
  ]
};
return brazecall;
```
{% alert note %}
다른 데이터를 포함하려면 해당 데이터도 포함해야 합니다. 콜백 페이로드에 필요한 모든 필드가 포함되도록 SEEN과도 논의하는 것을 잊지 마세요.
{% endalert %}

{: start="6"}
6\. 제공된 엔드포인트로 테스트 페이로드를 전송합니다. [SEEN 문서에](https://docs.seen.io/api-documentation/ntRoJJ3rXoHzFXhA94JiHB/callbacks/k9DEbcgkq3Vr2pxbHyPQbp) 정의된 콜백 페이로드를 사용하려면 [Postman](https://www.postman.com/) 또는 다른 유사한 서비스를 사용하여 직접 보낼 수 있습니다:

```json
{
        "customer_id": "101",
        "campaign_slug": "onboarding",
        "landing_page_url": "your.subdomain.com/v/12345",
        "video_url": "https://motions.seen.io/298abdcf-1f0f-46e7-9c26-a35b4c1e83cc/d3c1dffdf063986ad521a63e3e68fd7d1100c90a/output.m3u8",
        "thumbnail_url": "https://motions.seen.io/298abdcf-1f0f-46e7-9c26-a35b4c1e83cc/d3c1dffdf063986ad521a63e3e68fd7d1100c90a/thumbnail.jpg",
        "email_thumbnail_url": "https://motions.seen.io/298abdcf-1f0f-46e7-9c26-a35b4c1e83cc/d3c1dffdf063986ad521a63e3e68fd7d1100c90a/email_thumbnail.jpg"
       
}
```

{: start="7"}
7\. **유효성 검사를** 선택하여 모든 것이 의도한 대로 작동하는지 확인합니다.
8\. **저장** 및 **활성화를** 선택합니다.
