---
nav_title: 시트 랩
article_title: 시트 랩
description: "이 참고 문서에서는 스프레드시트에서 가져온 데이터로 마케팅 캠페인을 맞춤화할 수 있는 서비스인 Braze와 Sheetlabs의 파트너십에 대해 설명합니다."
alias: /partners/sheetlabs/
page_type: partner
search_tag: Partner

---

# 시트 랩

> [Sheetlabs][1]는 스프레드시트를 강력하고 잘 문서화된 API로 전환할 수 있는 플랫폼입니다. Google 시트나 Excel에서 데이터를 가져와서 API로 변환한 다음, Braze와 같은 다른 애플리케이션에서 해당 API를 사용할 수 있습니다.

_This integration is maintained by Sheetlabs._

## 통합 정보

Sheetlabs와 Braze 통합을 통해 [연결된 콘텐츠][2]를 활용하여 Braze 마케팅 캠페인에 Sheetlabs API를 포함할 수 있습니다. 이는 일반적으로 마케팅 팀에서 직접 업데이트하는 Google 스프레드시트와 Braze 템플릿 사이의 가교 역할을 하는 데 사용됩니다. 이를 통해 번역이나 대규모 사용자 지정 속성 세트와 같은 Braze 템플릿으로 더 많은 것을 달성할 수 있습니다.

## 전제 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Sheetlabs 계정 | 이 파트너십을 활용하려면 [Sheetlabs 계정][1]이 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 사용 사례

Braze와 Sheetlabs의 통합을 통해 다음과 같은 사용 사례를 달성할 수 있습니다:

1. **마케터 액세스 권한과 Braze 캠페인 액세스 권한을 분리합니다**: 일부 팀은 Braze 템플릿과 콘텐츠를 직접 구성할 수 있는 권한을 모든 직원에 부여하지 않기를 원할 수 있습니다. 대신 직원들이 스프레드시트에서 마케팅 콘텐츠를 업데이트하기를 원합니다. Sheetlabs는 스프레드시트와 Braze를 연결하는 가교 역할을 하며 실시간으로 업데이트할 수 있습니다.
2. **번역**: Braze 템플릿은 기본적으로 번역을 지원하지 않습니다. 여러 언어를 지원하려면 여러 템플릿을 만들어야 합니다. Sheetlabs와 Braze를 함께 사용하면 하나의 Braze 템플릿을 여러 언어로 번역할 수 있습니다.
3. **사용자 지정 속성 확장하기**: Braze는 구성할 수 있는 특정 수의 사용자 지정 속성을 제공합니다. Sheetlabs를 Braze와 함께 사용하면 이 초기 할당량 외에 추가 커스텀 속성을 추가할 수 있습니다.

이러한 사용 사례에 대한 자세한 내용은 [Sheetlabs][3]를 참조하세요.

## 통합

### 1단계: 스프레드시트를 Sheetlabs로 가져오기

Sheetlabs에서 Excel 스프레드시트를 업로드하거나 Google 계정을 연결하고 Google 시트를 가져옵니다. 

- Excel 스프레드시트를 가져오려면 메뉴 표시줄에서 **데이터 테이블**을 클릭한 다음, **CSV/Excel에서 가져오기**를 클릭합니다.
- Google 스프레드시트에서 가져오려면 메뉴 표시줄에서 **데이터 테이블**을 클릭한 다음, **Google에서 가져오기**를 클릭합니다. 그런 다음 Google 로그인 자격 증명을 제공하고 시트를 가져와야 합니다.

또한 Google 시트를 동기화 상태로 유지하도록 선택할 수도 있습니다. 즉, 시트가 변경될 때 Sheetlabs가 자동으로 Google 시트에서 최신 데이터를 가져옵니다.

나중에 조회할 때 사용할 수 있도록 스프레드시트나 다른 곳에 Braze 사용자 ID를 포함하세요.

### 2단계: Sheetlabs에서 API 만들기

그런 다음, Sheetlabs에서 **API > API 생성**으로 이동하여 API의 이름을 제공합니다. 스프레드시트의 조회 필드(예: Braze 사용자 ID)를 통해 쿼리를 허용할 수 있습니다.

이 시점에서 다음과 같은 링크를 통해 API에 액세스할 수 있어야 합니다.<br> [`https://sheetlabs.com/ACME/email1_translations?country=en`][4].

### 3단계: Braze 연결된 콘텐츠에서 API 사용

API에 액세스할 수 있으므로 연결된 콘텐츠 호출에 사용할 수 있습니다. 다음은 번역 템플릿의 모습에 대한 예시입니다:

{% raw %}
```js
{% connected_content https://sheetlabs.com/ACME/email1_translations?country={{${country}}} :save translations %}

{{translations[0].greeting}} {{${first_name}}},

{{translations[0].message_body}}
```
{% endraw %}

{% alert tip %}
Sheetlabs와의 통합에 대한 더 많은 예제와 조언은 [Sheetlabs 설명서](https://app.sheetlabs.com/docs/producers/braze/)를 참조하세요.
{% endalert %}



[1]: https://sheetlabs.com/
[2]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
[3]: https://app.sheetlabs.com/docs/producers/braze/
[4]: https://sheetlabs.com/ACME/email1_translations?country=en