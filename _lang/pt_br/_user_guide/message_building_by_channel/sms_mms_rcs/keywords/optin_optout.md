---
nav_title: Palavras-chave Opt-in e opt-out
article_title: Palavras-chave para SMS Opt-In/Opt-Out
page_order: 0
description: "Este artigo de referência aborda como o Braze processa palavras-chave básicas de opt-in e opt-out para mensagens SMS."
page_type: reference
alias: /optin_optout/
tool:
  - Dashboard

channel:
  - SMS
---

# Palavras-chave de opt-in e opt-out

> As regulamentações exigem que haja respostas para todas as respostas de palavras-chave opt-in, opt-out e ajuda/informação. O Braze processa automaticamente as seguintes mensagens _exatas, com uma única palavra e sem distinção entre maiúsculas e minúsculas_, atualizando automaticamente o [estado do grupo de assinaturas]({{site.baseurl}}/sms_rcs_subscription_groups/) para o usuário e seu número de telefone associado em todas as solicitações recebidas.

## Visão geral das palavras-chave

O Braze processará as seguintes palavras-chave automaticamente e atualizará o estado do grupo de assinaturas para o número de telefone em todas as solicitações recebidas. Observe que essas palavras-chave e respostas padrão também podem ser personalizadas. 

Tipo | Palavra-chave | Alterar | Tipo | Palavra-chave
\|-|-------|---|
|Opt-in| `START`<br> `YES`<br> `UNSTOP` | Qualquer solicitação de entrada com uma dessas palavras-chave `Opt-In` resultará em uma mudança de estado do grupo de assinatura para `subscribed`. Além disso, o conjunto de remetentes associados a esse grupo de assinaturas agora poderá enviar uma mensagem SMS, MMS ou RCS para esse cliente (dependendo do tipo de mensagem que os remetentes suportam). <br><br>O usuário receberá sua resposta automática Opt-In definida.  |
|Opt-out| `STOP`<br> `STOPALL`<br> `UNSUBSCRIBE`<br> `CANCEL`<br> `END`<br> `QUIT` | Qualquer solicitação de entrada com uma dessas palavras-chave `Opt-Out` resultará em uma mudança de estado do grupo de assinatura para `unsubscribed`. Além disso, o conjunto de números associados a esse grupo de assinatura não poderá mais enviar mensagens para esse cliente.<br><br>O usuário receberá a resposta automática Opt-Out definida. |
| Ajuda `HELP`<br> `INFO` | O usuário receberá a resposta automática da Ajuda definida. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Somente a **mensagem exata, de uma única palavra,** será processada (sem distinção entre maiúsculas e minúsculas). Palavras-chave como `STOP PLEASE` serão ignoradas, a menos que [a opção de exclusão difusa]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/fuzzy_opt_out/) esteja ativada.

Se um destinatário usar as palavras-chave `HELP` ou `INFO`, uma resposta será acionada automaticamente. A resposta padrão para essas mensagens de resposta automática será definida durante o período de [integração]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process) e aquisição do número de telefone. Observe que você pode continuar a atualizar essas respostas após o período inicial de integração.

{% alert tip %}
Interessado em expandir seu processamento de opt-out? Experimente o [fuzzy opt-out]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/fuzzy_opt_out/), um recurso que tenta reconhecer quando uma mensagem recebida não corresponde a uma palavra-chave de opt-out, mas indica a intenção de opt-out.
{% endalert %}

