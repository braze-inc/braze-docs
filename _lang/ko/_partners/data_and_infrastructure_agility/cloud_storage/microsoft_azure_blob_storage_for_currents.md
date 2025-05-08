---
nav_title: Microsoft Azure Blob Storage
article_title: Microsoft Azure Blob Storage
alias: /partners/microsoft_azure_blob_storage_for_currents/
description: "이 참조 문서에서는는 구조화되지 않은 데이터를 위한 대규모 확장 가능한 오브젝트 스토리인 Microsoft Azure Blog Storage와 Braze 커런츠 간의 파트너십을 간략히 설명합니다."
page_type: partner
tool: Currents
search_tag: Partner

---

# Microsoft Azure Blob Storage

> [Microsoft Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/)는 비정형 데이터용 대규모로 확장 가능한 오브젝트 스토리지로, Microsoft에서 Azure 제품군의 일부로 제공됩니다.

Braze와 Microsoft Azure Blob Storage 통합을 통해 데이터를 Azure로 다시 내보내고 커런츠 데이터를 스트리밍할 수 있습니다. 나중에 ETL 프로세스(추출, 변환, 로드)를 사용하여 데이터를 다른 위치로 전송할 수 있습니다.

## 전제 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Microsoft Azure 및 Azure 스토리지 계정 | 이 파트너십을 활용하려면 Microsoft Azure 및 Azure 스토리지 계정이 필요합니다. |
| 커런츠 | 커런츠로 데이터를 내보내려면 계정에 [Braze 커런츠]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)가 설정되어 있어야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

Microsoft Azure Blob Storage와 통합하려면 Braze가 데이터를 Azure로 다시 내보내거나 커런츠 데이터를 스트리밍할 수 있도록 하는 스토리지 계정과 연결 문자열이 있어야 합니다.

### 1단계: 스토리지 계정 생성

Microsoft Azure에서 사이드바의 **스토리지 계정**으로 이동하고 **\+ 추가**를 클릭하여 새 스토리지 계정을 생성합니다. 다음으로, 저장소 계정 이름을 제공하십시오. 다른 기본값 설정은 업데이트할 필요가 없습니다. 마지막으로 **검토 + 만들기**를 선택합니다. 

스토리지 계정이 이미 있어도 Braze 데이터 전용으로 새 계정을 생성하는 것이 좋습니다.

![]({% image_buster /assets/img/azure-currents-step-1.png %})

### 2단계: 연결 문자열 가져오기

저장소 계정이 배포되면 저장소 계정에서 **액세스 키** 메뉴로 이동하여 연결 문자열을 기록하십시오.

Microsoft는 하나의 키를 재생성하는 동안 다른 키를 사용하여 연결을 유지하도록 두 개의 액세스 키를 제공합니다. 이중 하나의 연결 문자열만 있으면 됩니다.

{% alert note %}
Braze는 이 메뉴의 연결 문자열을 사용하며, 키는 사용하지 않습니다.
{% endalert %}

![]({% image_buster /assets/img/azure-currents-step-2.png %})

### 3단계: Blob 서비스 컨테이너를 생성합니다

스토리지 계정의 **Blobs** 메뉴에서 **Blob 서비스** 섹션으로 이동합니다. 이전에 생성한 스토리지 계정 내에서 Blob 서비스 컨테이너를 생성합니다. 

Blob 서비스 컨테이너의 이름을 제공하십시오. 다른 기본값 설정은 업데이트할 필요가 없습니다.

![]({% image_buster /assets/img/azure-currents-step-3.png %})

### 4단계: 커런츠 설정

Braze에서 **커런츠 > + 커런츠 생성 > Azure Blob 데이터 내보내기**로 이동하여 통합 이름과 연락처 이메일을 제공합니다.

다음으로, 연결 문자열, 컨테이너 이름 및 BlobStorage 접두사(선택 사항)를 제공합니다.

![Braze의 Microsoft Azure Blob storage 커런츠 페이지. 이 페이지에는 통합 이름, 연락처 이메일, 연결 문자열, 컨테이너 이름 및 접두사에 대한 필드가 있습니다.]({% image_buster /assets/img/maz.png %})

마지막으로, 페이지 하단으로 스크롤하여 내보내고자 하는 메시지 참여 이벤트 또는 고객 행동 이벤트를 선택하십시오. 완료되면 커런츠를 시작합니다.

### 5단계: Azure 데이터 내보내기 설정

다음은 다음에 사용되는 자격 증명을 구성합니다:
1. 세그먼트는 API를 통해 내보냅니다
2. CSV 내보내기(대시보드를 통해 캠페인, 세그먼트, 캔버스 사용자 데이터 내보내기)
3. 참여 보고서

Braze에서 **파트너 통합** > **기술 파트너** > **Microsoft Azure**로 이동하여 연결 문자열, Azure 스토리지 컨테이너 이름 및 Azure 스토리지 접두사를 제공합니다.

{% alert note %}
[이전 탐색]({{site.baseurl}}/navigation)을 사용하는 경우 **통합**에서 **기술 파트너**를 찾을 수 있습니다.
{% endalert %}

다음으로, **기본 데이터 내보내기 대상으로 설정** 상자가 선택되어 있는지 확인합니다. 이렇게 하면 내보낸 데이터가 Azure로 전송됩니다. 완료되면 통합을 저장하십시오.

![Braze의 Microsoft Azure 데이터 내보내기 페이지. 이 페이지에는 연결 문자열, 컨테이너 이름 및 접두사에 대한 필드가 있습니다.]({% image_buster /assets/img/azure_data_export.png %})

{% alert important %}
연결 문자열을 최신 상태로 유지하는 것이 중요합니다. 커넥터의 자격 증명이 만료되면 커넥터가 이벤트 전송을 중지합니다. 이 현상이 **48시간** 이상 지속되면 커넥터의 이벤트가 삭제되고 데이터가 영구적으로 손실됩니다.
{% endalert %}

## 내보내기 동작

클라우드 데이터 스토리지 솔루션을 통합하고 API, 대시보드 보고서 또는 CSV 보고서를 내보내려고 하는 사용자는 다음을 경험합니다.

- 모든 API 내보내기는 응답 본문에 다운로드 URL을 반환하지 않으며 데이터 스토리지를 통해 검색해야 합니다.
- 모든 대시보드 보고서 및 CSV 보고서는 사용자의 이메일로 전송되어 다운로드할 수 있으며(저장 권한 필요 없음), 데이터 저장소에 백업됩니다. 
