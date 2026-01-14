---
nav_title: SSL no Braze
article_title: Visão geral do SSL
page_order: 5
page_type: reference
description: "Este artigo de referência aborda o SSL, para que ele é usado e como é usado no Braze."
channel: email

---

# SSL no Braze

{% multi_lang_include video.html id="zP1N_wN0SsQ" align="right" %}

> Uma camada de soquete seguro (SSL) criptografa um URL com HTTPS, em vez do HTTP, que é menos seguro. O HTTPS em um URL indica que existe um certificado SSL ou TLS válido e confiável, e que o site é seguro para ser visitado e não é uma fonte de malware perigoso.

## Por que o SSL é importante?

Embora a maioria dos domínios não exija SSL, a Braze recomenda enfaticamente o uso de SSL pelos seguintes motivos principais.

Proteger seu site e seus links com SSL é uma prática comum, mesmo para empresas que não lidam diretamente com informações confidenciais de clientes. Os usuários confiam mais em links protegidos com SSL, e a camada adicional de autenticação ajuda a proteger seus dados.

### Necessário para rastreamento de cliques e aberturas

Na Braze, quando enviamos e-mails, primeiro transformamos seus links usando o subdomínio de rastreamento de links da sua marca para rastrear os cliques e as aberturas dos usuários. Por padrão, esses links começarão com HTTP. Isso significa que os usuários com um navegador ou extensão que restringe o tráfego não seguro podem ter dificuldade para passar pelo redirecionamento antes de chegar ao URL de destino, mesmo que o URL seja seguro. Isso pode levar a imagens quebradas e a um rastreamento impreciso de cliques e aberturas em seus e-mails. Por esse motivo, é uma prática recomendada aplicar uma camada SSL ao subdomínio de rastreamento de links para confirmar redirecionamentos seguros em seus e-mails. 

### Requisitos do navegador

Os protocolos SSL estão se tornando mais predominantes atualmente, pois os principais navegadores, como o Google Chrome, estão começando a restringir o tráfego por meio de URLs não seguros para proteger seus usuários. As empresas com SSL em seus sites confirmam com esses principais navegadores que seu conteúdo é confiável, minimizando problemas de visualização de conteúdo, como links quebrados e imagens em seus e-mails.

### Requisito de domínios HSTS 

Independentemente dos navegadores pelos quais seus usuários possam estar acessando seus e-mails, é necessário configurar o SSL se tiver um domínio HTTP Strict Transport Security (HSTS) e configurar uma CDN para enviar os certificados de segurança necessários. Se o SSL não for configurado, as imagens e os links da Web serão interrompidos.

## Aquisição de um certificado SSL

Você pode adquirir um certificado SSL usando um terceiro, geralmente uma CDN (Content Delivery Network). Uma CDN pode hospedar o certificado SSL e fornecê-lo ao navegador sempre que um de seus links for clicado. Isso é feito redirecionando o tráfego por meio da CDN para aplicar os certificados necessários antes de enviá-lo aos nossos parceiros de e-mail SendGrid ou SparkPost.

Para começar a configurar seu SSL, entre em contato com o gerente de sucesso do cliente Braze para iniciar uma configuração completa de e-mail Braze.

Depois que o Braze tiver iniciado essa configuração, siga estas etapas:
1. O Braze fornecerá registros DNS para adicionar ao seu registro de domínio.
2. O Braze verificará se os registros foram adicionados corretamente ao seu registro.
3. Depois disso, você selecionará uma CDN e obterá certificados SSL de um provedor terceirizado. 
4. Nesse ponto, você configurará sua CDN. Observe que o Braze não poderá ajudar a solucionar problemas de configuração de CDN. Entre em contato com seu provedor de CDN para obter mais assistência.
5. Entre em contato com o gerente de sucesso do cliente para ativar o SSL.

### O que é uma CDN e por que eu preciso dela?

Uma rede de distribuição de conteúdo (CDN) é uma plataforma de servidores que ajuda a garantir tempos de carregamento rápidos de conteúdo de alta qualidade em várias mídias, além de lidar com certificados de segurança. 

{% alert important %}
A configuração da CDN sempre ocorre após a validação dos registros DNS pelo Braze. Se ainda não tiver iniciado essa etapa, entre em contato com o gerente de sucesso do cliente para obter mais informações sobre como começar.
{% endalert %}

Na Braze, para fazer o rastreamento de cliques e aberturas, nossos parceiros de entrega transformam os links usando um subdomínio de marca, e a CDN aplica o certificado SSL a esses links recém-transformados. Muitas vezes, nossos parceiros de entrega precisam apresentar certificados válidos e confiáveis ao navegador do destinatário do e-mail para que os links e as imagens sejam exibidos corretamente. Como o Braze não solicita nem gerencia esses certificados, isso deve ser configurado por você por meio de uma CDN. 

{% alert note %}
Se você não puder ou não quiser usar as CDNs listadas ao configurar o SSL para rastreamento de cliques e aberturas, poderá definir uma configuração SSL personalizada. Observe que CDNs alternativos ou proxies personalizados podem resultar em uma configuração mais complexa e diferenciada. Consulte os artigos [do SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) e [do SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/) sobre esse tópico.
{% endalert %}

#### Recursos adicionais

{% alert important %}
Para obter mais assistência na solução de problemas da configuração da CDN, entre em contato com o provedor da CDN.
{% endalert %}

A tabela a seguir inclui guias passo a passo escritos por parceiros do ESP sobre como configurar determinadas CDNs. Embora sua CDN específica possa não estar listada, você deve se certificar de que sua CDN tem a capacidade de aplicar certificados SSL.

| SendGrid | SparkPost |
| -------- | --------- |
| [AWS Cloudfront](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront)<br>[CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare)<br>[Rapidamente](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly)<br>[KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) | [AWS Cloudfront](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-aws-cloudfront)<br>[CloudFlare](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare)<br>[Rapidamente](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly)<br>[Google Cloud Platform](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-google-cloud-platform)<br>[Microsoft Azure](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-microsoft-azure) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para o Amazon SES, consulte [Opção 2: Configuração de um domínio HTTPS](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) e especifique o domínio de rastreamento da AWS por sua região com base no cluster do Braze:

- **Clusters Braze US:** `r.us-east-1.awstrack.me`
- **Brasagem de clusters da UE:** `r.eu-central-1.awstrack.me`

{% alert important %}
Ao configurar o domínio de rastreamento de cliques da CDN, certifique-se de ativar o cabeçalho `X-Forwarded-Host`. Isso é usado para evitar possíveis problemas de segurança, como ataques ao cabeçalho do host. Consulte a documentação da CDN ou sua equipe de suporte para saber como fazer isso, pois isso varia de acordo com a CDN.
{% endalert %}

#### Solução de problemas

Embora a configuração da CDN, os certificados e os problemas de proxy devam ser tratados com sua CDN, aqui estão algumas dicas gerais de solução de problemas para ajudar a identificar problemas comuns com a configuração do rastreamento de cliques SSL.

##### Problemas de registro de domínio

Um comando dig pode informar se você está apontando o rastreamento do link para a CDN. Isso pode ser feito em seu terminal, executando `dig CNAME link_tracking_subdomain`. Depois que o comando for executado, em `ANSWER SECTION`, ele deverá listar para onde seu CNAME está apontado. Se ele apontou para o provedor de serviços de e-mail escolhido (SendGrid ou SparkPost) e não para a sua CDN, tente reconfigurar o registro do domínio para apontar para a sua CDN.

##### Problemas de CDN

Se os links de e-mail ao vivo começarem a quebrar durante a configuração, isso geralmente significa que você apontou o DNS para a CDN sem que ela estivesse configurada corretamente. Isso pode aparecer como um erro de "link errado". Entre em contato com seu provedor de CDN e analise a documentação dele para ajudar a solucionar problemas de configuração da CDN.

##### Status de ativação do SSL

Se você tiver concluído a configuração do SSL e seus links ainda aparecerem como HTTP e não como HTTPS, entre em contato com o gerente de sucesso do cliente da Braze para certificar-se de que o SSL foi ativado pela Braze. O SSL só pode ser ativado pelo Braze depois que todos os aspectos de sua configuração de SSL tiverem sido concluídos.

