---
nav_title: Enviar e-mails para o Apple Private Relay
article_title: Envio de e-mails para o Apple Private Relay
alias: /email_relay/
page_order: 0
description: "Este artigo aborda o processo de envio de e-mails para o Apple Private Relay."
channel:
  - email
toc_headers: h2
---

# Enviar e-mails para o Apple Private Relay

> O recurso de login único (SSO) da Apple permite que seus usuários compartilhem seus endereços de e-mail (`example@icloud.com`) ou ocultem seus endereços de e-mail mascarando o que é fornecido às marcas (`tq1234snin@privaterelay.appleid.com`) em vez do endereço de e-mail pessoal. A Apple encaminhará as mensagens enviadas para os endereços de relay para o endereço de e-mail real do usuário. 

Para enviar e-mails para o relay de e-mail privado da Apple, registre seus domínios de envio com a Apple. Se você não configurar seus domínios com a Apple, os e-mails enviados para endereços de relay resultarão em bounces.

Se um usuário decidir desativar o encaminhamento de e-mail para o e-mail de relay do seu app, a Braze receberá informações de bounce de e-mail normalmente. Esses usuários podem gerenciar os apps que usam o login com a Apple na página de configurações do Apple ID (consulte a [documentação da Apple](https://support.apple.com/en-us/HT210426)).

{% tabs %}
{% tab SendGrid %}

## Configurar o SendGrid 

Se você usar o SendGrid como provedor de e-mail, poderá enviar e-mails para a Apple sem fazer alterações no DNS. 

1. Faça login no [Portal do desenvolvedor da Apple](https://developer.apple.com/)
2. Acesse a página **Certificates, Identifiers & Profiles**.
3. Selecione **Services** > **Sign in with Apple for Email Communication**.
4. Na seção **Email Sources**, adicione os domínios e subdomínios.
- O endereço deve ser formatado como: `bounces+<YOUR_UID>@<YOUR_WHITELABELED_SUBDOMAIN_AND_DOMAIN>` (um exemplo é: `bounces+1234567@braze.online.docs.com`). 

Se o endereço "From" desejado for um endereço `abmail`, inclua-o em seu subdomínio. Por exemplo, use `abmail.docs.braze.com` em vez de `docs.braze.com`.

{% endtab %}
{% tab SparkPost %}

## Configurar o SparkPost 

Para configurar o Apple Private Relay para o SparkPost, siga estas etapas: 

1. Faça login com a Apple.
2. Siga a [documentação da Apple](https://developer.apple.com/help/account/configure-app-capabilities/configure-private-email-relay-service) para registrar os domínios de e-mail.
3. A Apple verificará automaticamente os domínios, mostrará quais são verificados e fornecerá a opção de reverificar ou excluir os domínios.

### Quando o domínio de envio também é o domínio de bounce

Se um domínio de envio também for usado como domínio de bounce, não será possível armazenar nenhum registro e será necessário seguir estas etapas adicionais:

1. Se o domínio já tiver sido verificado no SparkPost, será **necessário** criar registros MX e TXT: 

| Instância | Registro MX                   | Registro TXT                                    |
|----------|-----------------------------|-----------------------------------------------|
| EUA       | `smtp.sparkpostmail.com`    | `"v=spf1 redirect=_spf.sparkpostmail.com"`    |
| UE       | `smtp.eu.sparkpostmail.com` | `"v=spf1 redirect=_spf.eu.sparkpostmail.com"` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert important %}
Para evitar falhas de SPF, é necessário criar os registros MX e TXT e propagá-los no DNS **antes de** excluir o registro CNAME.
{% endalert %}

{:start="2"}
2. Exclua o registro CNAME.
3. Substitua-o pelos registros MX e TXT para obter o roteamento adequado.
4. Crie seu registro A para apontar para sua CDN ou hospedagem de arquivos.

{% endtab %}
{% tab Amazon SES %}

## Configurar o Amazon SES

### Configurar um domínio MAIL FROM personalizado

Para configurar o Apple Private Relay para o Amazon Simple Email Service (SES), primeiro é necessário configurar um domínio MAIL FROM personalizado no SES. Para mais detalhes, consulte a [documentação da AWS](https://docs.aws.amazon.com/ses/latest/dg/mail-from.html).

### Registrar domínios com a Apple

1. Faça login com a Apple.
2. Siga a [documentação da Apple](https://developer.apple.com/help/account/configure-app-capabilities/configure-private-email-relay-service) para registrar os domínios de e-mail.
3. A Apple verificará automaticamente os domínios, mostrará quais são verificados e fornecerá a opção de reverificar ou excluir os domínios.

{% endtab %}
{% endtabs %}

Se tiver mais perguntas, abra um [tíquete de suporte]({{site.baseurl}}/braze_support/).