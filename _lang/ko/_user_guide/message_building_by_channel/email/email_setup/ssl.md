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

> 보안 소켓 계층(SSL)은 HTTP 대신 HTTPS로 URL을 암호화합니다. HTTPS는 유효하고 신뢰할 수 있는 SSL 또는 TLS 인증서가 존재하며 해당 웹사이트를 안전하게 방문할 수 있음을 나타냅니다.

## SSL이 왜 중요한가요?

대부분의 도메인은 SSL이 필요하지 않지만, Braze는 다음과 같은 이유로 SSL 사용을 강력히 권장합니다.

SSL로 웹사이트와 링크를 보호하는 것은 민감한 고객 정보를 직접 다루지 않는 회사에서도 일반적인 관행입니다. 사용자는 SSL로 보호된 링크를 더 신뢰하며, 추가 인증 계층은 귀하의 데이터를 보호하는 데 도움이 됩니다.

### 클릭 및 오픈 추적에 필요

Braze는 클릭 및 열람을 추적하기 위해 귀사의 브랜드 링크 추적 서브도메인을 사용하여 링크를 변환합니다. 기본값으로 이러한 링크는 HTTP로 시작합니다. 비보안 트래픽을 제한하는 브라우저나 확장 프로그램을 사용하는 사용자는 대상 URL이 보안 URL이라 하더라도 해당 URL 이전의 리다이렉션을 통과하는 데 어려움을 겪을 수 있습니다. 이로 인해 이미지가 깨지거나 추적이 부정확해질 수 있습니다. 링크 추적 서브도메인에 SSL을 적용하여 안전한 리디렉션을 확인하십시오.

### 브라우저 요구 사항

Google Chrome과 같은 주요 브라우저는 사용자를 보호하기 위해 비보안 URL을 통한 트래픽을 제한합니다. SSL을 사용하면 콘텐츠의 신뢰성을 확인하는 데 도움이 되며, 이메일 내 깨진 링크나 이미지 같은 문제를 최소화합니다.

### HSTS 도메인 요구 사항 

HTTP Strict Transport Security(HSTS) 도메인이 있는 경우 SSL을 설정하고 CDN을 구성하여 필요한 보안 인증서를 전송하도록 하십시오. SSL이 없으면 이미지 및 웹 링크가 깨집니다.

## SSL 인증서 획득

제3자(일반적으로 CDN)를 통해 SSL 인증서를 획득하십시오. CDN은 인증서를 호스팅하며, 사용자가 링크를 클릭할 때 트래픽을 CDN을 통해 리다이렉트하여 인증서를 적용한 후 SendGrid 또는 SparkPost로 전송함으로써 브라우저에 인증서를 제공합니다.

SSL 설정을 시작하려면 Braze 이메일 설정 전체를 시작하기 위해 Braze 고객 성공 매니저에게 문의하십시오.

Braze가 설정을 시작한 후 다음 단계를 따르십시오:
1. Braze는 도메인 등록부에 추가할 DNS 레코드를 제공합니다.
2. Braze는 레코드가 레지스트리에 올바르게 추가되었는지 확인할 것입니다.
3. 이후, CDN을 선택하고 타사 제공업체로부터 SSL 인증서를 발급받게 됩니다. 
4. 이 시점에서 CDN을 설정합니다. Braze는 CDN 구성 문제를 해결하는 데 도움을 줄 수 없음을 유의하세요. 추가 지원이 필요하시면 CDN 제공업체에 문의하십시오.
5. SSL을 활성화하려면 고객 성공 매니저에게 문의하십시오.

### CDN이란 무엇이며, 왜 필요한가요?

콘텐츠 전달 네트워크(CDN)는 여러 매체에서 콘텐츠의 빠른 로딩 시간을 보장하는 동시에 보안 인증서를 처리하는 서버 플랫폼입니다. 

{% alert important %}
CDN 구성은 항상 Braze에서 DNS 레코드를 검증한 후에 따릅니다. 이 단계를 아직 시작하지 않으셨다면, 시작 방법에 대한 자세한 내용은 고객 성공 매니저에게 문의하십시오.
{% endalert %}

클릭 및 열람 추적을 위해 배송 파트너는 브랜드화된 서브도메인을 사용하여 링크를 변환하며, CDN은 해당 변환된 링크에 SSL 인증서를 적용합니다. 파트너는 링크와 이미지가 제대로 표시되도록 수신자의 브라우저에 유효한 인증서를 제시해야 하는 경우가 많습니다. Braze는 인증서를 요청하거나 관리하지 않으므로, CDN을 통해 이 설정을 구성해야 합니다. 

{% alert note %}
목록에 있는 CDN을 SSL 클릭 및 오픈 추적에 사용할 수 없거나 원하지 않는 경우, 커스텀 SSL 구성을 설정할 수 있습니다. 대체 CDN이나 커스텀 프록시는 더 복잡한 설정을 초래할 수 있습니다. [SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) 및 [SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/) 설명서를 참조하십시오.
{% endalert %}

#### 추가 자료

{% alert important %}
CDN 구성 문제 해결을 위해 CDN 제공업체에 문의하십시오.
{% endalert %}

The following table includes step-by-step guides written by ESP partners on how to configure certain CDNs. 특정 CDN이 나열되지 않았더라도, CDN이 SSL 인증서를 적용할 수 있는지 확인해야 합니다.

| SendGrid | SparkPost |
| -------- | --------- |
| [AWS Cloudfront](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront)<br>[CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare)<br>[빠르게](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly)<br>[KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) | [AWS Cloudfront](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-aws-cloudfront)<br>[CloudFlare](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare)<br>[빠르게](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly)<br>[구글 클라우드 플랫폼](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-google-cloud-platform)<br>[Microsoft Azure](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-microsoft-azure) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For Amazon SES, refer to [Option 2: HTTPS 도메인 구성](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) 및 Braze 클러스터에 기반하여 리전별로 AWS 추적 도메인 지정:

- **Braze US clusters:** `r.us-east-1.awstrack.me`
- **Braze EU clusters:** `r.eu-central-1.awstrack.me`

{% alert important %}
CDN의 클릭 추적 도메인을 구성할 때 호스트 헤더 공격과 같은 잠재적 보안 문제를 방지하려면  `X-Forwarded-Host`헤더를 인에이블하십시오. 단계에 대해서는 CDN 설명서 또는 지원팀에 문의하십시오.
{% endalert %}

#### 문제 해결

CDN 구성, 인증서 및 프록시 문제는 CDN 제공업체와 협의하되, 일반적인 SSL 클릭 추적 문제를 식별하려면 다음 팁을 활용하세요.

##### 도메인 등록 문제

dig 명령어를 실행하여 CDN에 대한 포인트 링크 추적이 설정되었는지 확인하십시오. 터미널에서 다음 명령어를 실행하세요`dig CNAME link_tracking_subdomain`. 아래에는 CNAME이 가리키는`ANSWER SECTION` 위치를 나열합니다. 이메일 서비스 제공업체(SendGrid 또는 SparkPost)를 가리키고 CDN을 가리키지 않는 경우, 도메인 레지스트리를 재구성하여 CDN을 가리키도록 설정하십시오.

##### CDN 문제

설정 중 실시간 이메일 링크가 끊어지는 경우, 적절한 구성 전에 DNS를 CDN으로 지정한 것일 수 있습니다. 이것은 "잘못된 링크" 오류로 나타날 수 있습니다. CDN 공급업체에 문의하고 해당 설명서를 검토하여 구성 문제를 해결하십시오.

##### SSL 인에이블먼트 상태

SSL 설정을 완료했는데도 링크가 여전히 HTTP로 표시된다면, Braze 고객 성공 매니저에게 문의하여 Braze에서 SSL을 인에이블했는지 확인하십시오. Braze는 모든 설정 단계가 완료된 후에만 SSL을 인에이블합니다.

