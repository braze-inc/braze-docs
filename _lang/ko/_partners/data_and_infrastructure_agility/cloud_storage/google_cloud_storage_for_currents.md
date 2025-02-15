---
nav_title: Google Cloud Storage
article_title: Google Cloud Storage
alias: /partners/google_cloud_storage_for_currents/
description: "이 참조 문서에서는는 구조화되지 않은 데이터를 위한 대규모 확장 가능한 오브젝트 스토리인 Google Cloud Storage와 Braze 간의 파트너십을 간략히 설명합니다."
page_type: partner
tool: Currents
search_tag: Partner

---

# Google Cloud Storage

> [Google Cloud Storage](https://cloud.google.com/storage/)는 Google이 클라우드 컴퓨팅 제품 스위트의 일부로 제공하는 대규모 확장 가능한 비정형 데이터용 오브젝트 스토리지입니다.

Braze와 Google Cloud Storage의 통합을 통해 커런츠 데이터를 Google Cloud Storage로 스트리밍할 수 있습니다. 나중에 ETL 프로세스(추출, 변환, 로드)를 사용하여 데이터를 다른 위치(예: Google BigQuery)로 전송할 수 있습니다.

## 필수 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Google 클라우드 스토리지 계정 | 이 파트너십을 활용하려면 Google Cloud Storage 계정이 필요합니다. |
| 커런츠 | 데이터를 Google Cloud Storage로 다시 내보내려면 계정에 [Braze 커런츠]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)를 설정해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

Google Cloud Storage와 통합하려면, Braze가 기록 중인 스토리지 버킷에 대한 정보를 가져오고(`storage.buckets.get`) 해당 버킷 내에서 오브젝트를 생성(`storage.objects.create`)할 수 있도록 적절한 자격 증명을 설정해야 합니다. 

다음 지침을 사용하여 수행할 수 있습니다. 이 지침에서는 커런츠 통합에 사용할 비공개 키를 생성하는 역할 및 서비스 계정을 생성하는 과정을 안내합니다.

### 1단계: 역할 생성

**IAM 및 관리자** > **역할** > **\+ 역할 만들기로** 이동하여 Google Cloud Platform 콘솔에서 새 역할을 만듭니다.

![][2]

그런 다음, 역할에 이름을 지정하고 **+권한 추가**를 선택하고 다음을 추가합니다. `storage.buckets.get`, `storage.objects.create`, `storage.objects.get`. 그런 다음, **생성**을 선택합니다.

선택적으로, `storage.objects.delete` 권한을 추가하여 Braze에서 불완전한 파일을 정리할 수 있습니다. 드문 경우이긴 하지만 Google Cloud가 연결을 조기에 종료하면 Braze가 불완전한 파일을 Google Cloud Storage에 기록할 수 있습니다. 정상적인 상황에서는 Braze가 재시도하여 올바른 데이터로 새 파일을 생성하고 이전 파일은 Google Cloud Storage에 남겨둡니다.

![][3]

### 2단계: 서비스 계정 만들기

Google Cloud Platform 콘솔에서 **IAM 및 관리자** > **서비스 계정**으로 이동하고 **서비스 계정 생성**을 선택하여 새 서비스 계정을 생성하니다.

![][4]

그런 다음 서비스 계정에 이름을 지정하고 새로 만든 사용자 지정 역할에 대한 액세스 권한을 부여합니다.

![Google Cloud Platform의 서비스 생성 페이지에서 '역할 선택' 필드에 역할의 이름을 입력합니다.][5]

#### 키 만들기

페이지 하단에서 **키 생성** 버튼을 사용하여 Braze에서 사용할 **JSON** 개인키를 생성합니다. 키가 생성되면 컴퓨터에 다운로드됩니다.

![][6]

### 3단계: Braze에서 전류 설정

Braze에서 **전류** > **\+ 전류 만들기** > **Google 클라우드 스토리지 데이터 내보내기로** 이동하여 연동 이름과 연락처 이메일을 입력합니다.

그런 다음, **GCS JSON 자격 증명** 아래에 JSON 비공개 키를 업로드하고 CGS 버킷 이름과 GCS 접두사(선택 사항)를 제공합니다. 

{% alert important %}
커넥터의 자격 증명이 만료되면 커넥터가 이벤트 전송을 중지하므로 자격 증명 파일을 최신 상태로 유지하는 것이 중요합니다. 이 상태가 **48시간** 이상 지속되면 커넥터의 이벤트가 삭제되고 데이터가 영구적으로 손실됩니다.
{% endalert %}

![Braze의 Google 클라우드 스토리지 전류 페이지. 이 페이지에는 통합 이름, 연락처 이메일, GCS JSON 자격 증명, GCS 버킷 이름 및 접두사에 대한 필드가 있습니다.][7]

마지막으로 페이지 하단으로 스크롤하여 내보내려는 메시지 참여 이벤트 또는 고객 행동 이벤트를 선택합니다. 완료되면 Current를 실행합니다.

### 4단계: Google 클라우드 스토리지(GCS) 내보내기 설정하기

Google Cloud Storage(GCS) 내보내기를 설정하려면 **기술 파트너** > **Google Cloud Storage**로 이동하여 GCS 자격 증명을 입력한 다음, **기본 데이터 내보내기 대상으로 설정**을 선택합니다.

{% alert tip %}
**GCS JSON 자격 증명**은 [Google Cloud 설명서](https://cloud.google.com/iam/docs/keys-create-delete)의 단계에 따라 생성됩니다. 생성된 전체 JSON 값을 입력해야 합니다.
{% endalert %}

![Braze 대시보드의 Google Cloud Storage 페이지.][8]{: style="max-width:70%;"}

해당 Google Cloud IAM 서비스 계정에 다음 권한이 있어야 합니다(Braze의 **Google Cloud 저장소** 페이지에서 **자격증명 테스트** 버튼을 선택하여 확인할 수 있습니다):
- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.get`
- `storage.objects.list`

내보낸 파일의 구성과 콘텐츠는 AWS S3, Microsoft Azure 및 Google Cloud Storage 통합에서 동일합니다.

## 내보내기 동작

클라우드 데이터 스토리지 솔루션을 통합하고 API, 대시보드 보고서 또는 CSV 보고서를 내보내려고 하는 사용자는 다음을 경험합니다.

- 모든 API 내보내기는 응답 본문에 다운로드 URL을 반환하지 않으며 데이터 스토리지를 통해 검색해야 합니다.
- 모든 대시보드 보고서와 CSV 보고서는 다운로드할 수 있도록 사용자 이메일로 전송되며(스토리지 권한이 필요하지 않음) 데이터 스토리지에 백업됩니다. 

[2]: {% image_buster /assets/img/gcs1.png %}
[3]: {% image_buster /assets/img/gcs2.png %}
[4]: {% image_buster /assets/img/gcs3.png %}
[5]: {% image_buster /assets/img/gcs4.png %}
[6]: {% image_buster /assets/img/gcs5.png %}
[7]: {% image_buster /assets/img/gcs6.png %}
[8]: {% image_buster /assets/img/gcs7.png %}
