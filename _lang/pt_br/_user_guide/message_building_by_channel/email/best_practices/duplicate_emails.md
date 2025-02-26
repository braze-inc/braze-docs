---
nav_title: Envio de e-mails duplicados
article_title: Envio de e-mails duplicados
page_order: 7
page_type: reference
description: "Este artigo aborda as práticas recomendadas para o gerenciamento de e-mails duplicados."
channel: email

---

# Envio de e-mails duplicados

> Para e-mails duplicados, se um e-mail cancelar a inscrição, outros perfis (até 100 perfis) com esse endereço de e-mail serão atualizados para refletir o mesmo estado de inscrição. Isso se aplica a cancelamentos de inscrição e outras alterações no estado da assinatura, como o estado da assinatura global de e-mail e os status de grupos de inscrições individuais.

## Atualizações de inscrição por e-mail

O Braze verifica automaticamente e remove endereços de e-mail duplicados quando uma campanha de e-mail é enviada. Dessa forma, um e-mail é enviado apenas uma vez e é "deduplicado", o que verifica se o mesmo e-mail não é enviado várias vezes, mesmo que vários perfis de usuário compartilhem um endereço comum.

{% alert tip %}
Certifique-se de estar familiarizado com as ferramentas que o Braze fornece para [gerenciar as inscrições de e-mail dos usuários]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions) e direcionar campanhas para usuários com estados de inscrição específicos. Essas ferramentas são essenciais para a conformidade com as [leis anti-spam]({{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations).
{% endalert %}

Se os usuários compartilharem um endereço de e-mail, a atualização de um desses usuários propagará as alterações da inscrição para todos eles (até 100 usuários).

## Comportamento de envio de mensagens

Como a deduplicação ocorre quando os usuários direcionados são incluídos no mesmo envio, as campanhas disparadas (excluindo as campanhas disparadas por API) e os Canvas podem resultar em vários envios para o mesmo endereço de e-mail (mesmo dentro de um período de tempo em que os usuários poderiam ser excluídos devido à reeligibilidade) se diferentes usuários com e-mails correspondentes registrarem o evento de eventos disparados em momentos diferentes.

## Exemplos

Por exemplo, se o usuário A e o usuário B compartilharem o e-mail `johndoe@example.com`, mas o perfil deles estiver em um fuso horário diferente, quando o evento de gatilho da campanha incluir o envio no fuso horário de um usuário, o e-mail `johndoe@example.com` receberá dois e-mails.

Se você definir ou atualizar o endereço de e-mail do Usuário A para outro endereço de e-mail compartilhado por um Usuário B existente, o Usuário A herdará o estado de inscrição que já existe do Usuário B, a menos que a configuração de **envio de e-mail para os usuários** esteja ativada.

{% alert important %}
Se você enviar uma campanha de API por meio de uma chamada de API (excluindo campanhas disparadas por API) e vários usuários forem especificados no público do segmento com o mesmo endereço de e-mail, nós a enviaremos para esse endereço quantas vezes forem listadas na chamada. Isso ocorre porque presumimos que as chamadas de API são construídas propositadamente.
<br><br>
**Campanhas disparadas por API**<br>
Observe que as campanhas disparadas pela API deduplicarão ou enviarão duplicatas, dependendo de onde o público estiver definido. <br>\- A dedução poderá ocorrer se houver e-mails duplicados em um segmento de destino ou e-mails duplicados devido a IDs duplicados no [campo do destinatário]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) de uma chamada disparada por API. <br>\- Ocorrerão envios de e-mail duplicados se você direcionar diretamente IDs de usuários separados dentro do campo de destinatário de uma chamada disparada por API.
{% endalert %}
