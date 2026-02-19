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

> SSL(보안 소켓 계층)은 HTTP 대신 HTTPS로 URL을 암호화합니다. HTTPS는 유효하고 신뢰할 수 있는 SSL 또는 TLS 인증서가 존재하며 웹사이트를 방문해도 안전하다는 것을 나타냅니다.

## SSL이 왜 중요한가요?

대부분의 도메인은 SSL이 필요하지 않지만, Braze는 이러한 이유로 SSL 사용을 강력히 권장합니다.

SSL로 웹사이트와 링크를 보호하는 것은 민감한 고객 정보를 직접 다루지 않는 회사에서도 일반적인 관행입니다. 사용자는 SSL로 보호된 링크를 더 신뢰하며, 추가 인증 계층은 귀하의 데이터를 보호하는 데 도움이 됩니다.

### 클릭 및 오픈 추적에 필요

Braze는 브랜드 링크 추적 하위 도메인을 사용하여 링크를 변환하여 클릭 및 열기를 추적합니다. 기본값으로 이러한 링크는 HTTP로 시작합니다. 비보안 트래픽을 제한하는 브라우저 또는 확장 프로그램을 사용하는 사용자는 대상 URL이 안전하더라도 리디렉션 앞의 리디렉션을 통과하는 데 어려움을 겪을 수 있습니다. 이로 인해 이미지가 깨지거나 부정확한 추적이 발생할 수 있습니다. 링크 추적 하위 도메인에 SSL을 적용하여 보안 리디렉션을 확인합니다.

### 브라우저 요구 사항

Google Chrome과 같은 주요 브라우저는 사용자를 보호하기 위해 안전하지 않은 URL을 통한 트래픽을 제한합니다. SSL을 사용하면 콘텐츠가 신뢰할 수 있음을 확인하고 이메일의 링크 및 이미지가 깨지는 등의 문제를 최소화할 수 있습니다.

### HSTS 도메인 요구 사항 

HSTS(HTTP 엄격한 전송 보안) 도메인을 사용하는 경우 SSL을 설정하고 필요한 보안 인증서를 전송하도록 CDN을 구성합니다. SSL이 없으면 이미지 및 웹 링크가 끊어집니다.

## SSL 인증서 획득

제3자, 일반적으로 CDN(콘텐츠 전송 네트워크)을 통해 SSL 인증서를 획득합니다. CDN은 인증서를 호스팅하고 사용자가 링크를 클릭할 때 CDN을 통해 트래픽을 리디렉션하여 인증서를 적용하여 SendGrid 또는 SparkPost로 보내기 전에 브라우저에 제공합니다.

SSL 설정을 시작하려면 Braze 고객 성공 매니저에게 문의하여 전체 Braze 이메일 설정을 시작하세요.

Braze가 설정을 시작하면 다음 단계를 따르세요:
1. Braze는 도메인 등록부에 추가할 DNS 레코드를 제공합니다.
2. Braze는 레코드가 레지스트리에 올바르게 추가되었는지 확인할 것입니다.
3. 이후, CDN을 선택하고 타사 제공업체로부터 SSL 인증서를 발급받게 됩니다. 
4. 이 시점에서 CDN을 설정합니다. Braze는 CDN 구성 문제를 해결하는 데 도움을 줄 수 없음을 유의하세요. 추가 지원이 필요한 경우 CDN 제공업체에 문의하세요.
5. SSL을 사용 설정하려면 고객 성공 매니저에게 문의하세요.

### CDN이란 무엇이며, 왜 필요한가요?

CDN(콘텐츠 전송 네트워크)은 여러 매체에서 콘텐츠의 빠른 로드 시간을 보장하는 동시에 보안 인증서를 처리하는 서버 플랫폼입니다. 

{% alert important %}
CDN 구성은 항상 Braze에서 DNS 레코드를 검증한 후에 따릅니다. 아직 이 단계를 시작하지 않았다면 고객 성공 매니저에게 문의하여 시작하는 방법에 대한 자세한 내용을 알아보세요.
{% endalert %}

클릭 및 열기 추적을 위해 전달 파트너는 브랜드 하위 도메인을 사용하여 링크를 변환하고 CDN은 변환된 링크에 SSL 인증서를 적용합니다. 파트너는 링크와 이미지가 올바르게 표시되도록 수신자의 브라우저에 유효한 인증서를 제시해야 하는 경우가 많습니다. Braze는 인증서를 요청하거나 관리하지 않으므로 CDN을 통해 설정해야 합니다. 

{% alert note %}
SSL 클릭 및 열기 추적을 위해 나열된 CDN을 사용할 수 없거나 사용하고 싶지 않은 경우 커스텀 SSL 구성을 설정할 수 있습니다. 대체 CDN 또는 커스텀 프록시를 사용하면 설정이 더 복잡해질 수 있습니다. [SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) 및 [SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/) 설명서를 참조하세요.
{% endalert %}

#### 추가 자료

{% alert important %}
CDN 구성에 대한 문제 해결은 CDN 제공업체에 문의하세요.
{% endalert %}

The following table includes step-by-step guides written by ESP partners on how to configure certain CDNs. 특정 CDN이 나열되지 않았더라도, CDN이 SSL 인증서를 적용할 수 있는지 확인해야 합니다.

| SendGrid | SparkPost |
| -------- | --------- |
| [AWS Cloudfront](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront)<br>[CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare)<br>[빠르게](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly)<br>[KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) | [AWS Cloudfront](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-aws-cloudfront)<br>[CloudFlare](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare)<br>[빠르게](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly)<br>[구글 클라우드 플랫폼](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-google-cloud-platform)<br>[Microsoft Azure](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-microsoft-azure) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For Amazon SES, refer to [Option 2: HTTPS 도메인](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) 을 구성하고 Braze 클러스터를 기반으로 지역별로 AWS 추적 도메인을 지정합니다:

- **Braze US clusters:** `r.us-east-1.awstrack.me`
- **Braze EU clusters:** `r.eu-central-1.awstrack.me`

{% alert important %}
CDN의 클릭 추적 도메인을 구성할 때 `X-Forwarded-Host` 헤더를 인에이블먼트하여 호스트 헤더 공격과 같은 잠재적인 보안 문제를 방지하세요. 단계는 CDN 설명서 또는 지원팀에 문의하세요.
{% endalert %}

#### 문제 해결

CDN 구성, 인증서 및 프록시 문제는 CDN에서 처리해야 하지만, 이 팁을 사용하여 일반적인 SSL 클릭 추적 문제를 식별할 수 있습니다.

##### 도메인 등록 문제

dig 명령을 실행하여 CDN에서 포인트 링크 추적을 확인합니다. 터미널에서 `dig CNAME link_tracking_subdomain` 을 실행합니다. `ANSWER SECTION` 아래에 CNAME이 가리키는 위치가 나열됩니다. CDN이 아닌 이메일 서비스 제공업체(SendGrid 또는 SparkPost)를 가리키는 경우 도메인 레지스트리가 CDN을 가리키도록 다시 구성하세요.

##### CDN 문제

설정 중에 라이브 이메일 링크가 끊어지는 경우 적절한 설정 전에 DNS가 CDN을 가리키고 있을 가능성이 높습니다. 이것은 "잘못된 링크" 오류로 나타날 수 있습니다. CDN 제공업체에 문의하여 해당 설명서를 검토하여 구성 문제를 해결하세요.

##### SSL 인에이블먼트 상태

SSL 설정을 완료했는데도 링크가 여전히 HTTP로 표시되는 경우 Braze 고객 성공 매니저에게 문의하여 SSL이 인에이블되었는지 확인하세요. 모든 설정 단계가 완료된 후에만 Braze에서 SSL을 인에이블먼트합니다.

