---
nav_title: Judo
article_title: Judo
description: "이 참조 문서에서는 iOS 및 Android 앱에 위치 컨텍스트와 추적 기능을 추가할 수 있는 노코드 서버 기반 UI 플랫폼인 Judo와 Braze 간의 파트너십을 간략히 설명합니다."
alias: /partners/judo/
page_type: partner
search_tag: Partner

---

# Judo

> [Judo](https://judo.app)는 게시자가 앱 업데이트 없이도 풍부하고 매력적인 인앱 사용자 경험을 효율적으로 제공할 수 있도록 지원하는 서버 기반 UI 플랫폼입니다.

_This integration is maintained by Judo._

## 통합 정보

Braze와 Judo의 통합을 통해 캠페인과 캔버스에서 맞춤형 경험을 제공합니다. Braze 캠페인은 단순한 템플릿 랜딩 페이지 경험 대신, 여러 화면, Modal, 비디오, 커스텀 글꼴, 다크 모드 및 접근성과 같은 지원 설정으로 구성된 콘텐츠를 통합하여 코드 없이 구축되고 앱 업데이트 없이 배포할 수 있습니다. 또한 Braze의 데이터는 Judo 경험에서 개인화된 콘텐츠를 지원하기 위해 사용될 수 있습니다. 사용자 이벤트와 경험에서 얻은 데이터는 기여도 및 타겟팅을 위해 Braze에 피드백될 수 있습니다.

## 필수 조건

| 요구 사항 | 설명 |
|---|---|
| 유도 계정 | 이 파트너십을 활용하려면 [Judo](https://www.judo.app/) 계정이 필요합니다. |
| Judo SDK | Judo SDK는 [iOS](https://github.com/judoapp/judo-ios/) 및/또는 [Android](https://github.com/judoapp/judo-android) 앱에 통합되어야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 사용 사례

**온보딩**: Judo를 사용하는 앱 퍼블리셔는 풍부한 네이티브 온보딩 경험을 구축하고 배포합니다. 이제 이러한 경험은 Braze를 통해 조정된 개인화된 크로스채널 온보딩 여정의 한 요소가 될 수 있습니다. 다양한 인앱 흐름의 효과를 테스트하기 위해 앱 업데이트 없이도 경험을 개인화하고 빠르게 업데이트할 수 있습니다.

**전환**: 앱 게시자는 Braze의 데이터를 사용하여 개인화된 풍부한 인앱 경험을 생성함으로써 인앱 구매, 유료 가입 또는 Judo의 통합 훅을 사용한 상황별 판매를 유도할 수 있습니다. 이러한 경험에 대한 액세스는 Braze에서 생성된 참여 마케팅 캠페인을 통해 트리거될 수 있습니다.

**이벤트 기반 콘텐츠**: 스포츠 및 엔터테인먼트에서 Judo의 주요 목적은 이벤트를 미리 보고, 홍보하며, 요약할 수 있는 풍부한 경험을 구축하는 것입니다. 이 기능은 시즌 및 뉴스 중심 콘텐츠를 위한 다른 업종에서도 폭넓게 활용되고 있습니다. 이벤트를 적시에 홍보하거나 강조하기 위한 메시징을 리치 인앱 경험에 연결하면 게시자는 상황별 관련성이 높은 메시지를 전달하여 인게이지먼트를 유도할 수 있습니다.

## SDK 병렬 통합

Judo는 모바일 앱에서 Judo와 Braze SDK를 병렬 통합하는 데 필요한 일부 작업을 자동화하는 추가 라이브러리를 제공합니다. 

### 1단계: Judo-Braze 통합 라이브러리 설치

앱에 Judo-Braze 통합 라이브러리를 설치하고 설정하세요. 그러면 이벤트 추적이 자동으로 활성화됩니다.

- [iOS 설치
지침](https://github.com/judoapp/judo-braze-ios/wiki#installation)
- [Android 설치
지침](https://github.com/judoapp/judo-braze-android/wiki#installation).

### 2단계: 인앱 메시징 구성

이 단계에서는 iOS 및 Android용 커스텀 `ABKInAppMessageControllerDelegate` 및 `IInAppMessageManagerListener` 구현을 생성하는 작업을 포함합니다.

각 통합 라이브러리에 대해 번들로 제공되는 인앱 메시지 설정 설명서를 참조하세요.

- [iOS 인앱 메시징
설정](https://github.com/judoapp/judo-braze-ios/wiki#in-app-messaging-setup)
- [Android 인앱 메시징
설정](https://github.com/judoapp/judo-braze-android/wiki#in-app-messaging-setup).

## 이 통합 사용

앱 측 통합을 완료한 후에는 Judo 경험에 대한 테스트 Braze 인앱 메시지 캠페인을 실행하여 예상대로 실행되는지 확인할 수 있습니다.

### 1단계: 맞춤 코드 인앱 메시지 캠페인 만들기

Braze 플랫폼에서 **사용자 지정 코드** 메시지 유형으로 Braze 인앱 메시지 캠페인을 생성합니다. 그런 다음 사용자 지정 유형으로 **HTML 업로드를** 선택합니다. 메시지 콘텐츠를 기본 인앱 메시징 필드로 채워야 하며, 이 콘텐츠는 사용자에게 표시되지 않습니다.

!['커스텀 코드' 메시지 유형을 선택할 때 대시보드의 모습을 보여주는 이미지.][2]

다음으로 다음과 같은 최소한의 HTML 스니펫을 사용하여 양식 유효성 검사를 충족합니다: 
```
<a href="appboy://close">X</a>
```

Judo에서 다시 작성하고 이를 Judo 경험으로 대체하므로 프로덕션의 기기에는 표시되지 않습니다.

![캠페인의 작성 단계에 추가된 양식 유효성 검사 코드를 보여주는 이미지입니다.][3]

### 2단계: 유도용 키-값 쌍 설정하기
![이 이미지에서는 이 통합에 필요한 하나의 키-값 페어를 보여줍니다. 이때 '키'는 'Judo 경험'이고 '값'은 Judo 링크입니다.][4]{: style="float:right;max-width:50%;margin-left:15px;"}

캠페인에서 [커스텀 키-값 페어]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/)를 `judo-experience` 키와 함께 설정합니다. 여기에 표시하려는 Judo 경험의 URL을 제공합니다. 그러면 Judo-Braze 통합 라이브러리가 핸들러에서 이 키-값 페어를 감지하고 이를 사용하여 표준 Braze 인앱 메시지 UI 대신 Judo 경험을 삽입합니다.
<br><br>
### 3단계: 캠페인 마무리하기

마지막으로 캠페인 트리거를 설정하고 **배달** 및 **타겟 사용자** 섹션의 세그먼트를 통해 사용자를 선택하여 캠페인을 완료합니다. Braze 인앱 메시지의 다양한 구성 요소에 대해서는 인앱 메시지 [문서를]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/) 참조하세요.


[2]: {% image_buster /assets/img/judo/braze-campaign-select-custom-type.png %}
[3]: {% image_buster /assets/img/judo/braze-html-boilerplate.png %}
[4]: {% image_buster /assets/img/judo/braze-campaign-extras-judo-experience.png %}
