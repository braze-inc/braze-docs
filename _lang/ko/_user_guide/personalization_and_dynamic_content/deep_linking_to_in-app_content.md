---
nav_title: 앱 내 콘텐츠에 딥링킹하기
article_title: 인앱 콘텐츠 딥링킹
page_order: 3
description: "이 참조 문서에서는 인앱 메시지 콘텐츠에 딥링킹을 추가하는 방법에 대한 지침을 다룹니다."

---

# 앱 내 콘텐츠에 딥링킹하기

## 딥링킹이란 무엇인가요?

딥링킹은 네이티브 앱을 실행하고 특정 작업을 수행하거나 특정 콘텐츠를 표시하도록 추가 정보를 제공하는 방식입니다.

여기에는 세 가지 부분이 있습니다:

1. 실행할 앱을 식별합니다.
2. 앱에 어떤 작업을 수행할지 지시하세요.
3. 작업에 필요한 추가 데이터를 제공하세요.

딥링크는 앱의 특정 부분으로 연결되는 커스텀 URI로, 이 세 가지 부분이 모두 포함되어 있습니다. `http:` 은 거의 모든 사람에게 익숙한 체계이지만 체계는 어떤 단어로도 시작할 수 있습니다. 구성표는 문자로 시작해야 하지만 문자, 숫자, 더하기 기호, 빼기 기호 또는 점을 포함할 수 있습니다. 실제로는 충돌을 방지하는 중앙 레지스트리가 없으므로 도메인 네임을 계획에 포함하는 것이 가장 좋습니다. 예를 들어 `twitter://` 은 X(이전 트위터)용 모바일 앱을 실행하기 위한 iOS URI입니다.

딥링크 내 콜론 이후의 모든 내용은 자유 형식 텍스트입니다. 구조와 해석을 정의하는 것은 사용자의 몫이지만, 일반적인 규칙은 선행 `//` 및 쿼리 매개변수(예: `?foo=1&bar=2`)를 포함하여 `http:` URL을 따라 모델링하는 것입니다. 이전 예제에서 `twitter://user?screen_name=[id]` 은 앱에서 특정 프로필을 실행하는 데 사용됩니다.

{% alert important %}
Braze는 Flutter와 같은 래퍼를 사용하여 딥링킹을 전송하는 것을 지원하지 않습니다. 이 기능을 사용하려면 네이티브 레이어에서 딥링크를 구성해야 합니다.
{% endalert %}

## UTM 태그 및 캠페인 기여도

### UTM 태그란 무엇인가요?

[UTM(Urchin Traffic Manager) 태그를](https://support.google.com/analytics/answer/10917952?sjid=14344007686729081565-NC#zippy=%2Cin-this-article) 사용하면 링크 내에 캠페인 기여도 세부 정보를 직접 포함할 수 있습니다. UTM 태그는 Google 애널리틱스에서 캠페인 기여도 데이터를 수집하는 데 사용되며, 다음 속성을 추적하는 데 사용할 수 있습니다:

- `utm_source`: 트래픽 소스에 대한 식별자(예:`my_app`)
- `utm_medium`: 캠페인 매체(예:`newsfeed`)
- `utm_campaign`: 캠페인의 식별자(예:`spring_2016_campaign`)
- `utm_term`: 사용자를 앱 또는 웹사이트로 유도한 유료 검색어의 식별자(예:`pizza`)
- `utm_content`: 사용자가 클릭한 특정 링크 또는 콘텐츠의 식별자(예:`toplink` 또는 `android_iam_button2`)

UTM 태그는 일반 HTTP(웹) 링크와 딥링크 모두에 임베드할 수 있으며 Google 애널리틱스를 사용하여 추적할 수 있습니다.

### Braze와 함께 UTM 태그 사용

이메일 캠페인에 대한 캠페인 기여도 분석을 위해 일반 HTTP(웹) 링크와 함께 UTM 태그를 사용하려는 경우(예: 조직에서 이미 Google 애널리틱스를 사용하고 있는 경우), [Google의 URL 작성기를](https://ga-dev-tools.google/ga4/campaign-url-builder/) 사용하여 UTM 링크를 생성할 수 있습니다. 이러한 링크는 다른 링크와 마찬가지로 Braze 캠페인 카피에 쉽게 삽입할 수 있습니다.

앱에 대한 딥링크에서 UTM 태그를 사용하려면 앱에 관련 [Google 애널리틱스 SDK가](https://developers.google.com/analytics/devguides/collection/) 통합되어 있고 딥링크를 처리하도록 올바르게 구성되어 있어야 합니다. 확실하지 않은 경우 개발자에게 문의하세요.

분석 SDK가 통합 및 구성되면 UTM 태그를 Braze 캠페인에서 딥링크와 함께 사용할 수 있습니다. 캠페인에 대한 UTM 태그를 설정하려면 대상 URL 또는 딥링크에 필요한 UTM 태그를 포함하세요. 다음 예시는 푸시 알림 및 인앱 메시지에서 UTM 태그를 사용하는 방법을 보여줍니다.

#### UTM 태그로 푸시 열기 속성 기여도 부여하기

푸시 알림용 딥링크에 UTM 태그를 포함하려면 푸시 메시지의 클릭 시 동작을 딥링크로 설정한 다음 딥링크 주소를 작성하고 다음과 같은 방식으로 원하는 UTM 태그를 포함하세요:

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=push&utm_campaign=spring2016giftcards&utm_content=ios_deeplink
```

\![]({% image_buster /assets/img_archive/push_utm_tags.png %})

#### UTM 태그로 인앱 메시지 클릭 기여도 어트리뷰션하기

인앱 메시징의 딥링크에 UTM 태그를 포함하려면 다음을 사용하세요:

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=iam&utm_campaign=spring2021giftcards&utm_content=web_link
```

\![]({% image_buster /assets/img_archive/iam_utm_tags.png %})

