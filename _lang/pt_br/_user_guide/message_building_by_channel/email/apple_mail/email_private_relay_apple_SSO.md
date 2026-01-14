---
nav_title: Envio de e-mails para o Apple Private Relay
article_title: Envio de e-mails para o Apple Private Relay
alias: /email_relay/
page_order: 0
description: "Este artigo aborda o processo de envio de e-mails para o Apple Private Relay."
channel:
  - email
  
---

# Envio de e-mails para o Apple Private Relay

> O recurso de logon único (SSO) da Apple permite que seus usuários compartilhem seus endereços de e-mail (`example@icloud.com`) ou ocultem seus endereços de e-mail mascarando o que é fornecido às marcas (`tq1234snin@privaterelay.appleid.com`) em vez do endereço de e-mail pessoal. A Apple encaminhará as mensagens enviadas para os endereços de retransmissão para o endereço de e-mail real do usuário. 

Para enviar e-mails para o relé de e-mail privado da Apple, registre seus domínios de envio com a Apple. Se você não configurar seus domínios com a Apple, os e-mails enviados para endereços de retransmissão resultarão em devoluções.

Se um usuário decidir desativar o encaminhamento de e-mail para o e-mail de retransmissão do seu aplicativo, o Braze receberá as informações de devolução de e-mail normalmente. Esses usuários podem gerenciar aplicativos que usam o login com a Apple na página de configurações do ID Apple (consulte [a documentação da Apple](https://support.apple.com/en-us/HT210426)).

## Envio de e-mails para o SendGrid

Se você usar o SendGrid como provedor de e-mail, poderá enviar e-mails para a Apple sem fazer alterações no DNS. 

1. Faça login no [Portal do desenvolvedor da Apple](https://developer.apple.com/)
2. Vá para a página **Certificates, Identifiers & Profiles (Certificados, Identificadores Perfis** ).
3. Selecione **Services** > **Sign in with Apple for Email Communication**.
4. Na seção **Email Sources (Fontes de e-mail** ), adicione os domínios e subdomínios.
- O endereço deve ser formatado como: `bounces+<YOUR_UID>@<YOUR_WHITELABELED_SUBDOMAIN_AND_DOMAIN>` (um exemplo é: `bounces+1234567@braze.online.docs.com`). 

Se o endereço "From" desejado for um endereço `abmail`, inclua-o em seu subdomínio. Por exemplo, use `abmail.docs.braze.com` em vez de `docs.braze.com`.

## Envio de e-mails para o SparkPost

Para configurar o Apple Private Relay para o SparkPost, siga estas etapas: 

1. Faça login com a Apple.
2. Siga [a documentação da Apple](https://developer.apple.com/help/account/configure-app-capabilities/configure-private-email-relay-service) para registrar os domínios de e-mail.
3. A Apple verificará automaticamente os domínios, mostrará quais são verificados e fornecerá a opção de reverificar ou excluir os domínios.

### Considerações

Se um domínio de envio também for usado como domínio de rejeição, não será possível armazenar nenhum registro e será necessário seguir estas etapas adicionais:

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
2\. Exclua o registro CNAME.
3\. Substitua-o pelos registros MX e TXT para obter o roteamento adequado.
4\. Crie seu registro A para apontar para sua CDN ou hospedagem de arquivos.

Se você tiver mais perguntas, abra um [tíquete de suporte]({{site.baseurl}}/braze_support/).
