---
nav_title: URL 사용자 정의
article_title: 랜딩 페이지 URL 사용자 지정
description: "도메인을 Braze 워크스페이스에 연결하여 회사 브랜드로 랜딩 페이지 URL을 사용자 지정하는 방법을 알아보세요."
page_order: 1
---

# 랜딩 페이지 URL 사용자 지정

> 도메인을 Braze 워크스페이스에 연결하여 회사 브랜드로 랜딩 페이지 URL을 사용자 지정하는 방법을 알아보세요.

## How it works

[브레이즈에 도메인을 연결하면](#connecting-your-domain-to-braze) 모든 랜딩 페이지의 기본 도메인으로 사용됩니다. 예를 들어, 서브도메인 `forms.example.com`를 연결하면 랜딩 페이지 URL은 이제 `forms.example.com/holiday-sale`이 됩니다.

Braze 계정에 연결할 수 있는 사용자 정의 도메인의 수는 [요금제]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/#plan-tiers)에 따라 다릅니다. 제한을 늘리려면 Braze 계정 관리자에게 문의하세요.

## Braze에 도메인 연결하기

관리자에게 아래 단계를 따라 도메인을 Braze 계정에 연결하도록 요청하세요.

1. **설정** > **랜딩 페이지 설정으로** 이동합니다.
2. 연결하려는 도메인을 입력하고 **제출을** 선택합니다. 예를 들어, `forms.example.com`입니다.
3. **TXT** 및 **CNAME** 레코드를 복사하여 도메인 공급업체의 DNS 설정에 붙여넣습니다.
4. Braze 대시보드로 돌아와 연결을 확인합니다.

![랜딩 페이지 설정 페이지에는 각각의 이름과 값이 나열된 TXT 레코드 1개와 CNAME 레코드 2개가 있습니다.]({% image_buster /assets/img/landing_pages/connect_subdomain.png %})

{% alert note %}
도메인 제공자에 따라 연결하는 데 최대 48시간이 걸릴 수 있습니다. 프로세스가 완료되면 Braze 대시보드에서 랜딩 페이지에 사용자 정의 도메인을 사용하기 시작합니다.
{% endalert %}

## 도메인 제거

Braze 관리자라면 다음 단계를 완료하여 이전에 구성된 도메인을 제거할 수 있습니다:

1. **설정** > **랜딩 페이지 설정으로** 이동합니다.
2. **사용자 정의 도메인 제거** 선택
3. 도메인 제거를 확인합니다.
4. 도메인 설정에서 나열된 DNS 레코드를 제거합니다.

{% alert important %}
사용자 정의 도메인을 제거하면 해당 URL은 더 이상 유효하지 않습니다. 이 도메인을 사용하던 랜딩 페이지는 Braze에서 설정한 기본 도메인으로 자동으로 되돌아갑니다.
{% endalert %}


## DNS 리소스

아래 목록은 일반적으로 사용되는 도메인 공급업체에서 DNS 레코드를 만들고 관리하기 위한 리소스입니다. 다른 제공업체를 사용하는 경우 해당 제공업체의 설명서를 참조하거나 해당 지원팀에 문의하여 정보를 확인하세요.

| 도메인 제공자 | 리소스 |
| --- | --- |
| 블루호스트 | [DNS 레코드 설명](https://my.bluehost.com/hosting/help/508)<br> [DNS 관리 추가, 편집 또는 DNS 항목 삭제](https://my.bluehost.com/hosting/help/559) |
| 드림호스트 | [커스텀 DNS 레코드를 어떻게 추가하나요?](https://help.dreamhost.com/hc/en-us/articles/360035516812) |
| 고대디 | [CNAM 레코드를 추가하기](https://www.godaddy.com/help/add-a-cname-record-19236?) |
| 클라우드플레어 | [DNS 레코드 관리](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/) |
| 스퀘어스페이스 | [커스텀 DNS 설정 추가하기](https://support.squarespace.com/hc/en-us/articles/360002101888-Adding-custom-DNS-records-to-your-Squarespace-managed-domain) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 문제 해결 

### 도메인 연결에 실패했습니다.

도메인이 올바르게 입력되었는지, 도메인 제공업체 계정에서 Braze에 제출한 내용과 일치하는지 확인합니다. 정확하고 일치하면 Braze에서 제공한 TXT 및 CNAME 레코드를 확인합니다. 도메인 공급업체 계정에 입력한 레코드와 일치해야 합니다.

## Frequently asked questions

### 여러 하위 도메인을 내 워크스페이스에 연결하거나 하나의 하위 도메인을 여러 워크스페이스에 연결할 수 있나요?

아니요, 현재 워크스페이스에는 하나의 하위 도메인만 연결할 수 있습니다.

### 현재 기본 웹사이트 또는 전송 도메인에 사용하는 것과 동일한 하위 도메인을 사용할 수 있나요?

아니요, 이미 사용 중인 하위 도메인은 사용할 수 없습니다. 이러한 하위 도메인은 유효하지만 이미 다른 용도로 할당되었거나 필수 CNAME 레코드와 충돌하는 DNS 레코드가 있는 경우 랜딩 페이지에 사용할 수 없습니다.

