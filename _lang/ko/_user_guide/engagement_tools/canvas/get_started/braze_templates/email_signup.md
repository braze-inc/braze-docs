---
nav_title: 이중 옵트인을 통한 이메일 가입
article_title: 이중 옵트인을 통한 이메일 가입
page_order: 2
page_type: reference
description: "이 문서에서는 인증된 이메일 가입을 통해 도달 범위를 확장하기 위해 Braze 캔버스 템플릿을 사용하는 방법에 대해 설명합니다."
tool: Canvas
---

# 이중 옵트인을 통한 이메일 가입

> 이중 옵트인 이메일 가입 템플릿을 사용하여 인증된 이메일 가입으로 도달 범위를 확장하세요. 신규 사용자를 타겟팅하여 이메일을 캡처하고, 구독을 확인하고, 프로모션 코드를 수신하는 모든 과정을 한 번에 원활하게 진행할 수 있습니다.

이 문서에서는 사용자 라이프사이클의 고려 단계를 위해 설계된 **이중 옵트인 이메일 가입** 템플릿의 사용 사례를 안내합니다. 완료되면 사용자가 세션을 시작하거나 온보딩을 완료하지 않았을 때 이메일과 인앱 메시지를 보내는 캔버스를 만들 수 있습니다.

## 필수 조건

이 템플릿을 성공적으로 사용하려면 다음이 필요합니다:

- 한 페이지는 사용자의 이메일을 캡처하고 다른 페이지는 성공 메시지를 전달하는 [여러 페이지의 인앱 메시지로]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page) 구성됩니다.
- 사용자가 이메일 주소를 확인할 수 있는 확인 이메일입니다.
- 더블 옵트인한 사용자를 위한 전용 프로모션 코드가 포함된 환영 이메일이 전송됩니다.

## 필요에 맞게 템플릿 조정하기

칼로리 추적, 디지털 운동 수업, 플래시몹 마라톤 등의 기능으로 유명한 건강 앱인 Steppington에서 일한다고 가정해 보겠습니다. 캔버스를 만들기 전에 사용자의 앱 첫 사용 경험과 인상을 파악하기 위해 [여러 페이지로 구성된 인앱 및 브라우저 메시지를 설정하여]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page) 일련의 매력적인 질문을 포함했습니다.

템플릿에 액세스하려면 새 캔버스를 만들 때 **캔버스 템플릿 사용** > **브레이즈 템플릿을** 선택합니다. 그런 다음 **이중 옵트인을 통한 이메일 가입** 옆의 **템플릿 적용을** 선택합니다. 이제 템플릿을 검토하여 필요에 맞게 조정할 수 있습니다.

### 1단계: 세부 정보 설정

목표를 반영하도록 캔버스 세부 사항을 조정해 보겠습니다.

1. 템플릿 이름 옆의 **편집을** 선택합니다.

![캔버스의 현재 제목과 설명입니다.]({% image_buster /assets/img/canvas_templates/email_signup1.png %}){: style="max-width:50%;"}

{:start="2"}
2\. 캔버스 이름을 업데이트하여 신규 사용자가 앱을 처음 사용할 때 캔버스를 타겟팅할 수 있도록 지정합니다.
3\. 설명을 업데이트하여 이 캔버스에 사용자가 이중 옵트인할 수 있도록 개인화된 메시지가 포함되어 있음을 설명합니다.
4\. Canvas 홈 페이지에서 필터링할 수 있도록 **이메일** 태그를 추가합니다.

![캔버스의 새 이름, 설명 및 태그입니다.]({% image_buster /assets/img/canvas_templates/email_signup2.png %}){: style="max-width:90%;"}

### 2단계: 전환 이벤트 할당

다음으로 전환 이벤트를 할당해 보겠습니다. 전환 이벤트는 캔버스의 성공 여부를 측정하는 데 사용할 수 있는 일종의 지표입니다. **전환 이벤트 유형에서** **사용자 지정 이벤트 수행을** 선택합니다. 그런 다음 **사용자 지정 이벤트 이름에** **이메일_opt_in을** 선택합니다.

!["이메일 수신 동의의 전환 이벤트 유형에 대한 '전환 이벤트 할당' 섹션]({% image_buster /assets/img/canvas_templates/email_signup3.png %}){: style="max-width:90%;"}

가장 최근 사용자를 타겟팅하기 위해 템플릿의 전환 기한을 3일로 유지하겠습니다.

### 3단계: 참가 일정 맞춤 설정

사용자가 앱에서 세션을 시작할 때 캔버스에 입장할 수 있도록 입장 일정을 **액션 기반으로** 유지해 보겠습니다. 이렇게 하면 시기적절한 참여를 통해 관계를 구축할 수 있습니다.

또한 **액션 기반 옵션은** 그대로 유지하여 사용자가 세션을 시작할 때만 캔버스에 들어가도록 할 것입니다.

![세션을 시작하는 사용자를 캔버스에 입력하기 위한 작업 기반 입력 일정입니다.]({% image_buster /assets/img/canvas_templates/email_signup4.png %}){: style="max-width:90%;"}

**참가** 기간의 경우 **시작 시간(필수)** 을 원하는 날짜와 시간으로 업데이트합니다.

![시작 시간이 2025년 1월 16일 오후 12시 30분인 응모 창입니다. 사용자는 현지 시간대로 이 메시지를 입력합니다.]({% image_buster /assets/img/canvas_templates/email_signup5.png %}){: style="max-width:90%;"}

### 4단계: 타겟 오디언스 선택

타겟 고객을 사용자 프로필에 이메일 주소가 없는 스테핑턴팅 사용자로 정의하겠습니다. 템플릿의 기본 [세분화 필터]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) `Email Available is false` 를 유지하여 이 작업을 수행합니다.

!["사용 가능한 이메일이 거짓입니다" 필터가 적용된 참가 대상]({% image_buster /assets/img/canvas_templates/email_signup6.png %}){: style="max-width:90%;"}

### 5단계: 전송 설정을 선택하세요

기본 구독 설정을 유지하여 구독하거나 메시지 또는 알림 수신을 선택한 사용자에게만 전송하고 다른 설정(빈도 제한, 조용한 시간, 시드 그룹)은 건너뜁니다.

![기본 전송 옵션은 구독 또는 옵트인한 사용자에게만 전송합니다.]({% image_buster /assets/img/canvas_templates/email_signup7.png %}){: style="max-width:90%;"}

### 6단계: 캔버스 사용자 지정

이제 사용자에게 전송할 채널과 콘텐츠를 사용자 지정하여 캔버스를 구축하겠습니다. 이메일 가입 확인에 집중하고 있기 때문에 템플릿의 캔버스 단계와 채널을 추가하거나 제거할 필요가 없습니다.

1. 첫 번째 메시지 단계인 **이메일 가입을** 선택합니다. 여기에서 여러 페이지로 구성된 인앱(및 브라우저 내) 메시지를 사용하도록 템플릿을 업데이트합니다.

- 1페이지에 이메일이 캡처됩니다.
- 2페이지에 확인 메시지가 표시됩니다.

![사용자 이메일을 캡처하고 성공 메시지를 표시하는 두 페이지의 인앱 메시지.]({% image_buster /assets/img/canvas_templates/email_signup8.png %}){: style="max-width:90%;"}

{:start="2"}
2\. 여기서는 **구독된** 작업 경로 단계를 그대로 유지하겠습니다. 이 단계에서는 사용자를 하루 동안 두 그룹으로 나눕니다:

- 이메일로 스테핑턴턴을 구독한 사용자
- 이메일로 스테핑턴턴을 구독하지 않은 사용자

{:start="3"}
3\. 다음으로, 이메일 메시지 **확인** 단계에서 이메일 본문을 브랜드 확인 이메일로 바꿉니다. 그러면 구독한 사용자에게 이메일이 전송되고 이메일 주소를 확인하고 메시징 수신에 동의하라는 메시지가 표시됩니다.
4\. **구독 작업 경로 확인** 단계를 그대로 유지합니다. 이 단계에서는 이메일을 확인한 사용자와 그렇지 않은 사용자를 1주일의 기간을 두고 다시 나눕니다.
5\. 마지막으로, 전용 프로모션 코드가 포함된 확인 이메일을 통해 **환영 + 할인** 메시지 단계를 업데이트합니다.  

### 7단계: 캔버스 테스트 및 실행

캔버스를 테스트하고 검토하여 예상대로 작동하는지 확인한 후 **캔버스 시작을** 선택하여 캔버스를 실행합니다.

{% alert tip %}
캔버스 출시 전후에 고려해야 할 사항은 [출시 전/후 체크리스트를]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) 확인하세요.
{% endalert %}