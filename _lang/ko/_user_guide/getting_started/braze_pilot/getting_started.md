---
nav_title: 시작하기
article_title: Braze 파일럿 시작하기
page_order: 2
page_type: reference
description: "이 참조 문서에서는 엔지니어 또는 개발자에게 필요한 통합 단계를 간략하게 다룹니다."
---

# Braze 파일럿 시작하기

> 이 문서에서는 Braze 파일럿을 시작하는 방법에 대해 설명합니다. 여기서는 앱 다운로드, Braze 대시보드와의 연결 초기화, 설정 완료 과정을 안내해 드립니다.

## 1단계: Braze 파일럿 다운로드

Braze 파일럿을 사용하려면 먼저 Apple 앱 스토어 또는 Google Play 스토어 앱에서 앱을 다운로드해야 합니다. 앱 스토어에서 앱을 검색하거나 아래 QR 코드를 스캔하여 해당 기기의 앱 페이지로 이동할 수 있습니다.

## 2단계: 이용 약관에 동의

그런 다음 이용 약관에 동의한 다음 양식에 업무용 이메일을 입력합니다. 이메일은 앱 사용 분석용으로만 사용되며 마케팅 목적으로는 사용되지 않습니다.

\![Braze 파일럿 시작 페이지.]({% image_buster /assets/img/braze_pilot/pilot_welcome.png %}){:style="max-width:30%"}\![업무용 이메일 주소를 입력하는 옵션입니다.]({% image_buster /assets/img/braze_pilot/pilot_signin.png %}){:style="max-width:30%"}

## 3단계: Braze 소프트웨어 개발 키트로 연결 초기화하기

Braze 파일럿을 사용하면 모든 Braze 대시보드에 대해 소프트웨어 개발 키트를 초기화할 수 있습니다. 소프트웨어 개발 키트가 초기화되면 파일럿이 참여 데이터를 Braze로 전송하기 시작하고 해당 Braze 대시보드에서 시작된 모든 메시징을 트리거할 수 있습니다.

파일럿에서 소프트웨어 개발 키트 연결을 구성하는 방법에는 두 가지가 있습니다: 데모 QR 코드 및 설정 마법사.

{% tabs local %}
{% tab Demo QR codes %}

### 방법 1: 데모 QR 코드

소프트웨어 개발 키트 초기화에 필요한 모든 세부 정보가 포함된 QR 코드를 스캔하고, 고객 프로필을 생성하고, Braze Pilot의 특정 앱 시뮬레이션에 딥링크하세요. 무료 평가판의 특정 데모 캠페인에 대한 데모 QR 코드는 컴패니언 서랍에 렌더링되어 있습니다.

| Android용 파일럿 | iOS용 파일럿 |
| --- | --- |
| \![Android용 QR코드.]({% image_buster /assets/img/braze_pilot/android_qr_code.png %}){:style="max-width:60%"} | \![iOS용 QR코드.]({% image_buster /assets/img/braze_pilot/ios_qr_code.png %}){:style="max-width:60%"} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Setup wizard %}

### 방법 2: 설정 마법사

Braze 대시보드의 **앱 설정** 페이지에서 대시보드 워크스페이스와의 연결을 초기화하는 단계별 가이드를 따르세요.

\![Braze 파일럿 설정 마법사 1단계.]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

이 연결은 워크스페이스별로 다릅니다. 즉, 데모 워크스페이스에서 연결을 초기화한 다음 무료 평가판 대시보드에서 라이브 워크스페이스로 전환하면 해당 워크스페이스에서 소프트웨어 개발 키트를 다시 초기화해야 그곳에서 시작된 모든 캠페인을 받을 수 있습니다.

"데모 - Braze"가 활성 워크스페이스로 선택된 Braze 대시보드의 워크스페이스 드롭다운.]({% image_buster /assets/img/braze_pilot/dashboard_workspace.png %}){:style="max-width:60%"}

{% endtab %}
{% endtabs %}

## 4단계: 푸시 권한 허용

마지막으로 앱을 통해 푸시 기능을 테스트하려면 앱에서 푸시 권한을 보내도록 허용하는 것이 좋습니다. 기기 설정에서 앱의 설정을 업데이트하거나 Braze에서 앱으로 푸시 프라이머 메시지를 실행하는 등의 방법으로 앱에 이러한 권한을 부여할 수 있습니다.

{% tabs local %}
{% tab Update the settings for the app %}

기기 설정을 열고 Braze Pilot을 찾습니다. 그런 다음 잠금 화면에 알림이 표시되도록 설정을 업데이트합니다.

<style>
  .imgDiv {
      text-align: center;
    }
</style>

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/device_settings.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% tab Launch a push primer message %}

소비자에게 푸시 권한을 요청할 때와 마찬가지로 Braze 인앱 메시지를 사용하여 앱에 대한 푸시 권한을 요청할 수 있습니다. Braze에서 이러한 유형의 메시지를 구축하는 방법을 알아보려면 [푸시 프라이머 인앱 메시지를]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages#push-primer-in-app-messages) 참조하세요.

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/push_primer1.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% endtabs %}

## 5단계: 파일럿에서 Braze 메시징 경험하기

이제 Braze 파일럿의 사용자로서 Braze 대시보드에서 캠페인과 캔버스를 수신할 준비가 되었습니다! 데모 워크스페이스에서 시작된 캠페인을 방문하여 Braze 사용 사례에 대한 간단한 데모를 살펴본 다음, 라이브 워크스페이스로 이동하여 직접 캠페인을 전송해 보세요.

Braze에서 캠페인 및 캔버스를 설정하는 방법에 대한 자세한 내용은 [시작하기를 참조하세요: 캠페인 및 캔버스]({{site.baseurl}}/user_guide/getting_started/campaigns_canvases).