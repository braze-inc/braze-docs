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

Para enviar e-mails para o relay de e-mail privado da Apple, registre seus domínios de envio com a Apple. Se você não configurar seus domínios com a Apple, os e-mails enviados para endereços de retransmissão resultarão em bounces.

Se um usuário decidir desativar o envio de e-mail para o e-mail de retransmissão do seu app, a Braze receberá informações de bounce de e-mail normalmente. Esses usuários podem gerenciar os apps que usam o login com a Apple na página de configurações do ID Apple (consulte [a documentação da Apple](https://support.apple.com/en-us/HT210426)).

## Envio de e-mails para o SendGrid

Se você usar o SendGrid como provedor de e-mail, poderá enviar e-mails para a Apple sem fazer alterações no DNS. 

1. Acesse a página do **certificado da Apple** e permita o endereço de e-mail que deseja usar para o envio por meio do serviço de retransmissão de e-mail da Apple (o endereço "De" desejado).
- O endereço deve ser formatado como: `bounces+<YOUR_UID>@<YOUR_WHITELABELED_SUBDOMAIN_AND_DOMAIN>`(um exemplo é: `bounces+1234567@braze.online.docs.com`). 

![Opção para permitir a listagem de endereços de e-mail individuais na página do certificado da Apple.]({% image_buster /assets/img/email-relay-whitelabel-address.png %})

{:start="2"}
2\. Depois que o endereço for adicionado à página do certificado da Apple, os e-mails desse domínio serão entregues por meio do sistema Apple Private Relay.

{% alert important %}
Se o endereço "From" desejado for um endereço `abmail`, inclua-o em seu subdomínio. Por exemplo, use `abmail.docs.braze.com` em vez de `docs.braze.com`.
{% endalert %}

### Valores do endereço de origem

Consulte esta tabela para ver os componentes usados ao adicionar endereços de e-mail com o Apple Private Relay.

| Valor | Descrição |
|---|---|
| ID DO USUÁRIO | Esse valor é fornecido em seus registros DNS fornecidos pela Braze (da SendGrid). Não inclua a letra "u" em seu ID do usuário no endereço de e-mail. Por exemplo, se seu ID do usuário for apresentado na SendGrid como `u1234567.wl134.sendgrid.net`, então `1234567` é o valor do usuário. <br><br> Se não tiver acesso aos seus registros DNS, entre em contato com o gerente de sucesso do cliente Braze para fornecer seu ID do usuário. |
| Subdomínio e domínio com marca branca | O domínio e o subdomínio iniciais que você inseriu na SendGrid. Também é possível usar o **valor HOST** em seus registros DNS na SendGrid. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Envio de e-mails para o SparkPost

Para configurar o Apple Private Relay para o SparkPost, siga estas etapas: 

1. Faça login com a Apple.
2. Siga a [documentação da Apple](https://developer.apple.com/help/account/configure-app-capabilities/configure-private-email-relay-service) para registrar os domínios de e-mail.
3. A Apple verificará automaticamente os domínios e mostrará quais são verificados, além de oferecer a opção de reverificar ou excluir os domínios.

{% alert important %}
Certifique-se de concluir esse processo dentro de dois ou três dias após a criação dos arquivos de verificação, caso contrário, eles expirarão. A Apple não divulga por quanto tempo eles são válidos.
{% endalert %}

### Considerações

Se um domínio de envio também for usado como um domínio de bounce, não será possível armazenar nenhum registro e será necessário seguir estas etapas adicionais:

1. Se o domínio já tiver sido verificado no SparkPost, será **necessário** criar registros MX e TXT: 

| Instância | Registro MX                   | Registro TXT                                    |
|----------|-----------------------------|-----------------------------------------------|
| EUA       | `smtp.sparkpostmail.com`    | `"v=spf1 redirect=_spf.sparkpostmail.com"`    |
| UE       | `smtp.eu.sparkpostmail.com` | `"v=spf1 redirect=_spf.eu.sparkpostmail.com"` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert important %}
Para evitar falhas de SPF, é necessário criar os registros MX e TXT e propagá-los no DNS **antes** de excluir o registro CNAME.
{% endalert %}

{:start="2"}
2\. Exclua o registro CNAME.
3\. Substitua-o pelos registros MX e TXT para obter o roteamento adequado.
4\. Crie seu registro A para apontar para sua CDN ou hospedagem de arquivos.

Se tiver mais perguntas, abra um [tíquete de suporte]({{site.baseurl}}/braze_support/).
