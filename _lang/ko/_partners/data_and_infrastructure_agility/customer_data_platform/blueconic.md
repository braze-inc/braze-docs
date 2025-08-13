---
nav_title: BlueConic
article_title: BlueConic
description: "이 참조 문서에서는 Braze와 선도적인 순수 고객 데이터 플랫폼인 BlueConic의 파트너십을 통해 영구적인 개별 프로필에서 데이터를 통합한 다음 두 시스템 간에 동기화하여 Amazon Web Services S3 서버를 통해 가져오기 목표를 달성할 수 있는 방법을 설명합니다."
alias: /partners/blueconic/
page_type: partner
search_tag: Partner

---

# BlueConic

> 선도적인 퓨어플레이 고객 데이터 플랫폼인 [BlueConic][1]은 기업의 퍼스트파티 데이터를 다른 시스템에서 분리하여 언제 어디서나 액세스할 수 있게 함으로써 고객 관계를 혁신하고 비즈니스 성장을 촉진합니다. 

_이 통합은 블루코닉에서 유지 관리합니다._

## 통합 정보

Braze와 BlueConic의 통합을 통해 사용자는 영구적인 개별 프로필에서 데이터를 통합한 다음 Amazon Web Services S3 서버를 통해 가져오기 목표를 위해 두 시스템에서 데이터를 동기화할 수 있습니다. 잠재적인 목표에는 성장 중심 이니셔티브, 고객 라이프사이클 오케스트레이션, 모델링 및 분석, 디지털 제품 및 경험, 오디언스 기반 수익화 등이 있습니다. 이 통합은 예약 배치 가져오기 및 내보내기를 모두 지원합니다. 

{% alert important %}
통합을 사용할 때 BlueConic은 동기화할 때마다 델타(변경 데이터)를 전송합니다. 여기에는 마지막 전송 이후 변경된 모든 프로필과 해당 프로필의 모든 속성이 포함됩니다. 그에 따라 데이터 포인트 사용량을 모니터링하세요.
{% endalert %}

## 전제 조건

| 요구 사항 | 설명 |
| --- | --- |
| BlueConic 계정 | 이 파트너십을 활용하려면 [BlueConic 계정][1]이 필요합니다. 플러그인에 액세스하려면 BlueConic 계정 내에서 [연결을 보고 편집][4]할 수 있는 액세스 권한이 필요합니다. |
| Braze REST API 키 | `users.track`, `users.export.segment`, `campaigns.list`, `campaigns.details`, `segments.lists`, `segments.details` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | REST 엔드포인트 URL. 엔드포인트는 [인스턴스의 Braze URL에][2] 따라 달라집니다. |
| S3 인증 | 데이터를 내보내고 가져오려면 Amazon Web Services(S3) 서버에 액세스할 수 있어야 합니다. |
| 액세스 키 ID<br>비밀 액세스 키 | 액세스 키 ID와 비밀 액세스 키를 사용하면 가져오기 및 내보내기를 위해 S3 서버를 인증할 수 있습니다. |
| AWS 버킷 | 플러그인 내에서 S3에 연결해야 합니다. 인증이 완료되면 사용 가능한 버킷이 드롭다운 메뉴에 표시됩니다. 가져오거나 내보낼 파일이 저장되는 곳입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 통합

### 1단계: Braze 연결 만들기

BlueConic의 탐색 표시줄에서 **연결**을 선택한 다음, **연결 추가**를 선택합니다. 표시되는 프롬프트에서 **Braze**를 검색하고 **Braze 연결**을 선택합니다. 

회색 갈매기 모양 아이콘을 클릭하여 연결에서 사용 가능한 메타데이터 필드를 펼치거나 접습니다. 이러한 필드에서 이 연결을 즐겨찾기에 추가하고, 연결 이름을 지정하며, 라벨을 추가하고, 설명을 추가하며, 연결이 [실행되거나 실행되지 않을][5] 경우 이메일 알림을 받도록 선택할 수 있습니다. 

설정을 저장합니다.

### 2단계: Braze 연결 구성

BlueConic과 Braze 간의 연결을 구성하려면 연결을 인증하기 위해 Braze 계정 자격 증명과 Amazon Web Services(S3) 계정 정보를 추가해야 합니다. 

1. BlueConic의 왼쪽 패널에 있는 **설정** 섹션에서 **설정 및 실행**을 선택합니다.<br><br>
2. Braze 인증 페이지가 열리면 여기에 Braze REST API 엔드포인트와 Braze API 키를 입력합니다.<br>
![]({% image_buster /assets/img/blueconic/braze2.png %}){: style="max-width:80%;"}<br><br>
3. S3 설정 및 인증 섹션에서 이러한 자격 증명을 입력합니다: Amazon Web Services(S3) 액세스 키 ID, 비밀 액세스 키 및 S3 버킷. Braze와 Amazon S3 연동을 설정할 때 구성한 [자격 증명과 동일한 자격 증명이어야]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3/) 합니다. 설정을 저장합니다. <br>![]({% image_buster /assets/img/blueconic/braze3.png %}){: style="max-width:80%;"}

### 3단계: 가져오기 또는 내보내기 목표 만들기(가져오기 매핑)

인증이 완료되면 가져오기 또는 내보내기 목표를 하나 이상 생성하고, 연결을 켠 후에, 연결을 예약하거나 실행해야 합니다.

{% tabs %}
{% tab 가져오기 %}

1. 왼쪽 패널에서 **BlueConic으로 데이터 가져기**를 선택하여 Braze 데이터 구성 페이지를 엽니다.<br><br>
2. Braze에서 데이터의 위치를 선택합니다. 여기에서 Braze 오디언스를 선택하여 가져올 데이터를 찾을 위치를 BlueConic에 알려줄 수 있습니다.<br>!['BlueConic 테스트 사용자'로 설정된 BlueConic Braze 오디언스.]({% image_buster /assets/img/blueconic/braze4.png %}){: style="max-width:80%;"}<br><br>
3. 다음으로 Braze와 BlueConic 간의 식별자를 매핑합니다. <br>![BlueConic 'Braze 외부 ID' 필드에 매핑되도록 설정된 Braze 필드 '외부 ID'.]({% image_buster /assets/img/blueconic/braze5.png %}){: style="max-width:80%;"}<br><br> 두 시스템 간에 고객 데이터를 연결하려면 고객 식별자를 하나 이상 입력합니다.<br>**생성 허용...** 확인란을 사용하여 BlueConic에서 기존 BlueConic 프로필과 일치하지 않는 데이터에 대한 새 프로필을 생성할 수 있도록 허용합니다.<br><br>
4. 다음으로, Braze 필드에 내보내려는 BlueConic 데이터 필드를 일치시킵니다. 드롭다운 필드를 사용하여 왼쪽에서 BlueConic 프로필 식별자 또는 프로필 속성정보를 선택하고 해당 Braze 프로필 식별자를 선택합니다. 그런 다음, 드롭다운 메뉴를 사용하여 가져온 콘텐츠가 기존 값에 추가되는 방식을 지정합니다(더하기, 합치기, 프로필 속성정보가 비어 있는 경우에만 설정, Braze 필드가 비어 있는 경우 지우도록 설정).<br>![]({% image_buster /assets/img/blueconic/braze6.png %}){: style="max-width:80%;"}<br><br>**매핑 추가** 버튼을 사용하여 필요에 따라 매핑 행을 추가로 생성합니다. **나머지 필드 추가** 옵션을 사용하여 여러 매핑 행을 추가할 수 있습니다. BlueConic은 나머지 Braze 필드를 감지하고 BlueConic 프로필 속성과 일치시킵니다. 가져오기에 대한 병합 전략(설정, 더하기, 합치기, 빈 경우 설정 또는 지우기)을 설정하고 BlueConic 프로필 속성정보 이름에 커스텀 접두사를 제공할 수 있습니다.<br><br>
5. 마지막으로 **연결 실행을** 선택하여 연결을 시작합니다. 연결 예약 및 실행에 대해 자세히 알아보려면 [BlueConic을](https://support.blueconic.com/hc/en-us/articles/205957522-Scheduling-Connections) 방문하세요.
{% endtab %}
{% tab 내보내기 %}

1. 왼쪽 패널에서 **Braze로 데이터 내보내기**를 선택하여 BlueConic에서 Braze로 데이터 내보내기를 구성합니다.<br><br>
2. 내보낼 BlueConic 세그먼트를 선택합니다. 이 세그먼트의 프로필 중 Braze에서 일치하는 식별자가 있는 프로필만 내보내집니다.<br>![20,000개의 프로필을 포함하는 BlueConic 세그먼트.]({% image_buster /assets/img/blueconic/braze8.png %}){: style="max-width:80%;"}<br><br>
3. 다음으로, BlueConic 프로필과 Braze 필드 사이에 식별자를 연결합니다. 선택적으로 기존 일치 항목을 찾을 수 없는 경우 BlueConic이 새 레코드를 생성하도록 선택할 수 있습니다.<br>![BlueConic 'Braze 외부 ID' 필드에 매핑되도록 설정된 Braze 필드 '외부 ID'.]({% image_buster /assets/img/blueconic/braze7.png %}){: style="max-width:80%;"}<br><br>
4. 다음으로, Braze 필드에 내보내려는 BlueConic 데이터 필드를 일치시킵니다. BlueConic 아이콘의 드롭다운 메뉴를 사용하여 내보내려는 [정보](https://support.blueconic.com/hc/en-us/articles/4405501836955-Braze-Connection#creating-export-goals) 유형을 선택합니다. 사용 가능한 정보로, 프로필 속성정보, BlueConic 프로필 식별자, 연결된 세그먼트, 조회된 모든 상호 작용, 권한 수준 및 정적 텍스트 값이 포함됩니다.<br>![]({% image_buster /assets/img/blueconic/braze6.png %}){: style="max-width:80%;"}<br><br>
5. 마지막으로 **연결 실행을** 클릭하여 연결을 시작합니다. 연결 예약 및 실행에 대해 자세히 알아보려면 [BlueConic을](https://support.blueconic.com/hc/en-us/articles/205957522-Scheduling-Connections) 방문하세요.
{% endtab %}
{% endtabs %}

## 4단계: 연결 토글

Braze 연결 제목 옆에 있는 토글을 사용하여 연결을 켜고 끕니다. 예약된 시간 동안 실행하려면 연결이 켜져 있어야 합니다. 


[1]: https://www.blueconic.com/
[2]: https://portal.aws.amazon.com/billing/signup#/start
[3]: https://console.aws.amazon.com/iam/home?#security_credential
[4]: https://support.blueconic.com/hc/en-us/articles/202607121-BlueConic-Roles
[5]: https://support.blueconic.com/hc/en-us/articles/205957522#h_01F4VR7SG7NKB3FMQXCB2Q8JNZ