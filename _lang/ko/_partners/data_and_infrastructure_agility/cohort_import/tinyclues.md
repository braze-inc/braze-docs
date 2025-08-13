---
nav_title: Tinyclues
article_title: Tinyclues
alias: /partners/tinyclues/
description: "이 참조 문서에서는 매우 사용자 친화적인 UI를 사용하여 더 많은 타겟팅 캠페인으로 전송하고, 새로운 제품 기회를 찾고, 수익을 높일 수 있는 잠재고객 구축 기능을 제공하는 Braze와 Tinyclues의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner

---

# Tinyclues

> [Tinyclues는](https://www.tinyclues.com/) 고객 경험에 영향을 주지 않으면서 캠페인 수와 수익을 늘릴 수 있는 잠재고객 구축 기능으로, 온라인과 오프라인에서 CRM 캠페인의 성과를 추적할 수 있는 분석 기능을 제공합니다.

Braze와 Tinyclues의 통합은 사용자에게 더 나은 CRM 계획 및 전략의 길을 열어주며, 사용자 친화적인 UI를 통해 더 많은 타겟팅 캠페인을 보내고, 새로운 제품 기회를 모색하며, 매출을 확대할 수 있도록 지원합니다.

## 전제 조건

| 요구 사항 | 설명 |
|---|---|
| Tinyclues 계정 | 이 파트너십을 이용하려면 Tinyclues 계정이 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 데이터 가져오기 통합

Braze와 Tinyclues를 통합하려면 Tinyclues 플랫폼을 구성하고, 기존 Tinyclues 캠페인을 내보내고, 향후 캠페인에서 사용자를 타겟팅하는 데 사용할 수 있는 사용자 코호트 세그먼트를 Braze에서 만들어야 합니다.

### 1단계: Braze 데이터 가져오기 키 받기

Braze에서 **파트너 통합** > **기술 파트너**로 이동하여 **Tinyclues**를 선택합니다. 

여기에서 REST 엔드포인트를 찾아 Braze 데이터 가져오기 키를 생성합니다. 키가 생성된 후에는 새 키를 생성하거나 기존 키를 무효화할 수 있습니다.<br><br>![][6]{: style="max-width:90%;"} 

통합을 완료하려면 데이터 가져오기 키와 REST 엔드포인트를 Tinyclues 데이터 운영 팀에 제공해야 합니다. 그러면 설정이 완료되면 Tinyclues에서 연결을 설정하고 연락을 드립니다.

### 2단계: Tinyclues 플랫폼에서 캠페인 내보내기

Braze에서 사용할 Tinyclues 사용자 코호트를 생성하려면 항상 먼저 Tinyclues 플랫폼에서 코호트를 내보내야 합니다.

Tinyclues에서 내보내려는 캠페인을 선택하고 **캠페인 내보내기**를 클릭합니다. 내보내면 오디언스가 자동으로 Braze 계정에 업로드됩니다.

![][1]

### 3단계: Tinyclues 맞춤 오디언스에서 세그먼트 만들기

Braze에서 **세그먼트로** 이동하여 Tinyclues 코호트 세그먼트의 이름을 지정하고 **Tinyclues 코호트를** 필터로 선택합니다. 여기에서 포함할 Tinyclues 코호트를 선택할 수 있습니다. Tinyclues 코호트 세그먼트가 생성된 후에는 캠페인이나 캔버스를 만들 때 오디언스 필터로 선택할 수 있습니다.

![][3]{: style="max-width:90%;"}<br><br>
![Braze 세그먼트 빌더에서 사용자 속성 필터 'Tinyclues 코호트'는 '포함' 및 '기본 코호트'로 설정되어 있습니다.][4]{: style="max-width:90%;"}

코호트를 찾는 데 문제가 있나요? [문제 해결](#troubleshooting) 섹션에서 지침을 확인하세요. 

{% alert important %}
Braze 내에 이미 존재하는 사용자만 코호트에 추가되거나 제거됩니다. 코호트 가져오기는 Braze에서 새로운 사용자를 생성하지 않습니다.
{% endalert %}

## 이 통합 사용

Tinyclues 세그먼트를 사용하려면 Braze 캠페인 또는 캔버스를 생성하고 세그먼트를 타겟 오디언스로 선택합니다. 

![타겟팅 단계의 Braze 캠페인 빌더에서 '세그먼트별 타겟 사용자' 필터가 'Tinyclues 코호트'로 설정되어 있습니다.][5]{: style="max-width:90%;"}

## 사용자 일치

식별된 사용자는 `external_id` 또는 `alias`로 일치할 수 있습니다. 익명 사용자는 `device_id`로 매칭될 수 있습니다. 익명 사용자로 처음 생성된 식별된 사용자는 `device_id`로 식별할 수 없으며, `external_id` 또는 `alias`로 식별해야 합니다.

## 문제 해결

목록에서 적합한 코호트를 찾는 데 문제가 있나요? Tinyclues에서 캠페인 세부 정보를 확인하고 **파일 이름 내보내기**를 선택하여 이름을 확인합니다.

![캠페인 세부 정보 페이지 하단에 코호트 이름이 표시됩니다.][2]{: style="max-width:30%;"}

여전히 오디언스를 검색하는 데 문제가 있나요? 추가 지원이 필요한 경우 [Tinyclues 팀에](mailto:support@tinyclues.com) 문의하세요.

[1]: {% image_buster /assets/img/tinyclues/tinyclues_1.png %}
[2]: {% image_buster /assets/img/tinyclues/tinyclues_2.png %}
[3]: {% image_buster /assets/img/tinyclues/tinyclues_3.png %}
[4]: {% image_buster /assets/img/tinyclues/tinyclues_4.png %}
[5]: {% image_buster /assets/img/tinyclues/tinyclues_5.png %}  
[6]: {% image_buster /assets/img/tinyclues/tinyclues_6.png %}  