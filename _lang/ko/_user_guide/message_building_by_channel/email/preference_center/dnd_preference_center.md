---
nav_title: 드래그 앤 드롭 이메일 환경 설정 센터
article_title: 드래그 앤 드롭 이메일 환경설정 센터
alias: "/dnd_preference_center/"
description: "이 참조 페이지에서는 드래그 앤 드롭 편집기로 이메일 환경설정 센터를 만드는 방법에 대해 설명합니다."
page_order: 2
---

# 드래그 앤 드롭으로 이메일 환경설정 센터 만들기

> 드래그 앤 드롭 편집기를 사용하여 환경설정 센터를 만들고 커스텀하여 특정 유형의 커뮤니케이션을 수신할 사용자를 관리할 수 있습니다. 작업 공간당 최대 100개의 환경설정 센터를 만들 수 있습니다.

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='dnd editors' %}

## 1단계: 이메일 환경설정 센터 만들기

**오디언스** > **이메일 환경설정 센터로** 이동하여 환경설정 센터를 만듭니다.

여기에 커스텀 환경 설정 센터 목록이 표시됩니다. **새로 만들기를** 선택하여 새 환경설정 센터를 만들거나 기존 환경설정 센터의 이름을 선택하여 변경할 수 있습니다.

이름, 설명, 유형, 상태, 마지막 편집 날짜, 사용자가 만든 커스텀 환경설정 센터의 목록입니다.]({% image_buster /assets/img/preference_center/preference_center1.png %})

## 2단계: 이메일 기본 설정 센터 이름 지정하기

환경설정 센터 이름에는 영숫자, 대시 또는 밑줄만 포함할 수 있습니다. 입력한 이름에 따라 생성된 Liquid 태그의 구문이 결정됩니다. 

이 Liquid 태그는 모든 아웃바운드 이메일 캠페인 또는 캔버스 단계에 포함할 수 있으며 사용자를 환경설정 센터로 안내합니다.

기본 설정 센터의 Liquid 예시.]({% image_buster /assets/img/preference_center/preference_center2.png %})

## 3단계: 환경설정 센터에 구독 그룹 추가하기

드래그 앤 드롭 편집기에서 환경설정 센터 디자인을 시작하려면 **편집기 실행을** 선택합니다.

### 사용 가능한 구독 그룹 정의하기

환경설정 센터에 표시할 구독 그룹을 결정하려면 **\+ 구독 그룹 추가** 버튼을 선택하여 원하는 구독 그룹을 선택할 수 있는 모달을 실행합니다. 선택한 후 **구독 그룹 추가** 버튼을 선택하여 환경설정 센터에 **구독 그룹을** 추가합니다.

스마트 블록을 선택하고 블록 속성을 조정하여 선택한 구독 그룹을 추가로 구성할 수 있습니다.
- 구독 그룹 순서 조정하기
- 추가 구독 그룹 추가 또는 제거하기
- 설명 포함
- 이 블록에 표시된 모든 구독 그룹에 사용자를 가입할 수 있는 **모두에 구독** 확인란을 추가하거나 제거합니다.
- 이 블록에 표시된 모든 구독 그룹에서 사용자를 탈퇴하는 **모두에서** 구독 취소 확인란을 추가하거나 제거합니다.

\![모든 메시지, 마케팅, 뉴스레터, 주간 이메일에 가입하거나 모두 탈퇴할 수 있는 옵션이 있는 환경설정 센터의 예입니다.]({% image_buster /assets/img/preference_center/preference_center3.png %}){: style="max-width:38%;"}\![]({% image_buster /assets/img/preference_center/preference_center4.png %}){: style="max-width:45%;"}

템플릿 하단의 **모든** 수신 **거부** 버튼은 제거할 수 없으며 사용자가 모든 이메일 메시지 수신에서 [전역적으로 탈퇴합니다]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states).

## 4단계: 드래그 앤 드롭 편집기를 사용하여 환경설정 센터 커스텀하기

### 공통 스타일 설정

환경설정 센터의 **공통 스타일** 탭에서 모든 관련 블록에 적용되도록 특정 스타일을 설정할 수 있습니다. 이 섹션에서 설정한 스타일은 특정 블록에 대해 재정의하는 경우를 제외하고 메시징의 모든 곳에서 사용됩니다. 보다 쉬운 디자인 경험을 위해 블록 수준에서 스타일을 커스텀하기 전에 페이지 수준 스타일을 설정하는 것이 좋습니다.

텍스트, 버튼 및 링크에 대한 일반적인 스타일 설정의 예입니다.]({% image_buster /assets/img/preference_center/preference_center5.png %}){: style="max-width:45%;"}

{% alert tip %}
공통 스타일로 돌아가려면 개별 블록 속성에서 'X' 버튼을 선택합니다. 그런 다음 메시지 컨테이너, 메시지 'X' 버튼 또는 편집기 배경을 선택합니다.
{% endalert %}

## 드래그 앤 드롭 환경 설정 센터 구성 요소

드래그 앤 드롭 편집기는 행과 블록이라는 두 가지 주요 구성 요소를 사용하여 환경설정 센터를 빠르고 쉽게 구성할 수 있습니다. 모든 블록은 일렬로 배치해야 합니다.

{% tabs %}
{% tab Rows %}

행은 셀을 사용하여 메시지 섹션의 가로 구성을 정의하는 구조적 단위입니다.

메시징에서 행 유형을 선택하는 옵션입니다.]({% image_buster /assets/img/preference_center/preference_center6.png %}){: style="max-width:45%;"}

행을 선택하면 열 커스텀 섹션에서 필요한 열 개수를 추가하거나 제거하여 서로 다른 콘텐츠 요소를 나란히 배치할 수 있습니다. 기존 열의 크기를 슬라이드하여 조정할 수도 있습니다.

배경색, 테두리 스타일, 테두리 반경, 패딩 등 열 속성을 커스텀할 수 있는 옵션입니다.]({% image_buster /assets/img/preference_center/preference_center7.png %}){: style="max-width:45%;"}

행과 열 속성의 서식을 지정하기 전에 행 내부의 블록에 서식을 지정하는 것이 좋습니다. 여러 곳에서 간격과 정렬을 조정할 수 있으므로 기초부터 시작하면 진행하면서 쉽게 편집할 수 있습니다.

{% endtab %}
{% tab Blocks %}

콘텐츠 블록은 메시징에 사용할 수 있는 다양한 유형의 콘텐츠를 나타냅니다. 기존 행 세그먼트 안으로 드래그하면 셀 너비에 맞게 자동으로 조정됩니다.

제목, 단락, 버튼, 이미지, 스페이서 등 블록을 선택할 수 있는 옵션입니다.]({% image_buster /assets/img/preference_center/preference_center8.png %}){: style="max-width:45%;"}

모든 블록에는 패딩을 세밀하게 제어하는 등 고유한 설정이 있습니다. 오른쪽 패널은 선택한 콘텐츠 요소의 스타일링 패널로 자동 전환됩니다. 자세한 내용은 [편집기 블록 속성을]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/editor_blocks/) 참조하세요.

환경설정 센터에서 커스텀 코드 블록을 사용하는 경우 사용자에게 전달할 때 커스텀 코드에서 인라인 프레임이 생성되지 않을 수 있습니다.

{% endtab %}
{% endtabs %}

## 5단계: 확인 페이지 커스텀하기

확인 페이지를 커스텀하는 것을 잊지 마세요! 드래그 앤 드롭 편집기 창 상단에서 **확인 페이지를** 선택하여 이 페이지를 편집할 수 있습니다. 이 페이지는 환경설정 센터를 사용하여 환경설정을 업데이트한 후 사용자에게 표시됩니다. 위와 동일한 스타일링 기능이 이 페이지에도 적용됩니다.

사용자의 기본 설정을 알리는 확인 페이지의 예시가 업데이트되었습니다.]({% image_buster /assets/img/preference_center/preference_center9.png %}){: style="max-width:65%;"}

## 6단계: 환경설정 센터 미리보기 및 실행

편집기 내에서 **미리보기** 탭을 선택하여 환경설정 센터를 미리 볼 수 있습니다. 그러나 테스트 기능은 비활성화되어 있습니다. 환경설정 센터를 편집한 후 **완료** 버튼을 선택하여 편집기를 닫을 수 있습니다.

환경설정 센터와 확인 페이지의 미리보기가 모두 표시됩니다. 나중에 이 환경설정 센터로 돌아가려면 **초안으로 저장을** 선택하거나, 만족스러운 경우 **환경설정 센터 시작을** 선택합니다.

환경설정 센터를 실행하면 실행 후에는 편집할 수 없으므로 이름을 확인하라는 메시지가 표시됩니다. 이름을 확인하면 환경설정 센터가 시작되고 사용할 준비가 완료됩니다.

## 환경설정 센터 사용

{% multi_lang_include alerts/important_alerts.md alert='Preference Center warning' %}

이메일에 환경설정 센터 링크를 포함하려면 **Liquid 복사** 아이콘을 선택하여 원하는 환경설정 센터의 Liquid 태그를 복사합니다.

환경설정 센터의 행에 있는 Copy Liquid 옵션을 클릭합니다.]({% image_buster /assets/img/preference_center/preference_center10.png %}){: style="max-width:75%;"}

[탈퇴 URL을]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/#adding-a-custom-unsubscribe-link) 삽입하는 방법과 유사하게 이메일의 원하는 위치에 Liquid 태그를 추가합니다.

## 오류 처리

사용자가 환경설정 센터에서 **저장을** 선택할 때 오류가 발생하면 다음과 같은 기본값 오류 메시지가 표시되며, 편집기에서 커스텀하거나 스타일을 지정할 수 없습니다. 그러나 오류 메시지의 현지화는 이 페이지에서 계속 지원됩니다. 

"환경설정을 저장하는 동안 문제가 발생했습니다."라는 오류 메시지가 표시됩니다. 다시 시도해 주세요."]({% image_buster /assets/img/preference_center/preference_center11.png %}){: style="max-width:55%;"}

