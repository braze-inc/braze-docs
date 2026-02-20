---
nav_title: LiftIgniter
article_title: LiftIgniter
alias: /partners/liftigniter/
description: "This reference article outlines the partnership between Braze and LiftIgniter, a leading personalization platform, helping enterprises transform their customer experiences."
page_type: partner
search_tag: Partner

---

# Liftigniter

> [LiftIgniter는](https://www.liftigniter.com/) 기업이 모든 터치포인트에서 실시간 개인화를 통해 고객 경험을 혁신할 수 있도록 지원하는 선도적인 개인화 플랫폼입니다.

_This integration is maintained by Liftigniter._

## 통합 정보

LiftIgniter와 Braze의 통합은 연결된 콘텐츠를 사용하여 뉴스 기사, 의류, 기타 리테일 아이템 및 동영상과 같은 흥미로운 주제를 추천할 수 있도록 합니다.

## 필수 조건

| Requirement| Description|
| ---| ---|
| LiftIgniter account | A [LiftIgniter account](https://console.liftigniter.com/login) is required to take advantage of this partnership. |
| LiftIgniter API integration | You must [integrate](https://support.liftigniter.com/support/solutions/articles/30000024667-api-integration-overview) LiftIgniter into your site or app to be able to pull recommendations from there. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integration

Use [LiftIgniter's REST API](https://documenter.getpostman.com/view/2166502/liftigniter/7TFGvSV#9bdf75da-edd6-45ec-9c28-a0edefad1389) to insert personalized content into your messages. After you have your LiftIgniter account and LiftIgniter is integrated into your app, add the following template into your message composer to call content into your messages, replacing information as needed (`x-api-key`, `theapikey`, etc.).

{% raw %}
```
{% connected_content https://query.petametrics.com/v3/lkdk9usg5av95fvs/userId/model :method post :headers {"x-api-key": "theapikey"} :body "UseActivity"=false :content_type application/json :save json %}
```

Next, write your message, defining the content you would like to call with JSON. For example, `{{json.items[0].title}}`.

{% endraw %}

![LiftIgniter의 특정 연결된 콘텐츠 호출이 포함된 푸시 캠페인을 보여주는 이미지. 이미지 필드에 연결된 콘텐츠 로직도 추가되었습니다.]({% image_buster /assets/img/liftigniter.png %})

이 메시지를 작성기 본문에 입력하면 메시지를 미리 볼 수 있습니다. 다음 예시와 같이 이미지를 가져올 수도 있습니다:

![메시지가 전송된 후 어떤 모습일지 미리 볼 수 있는 이미지입니다.]({% image_buster /assets/img/liftigniter2.png %})


