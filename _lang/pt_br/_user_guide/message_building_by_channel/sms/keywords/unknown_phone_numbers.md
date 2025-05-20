---
nav_title: Lidando com Números de Telefone Desconhecidos
article_title: Lidando com Números de Telefone SMS Desconhecidos
page_order: 4
description: "Este artigo de referência cobre como a Braze processa números de telefone SMS desconhecidos de novos usuários."
page_type: reference
channel:
  - SMS
  
---

# Lidando com números de telefone desconhecidos - novos usuários

> Você pode descobrir que, depois de configurar o SMS com Braze, você recebe mensagens de usuários desconhecidos. As etapas a seguir descrevem como um usuário e número não identificados são processados.

{% alert important %}
Você é atualmente um cliente de SMS não nativo? Se for o caso, visite a [documentação de SMS não nativa]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/) para o seu artigo correspondente sobre como lidar com números de telefone desconhecidos.
{% endalert %}

## Aceitação/saída e fluxo de trabalho de palavras-chave personalizadas para números desconhecidos

Braze aborda automaticamente um número desconhecido de uma das três maneiras:

1. Se uma palavra-chave de aceitação for enviada por mensagem de texto:
  * Braze cria um perfil anônimo
  * Nosso sistema define o atributo do telefone
  * Inscreve o usuário no grupo de inscrições correspondente com base na palavra-chave de aceitação recebida pelo Braze.<br><br>
2. Se uma palavra-chave de exclusão for enviada por mensagem de texto:
  * Braze cria um perfil anônimo
  * Nosso sistema define o atributo do telefone
  * Cancela a inscrição do usuário do grupo de inscrições correspondente com base na palavra-chave de exclusão recebida pela Braze.<br><br>
3. Se qualquer outra palavra-chave personalizada for enviada por texto:
  * Braze ignora a mensagem de texto e não faz nada.

[ualink]: {{site.baseurl}}/api/objects_filters/user_alias_object/
[telink]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[uaolink]: {{site.baseurl}}/api/objects_filters/user_attributes_object/
[e.164]: https://en.wikipedia.org/wiki/E.164