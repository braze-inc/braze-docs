---
nav_title: 자카드
article_title: 자카드
page_order: 1
description: "이 참조 문서에서는 웹훅을 통해 구독자로부터 클릭 추적 정보를 수집하기 위해 Braze 전류 및 커넥티드 콘텐츠를 활용하는 Braze와 자카드 동적 최적화 간의 파트너십에 대해 설명합니다. 그런 다음 Jacquard는 이러한 이벤트를 언어 배리언트에 다시 연결하여 실시간 언어 최적화를 수행합니다."
page_type: partner
search_tag: Partner
---

# 자카드 동적 최적화

> [Jacquard는][1] 인공 지능, 컴퓨터 언어학, 고객 중심 정신을 결합하여 브랜드 보이스에 맞게 맞춤화된 브랜드 언어를 채널 전반에 걸쳐 대규모로 배포할 수 있도록 지원합니다.

Jacquard X에서 제공하는 동적 최적화는 Braze Currents 및 연결된 콘텐츠를 활용하여 웹훅을 통해 구독자로부터 클릭 추적 정보를 수집합니다. 그런 다음 Jacquard는 이러한 이벤트를 언어 배리언트에 다시 연결하여 실시간 언어 최적화를 수행합니다. 

## 전제 조건

| 요구 사항 | 설명 |
|---|---|
| Jacquard 계정 | 이 파트너십을 이용하려면 [Jacquard 계정이][1] 필요합니다. |
| Jacquard 연결 서버 토큰 | Jacquard 언어에 액세스하기 위한 Braze 캠페인의 비밀번호로 사용되는 긴 문자열.<br><br>아직 제공받지 못한 경우 Jacquard 고객 성공 매니저에게 요청할 수 있습니다. |
| 커런츠 | 데이터를 커런츠로 내보내려면 계정에 [Braze 커런츠]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)를 설정해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

### 1단계: Jacquard Amazon S3 자격 증명 요청하기

Braze에서 클릭 추적 이벤트를 수신하려면 전용 Amazon S3 버킷을 설정하는 Jacquard가 필요합니다. 이 프로세스를 시작하려면 Jacquard 고객 성공 매니저에게 문의하세요. 버킷이 생성되면 Current를 만들 수 있는 고유한 자격 증명이 제공됩니다. 

### 2단계: 현재 만들기

1. Braze에서 **커런츠 > 새 커런츠 생성 > Amazon S3 데이터 내보내기**를 선택합니다. 
2. 다음으로, 현재 이름을 지정하고 연락처 이메일을 입력합니다.
3. 자격 증명 상자에 Jacquard AWS 액세스 키 ID와 비밀 액세스 키를 추가합니다. 그런 다음, AWS S3 버킷 이름으로 'phrasee-braze-currents-exports'를 추가합니다. 
4. 마지막으로 Jacquard 고객 성공 관리자로부터 받은 AWS S3 버킷 폴더를 추가합니다. 회사 이름이 될 가능성이 높습니다.
5. **일반 설정에서**'익명 사용자의 이벤트 포함' 상자를 선택하고 **참여 이벤트 관리에서** '이메일 클릭'을 선택합니다.
6. 완료했으면 **커런츠 시작**을 선택합니다.

### 3단계: 개인 식별 정보(PII) 삭제 요청.

다음으로, Braze 계정 팀에 문의하여 개인 식별 정보가 Jacquard에 전송되지 않도록 하세요.

기본적으로 커런츠에는 이메일 및 주소와 같은 특정 PII 속성이 포함됩니다. Jacquard는 PII를 수신할 수 없으며 앞으로도 수신하지 않으므로, Jacquard로 전달되는 모든 이벤트 데이터에 대해 이 기능을 해제하도록 Braze 계정 팀에 요청해야 합니다.

### 4단계: 자카드 X 코드 스니펫 

필요한 코드 스니펫은 Jacquard 계정 팀에 문의하세요.

이 스니펫은 [연결된 콘텐츠]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content)를 활용하며, 이메일에 배치된 후에는 언어와 추적 픽셀을 동적으로 가져와서 Jacquard에서 Jacquard X를 통해 실시간으로 언어를 최적화할 수 있습니다.


[1]: https://www.jacquard.com/
[3]: mailto:awesome@phrasee.co