---
nav_title: 도메인 연결
article_title: 도메인 연결
description: "이 문서에서는 사용자 지정 도메인을 Braze 랜딩 페이지에 연결하는 방법에 대해 설명합니다."
page_order: 1
alias: /landing_pages/connect_domain/
---

# 도메인 연결

> 자체 도메인을 Braze 작업 영역에 연결하여 브랜드에 맞게 랜딩 페이지 URL을 사용자 지정하세요.

도메인 또는 하위 도메인을 Braze 계정에 연결하려면 관리자가 아래 단계를 따르도록 합니다.

1. **설정** > **랜딩 페이지 설정으로** 이동합니다.
2. 연결하려는 도메인 또는 하위 도메인을 입력하고 **제출을** 선택합니다. 예를 들어, `forms.example.com`입니다.
3. **TXT** 및 **CNAME** 레코드를 복사하여 도메인 공급업체의 DNS 설정에 붙여넣습니다.
4. Braze 대시보드로 돌아와 연결을 확인합니다.

![랜딩 페이지 설정 페이지에 TXT 레코드 1개와 CNAME 레코드 2개가 각각의 이름과 값과 함께 나열되어 있습니다.][1]

{% alert note %}
도메인 공급업체에 따라 연결에 최대 48시간이 걸릴 수 있습니다. 프로세스가 완료되면 Braze 대시보드에서 랜딩 페이지에 사용자 지정 도메인을 사용하기 시작합니다.
{% endalert %}

## Braze에서 도메인 사용

도메인 인증이 완료되면 해당 도메인은 Braze에서 기본적으로 사용됩니다. 예를 들어 하위 도메인 `forms.example.com` 을 연결하면 랜딩 페이지 URL이 `forms.example.com/holiday-sale` 과 같이 업데이트됩니다.

{% alert note %}
사용자 정의 도메인 삭제 기능이 곧 출시될 예정입니다. 하위 도메인을 제거해야 하는 경우 고객 성공 관리자에게 문의하세요.
{% endalert %}

## 도메인 공급업체의 리소스

아래 목록은 일반적으로 사용되는 도메인 공급업체에서 DNS 레코드를 만들고 관리하기 위한 리소스입니다. 다른 제공업체를 사용하는 경우 해당 제공업체의 설명서를 참조하거나 해당 지원팀에 문의하여 정보를 확인하세요.

| 도메인 공급자 | 리소스 |
| --- | --- |
| Bluehost | [DNS 레코드 설명](https://my.bluehost.com/hosting/help/508)<br> [DNS 관리 DNS 항목 편집 또는 삭제 추가](https://my.bluehost.com/hosting/help/559) |
| 드림호스트 | [사용자 지정 DNS 레코드는 어떻게 추가하나요?](https://help.dreamhost.com/hc/en-us/articles/360035516812) |
| GoDaddy | [CNAME 레코드 추가](https://www.godaddy.com/help/add-a-cname-record-19236?) |
| Cloudflare | [DNS 레코드 관리](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/) |
| 스퀘어스페이스 | [사용자 지정 DNS 설정 추가](https://support.squarespace.com/hc/en-us/articles/360002101888-Adding-custom-DNS-records-to-your-Squarespace-managed-domain) |

{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 문제 해결 

### 도메인 연결에 실패했습니다.

도메인이 올바르게 입력되었는지, 도메인 제공업체 계정에서 Braze에 제출한 내용과 일치하는지 확인합니다. 정확하고 일치하면 Braze에서 제공한 TXT 및 CNAME 레코드를 확인합니다. 도메인 공급업체 계정에 입력한 레코드와 일치해야 합니다.

## 자주 묻는 질문

### 여러 하위 도메인을 내 워크스페이스에 연결하거나 하나의 하위 도메인을 여러 워크스페이스에 연결할 수 있나요?

아니요, 현재 워크스페이스에는 하나의 하위 도메인만 연결할 수 있습니다.

[1]: {% image_buster /assets/img/landing_pages/connect_subdomain.png %}
