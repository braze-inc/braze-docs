---
nav_title: 콘텐츠
article_title: 콘텐츠
description: "이 참고 문서에서는 커넥티드 콘텐츠를 동적으로 사용하여 콘텐츠풀의 콘텐츠를 브레이즈 캠페인으로 가져올 수 있는 콘텐츠 관리 시스템인 브레이즈와 콘텐츠풀 간의 파트너십에 대해 설명합니다."
alias: /partners/contentful/
page_type: partner
search_tag: Partner
---

# 콘텐츠

>[Contentful은](https://www.contentful.com/) 모든 플랫폼에 콘텐츠를 생성, 관리 및 배포할 수 있는 헤드리스 콘텐츠 관리 시스템입니다. 콘텐츠 관리 시스템(CMS)과 달리 콘텐츠풀에서는 관리할 콘텐츠를 결정할 수 있도록 콘텐츠 모델을 만들 수 있습니다.<br><br>이 페이지에서는 콘텐츠풀의 콘텐츠 전송 API에서 데이터를 가져오도록 Braze 커넥티드 콘텐츠를 구성하는 단계별 가이드를 제공합니다. 

통합 후에는 Contentful의 RESTful API를 사용하여 웹사이트, 모바일 앱(iOS, Android, Windows) 또는 기타 여러 플랫폼과 같은 여러 채널에 콘텐츠를 제공할 수 있습니다. 또한 콘텐츠풀에서 콘텐츠를 동적으로 가져와서 Braze 캠페인에 사용할 수도 있습니다.

## 필수 조건

시작하기 전에 다음이 필요합니다:

| 전제 조건          | 설명                        |
|-----------------------|------------------------------------|
| 콘텐츠가 풍부한 계정 | 콘텐츠 전송 API에 액세스할 수 있는 콘텐츠풀 계정이 필요합니다. |
| Braze 계정 | 커넥티드 콘텐츠 기능에 액세스할 수 있는 Braze 계정이 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

### 1단계: Contentful API 자격 증명 받기

1. 자격 증명을 사용하여 [Contentful에 로그인합니다](https://app.contentful.com/login).
2. **설정** > **API 키로** 이동하여 Contentful 대시보드에서 API 액세스 토큰을 만들거나 검색합니다. 아직 API 키가 없는 경우 새로 생성하세요:<br>2.1 **API 키 추가를** 선택합니다.<br>2.2 필요한 세부 정보를 입력하고 적절한 환경을 선택합니다.<br>2.3 **저장을** 선택하고 **스페이스 ID** 및 **콘텐츠 전송 API - 액세스 토큰을** 기록합니다.
3. Contentful API를 통해 액세스하려는 콘텐츠 모델을 식별합니다.

### 2단계: Braze 커넥티드 콘텐츠 구성

1. 자격 증명을 사용하여 [Braze에 로그인합니다](https://dashboard.braze.com/sign_in).
2. Braze 대시보드에서 **템플릿** > **콘텐츠 블록** > **콘텐츠 블록 만들기** > **HTML 콘텐츠 블록으로** 이동합니다.
3. Contentful의 [Contentful 콘텐츠 전송 API URL에](https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/links) 연결된 콘텐츠 요청을 생성합니다. Contentful 콘텐츠 전송 API URL의 예는 ```https://cdn.contentful.com/spaces/{space_id}/environments/{environment_id}/entries``` 입니다.<br><br> 다양한 자산을 검색하려면 특정 변수를 포함해야 합니다. 예제 커넥티드 콘텐츠 URL 요청은 Contentful의 [엔트리](https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/entries/entry/get-a-single-entry/console) 엔드포인트를 대상으로 합니다. 이 엔드포인트에는 `{space_id}` 및 `{environment_id}`, 또는 `{entry_id}` 및 `{access_token}` 와 같은 변수가 필요합니다. 콘텐츠풀 인스턴스에서 가져올 수 있습니다. 이 콘텐츠 블록 예시에서는 변수를 Contentful 스페이스 ID 및 환경 ID로 바꿔야 합니다.<br><br>예제 콘텐츠 전송 API URL은 Contentful의 사용 가능한 엔드포인트 중 하나만 사용합니다. 다양한 URL을 활용하여 다양한 사용 사례를 달성할 수 있습니다. 예를 들어 [이미지 API를](https://www.contentful.com/developers/docs/references/images-api/) 사용하여 콘텐츠풀에 저장된 이미지를 캡처할 수 있습니다. 자세한 내용은 [콘텐츠 전송 API를](https://www.contentful.com/developers/docs/references/content-delivery-api/) 검토하세요.

{% alert note %}
예를 들어 이미지 API에는 `{asset_id}`, `{unique_id},` 및 `{name}` 와 같이 엔드포인트마다 새로운 변수가 필요할 수 있습니다. 자세한 안내는 Contentful에 문의하세요.
{% endalert %}

{% raw %}
```json
        {% assign space_id = "YOUR-CONTENTFUL-SPACE-ID"}
        {% assign environment_id = "YOUR-CONTENTFUL-ENVIRONMENT-ID"}
        {% assign entry_id = "YOUR-CONTENTFUL-ENTRY-ID"}
        {% assign access_token = "YOUR-CONTENTFUL-ACCESS-TOKEN"}
         {% connected_content https://cdn.contentful.com/spaces/{space_id}/environments/{environment_id}/entries/{entry_id}?access_token={access_token}
         :method get
         :headers {
             "Authorization": "YOUR_CONTENTFUL_ACCESS_TOKEN"
                 }
               :content_type application/json
               :save response %}
```
{% endraw %}

{: start="4"}
4\. "테스트 엔드포인트"를 사용하여 Braze가 Contentful API에 성공적으로 연결하고 원하는 데이터를 검색할 수 있는지 테스트합니다.
5\. **완료를** 선택하여 콘텐츠 블록을 저장합니다.
6\. 콘텐츠 블록에 "Contentful API"와 같은 설명이 포함된 이름을 지정한 다음 **콘텐츠 블록 시작을** 선택합니다.

### 3단계: 캠페인 및 캔버스에서 커넥티드 콘텐츠 사용

1. Braze에서 새 캠페인을 만들거나 기존 캠페인을 편집합니다.
2. 연결된 콘텐츠 블록을 사용하여 Contentful에서 가져온 데이터를 삽입합니다. 구성 중에 정의한 데이터 경로를 사용하여 캠페인 콘텐츠를 동적으로 채울 수 있습니다.<br><br>
- **응답 경로:** 브레이즈 캠페인 또는 캔버스에 콘텐츠 블록을 포함시킨 후, 메시지에 `{response}` 변수를 삽입하면 응답을 사용할 수 있게 됩니다.<br><br>JSON 점 표기법을 사용하면 콘텐츠풀의 응답 본문 중 메시지에 포함할 부분을 지정할 수 있습니다. 이는 사용 사례에 따라 달라질 수 있습니다. 예를 들어 Contentful의 엔트리 엔드포인트에서 제목 값({% raw %}```liquid{{response.items[0].fields.title}}```{% endraw %})을 사용하면 다음과 같은 응답을 받을 수 있습니다:

{% raw %}
```json
   {
  "fields": {
    "title": {
      "en-US": "Hello!"
    },
    "body": {
      "en-US": "This is a sample message!"
    }
  },
  "metadata": {
    "tags": [
      {
        "sys": {
          "type": "Link",
          "linkType": "Tag",
          "id": "nyCampaign"
        }
      }
    ]
  },
  "sys": {
    "id": "5KsDBWseXY6QegucYAoacS",
    "type": "Entry",
    "version": 1,
    "space": {
      "sys": {
        "type": "Link",
        "linkType": "Space",
        "id": "yadj1kx9rmg0"
      }
    },
    "contentType": {
      "sys": {
        "type": "Link",
        "linkType": "ContentType",
        "id": "hfM9RCJIk0wIm06WkEOQY"
      }
    },
    "createdAt": "2016-12-20T10:43:35.772Z",
    "updatedAt": "2016-12-20T10:43:35.772Z",
    "revision": 1
  }
}
```
{% endraw %}

{: start="3" }
3\. 캠페인을 미리 보고 테스트하여 연결된 콘텐츠 데이터가 올바르게 표시되는지 확인합니다.
4\. 설정이 만족스러우면 캠페인을 시작하세요.

## 문제 해결

### API 응답

Contentful API 자격 증명과 엔드포인트 URL이 올바른지 확인하세요. Braze에서 API 호출에 문제가 있을 수 있는 오류 메시지가 있는지 확인합니다.

### 데이터 매핑

응답 경로 매핑이 올바르게 구성되었는지, API 응답 구조가 예상과 일치하는지 확인합니다.

## 추가 자료

- [콘텐츠 전송 API 문서](https://www.contentful.com/developers/docs/references/content-delivery-api/)
- [브레이즈 커넥티드 콘텐츠]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)
- [브레이즈 콘텐츠 블록]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)
