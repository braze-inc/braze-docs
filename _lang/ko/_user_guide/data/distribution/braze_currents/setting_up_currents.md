---
nav_title: 커런츠 설정하기
article_title: 커런츠 설정하기
page_order: 0
page_type: tutorial
description: "이 사용법 문서에서는 Braze 커런츠를 통합하고 구성하는 과정을 안내합니다."
tool: Currents
search_rank: 8
---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/currents-the-basics-2/){: style="float:right;width:120px;border:0;" class="noimgborder"} 커런츠 설정하기

> 이 페이지에서는 Braze 커런츠 통합 및 구성에 대한 일반적인 프로세스를 간략하게 설명하고 설명합니다.

{% alert important %}
커런츠는 특정 Braze 패키지에 포함되어 있습니다. 궁금한 점이 있거나 액세스 권한을 얻으려면 Braze 담당자에게 문의하세요.
{% endalert %}

## 요구 사항

파트너와 함께 커런츠를 사용하려면 동일한 기본 매개변수와 연결 방법이 필요합니다.

각 파트너는 데이터 파일을 쓰고 보낼 수 있는 권한이 있어야 하며, Braze는 해당 파일을 쓸 위치, 특히 버킷 이름이나 키를 요청합니다.

다음 요구 사항은 대부분의 파트너와 통합하기 위한 기본적이고 최소한의 요구 사항입니다. 일부 파트너는 이러한 기본 요구 사항과 관련된 미묘한 차이와 함께 각 [파트너 설명서에]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) 나열된 추가 매개 변수를 요구할 수 있습니다.

| 요구 사항 | 원산지 | 액세스 | 설명
|---|---|---|---|
| 파트너 계정 | 해당 파트너와 계정을 연결하거나 Braze 계정 매니저에게 문의하여 제안을 받으세요. | 해당 파트너의 사이트를 확인하거나 해당 파트너에게 연락하여 가입하세요. | 회사 계정을 통해 해당 데이터에 액세스할 수 없는 경우 Braze는 파트너에게 데이터를 전송하지 않습니다.
| 파트너 API 키 또는 토큰 | 일반적으로 파트너의 대시보드입니다. | 지정된 Braze 필드에 복사하여 붙여넣기만 하면 됩니다. | Braze에는 해당 파트너의 통합 페이지에 이를 위한 지정 필드가 있습니다. 데이터를 전송할 위치를 매핑하려면 이 정보가 필요합니다. **파트너 키 또는 토큰을 최신 상태로 유지하는 것이 중요하며, 자격 증명이 유효하지 않으면 커넥터가 비활성화되고 이벤트가 삭제될 수 있습니다.**
| 인증 코드/키, 비밀 키, 인증 파일 | 해당 파트너의 계정 담당자에게 문의하세요. 파트너의 대시보드에도 존재할 수 있습니다. | 키를 복사하여 지정된 Braze 필드에 붙여넣습니다. `.json` 또는 기타 인증 파일을 생성하여 Braze의 적절한 위치에 업로드합니다. | Braze에는 해당 파트너의 통합 페이지에 이를 위한 지정 필드가 있습니다. 이렇게 하면 Braze에 자격 증명이 부여되고 파트너 계정에 파일을 쓸 수 있는 권한이 부여됩니다. **자격 증명이 유효하지 않으면 커넥터가 비활성화되고 이벤트가 삭제될 수 있으므로 인증 정보를 최신 상태로 유지하는 것이 중요합니다.**
| 버킷, 폴더 경로 | 일부 파트너는 버킷별로 데이터를 정리하고 정렬합니다. 파트너의 대시보드에서 찾을 수 있습니다. | 필요한 경우 버킷 이름 또는 파일 경로를 Braze의 지정된 공간에 정확히 복사해야 합니다. 데이터가 손실되는 것을 원하지 않습니다! | 일부 파트너에게는 필수 사항이지만, 필요할 때 올바르게 처리하는 것이 중요합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
파트너 키, 파트너 토큰 및 인증 세부 정보를 최신 상태로 유지하는 것이 중요하며, 커넥터의 자격 증명이 만료되면 커넥터는 이벤트 전송을 중단합니다. 이 상태가 **5일** 이상 지속되면 커넥터의 이벤트가 삭제되고 데이터가 영구적으로 손실됩니다.
{% endalert %}

## 커런츠 설정하기

### 1단계: 파트너 선택

Braze 커런츠를 사용하면 플랫 파일을 사용하여 데이터 스토리지를 통해 통합하거나 지정된 엔드포인트에 일괄 JSON 페이로드를 사용하여 행동 분석 및 고객 데이터 파트너와 통합할 수 있습니다.  

통합을 시작하기 전에 어떤 통합이 목적에 가장 적합한지 결정하는 것이 가장 좋습니다. 예를 들어, 이미 mParticle과 세그먼트를 사용하고 있고 거기서 Braze 데이터를 스트리밍하고 싶다면 일괄 처리된 JSON 페이로드를 사용하는 것이 가장 좋습니다. 데이터를 직접 조작하거나 좀 더 복잡한 데이터 분석 시스템을 원한다면 데이터 저장소를 사용하는 것이 가장 좋습니다[(Braze는 이 방법을 사용합니다]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/)!).

### 2단계: 오픈 커런츠

시작하려면 **파트너 통합** > **데이터 내보내기로** 이동하세요. 커런츠 통합 관리 페이지로 이동합니다.

\![Braze 대시보드의 커런츠 페이지]({% image_buster /assets/img_archive/currents-main-page.png %})

### 3단계: 파트너 추가

화면 상단의 드롭다운을 선택하여 '커런츠 커넥터'라고도 하는 파트너를 추가합니다.

각 파트너마다 다른 구성 단계가 필요합니다. 각 [파트너]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) 통합을 인에이블하려면 [사용 가능한 파트너]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) 목록을 참조하고 해당 페이지의 지침을 따르세요.

### 4단계: 이벤트 구성

사용 가능한 옵션에서 확인란을 선택하여 해당 파트너에게 전달할 이벤트를 선택합니다. 이러한 이벤트 목록은 [고객 행동 이벤트]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) 및 [메시지 참여 이벤트]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) 라이브러리에서 확인할 수 있습니다.

\![]({% image_buster /assets/img/current4.png %})

필요한 경우 [이벤트 전달 의미]({{site.baseurl}}/user_guide/data/braze_currents/event_delivery_semantics/) 문서에서 이벤트에 대해 자세히 알아볼 수 있습니다.

### 5단계: 필드 변환 설정

커런츠 필드 변환을 사용하여 문자열 필드를 제거하거나 해시할 수 있습니다.

- **제거합니다:** 문자열 필드를 `[REDACTED]` 로 바꿉니다. 이 기능은 파트너가 누락되거나 비어 있는 필드가 있는 이벤트를 거부하는 경우에 유용합니다.
- **해시:** 문자열 필드에 SHA-256 해싱 알고리즘을 적용합니다.

이러한 변환 중 하나에 대한 필드를 선택하면 해당 필드가 표시되는 모든 이벤트에 해당 변환이 적용됩니다. 예를 들어 해싱을 위해 `email_address` 을 선택하면 이메일 보내기, 이메일 열기, 이메일 반송 및 구독 그룹 상태 변경 이벤트에서 `email_address` 필드가 해시됩니다.

\![필드 변환 추가]({% image_buster /assets/img/current3.png %})

### 6단계: 통합 테스트하기

{% alert important %}
커런츠는 페이로드가 900KB를 초과하는 지나치게 큰 이벤트를 삭제합니다.
{% endalert %}

테스트하기 전에 [GitHub에서 샘플 커런츠 데이터를](https://github.com/Appboy/currents-examples) 확인해 보세요. 테스트할 준비가 되면 아래 옵션을 선택합니다:

#### 테스트 이벤트 보내기

통합을 테스트하려면 **테스트 이벤트 보내기를** 선택하여 선택한 각 이벤트 유형에서 이 커런트로 하나의 이벤트를 보내면 됩니다. 각 이벤트 유형에 대한 자세한 내용은 [고객 행동 이벤트]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) 및 [메시지 참여 이벤트]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) 라이브러리를 참조하세요.

Braze 대시보드의 "커런츠 테스트" 페이지.]({% image_buster /assets/img/currents/current_test_events.png %}){: style="max-width:70%;"}

#### 커런츠 커넥터 테스트

테스트 커런츠 커넥터는 다양한 대상을 테스트하고 사용해 볼 수 있는 기존 커넥터의 무료 버전입니다. 테스트 커런츠가 있습니다:

- 구축할 수 있는 테스트 커런츠 커넥터 수에는 제한이 없습니다.
- 7일의 롤링 기간당 총 최대 10,000개의 이벤트가 집계됩니다. 이 이벤트 총계는 대시보드에서 매시간 업데이트됩니다.

테스트 커런츠 커넥터가 전송 한도에 도달하면 커넥터는 다음 7일 동안 이벤트를 전송할 수 없습니다.

테스트 커런츠 커넥터를 업그레이드하려면 대시보드에서 통합을 편집하고 **테스트 통합 업그레이드를** 선택합니다.

## 커런츠 업데이트하기

{% multi_lang_include updating_currents.md %}

## IP 허용 목록

Braze는 나열된 IP에서 커런츠 데이터를 전송합니다:

{% multi_lang_include data_centers.md datacenters='ips' %}
