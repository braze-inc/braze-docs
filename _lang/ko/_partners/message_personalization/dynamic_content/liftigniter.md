---
nav_title: LiftIgniter
article_title: LiftIgniter
alias: /partners/liftigniter/
description: "이 참조 문서에서는 기업이 고객 경험을 혁신할 수 있도록 지원하는 선도적인 개인화 플랫폼인 Braze와 LiftIgniter의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner

---

# Liftigniter

> LiftIgniter는 선도적인 개인화 플랫폼으로, 기업이 모든 접점에서 실시간 개인화를 통해 고객 경험을 혁신하도록 돕습니다.

LiftIgniter와 Braze의 통합을 통해 연결된 콘텐츠를 활용하여 브랜드는 뉴스 기사, 의류, 기타 소매유통 품목, 동영상 등의 흥미로운 주제를 추천할 수 있습니다.

## 필수 조건

| 요구 사항| 설명|
| ---| ---|
| LiftIgniter 계정 | 이 파트너십을 이용하려면 [LiftIgniter 계정이](https://console.liftigniter.com/login) 필요합니다. |
| LiftIgniter API 통합 | 사이트 또는 앱에서 추천을 가져올 수 있으려면 LiftIgniter를 사이트 또는 앱에 [통합](https://support.liftigniter.com/support/solutions/articles/30000024667-api-integration-overview)해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 통합

[LiftIgniter의 REST API를](https://documenter.getpostman.com/view/2166502/liftigniter/7TFGvSV#9bdf75da-edd6-45ec-9c28-a0edefad1389) 사용하여 메시지에 개인화된 콘텐츠를 삽입하세요. LiftIgniter 계정이 있고 LiftIgniter가 앱에 통합된 후, 메시지 작성기에 다음 템플릿을 추가하여 필요에 따라 정보를 대체하면서 콘텐츠를 메시지로 호출합니다(`x-api-key`, `theapikey` 등).

{% raw %}
```
{% connected_content https://query.petametrics.com/v3/lkdk9usg5av95fvs/userId/model :method post :headers {"x-api-key": "theapikey"} :body "UseActivity"=false :content_type application/json :save json %}
```

다음으로, JSON으로 호출하려는 콘텐츠를 정의하여 메시지를 작성합니다. 예: `{{json.items[0].title}}`.

{% endraw %}

![LiftIgniter의 특정 연결된 콘텐츠 호출이 포함된 푸시 캠페인을 보여주는 이미지. 이미지 필드에 연결된 콘텐츠 로직도 추가되었습니다.][1]

이 메시지를 작성기 본문에 입력하면 메시지를 미리 볼 수 있습니다. 다음 예시와 같이 이미지를 가져올 수도 있습니다:

![메시지가 전송된 후 어떤 모습일지 미리 볼 수 있는 이미지입니다.][2]

[1]: {% image_buster /assets/img/liftigniter.png %}
[2]: {% image_buster /assets/img/liftigniter2.png %}