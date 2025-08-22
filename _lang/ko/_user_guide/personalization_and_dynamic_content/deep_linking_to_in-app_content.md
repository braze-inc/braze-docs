---
nav_title: 인앱 콘텐츠 딥링킹
article_title: 인앱 콘텐츠 딥링킹
page_order: 3
description: "이 참조 문서에서는 인앱 메시지 콘텐츠에 딥링크를 추가하는 방법에 대한 지침을 다룹니다."

---

# 인앱 콘텐츠에 대한 딥링킹

## 딥링킹이란 무엇인가요?

Deep linking is a way of launching a native app and providing additional information telling it to do a specific action or show specific content.

여기에는 세 가지 부분이 있습니다:

1. Identify which app to launch.
2. Instruct the app on which action to perform.
3. Provide the action with any additional data it will need.

딥링크는 앱의 특정 부분으로 연결되며 이 세 가지 부분을 모두 포함하는 사용자 지정 URI입니다. 커스텀 스키마를 정의하는 것이 핵심입니다. `http:`는 거의 모든 사람에게 익숙한 스키마이지만 스키마는 어떤 단어로도 시작할 수 있습니다. 구성표는 문자로 시작해야 하지만 문자, 숫자, 더하기 기호, 빼기 기호 또는 점을 포함할 수 있습니다. 실제로는 충돌을 방지하는 중앙 레지스트리가 없으므로 도메인 네임을 이 체계에 포함하는 것이 가장 좋습니다. 예를 들어 `twitter://`은 X(이전 트위터)용 모바일 앱을 실행하기 위한 iOS URI입니다.

딥링크 내 콜론 이후의 모든 내용은 자유 형식 텍스트입니다. It's up to you to define its structure and interpretation; however, a common convention is to model it after `http:` URLs, including a leading `//` and query parameters (for example, `?foo=1&bar=2`). 이전 예제에서 `twitter://user?screen_name=[id]`는 앱에서 특정 프로필을 실행하는 데 사용됩니다.

{% alert important %}
Braze doesn't support using a wrapper like Flutter to send deep links. 이 기능을 사용하려면 네이티브 레이어에서 딥 링크를 구성해야 합니다.
{% endalert %}

## UTM 태그 및 캠페인 어트리뷰션

### UTM 태그란 무엇인가요?

[UTM (Urchin Traffic Manager) tags](https://support.google.com/analytics/answer/10917952?sjid=14344007686729081565-NC#zippy=%2Cin-this-article) allow you to include campaign attribution details directly within links. UTM 태그는 Google 애널리틱스에서 캠페인 어트리뷰션 데이터를 수집하는 데 사용되며, 다음 속성을 추적하는 데 사용할 수 있습니다:

- `utm_source`: The identifier for the source of the traffic (for example,`my_app`)
- `utm_medium`: The campaign medium (for example,`newsfeed`)
- `utm_campaign`: The identifier for the campaign (for example,`spring_2016_campaign`)
- `utm_term`: Identifier for a paid search term that brought the user to your app or website (for example,`pizza`)
- `utm_content`: An identifier for the specific link or content that the user clicked on (for example,`toplink` or `android_iam_button2`)

UTM 태그는 일반 HTTP(웹) 링크와 딥링크에 모두 임베드할 수 있으며 Google 애널리틱스를 사용하여 추적할 수 있습니다.

### Braze에서 UTM 태그 사용

If you want to use UTM tags with regular HTTP (web) links (for example, to do campaign attribution for your email campaigns) and your organization already uses Google Analytics, you can use [Google's URL builder](https://ga-dev-tools.google/ga4/campaign-url-builder/) to generate UTM links. 이러한 링크는 다른 링크와 마찬가지로 Braze 캠페인 카피에 쉽게 삽입할 수 있습니다.

To use UTM tags in deep links to your app, your app must have the relevant [Google Analytics SDK](https://developers.google.com/analytics/devguides/collection/) integrated and correctly configured to handle deep links. 확실하지 않은 경우 개발자에게 문의하세요.

Analytics SDK가 통합되고 구성된 후, UTM 태그는 Braze 캠페인에서 딥 링크와 함께 사용할 수 있습니다. 캠페인을 위한 UTM 태그를 설정하려면, 대상 URL 또는 딥 링크에 필요한 UTM 태그를 포함하세요. 다음 예는 푸시 알림 및 인앱 메시지에서 UTM 태그를 사용하는 방법을 보여줍니다.

#### UTM 태그로 푸시 열기 어트리뷰션

푸시 알림을 위한 딥링크에 UTM 태그를 포함하려면, 푸시 메시지의 클릭 동작을 딥링크로 설정한 다음, 딥링크 주소를 작성하고 원하는 UTM 태그를 다음과 같은 방식으로 포함하세요:

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=push&utm_campaign=spring2016giftcards&utm_content=ios_deeplink
```

![]({% image_buster /assets/img_archive/push_utm_tags.png %})

#### UTM 태그를 사용한 인앱 메시지 클릭 어트리뷰션

앱 내 메시지의 딥 링크에 UTM 태그를 포함하려면 다음을 사용하세요:

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=iam&utm_campaign=spring2021giftcards&utm_content=web_link
```

![]({% image_buster /assets/img_archive/iam_utm_tags.png %})

