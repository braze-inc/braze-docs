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

> Com o lançamento do iOS 13, a Apple introduziu uma funcionalidade para os clientes da Apple que afeta a forma como os e-mails são enviados a eles. O recurso de logon único (SSO) da Apple permite que seus usuários compartilhem seus endereços de e-mail (`example@icloud.com`) ou ocultem seus endereços de e-mail, mascarando o que é fornecido às marcas (`tq1234snin@privaterelay.appleid.com`) em oposição ao endereço de e-mail pessoal.

Esses usuários podem gerenciar os apps que usam o login com a Apple na página de configurações do ID Apple (consulte [a documentação da Apple](https://support.apple.com/en-us/HT210426)). Se um usuário decidir desativar o envio de e-mail para o e-mail de retransmissão do seu app, a Braze receberá informações de bounce de e-mail normalmente. Para enviar e-mails para o relay de e-mail privado da Apple, registre seus domínios de envio com a Apple.

## Envio de e-mails para o SendGrid

Se você usar o SendGrid como provedor de e-mail, poderá enviar e-mails para a Apple sem fazer alterações no DNS. Acesse a página do **certificado da Apple** e permita o endereço de e-mail que deseja usar para o envio por meio do serviço de retransmissão de e-mail da Apple (o endereço "De" desejado).  

![Opção para permitir a listagem de endereços de e-mail individuais na página do certificado da Apple.]({% image_buster /assets/img/email-relay-whitelabel-address.png %})

O endereço deve ser formatado como: `bounces+<YOUR_UID>@<YOUR_WHITELABELED_SUBDOMAIN_AND_DOMAIN>`(e.g., `bounces+1234567@braze.online.docs.com`). Depois que o endereço for adicionado à página do certificado da Apple, os e-mails desse domínio serão entregues por meio do sistema Apple Private Relay.

{% alert important %}
Se o endereço "From" desejado for um endereço `abmail`, inclua-o em seu subdomínio. Por exemplo, use `abmail.docs.braze.com` em vez de `docs.braze.com`. Esse pode não ser o caso de seu endereço. Verifique seus registros DNS no SendGrid.
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
2. Adicione os domínios de e-mail. 
3. A Apple verificará automaticamente os domínios e mostrará quais são verificados, além de oferecer a opção de reverificar ou excluir os domínios.

{% alert important %}
Certifique-se de concluir esse processo dentro de 2 a 3 dias após a criação dos arquivos de verificação, caso contrário, eles expirarão. A Apple não divulga por quanto tempo eles são válidos.
{% endalert %}

Se tiver mais perguntas, abra um [tíquete de suporte]({{site.baseurl}}/braze_support/).
