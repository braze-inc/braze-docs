---
nav\_title: URL 글 제목 사용자 지정하기: 랜딩 페이지 URL 설명 사용자 지정: "도메인을 Braze 워크스페이스에 연결하여 회사 브랜드로 랜딩 페이지 URL을 사용자 지정하는 방법을 알아보세요." page\_order: 1
---

# 랜딩 페이지 URL 사용자 지정

> 도메인을 Braze 워크스페이스에 연결하여 회사 브랜드로 랜딩 페이지 URL을 사용자 지정하는 방법을 알아보세요.

## 작동 방식

[브레이즈에 도메인을 연결하면](#connecting-your-domain-to-braze) 모든 랜딩 페이지의 기본 도메인으로 사용됩니다. 예를 들어 하위 도메인 `forms.example.com을` 연결하면 이제 랜딩 페이지 URL은 `forms.example.com/holiday-sale이` 됩니다.

{% 경고 메모 %} 사용자 지정 도메인 삭제가 곧 제공될 예정입니다. 도메인을 제거해야 하는 경우 고객 성공 관리자에게 문의하세요. {% endalert %}

## Braze에 도메인 연결하기

관리자에게 아래 단계를 따라 도메인을 Braze 계정에 연결하도록 요청하세요.

1. **설정** > **랜딩 페이지 설정으로** 이동합니다.
2. 연결하려는 도메인을 입력하고 **제출을** 선택합니다. 예를 들어, `forms.example.com`.
3. **TXT** 및 **CNAME** 레코드를 복사하여 도메인 공급업체의 DNS 설정에 붙여넣습니다.
4. Braze 대시보드로 돌아와 연결을 확인합니다.

각 이름과 값이 나열된 TXT 레코드 1개와 CNAME 레코드 2개가 있는 랜딩 페이지 설정 페이지]\[1]

{% 경고 참고 %} 도메인 공급업체에 따라 연결에 최대 48시간이 걸릴 수 있습니다. 프로세스가 완료되면 Braze 대시보드에서 랜딩 페이지에 사용자 지정 도메인을 사용하기 시작합니다. {% endalert %}

## DNS 리소스

아래 목록은 일반적으로 사용되는 도메인 공급업체에서 DNS 레코드를 만들고 관리하기 위한 리소스입니다. 다른 제공업체를 사용하는 경우 해당 제공업체의 설명서를 참조하거나 해당 지원팀에 문의하여 정보를 확인하세요.

| 도메인 공급자 | 리소스 | | --- | --- | Bluehost | [DNS 레코드 설명](https://my.bluehost.com/hosting/help/508)<br> [DNS 관리 DNS 항목 편집 또는 삭제 추가](https://my.bluehost.com/hosting/help/559) | | Dreamhost | [사용자 정의 DNS 레코드를 추가하려면 어떻게 해야 하나요?](https://help.dreamhost.com/hc/en-us/articles/360035516812) | GoDaddy | [CNAME 레코드 추가하기](https://www.godaddy.com/help/add-a-cname-record-19236?) | Cloudflare | [DNS 레코드 관리하기](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/) | Squarespace | [사용자 정의 DNS 설정 추가하기](https://support.squarespace.com/hc/en-us/articles/360002101888-Adding-custom-DNS-records-to-your-Squarespace-managed-domain) | {: .reset-td-br-1 .reset-td-br-2 역할="프레젠테이션" }

## 문제 해결 

### 도메인 연결에 실패했습니다.

도메인이 올바르게 입력되었는지, 도메인 제공업체 계정에서 Braze에 제출한 내용과 일치하는지 확인합니다. 정확하고 일치하면 Braze에서 제공한 TXT 및 CNAME 레코드를 확인합니다. 도메인 공급업체 계정에 입력한 레코드와 일치해야 합니다.

## 자주 묻는 질문

### 여러 하위 도메인을 내 워크스페이스에 연결하거나 하나의 하위 도메인을 여러 워크스페이스에 연결할 수 있나요?

아니요, 현재 워크스페이스에는 하나의 하위 도메인만 연결할 수 있습니다.

### 현재 기본 웹사이트 또는 전송 도메인에 사용하는 것과 동일한 하위 도메인을 사용할 수 있나요?

아니요, 이미 사용 중인 하위 도메인은 사용할 수 없습니다. 이러한 하위 도메인은 유효하지만 이미 다른 용도로 할당되었거나 필수 CNAME 레코드와 충돌하는 DNS 레코드가 있는 경우 랜딩 페이지에 사용할 수 없습니다.

\[1]: {% image\_buster /assets/img/랜딩\_페이지/connect\_subdomain.png %}
