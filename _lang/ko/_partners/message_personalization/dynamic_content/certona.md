---
nav_title: Certona
article_title: Certona
alias: /partners/certona/
description: "이 참조 문서에서는 고객 생애주기 전반에 걸쳐 개인화를 제공하는 실시간 옴니채널 개인화 솔루션인 Certona와 Braze 간의 파트너십을 간략히 설명합니다. Use Certona with Braze Connected Content partner to easily insert content recommendations across multichannel campaigns."
page_type: partner
search_tag: Partner

---

# Certona

> Certona 플랫폼은 고객 생애주기 전반에서 개인화를 촉진합니다. 고도로 개인화된 이메일 캠페인부터 머신러닝 기반 제품 추천에 이르기까지 Certona는 개인화의 힘을 활용할 수 있도록 지원합니다.

_This integration is maintained by Certona._

## 통합 정보

Braze와 Certona의 통합은 연결된 콘텐츠를 통해 Braze 캠페인과 캔버스에서 Certona의 머신 러닝 제품 추천을 활용합니다.

## 필수 조건

| 요구 사항| 설명|
| ---| ---|
| [Certona 계정](https://manage.certona.com/) | 이 파트너십을 이용하려면 Certona 계정이 필요합니다. |
| [Certona REST API 엔드포인트](https://manage.certona.com/) | 이 엔드포인트는 사용자 ID를 기반으로 추천 콘텐츠를 가져오기 위해 Braze 캠페인 메시지에서 직접 사용됩니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

Certona의 REST API를 사용하여 메시지에 개인화된 콘텐츠를 삽입할 수 있습니다. Certona REST API 엔드포인트와 함께 다음 연결된 콘텐츠 템플릿을 Braze 메시지 작성기에 추가하여 이 작업을 수행할 수 있습니다.

{% raw %}
```liquid
{% connected_content {CERTONA_REST_API_KEY} :save recommendations %}
```

그런 다음, 관련 텍스트나 이미지 등 호출하려는 콘텐츠를 정의합니다. 예: `{{recommendations.CertonaObject.RecommendedItems[0].Items[0].name}}`.

{% endraw %}

![메시지 본문에 Certona 관련 커넥티드 콘텐츠가 포함된 푸시 캠페인 이미지입니다.][1]

이 메시지를 작성기 본문에 입력한 후에는 연결된 콘텐츠 호출을 미리 보고 올바른 정보를 표시했는지 확인합니다.

![사용자가 메시지를 보내기 전에 철저히 테스트하도록 권장하는 '테스트' 탭을 보여주는 이미지입니다.][2]


[1]: {% image_buster /assets/img/certona.png %}
[2]: {% image_buster /assets/img/certona2.png %}