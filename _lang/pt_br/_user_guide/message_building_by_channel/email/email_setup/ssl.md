---
nav_title: SSL na Braze
article_title: Visão geral do SSL
page_order: 5
page_type: reference
description: "Este artigo de referência aborda o SSL, para que ele é usado e como é usado na Braze."
channel: email

---

# SSL na Braze

{% multi_lang_include video.html id="zP1N_wN0SsQ" align="right" %}

> Uma camada de soquete seguro (SSL) criptografa uma URL com HTTPS em vez de HTTP. HTTPS indica que um certificado SSL ou TLS válido e confiável existe e que o site é seguro para visitar.

## Por que o SSL é importante?

A maioria dos domínios não requer SSL, mas a Braze recomenda fortemente o uso de SSL por essas razões.

Proteger seu site e seus links com SSL é uma prática comum, mesmo para empresas que não lidam diretamente com informações confidenciais de clientes. Os usuários confiam mais em links protegidos com SSL, e a camada adicional de autenticação ajuda a proteger seus dados.

### Necessário para rastreamento de cliques e aberturas

A Braze transforma seus links usando seu subdomínio de rastreamento de links da marca para rastrear cliques e aberturas. Por padrão, esses links começam com HTTP. Usuários com navegadores ou extensões que restringem tráfego não seguro podem ter dificuldade em passar pelo redirecionamento antes da URL de destino, mesmo que a URL seja segura. Isso pode causar imagens quebradas e rastreamento impreciso. Aplique SSL ao subdomínio de rastreamento de links para confirmar redirecionamentos seguros.

### Requisitos do navegador

Principais navegadores, como o Google Chrome, restringem o tráfego através de URLs não seguras para proteger os usuários. Usar SSL ajuda a confirmar que o conteúdo é confiável e minimiza problemas como links e imagens quebradas em e-mails.

### Requisito de domínios HSTS

Se você tem um domínio com HTTP Strict Transport Security (HSTS), configure o SSL e configure um CDN para enviar os certificados de segurança necessários. Sem SSL, links de imagem e da web quebram.

## Aquisição de um certificado SSL

Adquira um certificado SSL através de um terceiro, geralmente uma Rede de Distribuição de Conteúdo (CDN). Um CDN hospeda o certificado e o fornece ao navegador quando um usuário clica em um link, redirecionando o tráfego através do CDN para aplicar os certificados antes de enviá-lo ao SendGrid ou SparkPost.

Para iniciar a configuração do SSL, entre em contato com seu gerente de sucesso do cliente da Braze para iniciar uma configuração completa de e-mail da Braze.

Após a Braze iniciar a configuração, siga estas etapas:
1. A Braze fornecerá registros DNS para serem adicionados ao seu registro de domínio.
2. A Braze verificará se os registros foram adicionados corretamente ao seu registro.
3. Depois disso, você selecionará uma CDN e obterá certificados SSL de um provedor terceirizado. 
4. Nesse ponto, você configurará sua CDN. Observe que a Braze não poderá ajudar a solucionar problemas de configuração de CDN. Entre em contato com seu provedor de CDN para qualquer assistência adicional.
5. Entre em contato com seu gerente de sucesso do cliente para ativar o SSL.

### O que é uma CDN e por que eu preciso dela?

Uma rede de entrega de conteúdo (CDN) é uma plataforma de servidores que ajuda a garantir tempos de carregamento rápidos de conteúdo em vários meios, enquanto também lida com certificados de segurança. 

{% alert important %}
A configuração da CDN sempre ocorre depois que os registros DNS são validados pela Braze. Se você ainda não iniciou esta etapa, entre em contato com seu gerente de sucesso do cliente para mais informações sobre como começar.
{% endalert %}

Para rastreamento de cliques e aberturas, os parceiros de entrega transformam links usando um subdomínio de marca e a CDN aplica o certificado SSL a esses links transformados. Os parceiros muitas vezes devem apresentar certificados válidos ao navegador do destinatário para que links e imagens sejam exibidos corretamente. Como a Braze não solicita ou gerencia certificados, você deve configurar isso através de uma CDN. 

{% alert note %}
Se você não puder ou não quiser usar as CDNs listadas para rastreamento de cliques e aberturas SSL, pode configurar uma configuração SSL personalizada. CDNs alternativas ou proxies personalizados podem resultar em uma configuração mais complexa. Consulte a documentação do [SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) e [SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/).
{% endalert %}

#### Recursos adicionais

{% alert important %}
Para solucionar problemas de configuração da sua CDN, entre em contato com seu provedor de CDN.
{% endalert %}

Consulte os seguintes recursos de parceiros ESP sobre como configurar certas CDNs. Embora sua CDN específica possa não estar listada, você precisa se certificar de que sua CDN tem a capacidade de aplicar certificados SSL.

**SendGrid**

- [AWS Cloudfront](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront)
- [CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare)
- [Fastly](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly)
- [KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn)

**SparkPost**
- [AWS Cloudfront](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-aws-cloudfront)
- [CloudFlare](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare)
- [Fastly](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly)
- [Google Cloud Platform](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-google-cloud-platform)
- [Microsoft Azure](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-microsoft-azure) 

**Amazon SES:**
- Consulte [Configurando domínios personalizados para rastreamento de aberturas e cliques](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) e especifique o domínio de rastreamento AWS por região com base no seu cluster Braze:
    - **Clusters Braze nos EUA:** `r.us-east-1.awstrack.me`
    - **Clusters Braze na UE:** `r.eu-central-1.awstrack.me`
- [AWS Cloudfront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https.html)
- [CloudFlare](https://developers.cloudflare.com/ssl/get-started/)
- [Fastly](https://www.fastly.com/documentation/guides/getting-started/domains/securing-domains/setting-up-tls-with-certificates-fastly-manages/)
- [KeyCDN](https://www.keycdn.com/support/how-to-setup-custom-ssl)
- [Google Cloud](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs)


{% alert important %}
Quando você configura o domínio de rastreamento de cliques da sua CDN, ative o cabeçalho `X-Forwarded-Host` para evitar potenciais problemas de segurança, como ataques de cabeçalho de host. Consulte a documentação da CDN ou sua equipe de suporte para obter as etapas.
{% endalert %}

#### Solução de problemas

Embora você deva lidar com a configuração da CDN, certificados e problemas de proxy com sua CDN, use estas dicas para identificar problemas comuns de rastreamento de cliques SSL.

##### Problemas de registro de domínio

Execute um comando dig para confirmar que você aponta o rastreamento de links para a CDN. No seu terminal, execute `dig CNAME link_tracking_subdomain`. Em `ANSWER SECTION`, ele lista para onde seu CNAME aponta. Se apontar para o prestador de serviço de e-mail (SendGrid ou SparkPost) e não para sua CDN, reconfigure seu registro de domínio para apontar para sua CDN.

##### Problemas de CDN

Se os links de e-mail ao vivo quebrarem durante a configuração, você provavelmente apontou o DNS para sua CDN antes da configuração adequada. Isso pode aparecer como um erro de "link errado". Entre em contato com seu provedor de CDN e revise a documentação deles para solucionar a configuração.

##### Status de ativação do SSL

Se você concluir a configuração do SSL e os links ainda aparecerem como HTTP, entre em contato com seu gerente de sucesso do cliente da Braze para confirmar se a Braze ativou o SSL. A Braze ativa o SSL somente após todas as etapas de configuração estarem completas.