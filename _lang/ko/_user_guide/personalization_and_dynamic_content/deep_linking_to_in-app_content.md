---
nav_title: 인앱 콘텐츠 딥링킹
article_title: 인앱 콘텐츠 딥링킹
page_order: 3
description: "이 참조 문서에서는 인앱 메시지 콘텐츠에 딥링크를 추가하는 방법에 대한 지침을 다룹니다."

---

# 인앱 콘텐츠에 대한 딥링킹

## 딥링킹이란 무엇인가요?

딥링킹은 네이티브 앱을 실행하고 특정 작업을 수행하거나 특정 콘텐츠를 표시하도록 추가 정보를 제공하는 방법입니다.

여기에는 세 가지 부분이 있습니다:

1. 실행할 앱 식별
2. 앱에 어떤 작업을 수행할지 지시하십시오.
3. 작업에 필요한 추가 데이터를 제공하세요.

딥링크는 앱의 특정 부분으로 연결되며 이 세 가지 부분을 모두 포함하는 사용자 지정 URI입니다. 커스텀 스키마를 정의하는 것이 핵심입니다. `http:`는 거의 모든 사람에게 익숙한 스키마이지만 스키마는 어떤 단어로도 시작할 수 있습니다. 구성표는 문자로 시작해야 하지만 문자, 숫자, 더하기 기호, 빼기 기호 또는 점을 포함할 수 있습니다. 실제로는 충돌을 방지하는 중앙 레지스트리가 없으므로 도메인 네임을 이 체계에 포함하는 것이 가장 좋습니다. 예를 들어 `twitter://`은 X(이전 트위터)용 모바일 앱을 실행하기 위한 iOS URI입니다.

딥링크 내 콜론 이후의 모든 내용은 자유 형식 텍스트입니다. 구조와 해석을 정의하는 것은 사용자의 몫이지만, 일반적인 규칙은 선행 `//` 및 쿼리 매개변수(예: `?foo=1&bar=2`)를 포함하여 `http:` URL을 따라 모델링하는 것입니다. 이전 예제에서 `twitter://user?screen_name=[id]`는 앱에서 특정 프로필을 실행하는 데 사용됩니다.

{% alert important %}
Braze는 Flutter와 같은 래퍼를 사용하여 딥링크를 전송하는 것을 지원하지 않습니다. 이 기능을 사용하려면 네이티브 레이어에서 딥 링크를 구성해야 합니다.
{% endalert %}


## UTM 태그 및 캠페인 어트리뷰션

### UTM 태그란 무엇인가요?

[UTM(어치 트래픽 매니저) 태그][4]를 사용하면 링크 내에 캠페인 기여도 세부 정보를 바로 포함할 수 있습니다. UTM 태그는 Google 애널리틱스에서 캠페인 어트리뷰션 데이터를 수집하는 데 사용되며, 다음 속성을 추적하는 데 사용할 수 있습니다:

- `utm_source`트래픽 소스에 대한 식별자(예:`my_app`)
- `utm_medium`캠페인 매체(예:`newsfeed`)
- `utm_campaign`캠페인의 식별자(예:`spring_2016_campaign`)
- `utm_term`사용자를 앱 또는 웹사이트로 유도한 유료 검색어의 식별자(예:`pizza`)
- `utm_content`사용자가 클릭한 특정 링크/콘텐츠의 식별자(예:`toplink` 또는 `android_iam_button2`)

UTM 태그는 일반 HTTP(웹) 링크와 딥링크에 모두 임베드할 수 있으며 Google 애널리틱스를 사용하여 추적할 수 있습니다.

### Braze에서 UTM 태그 사용

이메일 캠페인에 캠페인 어트리뷰션을 수행하기 위해 일반 HTTP(웹) 링크와 함께 UTM 태그를 사용하려는 경우, 조직에서 이미 Google 애널리틱스를 사용하고 있다면 [Google의 URL 빌더를][6] 사용하여 간단히 UTM 링크를 생성할 수 있습니다. 이러한 링크는 다른 링크와 마찬가지로 Braze 캠페인 카피에 쉽게 삽입할 수 있습니다.

앱에 대한 딥 링크에서 UTM 태그를 사용하려면, 귀하의 앱에 관련된 [Google Analytics SDK][5]가 통합되어 있고 딥 링크를 처리하도록 올바르게 구성되어 있어야 합니다. 확실하지 않은 경우 개발자에게 문의하세요.

Analytics SDK가 통합되고 구성된 후, UTM 태그는 Braze 캠페인에서 딥 링크와 함께 사용할 수 있습니다. 캠페인을 위한 UTM 태그를 설정하려면, 대상 URL 또는 딥 링크에 필요한 UTM 태그를 포함하세요. 다음 예는 푸시 알림 및 인앱 메시지에서 UTM 태그를 사용하는 방법을 보여줍니다.

#### UTM 태그로 푸시 열기 어트리뷰션

푸시 알림을 위한 딥링크에 UTM 태그를 포함하려면, 푸시 메시지의 클릭 동작을 딥링크로 설정한 다음, 딥링크 주소를 작성하고 원하는 UTM 태그를 다음과 같은 방식으로 포함하세요:

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=push&utm_campaign=spring2016giftcards&utm_content=ios_deeplink
```

![][8]

#### UTM 태그를 사용한 인앱 메시지 클릭 어트리뷰션

앱 내 메시지의 딥 링크에 UTM 태그를 포함하려면 다음을 사용하세요:

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=iam&utm_campaign=spring2021giftcards&utm_content=web_link
```

![][10]

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/deep_linking/#Android_Deep_Advance
[4]: https://support.google.com/analytics/answer/1033863?hl=en
[5]: https://developers.google.com/analytics/devguides/collection/
[6]: https://support.google.com/analytics/answer/1033867
[8]: {% image_buster /assets/img_archive/push_utm_tags.png %}
[9]: {% image_buster /assets/img_archive/news_feed_utm_tags.png %}
[10]: {% image_buster /assets/img_archive/iam_utm_tags.png %}
[11]: {{site.baseurl}}/user_guide/engagement_tools/news_feed/creating_a_news_feed_item/
