---
nav_title: 드래그 앤 드롭 이메일 환경 설정 센터
article_title: 드래그 앤 드롭 이메일 환경 설정 센터
alias: "/dnd_preference_center/"
description: "이 참조 페이지에서는 드래그 앤 드롭 편집기를 사용하여 이메일 환경 설정 센터를 만드는 방법을 다룹니다."
page_order: 2
---

# 드래그 앤 드롭으로 이메일 환경 설정 센터 만들기

> 드래그 앤 드롭 편집기를 사용하여 사용자가 특정 유형의 커뮤니케이션을 수신하는지 관리하는 데 도움이 되는 환경 설정 센터를 만들고 사용자 지정할 수 있습니다. 워크스페이스당 최대 50개의 선호 센터를 가질 수 있습니다.

{% multi_lang_include drag_and_drop_access.md variable_name='dnd editors' %}

## 1단계: 이메일 환경 설정 센터 만들기

**오디언스** > **구독** > **이메일 환경 설정 센터**로 이동하여 환경 설정 센터를 만드세요.

여기에는 커스텀 선호 센터 목록이 표시됩니다. **Create New**을 선택하여 새 환경 설정 센터를 만들거나 기존 환경 설정 센터의 이름을 선택하여 변경하십시오.

![A list of custom preference centers with the name, description, type, status, last edited date, and created by user.]({% image_buster /assets/img/preference_center/preference_center1.png %})

## 2단계: 이메일 환경 설정 센터의 이름을 지정하세요

환경 설정 센터 이름은 영숫자, 대시 또는 밑줄만 포함할 수 있습니다. 제공한 이름은 생성된 Liquid 태그의 구문을 결정합니다. 

이 Liquid 태그는 모든 아웃바운드 이메일 캠페인 또는 캔버스 단계에 포함될 수 있으며 사용자를 선호 센터로 안내합니다.

![An example of Liquid for a preference center.]({% image_buster /assets/img/preference_center/preference_center2.png %})

## 3단계: 환경 설정 센터에 구독 그룹 추가

**런치 에디터**를 선택하여 드래그 앤 드롭 에디터에서 환경 설정 센터 디자인을 시작하세요.

### 사용 가능한 구독 그룹 정의

어떤 구독 그룹을 환경 설정 센터에 표시할지 결정하려면 **\+ 구독 그룹 추가** 버튼을 선택하여 원하는 구독 그룹을 선택할 수 있는 모달을 실행하십시오. 선택한 후, **구독 그룹 추가** 버튼을 선택하여 환경 설정 센터에 추가합니다.

선택한 구독 그룹을 스마트 블록을 선택하고 블록 속성을 조정하여 추가로 구성할 수 있습니다.
- 구독 그룹의 순서를 조정
- 구독 그룹 추가 또는 제거
- 설명 포함
- **모두 가입**할 수 있는 체크박스를 추가하거나 제거하여 사용자가 이 블록에 표시된 모든 구독 그룹에 가입할 수 있도록 합니다.
- 모든 구독 그룹에서 사용자를 탈퇴시키는 **모두 탈퇴** 체크박스를 추가하거나 제거합니다.

![An example of a preference center with the options to subscribe to all messages, marketing, newsletter, and weekly emails, or to unsubscribe from all.]({% image_buster /assets/img/preference_center/preference_center3.png %}){: style="max-width:38%;"} ![]({% image_buster /assets/img/preference_center/preference_center4.png %}){: style="max-width:45%;"}

템플릿 하단의 **탈퇴** 버튼은 제거할 수 없으며 사용자가 모든 이메일 메시지 수신을 [전역적으로 탈퇴]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states)하게 됩니다.

## 4단계: 드래그 앤 드롭 편집기를 사용하여 환경 설정 센터를 사용자 정의하십시오

### 일반 스타일 설정

환경 설정 센터의 **공통 스타일** 탭에서 모든 관련 블록에 적용할 특정 스타일을 설정할 수 있습니다. 이 섹션에 설정된 스타일은 특정 블록에 대해 재정의하지 않는 한 메시지의 모든 곳에서 사용됩니다. 더 쉬운 디자인 경험을 위해 블록 수준에서 스타일을 사용자 정의하기 전에 페이지 수준 스타일을 설정하는 것을 권장합니다.

![An example of common style settings for text, buttons, and links.]({% image_buster /assets/img/preference_center/preference_center5.png %}){: style="max-width:45%;"}

{% alert tip %}
일반 스타일로 돌아가려면 개별 블록 속성에서 "X" 버튼을 선택하십시오. 다음으로, 메시지 컨테이너, 메시지 "X" 버튼 또는 편집기 배경을 선택합니다.
{% endalert %}

## 드래그 앤 드롭 환경 설정 센터 구성 요소

드래그 앤 드롭 편집기는 선호도 센터 구성을 빠르고 쉽게 만드는 두 가지 주요 구성 요소를 사용합니다: 행과 블록. 모든 블록은 한 줄에 배치되어야 합니다.

{% tabs %}
{% tab 행 %}

행은 셀을 사용하여 메시지 섹션의 가로 구성을 정의하는 구조적 단위입니다.

![메시지에서 행 유형을 선택하는 옵션입니다.]({% image_buster /assets/img/preference_center/preference_center6.png %}){: style="max-width:45%;"}

행을 선택하면 열 사용자 지정 섹션에서 필요한 열 수를 추가하거나 제거하여 서로 다른 콘텐츠 요소를 나란히 배치할 수 있습니다. 기존 열의 크기를 조정하려면 슬라이드할 수도 있습니다.

![배경색, 테두리 스타일, 테두리 반경, 패딩 등 열 속성을 사용자 지정하는 옵션이 있습니다.]({% image_buster /assets/img/preference_center/preference_center7.png %}){: style="max-width:45%;"}

모범 사례로서, 행 내부의 블록을 포맷하기 전에 행 및 열 속성을 포맷하세요. 여러 곳에서 간격과 정렬을 조정할 수 있으므로, 기초부터 시작하면 편집하기가 더 쉽습니다.

{% endtab %}
{% tab 블록 %}

블록은 메시지에서 사용할 수 있는 다양한 유형의 콘텐츠를 나타냅니다. 기존 행 세그먼트 안에 하나를 끌어다 놓으면 셀 너비에 맞게 자동 조정됩니다.

![제목, 단락, 버튼, 이미지, 스페이서 등 블록을 선택하는 옵션입니다.]({% image_buster /assets/img/preference_center/preference_center8.png %}){: style="max-width:45%;"}

모든 블록에는 패딩에 대한 세밀한 제어와 같은 고유한 설정이 있습니다. 오른쪽 패널은 선택한 콘텐츠 요소에 대한 스타일링 패널로 자동 전환됩니다. 자세한 내용은 [편집기 블록 속성]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/editor_blocks/)을 참조하세요.

사용자 환경 설정 센터에서 커스텀 코드 블록을 사용하는 경우, 인라인 프레임이 사용자에게 전달될 때 커스텀 코드에서 생성되지 않을 수 있습니다.

{% endtab %}
{% endtabs %}

## 5단계: 확인 페이지를 사용자 정의하십시오

확인 페이지를 사용자 정의하는 것을 잊지 마세요! 드래그 앤 드롭 편집기 창 상단에서 **확인 페이지**를 선택하여 이 페이지를 편집할 수 있습니다. 이 페이지는 사용자들이 환경 설정 센터를 사용하여 환경 설정을 업데이트한 후에 표시됩니다. 위와 동일한 스타일링 기능이 이 페이지에도 적용됩니다.

![An example of a confirmation page to communicate the user's preferences have been updated.]({% image_buster /assets/img/preference_center/preference_center9.png %}){: style="max-width:65%;"}

## 6단계: 미리보기 및 선호도 센터 실행

편집기 내에서 **미리보기** 탭을 선택하여 환경 설정 센터를 미리 볼 수 있습니다. 그러나 기능 테스트는 비활성화되어 있습니다. 환경 설정 센터를 편집한 후 **완료** 버튼을 선택하여 편집기를 닫을 수 있습니다.

선호도 센터와 확인 페이지의 미리보기를 보게 될 것입니다. **저장**을 초안으로 저장을 선택하여 나중에 이 환경 설정 센터로 돌아가거나, 만족하시면 **환경 설정 센터 시작**을 선택하세요.

환경 설정 센터를 실행할 때 이름을 확인하라는 메시지가 표시됩니다. 실행 후에는 이름을 편집할 수 없습니다. 이름을 확인한 후, 환경 설정 센터가 실행되어 사용할 준비가 됩니다.

## 환경 설정 센터 사용

{% multi_lang_include preference_center_warning.md %}

이메일에 환경 설정 센터로의 링크를 삽입하려면 **Copy Liquid** 아이콘을 선택하여 원하는 환경 설정 센터의 Liquid 태그를 복사하십시오.

![The Copy Liquid option in the row of a preference center.]({% image_buster /assets/img/preference_center/preference_center10.png %}){: style="max-width:75%;"}

이메일의 원하는 위치에 Liquid 태그를 추가하세요. 이는 [탈퇴 URL]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/#adding-a-custom-unsubscribe-link)이 삽입되는 방식과 유사합니다.

## 오류 처리

사용자가 환경 설정 센터에서 **저장**을 선택할 때 오류가 발생하면, 다음 기본값 오류 메시지가 표시되며, 편집기에서 사용자 지정하거나 스타일을 지정할 수 없습니다. 그러나 이러한 페이지에서는 오류 메시지의 현지화가 여전히 지원됩니다. 

![문제를 저장하는 중 문제가 발생했습니다. Please try again."]({% image_buster /assets/img/preference_center/preference_center11.png %}){: style="max-width:55%;"}

