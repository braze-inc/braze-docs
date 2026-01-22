---
nav_title: SSL at Braze
article_title: SSL 개요
page_order: 5
page_type: reference
description: "이 참고 문서에서는 SSL의 정의와 용도, Braze에서 SSL을 사용하는 방법에 대해 설명합니다."
channel: email

---

# SSL at Braze

{% multi_lang_include video.html id="zP1N_wN0SsQ" align="right" %}

> SSL(보안 소켓 계층)은 보안성이 떨어지는 HTTP 대신 HTTPS로 URL을 암호화합니다. URL의 HTTPS는 유효하고 신뢰할 수 있는 SSL 또는 TLS 인증서가 존재하며 해당 웹사이트가 방문하기에 안전하며 위험한 멀웨어의 소스가 아님을 나타냅니다.

## SSL이 중요한 이유는 무엇인가요?

대부분의 도메인에는 SSL이 필요하지 않지만 다음과 같은 주요 이유 때문에 Braze는 SSL 사용을 강력히 권장합니다.

민감한 고객 정보를 직접 다루지 않는 회사에서도 웹사이트와 링크를 SSL로 보호하는 것은 일반적인 관행입니다. 사용자는 SSL로 보안된 링크를 더 신뢰하며, 추가 인증 계층은 사용자 데이터를 보호하는 데 도움이 됩니다.

### 클릭 및 열기 추적에 필요

Braze에서는 이메일을 발송할 때 먼저 브랜드 링크 추적 하위 도메인을 사용하여 링크를 변환하여 사용자 클릭 및 열람을 추적합니다. 기본값으로 이러한 링크는 HTTP로 시작됩니다. 즉, 비보안 트래픽을 제한하는 브라우저나 확장 프로그램을 사용하는 사용자는 대상 URL이 안전하더라도 리디렉션을 통과하기 전에 대상 URL에 도착하기 어려울 수 있습니다. 이로 인해 이미지가 깨지거나 이메일 전체에서 클릭 및 열기 추적이 부정확해질 수 있습니다. 따라서 링크 추적 하위 도메인에 SSL 계층을 적용하여 이메일에서 보안 리디렉션을 확인하는 것이 가장 좋습니다. 

### 브라우저 요구 사항

Google Chrome과 같은 주요 브라우저에서 사용자를 보호하기 위해 안전하지 않은 URL을 통한 트래픽을 제한하기 시작하면서 SSL 프로토콜이 점점 더 널리 사용되고 있습니다. 웹사이트에 SSL을 사용하는 기업은 이러한 주요 브라우저를 통해 콘텐츠가 신뢰할 수 있음을 확인하여 이메일의 끊어진 링크 및 이미지와 같은 콘텐츠 보기 문제를 최소화합니다.

### HSTS 도메인 요구 사항 

사용자가 어떤 브라우저에서 이메일에 액세스하는지에 관계없이 HTTP 엄격한 전송 보안(HSTS) 도메인이 있는 경우 SSL을 설정하고 필요한 보안 인증서를 전송하도록 CDN을 구성해야 합니다. SSL을 설정하지 않으면 이미지와 웹 링크가 모두 끊어집니다.

## SSL 인증서 획득하기

타사, 일반적으로 CDN(콘텐츠 전송 네트워크)을 사용하여 SSL 인증서를 획득할 수 있습니다. CDN은 SSL 인증서를 호스팅하여 링크 중 하나를 클릭할 때마다 브라우저에 제공할 수 있습니다. 이는 이메일 파트너인 SendGrid 또는 SparkPost로 트래픽을 전송하기 전에 필요한 인증서를 적용하기 위해 CDN을 통해 트래픽을 리디렉션하는 방식으로 이루어집니다.

SSL 설정을 시작하려면 Braze 고객 성공 매니저에게 연락하여 전체 Braze 이메일 설정을 시작하세요.

Braze가 이 설정을 시작한 후 다음 단계를 따르세요:
1. Braze는 도메인 레지스트리에 추가할 DNS 레코드를 제공합니다.
2. Braze는 레코드가 레지스트리에 올바르게 추가되었는지 확인합니다.
3. 그런 다음 CDN을 선택하고 타사 제공업체에서 SSL 인증서를 받습니다. 
4. 이 시점에서 CDN을 설정합니다. Braze는 CDN 구성 문제 해결에 도움을 드릴 수 없습니다. 추가 지원이 필요하면 CDN 제공업체에 문의하세요.
5. 고객 성공 매니저에게 연락하여 SSL을 사용 설정하세요.

### CDN이란 무엇이며 왜 필요한가요?

CDN(콘텐츠 전송 네트워크)은 여러 매체에서 고품질 콘텐츠를 빠르게 로드하는 동시에 보안 인증서를 처리할 수 있도록 지원하는 서버 플랫폼입니다. 

{% alert important %}
CDN 구성은 항상 Braze에서 DNS 레코드의 유효성을 검사한 후에 이루어집니다. 아직 이 단계를 시작하지 않았다면 고객 성공 매니저에게 문의하여 시작하는 방법에 대한 자세한 내용을 알아보세요.
{% endalert %}

Braze에서는 클릭 및 열기 추적을 위해 전달 파트너가 브랜드 하위 도메인을 사용하여 링크를 변환하고 CDN이 새로 변환된 링크에 SSL 인증서를 적용합니다. 이메일 전달 파트너는 링크와 이미지가 올바르게 표시되도록 이메일 수신자의 브라우저에 유효하고 신뢰할 수 있는 인증서를 제시해야 하는 경우가 많습니다. Braze는 이러한 인증서를 요청하거나 관리하지 않으므로 CDN을 통해 사용자 측에서 설정해야 합니다. 

{% alert note %}
클릭 및 열기 추적을 위해 SSL을 설정할 때 나열된 CDN을 사용할 수 없거나 사용하지 않으려는 경우 커스텀 SSL 구성을 설정할 수 있습니다. 대체 CDN 또는 커스텀 프록시를 사용하면 설정이 더 복잡하고 미묘하게 달라질 수 있습니다. 이 주제에 대한 [SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) 및 [SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/) 문서를 참조하세요.
{% endalert %}

#### 추가 리소스

{% alert important %}
CDN 구성 문제 해결에 대한 추가 지원이 필요하면 CDN 제공업체에 문의해야 합니다.
{% endalert %}

다음 표에는 특정 CDN을 구성하는 방법에 대해 이메일 서비스 공급업체가 작성한 단계별 가이드가 포함되어 있습니다. 특정 CDN이 목록에 없을 수도 있지만, 해당 CDN에 SSL 인증서를 적용할 수 있는 기능이 있는지 확인해야 합니다.

| SendGrid | SparkPost |
| -------- | --------- |
| [AWS 클라우프론트](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront)<br>[CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare)<br>[빠르게](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly)<br>[KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) | [AWS 클라우프론트](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-aws-cloudfront)<br>[CloudFlare](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare)<br>[빠르게](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly)<br>[Google 클라우드 플랫폼](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-google-cloud-platform)<br>[Microsoft Azure](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-microsoft-azure) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Amazon SES의 경우 [옵션 2를 참조하세요: HTTPS 도메인](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) 을 구성하고 Braze 클러스터를 기반으로 지역별로 AWS 추적 도메인을 지정합니다:

- **Braze US 클러스터:** `r.us-east-1.awstrack.me`
- **Braze EU 클러스터:** `r.eu-central-1.awstrack.me`

{% alert important %}
CDN의 클릭 추적 도메인을 구성할 때 `X-Forwarded-Host` 헤더를 인에이블먼트해야 합니다. 이는 호스트 헤더 공격과 같은 잠재적인 보안 문제를 방지하는 데 사용됩니다. 이 방법은 CDN에 따라 다르므로 CDN 설명서 또는 지원팀에 문의하세요.
{% endalert %}

#### 문제 해결

CDN 구성, 인증서 및 프록시 문제는 CDN에서 처리해야 하지만, 다음은 SSL 클릭 추적 설정의 일반적인 문제를 파악하는 데 도움이 되는 몇 가지 일반적인 문제 해결 팁입니다.

##### 도메인 레지스트리 문제

dig 명령을 사용하면 링크 추적이 CDN을 가리키고 있는지 여부를 알 수 있습니다. 터미널에서 `dig CNAME link_tracking_subdomain` 을 실행하여 이 작업을 수행할 수 있습니다. 명령이 실행되면 `ANSWER SECTION` 아래에 CNAME이 가리키는 위치가 나열됩니다. 선택한 이메일 서비스 제공업체(SendGrid 또는 SparkPost)를 가리키고 CDN을 가리키지 않는 경우 도메인 레지스트리를 CDN을 가리키도록 다시 구성해 보세요.

##### CDN 문제

설정 중에 라이브 이메일 링크가 끊어지기 시작하면 일반적으로 DNS가 제대로 구성되지 않은 상태에서 CDN을 가리키고 있다는 뜻입니다. 이는 '잘못된 링크' 오류로 나타날 수 있습니다. CDN 제공업체에 문의하여 해당 설명서를 검토하여 CDN 구성 문제 해결에 도움을 받으세요.

##### SSL 인에이블먼트 상태

SSL 설정을 완료했는데도 링크가 여전히 HTTPS가 아닌 HTTP로 표시되는 경우 Braze 고객 성공 매니저에게 문의하여 SSL이 인에이블먼트되었는지 확인하세요. SSL은 SSL 설정의 모든 측면이 완료된 후에만 Braze에서 인에이블먼트할 수 있습니다.

