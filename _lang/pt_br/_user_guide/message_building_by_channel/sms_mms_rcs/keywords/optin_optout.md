---
nav_title: Palavras-chave de aceitação e exclusão
article_title: Palavras-chave de aceitação/desistência de SMS
page_order: 0
description: "Este artigo de referência aborda como o Braze processa palavras-chave básicas de aceitação e exclusão para envio de mensagens SMS."
page_type: reference
alias: /optin_optout/
tool:
  - Dashboard

channel:
  - SMS
---

# Palavras-chave de aceitação e exclusão

> As regulamentações exigem que haja respostas para todas as respostas de palavras-chave de aceitação, exclusão e ajuda/informação. O Braze processa automaticamente as seguintes mensagens _exatas, com uma única palavra e sem distinção entre maiúsculas e minúsculas_, atualizando automaticamente o [estado do grupo de inscrições]({{site.baseurl}}/sms_rcs_subscription_groups/) para o usuário e seu número de telefone associado em todas as solicitações de entrada.

## Visão geral das palavras-chave

O Braze processará as seguintes palavras-chave automaticamente e atualizará o estado do grupo de inscrições para o número de telefone em todas as solicitações de entrada. Note que essas palavras-chave e respostas padrão também podem ser personalizadas. 

Tipo | Palavra-chave | Alterar | Tipo | Palavra-chave
\|-|-------|---|
|Aceitação `START`<br> `YES`<br> `UNSTOP` | Qualquer solicitação de entrada com uma dessas palavras-chave `Opt-In` resultará em uma mudança de estado do grupo de inscrições para `subscribed`. Além disso, o grupo de remetentes associado a esse grupo de inscrições agora poderá enviar uma mensagem SMS, MMS ou RCS para esse cliente (dependendo do tipo de envio de mensagens que os remetentes suportam). <br><br>O usuário receberá sua resposta automática de aceitação definida.  |
|Aceitação| `STOP`<br> `STOPALL`<br> `UNSUBSCRIBE`<br> `CANCEL`<br> `END`<br> `QUIT` | Qualquer solicitação de entrada com uma dessas palavras-chave `Opt-Out` resultará em uma mudança de estado do grupo de inscrições para `unsubscribed`. Além disso, o grupo de números associado a esse grupo de inscrições não poderá mais enviar mensagens para esse cliente.<br><br>O usuário receberá sua resposta automática de aceitação definida. |
| Ajuda `HELP`<br> `INFO` | O usuário receberá a resposta automática da Ajuda definida. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Somente a **mensagem exata, de uma única palavra,** será processada (não diferencia maiúsculas de minúsculas). Palavras-chave como `STOP PLEASE` serão ignoradas, a menos que [a aceitação fuzzy]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/fuzzy_opt_out/) esteja ativada.

Se um destinatário usar as palavras-chave `HELP` ou `INFO`, uma resposta será disparada automaticamente. A resposta padrão para essas mensagens de resposta automática será definida durante sua [integração]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process) e período de aquisição de número de telefone. Note que você pode continuar a atualizar essas respostas após o período inicial de integração.

{% alert tip %}
Quer em expandir o processamento de cancelamento de inscrição? Experimente o [fuzzy opt-out]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/fuzzy_opt_out/), um recurso que tenta reconhecer quando uma mensagem de entrada não corresponde a uma palavra-chave de aceitação, mas indica a intenção de exclusão.
{% endalert %}

