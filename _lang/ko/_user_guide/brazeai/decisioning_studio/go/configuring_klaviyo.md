---
nav_title: 클라비요로 구성하기
article_title: Klaviyo로 구성하는 BrazeAI 의사 결정 스튜디오
page_order: 3
description: "BrazeAI Decisioning <sup>StudioTM</sup> Go와 함께 사용하기 위해 Klaviyo Flow를 설정하는 방법을 알아보세요."
toc_headers: h2
---

# Klaviyo로 구성하여 BrazeAI Decisioning Studio™ Go 사용

> Klaviyo에서 입력 안내 템플릿과 흐름을 설정하여 BrazeAI Decisioning Studio™ Go를 통해 활성화를 트리거할 수 있습니다.

{% alert important %}
설정하는 모든 새 실험자에 대해 클라비요에서 새 플로우를 만들어야 합니다. 이전에 템플릿을 가져오기 위해 입력 안내자 플로우를 만든 경우에는 새 플로우를 만들어야 하며 이전 입력 안내자 플로우는 재사용할 수 없습니다.
{% endalert %}

Klaviyo에서 플로우를 만들기 전에 참조할 수 있는 BrazeAI Decisioning Studio™ Go 포털의 다음 세부 정보가 있어야 합니다:

- 흐름 이름
- 트리거 이벤트 이름

## 클라비요에서 입력 안내 템플릿 만들기

BrazeAI Decisioning Studio™ Go는 Klaviyo 계정의 기존 흐름과 연결된 템플릿을 가져옵니다. 어떤 플로우와도 연결되지 않은 템플릿을 사용하려면 사용하려는 템플릿이 포함된 입력 안내 플로우를 만들면 됩니다. 흐름은 초안으로 남겨둘 수 있으며 라이브 상태일 필요는 없습니다.

### 1단계: 흐름 설정

{% alert note %}
이 플레이스홀더 흐름의 목적은 원하는 콘텐츠를 BrazeAI Decisioning Studio™ Go로 가져오기 위한 것입니다. 이후 단계에서 별도의 플로우를 생성해야 하며, 이 플로우는 실험자가 라이브 상태가 되면 활성화를 트리거하는 데 BrazeAI Decisioning Studio™ Go가 사용합니다.
{% endalert %}

1. 클라비요에서 **플로우를** 선택합니다. 
2. **흐름 만들기** > **처음부터 만들기를** 선택합니다.
3. 입력 안내자 흐름에 알아볼 수 있는 이름을 지정한 다음 **흐름 만들기를** 선택합니다.

!["OFE 입력 안내서 플로우"라는 이름의 플로우입니다.]({% image_buster /assets/img/decisioning_studio_go/create_flow.png %})

{: start="4"}
4\. 트리거를 선택한 다음 플로우를 저장합니다.
5\. **확인을** 선택하고 **저장합니다**. 

### 2단계: 입력 안내 템플릿 만들기

다음으로 입력 안내 템플릿을 만듭니다: 

1. **트리거** 뒤에 **이메일** 노드를 드래그 앤 드롭합니다.

![트리거 노드와 이메일 노드가 있는 플로우입니다.]({% image_buster /assets/img/decisioning_studio_go/set_up_email_node.png %})

{: start="2"}
2\. **이메일** 노드에서 **템플릿 선택을** 선택합니다.
3\. 그런 다음 사용할 템플릿을 선택하고 **템플릿 사용을** 선택합니다.
4\. **저장** > **완료를** 선택합니다.
5\. (선택 사항) BrazeAI Decisioning Studio™ Go에서 사용할 템플릿을 더 추가하려면 다른 **이메일** 노드를 추가하고 2~4단계를 반복합니다.
6\. 모든 이메일을 **초안** 모드로 두고 플로우를 종료합니다.

BrazeAI Decisioning Studio™ Go 포털의 입력 안내 흐름에서 템플릿을 선택할 수 있어야 합니다.

![의사 결정 스튜디오 Go 포털의 입력 안내 클라비요 템플릿의 예입니다.]({% image_buster /assets/img/decisioning_studio_go/placeholder_flow.png %})

## 클라비요에서 플로우 만들기

### 1단계: 흐름 설정

1. 클라비요에서 **플로우** > **플로우 만들기를** 선택합니다.
2. **나만의 구축하기를** 선택합니다.
3. **이름에** BrazeAI Decisioning Studio™ Go 포털의 흐름 이름을 입력합니다. 그런 다음 **수동 생성을** 선택합니다.

![예제 플로우에 대해 '수동으로 만들기' 옵션을 선택했습니다.]({% image_buster /assets/img/decisioning_studio_go/flow1.png %}){: style="max-width:50%;"}

{: start="4"}
4\. 트리거를 선택합니다.
5\. 측정기준 이름을 BrazeAI Decisioning Studio™ Go 포털의 트리거 이벤트 이름과 일치시킵니다.

![트리거 이벤트 이름과 일치하는 측정기준 이름 예시 "OFE_TEST_CASE_API_EVENT_TRIGGER".]({% image_buster /assets/img/decisioning_studio_go/flow2.png %})

{: start="6"}
6\. Select **Save**.

{% alert note %}
실험자에게 기본 템플릿이 하나만 있는 경우 다음 단계를 진행합니다. 실험자에게 기본 템플릿이 두 개 이상인 경우 [3단계로 건너뜁니다: 흐름에 트리거 분할 추가](#step-3-add-a-trigger-split-to-your-flow).
{% endalert %}

### 2단계: 흐름에 이메일 추가하기 

1. **트리거** 노드 뒤에 **이메일** 노드를 드래그 앤 드롭합니다.
2. **이메일 세부 정보에서** **템플릿 선택을** 선택합니다.

!['이메일 세부정보' 섹션에서 '템플릿 선택' 옵션을 선택합니다.]({% image_buster /assets/img/decisioning_studio_go/flow3.png %})

{: start="3"}
3\. 기본 템플릿을 찾아 선택합니다. BrazeAI Decisioning Studio™ Go 포털의 **사용할 리소스** 섹션에서 템플릿 이름으로 템플릿을 검색할 수 있습니다.

![클라비요의 기본 템플릿 예시입니다.]({% image_buster /assets/img/decisioning_studio_go/flow4.png %})

{: start="4"}
4\. **템플릿 사용** > **저장을** 선택합니다.
5\. **제목란에** {% raw %}`{{event.SubjectLine}}`{% endraw %} 을 입력합니다.
6\. **발신자 이름과** **발신자 이메일 주소에** 사용하려는 세부 정보를 입력합니다.

!["이메일 1"의 제목란, 발신자 이름 및 발신자 이메일 주소 예시입니다.]({% image_buster /assets/img/decisioning_studio_go/flow5.png %})

{: start="7"}
7\. **완료를** 선택합니다.
8\. **최근에 이메일로 받은 프로필 건너뛰기** 확인란을 선택 취소한 다음 **저장을** 선택합니다.
9\. 이메일 노드에서 모드를 **임시** 보관에서 **실시간** 보관으로 업데이트합니다.

![이메일 노드에 연결된 트리거 노드를 보여주는 클라비요 플로우 에디터.]({% image_buster /assets/img/decisioning_studio_go/flow6.png %})

You're all set! 이제 BrazeAI Decisioning Studio™ Go를 통해 활성화를 트리거할 수 있습니다. 

### 3단계: 흐름에 트리거 분할 추가하기 

1. **트리거 노드** 뒤에 트리거 **분할** 노드를 드래그 앤 드롭합니다.
2. **트리거 분할** 노드를 선택하고 **차원을** **EmailTemplateID로** 설정합니다.

![차원 이메일 템플릿ID로 구성된 트리거 분할을 공급하는 트리거 노드를 보여주는 클라비요 플로우 다이어그램.]({% image_buster /assets/img/decisioning_studio_go/flow7.png %})

#### 3.1 단계: 이메일 템플릿 추가

1. BrazeAI Decisioning Studio™ Go 포털의 **리소스 사용** 섹션에서 첫 번째 템플릿의 **이메일 템플릿 ID를** 찾습니다. **차원** 필드에 **이메일 템플릿 ID를** 입력한 다음 **저장을** 선택합니다.
2. **이메일** 노드를 **트리거 분할의** **예** 분기로 드래그 앤 드롭합니다. 

![이메일 노드로 연결되는 Yes 브랜치와 다른 트리거 분할에 연결되는 No 브랜치가 있는 트리거 분할 노드가 있는 클라비요 플로우입니다.]({% image_buster /assets/img/decisioning_studio_go/flow8.png %})

{: start="3"}
3\. **이메일 세부 정보에서** **템플릿 선택을** 선택합니다.
4\. 기본 템플릿을 찾아 선택합니다. BrazeAI Decisioning Studio™ Go 포털의 **리소스 사용** 섹션에서 기본 템플릿 이름으로 템플릿을 검색할 수 있습니다.
5\. **템플릿 사용** > **저장을** 선택합니다.
6\. **제목란에** {% raw %}`{{event.SubjectLine}}`{% endraw %} 을 입력합니다.
7\. **발신자 이름과** **발신자 이메일 주소에** 사용하려는 세부 정보를 입력합니다.

![선택한 이메일 템플릿과 제목란, 발신자 이름, 발신자 이메일 주소에 대한 필드입니다.]({% image_buster /assets/img/decisioning_studio_go/flow5.png %})

{: start="8"}
8\. **완료를** 선택합니다.
9\. **최근에 이메일로 받은 프로필 건너뛰기** 확인란을 선택 취소한 다음 **저장을** 선택합니다.
10\. 이메일 노드에서 모드를 **임시** 보관에서 **실시간** 보관으로 업데이트합니다.

#### 3.2 단계: 새 트리거 분할 추가하기

그런 다음 실험자가 사용할 각 추가 기본 템플릿에 대해 **트리거 분할** 및 **이메일** 노드를 새로 만듭니다. 

1. 다른 **트리거 분할** 노드를 이전 **트리거 분할** 노드의 분기 **없음으로** 드래그 앤 드롭합니다.
2. **차원을** **이메일** **템플릿 ID로** 설정하고 설정 중인 기본 템플릿의 **이메일 템플릿 ID로** **차원** 값을 입력합니다.
3. Select **Save**.

![트리거 분할로 이어지는 트리거 노드를 보여주는 Klaviyo 흐름 편집기의 다이어그램. 트리거 분할에는 이메일 노드로 연결되는 예 분기와 추가 이메일 노드로 연결되는 다른 트리거 분할에 연결되는 아니요 분기가 있습니다.]({% image_buster /assets/img/decisioning_studio_go/flow9.png %})

{: start="4"}
4\. 새 트리거 분할의 **예** 브랜치에 **이메일** 노드를 드래그 앤 드롭합니다.
5\. [3.1단계의](#step-31-add-your-email-template) 1~5단계를 반복하여 해당 템플릿을 선택합니다.
5\. **제목란을** {% raw %}`{{event.SubjectLine}}`{% endraw %} 으로 설정하고 **최근 이메일로 받은 프로필 건너뛰기** 확인란을 선택 취소합니다.
6\. 실험자가 사용 중인 각 기본 템플릿에 대해 **트리거 분할** 노드와 **이메일** 노드가 하나씩 생길 때까지 이 과정을 반복합니다. 마지막 트리거 분할은 "아니요" 브랜치에 아무것도 없어야 합니다.

![여러 이메일 노드로 분기되는 여러 트리거 분할 노드가 있는 클라비요 플로우입니다.]({% image_buster /assets/img/decisioning_studio_go/flow10.png %})

{: start="7"}
7\. 각 **이메일** 노드에서 모드를 **임시** 보관에서 **실시간** 보관으로 업데이트합니다.

![노드 상태를 '라이브'로 업데이트하는 옵션입니다.]({% image_buster /assets/img/decisioning_studio_go/flow11.png %})

You're all set! 이제 BrazeAI Decisioning Studio™ Go를 통해 활성화를 트리거할 수 있습니다. 