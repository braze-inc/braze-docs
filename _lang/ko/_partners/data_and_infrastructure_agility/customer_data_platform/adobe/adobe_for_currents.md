---
nav_title: Adobe for 커런츠
article_title: Adobe for 커런츠
alias: /partners/adobe_for_currents/
description: "이 참고 문서는 Braze Currents와 Adobe 간의 파트너십을 설명합니다. Adobe는 브랜드가 Adobe 데이터를 (커스텀 속성 및 세그먼트) Braze에 실시간으로 연결하고 매핑할 수 있도록 하는 고객 데이터 플랫폼입니다."
page_type: partner
tool: Currents
search_tag: Partner
---

# Adobe for 커런츠

> [Adobe](https://www.adobe.com/)는 브랜드가 Adobe 데이터(커스텀 속성 및 세그먼트)를 Braze에 실시간으로 연결하고 매핑할 수 있는 고객 데이터 플랫폼입니다.

브레이즈와 어도비 통합을 통해 두 시스템 간의 정보 흐름을 원활하게 제어할 수 있습니다. [커런츠]({{site.baseurl}}/user_guide/data/braze_currents/)를 사용하면 데이터를 Adobe에 연결하여 전체 성장 스택에서 실행 가능하게 만들 수 있습니다. 

## 필수 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| 커런츠 | Adobe로 데이터를 다시 내보내려면, 귀하의 계정에 [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)가 설정되어 있어야 합니다. |
| 어도비 경험 플랫폼 계정 | 이 [Adobe Experience Platform 계정](https://experience.adobe.com/#/platform/home)은 이 파트너십을 활용하는 데 필요합니다. |
| 커넥터를 생성할 수 있는 권한 | 이 통합을 사용하기 위해 스트리밍 소스 연결을 생성하려면 권한이 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

### 1단계: Adobe에서 XDM 스키마 만들기

1. Adobe Experience Platform에서 **Schemas**로 이동 > **Create schema** 선택 > **Experience Event** 선택 > **Next** 선택.<br><br>![Adobe 스키마 페이지는 "Braze 커런츠 워크스루"라는 스키마에 대한 것입니다.][1]<br><br>
2. 스키마의 이름과 설명을 제공하십시오. 
3. **구성** 패널에서 스키마 속성을 구성하십시오:
- **필드 그룹**에서 **추가**를 선택한 다음 **Braze 커런츠 사용자 이벤트** 필드 그룹을 추가합니다.
- **저장**을 선택하십시오.

스키마에 대한 자세한 정보는 Adobe의 설명서 [스키마 만들기](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/tutorials/create-schema-ui)를 참조하십시오.

### 2단계: Adobe Experience Platform에 Braze 연결하기

1. Adobe Experience Platform에서 **Sources** > **Catalog** > **마케팅 자동화**으로 이동합니다.
2. Braze 커런츠를 위해 **데이터 추가**를 선택하십시오.
3. [Braze 커런츠 샘플 파일](https://github.com/Appboy/currents-examples/blob/master/sample-data/Adobe/adobe_examples.json)<br><br>![어도비 "데이터 추가 페이지".][2]<br><br>
4. 파일이 업로드된 후, 데이터 흐름 세부정보를 제공하십시오. 여기에는 데이터 세트 및 매핑할 스키마에 대한 정보가 포함됩니다. 
    - 이것이 Braze 커런츠 소스를 연결하는 첫 번째 경우라면, 새 데이터 세트를 만들고 [Step 1](#step-1-create-an-xdm-schema-in-adobe)에서 만든 스키마를 사용해야 합니다. 
    - 이것이 당신의 첫 번째가 아니라면, Braze 스키마를 참조하는 기존 데이터 세트를 사용하십시오.
5. 데이터에 대한 매핑을 구성하고 문제를 해결하십시오.
    - 스키마의 루트 수준에서 `id`에 대한 매핑을 `to _braze.appID`에서 `_id`으로 변경합니다.
    - `properties.is_amp`이 `_braze.messaging.email.isAMP`에 매핑되도록 하세요.
    - `time` 및 `timestamp` 매핑을 삭제한 다음 추가 아이콘 > **계산된 필드 추가**를 선택하고 **시간 * 1000**을 입력합니다. **저장**을 선택하십시오.
    - 새로운 소스 필드 옆에 있는 **맵 대상 필드**를 선택하고 스키마의 루트 수준에서 **타임스탬프**에 매핑합니다. <br><br>![어도비 "데이터 추가" 페이지와 매핑.][3]<br><br>
6. 문제를 해결했음을 확인하려면 **확인**을 선택하십시오.

{% alert important %}
브레이징 타임스탬프는 초 단위로 표현됩니다. Adobe Experience Platform에서 타임스탬프를 정확하게 반영하려면, 계산된 필드가 밀리초 단위여야 합니다. 초를 밀리초로 변환하려면 계산 **time * 1000**을 사용하세요.
{% endalert %}

{: start="7"}
7\. 다음 **Next**을 선택하고, 데이터 흐름 세부 정보를 검토한 후 **Finish**을 선택하십시오.<br><br>![어도비 "데이터 추가" 페이지에 매핑 오류가 없습니다.][4]

### 3단계: 자격 증명 수집

Braze에 입력할 다음 자격 증명을 수집하여 Braze가 Adobe Experience Platform에 데이터를 전송할 수 있도록 합니다.

| 필드         |설명                          |
|---------------|-------------------------------------|
| 클라이언트 ID     | 귀하의 Adobe Experience Platform 소스와 연결된 클라이언트 ID. |
| 클라이언트 비밀 | Adobe Experience Platform 소스와 관련된 클라이언트 비밀. |
| 테넌트 ID     | Adobe Experience Platform 소스와 관련된 임대인 ID. |
| 샌드박스 이름  | Adobe Experience Platform 소스와 연결된 샌드박스.   |
| 데이터플로우 ID   | Adobe Experience Platform 소스와 연결된 데이터 흐름 ID.   |
| 스트리밍 엔드포인트  | 귀하의 Adobe Experience Platform 소스와 연결된 스트리밍 엔드포인트. 브레이징은 이를 배치 스트리밍 엔드포인트로 자동 변환합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 4단계: 커런츠를 구성하여 데이터를 데이터 소스로 스트리밍합니다.

1. 브레이즈에서 **파트너 통합** > **데이터 내보내기**로 이동한 다음 **새로운 현재 만들기**를 선택합니다. 
2. 다음 사항을 제공하십시오:
    - 커넥터의 이름
    - 커넥터에 대한 알림을 위한 연락처 정보
    - [3](#step-3-gather-credentials)의 자격 증명
3. 받고 싶은 이벤트를 선택하세요.
4. 선택적으로 원하는 필드 제외 또는 변환을 구성합니다.
5. 현재 실행 **시작** 선택.

[1]: {% image_buster /assets/img/adobe/currents_sources.png %}
[2]: {% image_buster /assets/img/adobe/currents_add_data.png %}
[3]: {% image_buster /assets/img/adobe/currents_mapping.png %}
[4]: {% image_buster /assets/img/adobe/currents_no_errors.png %}