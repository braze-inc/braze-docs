---
nav_title: 배치 생성
article_title: Braze SDK를 위한 배너 카드 배치 만들기
hidden: true
description: "이 참조 문서에서는 배너 카드와 이 기능을 Braze SDK에 통합하는 방법에 대해 설명합니다."
platform:
  - iOS
  - Android
  - Web
  
---

# 배너 카드 배치 만들기

> 앱에서 배너 카드 캠페인을 시작하기 전에 Braze 대시보드에서 배치를 만들어야 합니다. 게재 위치는 앱에서 배너 카드를 표시할 수 있는 위치를 정의하는 것입니다.

{% alert important %}
배너 카드는 현재 얼리 액세스 중입니다. 이번 얼리 액세스에 참여하려면 Braze 계정 관리자에게 문의하세요.
{% endalert %}

## 필수 조건

배너 카드 사용을 시작하기 위한 최소 SDK 버전은 다음과 같습니다:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.6.0 %}

## 배치 생성

### 1단계: 새 게재 위치 만들기

**설정** > **배너 카드 배치**로 이동한 다음 **배치 만들기를** 선택합니다.

![배너 카드 게재 위치 섹션에서 게재 위치 ID를 생성합니다.]({% image_buster /assets/img/banner_cards/create_placement.png %})

### 2단계: 세부 정보 입력

배치에 이름을 지정하고 **배치 ID를** 부여합니다. 원하는 경우 배치에 대한 설명을 추가할 수 있습니다.

마케팅 팀과 협력하여 이 ID를 만드세요. 앱 코드에서 참조할 ID이며, 마케팅 팀은 이 ID를 사용하여 앱의 위치에 캠페인을 할당합니다. 

{% alert important %}
앱 또는 웹사이트와의 연동이 중단될 수 있으므로 실행 후 게재 위치 ID를 수정하지 마세요.
{% endalert %}

![봄 세일 프로모션 캠페인의 경우 배너 카드를 지정하는 배치 세부 정보가 왼쪽 사이드바에 표시됩니다.]({% image_buster /assets/img/banner_cards/placement_details_example.png %})

배너 카드 캠페인을 시작하는 방법에 대한 단계는 [배너 카드 만들기를]({{site.baseurl}}/create_banner_card/) 참조하세요.

## 다음 단계

이제 배너 카드 배치를 생성했으므로 다음을 수행할 수 있습니다:

- 배너 카드 통합
- 배너 카드 만들기
