---
nav_title: Grouparoo
page_order: 1
description: "이 글에서는 Braze와 Grouparoo 간의 파트너십을 설명합니다. Grouparoo는 오픈 소스 리버스 ETL 도구로, 데이터 웨어하우스의 데이터를 사용하여 마케팅, 영업 및 지원 도구를 쉽게 활용할 수 있게 해줍니다."
page_type: update

---

# Grouparoo

{% alert update %}
Grouparoo에 대한 지원은 2022년 4월부터 중단되었습니다.
{% endalert %}

> [Grouparoo](https://www.grouparoo.com/)는 창고에 있는 데이터를 사용하여 마케팅, 영업 및 지원 도구를 쉽게 사용할 수 있게 해주는 오픈 소스 리버스 ETL 도구입니다. 구성은 모델 중심 UI에서 수행되므로 비기술 팀 구성원도 운영을 지원하기 위해 데이터 동기화를 구성하고 예약할 수 있습니다.

Braze와 Grouparoo 통합은 데이터를 Braze로 전송하여 창고에 저장된 데이터를 운영하기 쉽게 만듭니다. 자동 동기화 일정을 설정하면 최신 정보로 고객 커뮤니케이션을 일관성 있게 강화할 수 있습니다.

## 필수 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Grouparoo 계정 및 프로젝트 | Grouparoo 계정과 프로젝트가 이 파트너십을 활용하는 데 필요합니다.<br><br>이 통합은 Grouparoo에서 제공하는 무료 커뮤니티 에디션 및 엔터프라이즈 솔루션과 함께 사용할 수 있습니다. 설정은 Grouparoo 구성 사용자 인터페이스에서 이루어집니다. |
| Braze REST API 키 | 사용자 및 추적 권한이 있는 Braze REST API 키. <br><br> 이는 **설정** > **API 키**에서 Braze 대시보드에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [당신의 REST 엔드포인트 URL](https://www.grouparoo.com/). 사용자의 엔드포인트는 인스턴스를 위한 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

### 1단계: Grouparoo에서 Braze 앱 만들기

Grouparoo에서 **앱**으로 이동하여 **Braze**를 선택하여 새 Braze 앱을 만드세요. 표시되는 모달에서 Braze API 키 및 REST 엔드포인트를 제공하십시오.

![]({% image_buster /assets/img/grouparoo/add-app.png %})

### 2단계: 모델 및 데이터 소스를 설정

이 통합은 다음 단계로 진행하기 전에 기존 모델과 데이터 소스가 설정되어 있어야 합니다. 이 설정이 되어 있지 않으면 Grouparoo 설명서를 방문하여 [모델](https://www.grouparoo.com/docs/config/models) 및 [데이터 소스](https://www.grouparoo.com/docs/config/sources)를 설정하는 방법을 배우십시오.

### 3단계: Grouparoo에서 Braze 대상을 생성하세요

#### 동기화 모드 선택

Grouparoo에서 탐색 모음에서 모델을 선택하세요. 다음으로, **대상** 섹션으로 스크롤하고 **새 대상 추가**을 클릭합니다.

다음으로, **Braze** 앱을 선택하고, 대상을 이름 짓고, 다음 중 원하는 동기화 모드를 선택하세요.
- **동기화**: 필요에 따라 Braze 사용자를 추가, 업데이트 및 제거합니다. 이 옵션은 새 레코드, 기존 레코드의 변경 사항 및 삭제를 찾습니다.
- **첨가제**: 필요에 따라 Braze 사용자를 추가 및 업데이트하지만, 아무도 제거하지 마십시오. 이 옵션은 Braze에 추가할 새로운 사용자와 기존 Braze 사용자의 변경 사항을 찾지만 삭제는 추적하지 않습니다.
- **강화**: Braze에 이미 존재하는 사용자만 업데이트하십시오. 사용자를 추가하거나 제거하지 마십시오. 이 옵션은 Braze의 기존 사용자만 업데이트합니다.

#### 속성 필드 매핑

다음으로, Grouparoo 속성 필드를 Braze 속성 필드에 매핑해야 합니다. 

![예제 속성 매핑 필드. 이메일, 이름, 성은 동등한 "이메일", "이름", "성" 그룹아루 필드로 설정됩니다.]({% image_buster /assets/img/grouparoo/mapping.png %}){: style="max-width:80%;"}

Braze `external_id` 필드가 소스 테이블의 기본 키에 매핑되었는지 확인하세요. 필요한 사용 사례에 따라 나머지 필드를 매핑합니다.

**레코드 속성정보 보내기** 섹션: 데이터를 매핑할 수 있는 미리 설정된 고객 프로필 필드 목록. 이 중 어느 것이든 Grouparoo 속성에서 동기화할 수 있습니다.

**선택적 Braze 고객 프로필 필드** 섹션: 선택적 커스텀 Braze 고객 프로필 필드를 생성합니다. **새 Braze 고객 프로필 필드**를 클릭하면 Braze에 매핑할 수 있는 모든 사용 가능한 속성을 볼 수 있습니다. 새로 만드는 모든 필드의 이름은 Grouparoo 속성과 동일하지만 이름을 변경할 수 있습니다.

#### Grouparoo 그룹

매핑 외에도 Grouparoo 그룹을 Braze 구독 그룹에 추가할 수도 있습니다. 

![Grouparoo 대상 구성 창의 "Braze 구독 그룹"에서 "최근 자동차 구매로 높은 가치를 지닌" Grouparoo 그룹이 "최근 자동차 구매로 높은 가치를 지닌" Braze 구독 그룹에 추가됩니다.]({% image_buster /assets/img/grouparoo/lists.png %}){: style="max-width:80%;"}

{% alert important %}
이 통합에 대한 추가 세부 정보 및 업데이트는 [Grouparoo의 설명서](https://www.grouparoo.com/docs/integrations/grouparoo-braze)에서 찾을 수 있습니다.
{% endalert %}

