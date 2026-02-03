---
nav_title: Certona
article_title: Certona
alias: /partners/certona/
description: "This reference article outlines the partnership between Braze and Certona, a real-time, omnichannel personalization solution that offers personalization across the customer lifecycle. Use Certona with Braze Connected Content partner to easily insert content recommendations across multichannel campaigns."
page_type: partner
search_tag: Partner

---

# Certona

> [Certona의](https://www.certona.com/) 플랫폼은 고객 생애주기 전반에 걸쳐 개인화를 촉진합니다. From highly individualized email campaigns to machine-learning-powered product recommendations, Certona ensures that you're harnessing the power of personalization.

_This integration is maintained by Certona._

## 통합 정보

Braze와 Certona의 통합은 연결된 콘텐츠를 통해 Braze 캠페인과 캔버스에서 Certona의 머신 러닝 제품 추천을 사용합니다.

## 필수 조건

| Requirement| Description|
| ---| ---|
| [Certona account](https://manage.certona.com/) | A Certona account is required to take advantage of this partnership. |
| [Certona REST API endpoint](https://manage.certona.com/) | This endpoint is used directly in your Braze campaign message to pull recommended content based on user ID. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Use Certona's REST API to insert personalized content into your messages. This can be done by adding the following Connected Content template into your Braze message composer along with your Certona REST API endpoint.

{% raw %}
```liquid
{% connected_content {CERTONA_REST_API_KEY} :save recommendations %}
```

Next, define the content you would like to call such as relevant text or images. For example, `{{recommendations.CertonaObject.RecommendedItems[0].Items[0].name}}`.

{% endraw %}

![메시지 본문에 Certona 관련 커넥티드 콘텐츠가 포함된 푸시 캠페인 이미지입니다.]({% image_buster /assets/img/certona.png %})

이 메시지를 작성기 본문에 입력한 후에는 연결된 콘텐츠 호출을 미리 보고 올바른 정보를 표시했는지 확인합니다.

![사용자가 메시지를 보내기 전에 철저히 테스트하도록 권장하는 '테스트' 탭을 보여주는 이미지입니다.]({% image_buster /assets/img/certona2.png %})


