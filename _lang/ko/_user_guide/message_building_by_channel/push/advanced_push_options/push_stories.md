---
nav_title: "푸시 스토리"
article_title: 푸시 스토리
page_order: 2
page_type: reference
description: "이 참조 문서에서는 푸시 스토리가 무엇인지, 푸시 스토리를 만드는 방법, 자주 묻는 질문에 대해 다룹니다."
channel:
  - push

---

# 푸시 스토리

> 푸시 스토리는 Braze에서 도입한 새로운 유형의 푸시 알림입니다. 이 기능은 Instagram과 Facebook에서 인기를 끌었던 사진 캐러셀 기능을 활용하여, 마케터가 푸시 내에서 페이지 캐러셀을 만들어 풍부하고 일관된 스토리를 전달할 수 있게 합니다. 이 페이지는 이미지, 클릭 동작, 제목 및 설명으로 구성됩니다. 사용자는 이 페이지를 스와이프하여 여러분이 전달하는 스토리를 볼 수 있습니다.

| Android 예시 (확장됨) | IOS 예시 (확장됨) |
| :-----: | :----------: |
| ![]({% image_buster /assets/img_archive/pushstories_android_preview.png %}) | ![]({% image_buster /assets/img_archive/pushstories_ios_preview.png %}) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
iOS SDK 버전 3.13.0 이상에서는 SDK가 이미지를 다운로드하는 방식이 변경되어 첫 번째 이미지의 썸네일이 푸시의 축소된 보기에 표시되지 않습니다. 메시지 문구에서 사용자가 푸시를 확장하여 이미지를 볼 수 있도록 안내해야 합니다.
{% endalert %}

## 필수 조건

푸시 스토리를 수신하려면 다음 SDK 버전이 필요합니다.

{% sdk_min_versions swift:5.0.0 android:2.2.0 %}


## 푸시 스토리 사용 방법

![]({% image_buster /assets/img_archive/pushstories_composer_dropdown2.png %}){: style="float:right;max-width:50%;margin-left:15px;margin-bottom:15px;"}

푸시 스토리를 사용하려면 다음과 같이 하세요:

1. [푸시 캠페인]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/)을 생성합니다.
2. **알림 유형**에서 **푸시 스토리**를 선택합니다.
3. **iOS** 또는 **Android**를 선택합니다. 푸시 메시지에서 두 가지를 모두 선택하면 푸시 스토리 생성 옵션이 표시되지 않습니다. 

### 푸시 스토리 작성기

페이지를 만들려면 다음 단계를 수행하세요:

1. 메인 작성기에서 **페이지 관리**를 클릭합니다.
    <br><br>![]({% image_buster /assets/img_archive/pushstories_add_pages.png %}){: style="max-width:70%"}<br><br>
2. 각 페이지에 이미지를 삽입하고 해당 이미지의 클릭 동작을 설정합니다.
3. 원하는 경우 각 페이지에 **제목** 및 **설명**을 추가합니다. 한 페이지에 제목과 설명을 사용하는 경우 모든 페이지에 삽입해야 합니다.

미리보기가 반영되며 상호작용할 수 있습니다.

![]({% image_buster /assets/img_archive/pushstories_composer.png %}){: style="max-width:60%"}

{% alert important %}
[연결된 콘텐츠]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content)로 이미지를 가져오는 경우 이미지 URL이 `https://`로 시작하는지 확인하세요. `http://`를 사용하면 앱이 충돌합니다.
{% endalert %}

### 이미지 및 텍스트 사양

다음 이미지 및 텍스트 사양은 푸시 스토리의 사진 캐러셀 부분에 적용됩니다. 사용자가 푸시 스토리를 활성화하기 위해 상호작용하는 기본 푸시에 대한 정보는 [푸시 이미지 및 텍스트 사양]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#push)을 참조하세요.

{% tabs %}
{% tab Images %}

- **이미지 비율:** 2:1 (필수)
- **권장 이미지 크기:** 500 KB
- **최대 이미지 크기:** 5 MB
- **파일 형식:** PNG, JPEG

{% endtab %}
{% tab Text %}

- **제목:** 30자 (권장)
- **설명:** 30자 (권장)

{% alert note %}
기기마다 문자 길이에 다소 차이가 있을 수 있지만, 푸시 스토리의 제목과 설명은 각각 한 줄로 제한됩니다. 나머지 메시지는 잘립니다. 항상 실제 기기에서 메시지를 테스트하세요.
{% endalert %}

{% endtab %}
{% endtabs %}

### 푸시 스토리 세분화

캠페인 또는 캔버스를 생성할 때, 푸시 스토리 페이지를 클릭했는지 여부에 따라 타겟팅할 사용자를 필터링할 수 있습니다. 그런 다음, 사용자를 타겟팅하는 데 사용할 캠페인과 페이지를 선택합니다.

### 푸시 스토리 분석

분석은 푸시 알림의 현재 분석 섹션과 매우 유사합니다. 푸시 스토리 분석에서는 **직접 열기** 측정기준을 열어 페이지별 클릭 수를 확인할 수 있습니다.

![iOS 푸시 성과 테이블에 샘플 분석과 직접 열기 측정기준의 확장된 세부 정보가 표시되어 있습니다.]({% image_buster /assets/img_archive/pushstories_analytics.png %})

## 문제 해결

### iOS

#### 자신에게 푸시 스토리를 보냈지만 알림을 받지 못했습니다

Apple은 여러 가지 요인에 따라 특정 유형의 알림이 기기로 전송되지 않도록 하는 규칙을 적용하고 있습니다. 여기에는 고객의 데이터 요금제, 알림 크기 및 고객의 저장 용량 평가가 포함됩니다. 그 결과 때때로 고객에게 알림이 전송되지 않을 수 있습니다.

이러한 제한 사항은 Apple이 부과한 것으로, 푸시 스토리를 설계할 때 고려해야 합니다.

#### 자신에게 푸시 스토리를 보냈지만 축소된 보기가 표시되었습니다

데이터 연결 손실 등으로 인해 모든 페이지가 로드되지 않는 특정 상황에서는 푸시 스토리가 축소된 알림만 표시됩니다.

### Android

#### 이미지를 클릭한 후에도 푸시 스토리가 닫히지 않습니다 

기본적으로 Android에서는 사용자가 이미지를 클릭한 후에도 푸시 스토리가 해제되지 않습니다. 알림을 해제하려면 [`cancelNotification`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-notification-utils/index.html#-1466259649%2FFunctions%2F-1725759721)을 호출하세요.