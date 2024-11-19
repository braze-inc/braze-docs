---
nav_title: Transcend
article_title: Transcend
description: "이 참조 문서에서는 Braze 사용자가 데이터 주체 요청을 자동으로 처리할 수 있도록 지원하는 데이터 프라이버시 인프라 플랫폼인 Transcend와 Braze 간의 파트너십을 간략히 설명합니다."
alias: /partners/transcend/
page_type: partner
search_tag: Partner

---

# Transcend

> Transcend는 데이터 프라이버시 인프라 회사로, 기업이 사용자의 데이터를 간편하게 제어할 수 있도록 하여, 모든 데이터 시스템과 벤더 내에서 데이터 주체 요청을 자동으로 처리합니다. 

Braze와 Transcend 파트너십을 통해 사용자는 수십 개의 데이터 시스템에서 데이터를 조율하여 사용자가 개인정보 요청을 자동화하며 팀이 GDPR 및 CCPA와 같은 규정을 준수하도록 돕습니다. Transcend는 최종 사용자에게 `privacy.\<company\>.com`에서 호스팅되는 제어판 또는 개인정보 보호 센터를 제공하여 사용자가 개인정보 보호 기본 설정을 관리하고, 데이터를 내보내거나 삭제할 수 있도록 합니다. 

## 필수 조건

| 요구 사항 | 설명 |
|---|---|
| Transcend 계정 | 이 파트너십을 활용하려면 관리자 권한이 있는 [Transcend](https://app.transcend.io/) 계정이 필요합니다. |
| Braze API 키 | `users.delete, users.alias.new, users.export.ids, email.unsubscribe,` 및 `email.blacklist` 권한이 있는 Braze REST API 키.<br><br>Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

Transcend는 데이터 프라이버시 규정에 따라 Braze 플랫폼에서 사용자의 액세스, 삭제 및 통신 옵트아웃을 프로그래밍 방식으로 허용합니다.

### 1단계: Braze 통합을 설정하십시오
시작하려면 [Transcend](https://app.transcend.io/login)에 로그인하세요.
1. **데이터 맵 > 데이터 사일로 추가 > Braze**로 이동하여 **연결** 버튼을 선택합니다.<br><br>
2. 계정이 프로비저닝되면 해당 URL 중 하나(`https://dashboard-01.braze.com`, `https://dashboard-02.braze.com, ..., https://dashboard-01.braze.eu`)에 로그인합니다.<br> 다음 [표]({{site.baseurl}}/api/basics/#endpoints)를 사용하여 대시보드 URL에 기반하여 포함해야 할 하위 도메인을 확인합니다.<br><br>
3. 연결되면 Transcend **Privacy Center** 탭으로 이동하십시오. 여기에서 Braze의 데이터를 귀하의 데이터 관행에 매핑해야 합니다. 이 작업을 수행하려면 적절한 명명 규칙을 사용하여 새 카테고리와 새 데이터 수집을 생성합니다(예: '메일링 목록또는 고객 프로필'). 완료되면 **게시**를 누르세요.<br><br>
4. 데이터 맵으로 돌아가서 Braze 데이터 사일로를 클릭합니다. **데이터 포인트 관리**를 확장하고 드롭다운에서 이전 단계에서 생성한 컬렉션 라벨(카테고리)을 선택합니다. 어떤 데이터 작업(예: 접근 또는 삭제)이 어떤 데이터 포인트에 대해 활성화되는지도 선택할 수 있습니다. <br><br>
5. 다음으로, 여전히 Braze 데이터 사일로에 있는 동안, **식별자 관리**를 확장합니다. 각 식별자를 활성화하려면 해당 상자를 선택하십시오. 예를 들어, Transcend에서 이메일 주소로 사용자를 검색하려면, 이메일 주소 식별자를 활성화하기 위해 상자를 선택해야 합니다.

{% alert note %}
식별자가 올바르게 활성화되지 않으면 Transcend가 특정 사용자의 요청을 처리하지 않을 수 있습니다.
{% endalert %}

### 2단계: 테스트 요청
Transcend는 최종사용자의 요청을 처리하기 전에 데이터 맵 전반에 걸쳐 요청을 테스트할 것을 권장합니다.
1. Transcend의 **Privacy Center**로 이동하여 **View your Privacy Center**를 클릭하십시오.<br><br>
2. 귀하의 **개인정보 보호 센터**에서 **제어권 가져오기**를 클릭한 다음 **내 데이터 다운로드**를 클릭합니다. 요청을 제출하기 전에 이메일을 입력하거나 로그인하여 본인 인증을 하세요.<br><br>
3. Transcend에서 보낸 메시지가 있는지 이메일을 확인합니다. 귀하는 요청을 확인하기 위해 확인 링크를 클릭하라는 요청을 받을 것입니다.<br><br>
4. 다음으로, **관리** 대시보드로 돌아가서 **수신 요청** 탭으로 이동하여 요청을 선택합니다. 여기에 요청이 표시되지 않으면 Transcend([support@transcend.io](mailto:support@transcend.io))에 문의하세요.<br><br>
5. 요청을 클릭한 후 **데이터 사일로** 탭으로 이동하여 **Braze**를 선택합니다. 반환된 데이터를 검사하고 확인합니다.<br><br>
6. 마지막으로 **보고서** 탭으로 이동하여 **승인 및 전송**을 클릭합니다. 요청과 함께 제출한 이메일 주소로 보고서를 받아야 합니다.

## Braze 통합을 제거
Transcend 데이터 맵에서 Braze 데이터 사일로를 제거하려면 다음을 수행합니다.
1. **데이터 맵**으로 이동하여 **Braze**를 클릭합니다. <br><br>
2. 화면 하단에서 **Remove Braze**을 확장하고 **Remove Silo**을 클릭합니다. 사일로를 제거할 것인지 묻는 프롬프트가 표시됩니다. **확인**을 클릭합니다. <br><br>
3. 데이터 맵으로 돌아가 사일로가 제거되었는지 확인합니다.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints