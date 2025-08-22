---
nav_title: Braze의 SSL
article_title: SSL 개요
page_order: 5
page_type: reference
description: "이 참조 문서에서는 SSL, 그것이 사용되는 용도 및 Braze에서 사용되는 방법에 대해 다룹니다."
channel: email

---

# Braze의 SSL

{% multi_lang_include video.html id="zP1N_wN0SsQ" align="right" %}

> 보안 소켓 계층 (SSL)은 보안성이 낮은 HTTP 대신 HTTPS로 URL을 암호화합니다. URL에 HTTPS가 있으면 유효하고 신뢰할 수 있는 SSL 또는 TLS 인증서가 존재하며, 웹사이트가 안전하게 방문할 수 있고 위험한 악성 소프트웨어의 출처가 아님을 나타냅니다.

## SSL이 왜 중요한가요?

대부분의 도메인은 SSL이 필요하지 않지만, Braze는 다음과 같은 주요 이유로 SSL 사용을 강력히 권장합니다.

SSL로 웹사이트와 링크를 보호하는 것은 민감한 고객 정보를 직접 다루지 않는 회사에서도 일반적인 관행입니다. 사용자는 SSL로 보호된 링크를 더 신뢰하며, 추가 인증 계층은 귀하의 데이터를 보호하는 데 도움이 됩니다.

### 클릭 및 오픈 추적에 필요

Braze에서 이메일을 보낼 때 먼저 사용자의 클릭 및 열람을 추적하기 위해 브랜딩된 링크 추적 서브도메인을 사용하여 링크를 변환합니다. 기본적으로, 이러한 링크는 HTTP로 시작됩니다. 이는 비보안 트래픽을 제한하는 브라우저나 확장을 사용하는 사용자가 URL이 안전하더라도 리디렉션을 통과하여 대상 URL에 도달하는 데 어려움을 겪을 수 있음을 의미합니다. 이로 인해 이메일 전반에 걸쳐 이미지가 깨지고 부정확한 클릭 및 오픈 추적이 발생할 수 있습니다. 이러한 이유로 이메일에서 안전한 리디렉션을 확인하기 위해 링크 추적 서브도메인에 SSL 레이어를 적용하는 것이 모범 사례입니다. 

### 브라우저 요구 사항

SSL 프로토콜은 오늘날 Google Chrome과 같은 주요 브라우저가 사용자를 보호하기 위해 비보안 URL을 통한 트래픽을 제한하기 시작하면서 점점 더 널리 사용되고 있습니다. SSL을 웹사이트에 사용하는 회사는 주요 브라우저와의 확인을 통해 콘텐츠가 신뢰할 수 있음을 보장하여 이메일에서 링크나 이미지가 깨지는 등의 콘텐츠 보기 문제를 최소화합니다.

### HSTS 도메인 요구 사항 

사용자가 어떤 브라우저에서 이메일에 액세스하든지 간에, HTTP 엄격 전송 보안(HSTS) 도메인이 있는 경우 SSL을 설정하고 필요한 보안 인증서를 전송하기 위해 CDN을 구성해야 합니다. SSL 설정 실패는 이미지 및 웹 링크가 깨지게 합니다.

## SSL 인증서 획득

타사, 일반적으로 콘텐츠 전달 네트워크(CDN)를 사용하여 SSL 인증서를 획득할 수 있습니다. CDN은 SSL 인증서를 호스팅하고 링크 중 하나가 클릭될 때마다 브라우저에 제공할 수 있습니다. 이는 트래픽을 CDN을 통해 리디렉션하여 필요한 인증서를 적용한 후 이메일 파트너인 SendGrid 또는 SparkPost로 보내는 방식으로 수행됩니다.

SSL 설정을 시작하려면 Braze 고객 성공 매니저에게 연락하여 전체 Braze 이메일 설정을 시작하세요.

Braze가 이 설정을 시작한 후 다음 단계를 따르십시오:
1. Braze는 도메인 등록부에 추가할 DNS 레코드를 제공합니다.
2. Braze는 레코드가 레지스트리에 올바르게 추가되었는지 확인할 것입니다.
3. 이후, CDN을 선택하고 타사 제공업체로부터 SSL 인증서를 발급받게 됩니다. 
4. 이 시점에서 CDN을 설정합니다. Braze는 CDN 구성 문제를 해결하는 데 도움을 줄 수 없음을 유의하세요. CDN 제공업체에 추가 지원을 요청하십시오.
5. 귀하의 고객 성공 매니저에게 연락하여 SSL을 켜십시오.

### CDN이란 무엇이며, 왜 필요한가요?

콘텐츠 전달 네트워크(CDN)는 여러 매체에서 고품질 콘텐츠의 빠른 로드 시간을 보장하고 보안 인증서를 처리하는 서버 플랫폼입니다. 

{% alert important %}
CDN 구성은 항상 Braze에서 DNS 레코드를 검증한 후에 따릅니다. 이 단계를 아직 시작하지 않았다면 고객 성공 매니저에게 연락하여 시작하는 방법에 대한 자세한 정보를 얻으세요.
{% endalert %}

Braze에서 클릭 및 오픈 추적을 수행하기 위해, 우리의 전달 파트너들은 브랜드 하위 도메인을 사용하여 링크를 변환하고, CDN은 새로 변환된 링크에 SSL 인증서를 적용합니다. 종종, 우리의 전달 파트너는 링크와 이미지가 올바르게 표시되도록 하기 위해 귀하의 이메일 수신자의 브라우저에 유효하고 신뢰할 수 있는 인증서를 제시해야 합니다. Braze는 이러한 인증서를 요청하거나 관리하지 않기 때문에 CDN을 통해 직접 설정해야 합니다. 

{% alert note %}
SSL을 클릭 및 오픈 추적을 설정할 때 나열된 CDN을 사용할 수 없거나 사용하지 않으려는 경우, 커스텀 SSL 구성을 설정할 수 있습니다. 대체 CDN 또는 커스텀 프록시를 사용하면 더 복잡하고 미묘한 설정이 될 수 있습니다. [SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) 및 [SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/) 기사 참조
{% endalert %}

#### 추가 자료

{% alert important %}
CDN 구성 문제 해결에 대한 추가 지원이 필요하면 CDN 제공업체에 문의해야 합니다.
{% endalert %}

The following table includes step-by-step guides written by ESP partners on how to configure certain CDNs. 특정 CDN이 나열되지 않았더라도, CDN이 SSL 인증서를 적용할 수 있는지 확인해야 합니다.

| SendGrid | SparkPost |
| -------- | --------- |
| [AWS Cloudfront](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront)<br>[CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare)<br>[빠르게](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly)<br>[KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) | [AWS Cloudfront](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-aws-cloudfront)<br>[CloudFlare](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare)<br>[빠르게](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly)<br>[구글 클라우드 플랫폼](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-google-cloud-platform)<br>[Microsoft Azure](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-microsoft-azure) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For Amazon SES, refer to [Option 2: Configuring an HTTPS domain](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) and specify the AWS tracking domain by your region based on your Braze cluster:

- **Braze US clusters:** `r.us-east-1.awstrack.me`
- **Braze EU clusters:** `r.eu-central-1.awstrack.me`

{% alert important %}
When configuring your CDN's click-tracking domain, make sure you enable the `X-Forwarded-Host` header. This is used to prevent potential security issues, such as host header attacks. Refer to the CDN documentation or your support team on how to do this, as this varies depending on the CDN.
{% endalert %}

#### 문제 해결

CDN 구성, 인증서 및 프록시 문제는 CDN에서 처리해야 하지만, SSL 클릭 추적 설정과 관련된 일반적인 문제를 식별하는 데 도움이 되는 몇 가지 일반적인 문제 해결 팁은 다음과 같습니다.

##### 도메인 등록 문제

dig 명령은 링크 추적이 CDN을 가리키고 있는지 여부를 알려줄 수 있습니다. 이 작업은 터미널에서 `dig CNAME link_tracking_subdomain`을 실행하여 수행할 수 있습니다. 명령이 실행된 후 `ANSWER SECTION` 아래에 CNAME이 가리키는 위치가 나열되어야 합니다. 선택한 이메일 서비스 공급자(SendGrid 또는 SparkPost)가 아닌 CDN을 가리키고 있다면, 도메인 레지스트리를 재구성하여 CDN을 가리키도록 해보세요.

##### CDN 문제

설정 중에 라이브 이메일 링크가 끊어지기 시작하면, 이는 일반적으로 DNS를 적절히 구성하지 않고 CDN으로 지정했음을 의미합니다. 이것은 "잘못된 링크" 오류로 나타날 수 있습니다. CDN 제공업체에 문의하고 설명서를 검토하여 CDN 구성을 문제 해결하는 데 도움을 받으세요.

##### SSL 인에이블먼트 상태

SSL 설정을 완료했지만 링크가 여전히 HTTP로 표시되고 HTTPS로 표시되지 않는 경우, Braze 고객 성공 매니저에게 연락하여 Braze에서 SSL이 활성화되었는지 확인하십시오. SSL은 SSL 설정의 모든 측면이 완료된 후에만 Braze에 의해 활성화될 수 있습니다.

