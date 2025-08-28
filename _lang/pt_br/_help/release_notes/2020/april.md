---
nav_title: Abril
page_order: 9
noindex: true
page_type: update
description: "Este artigo contém notas de versão para abril de 2020."
---
# Abril de 2020

## Parceria com a Movable Ink

A Movable Ink oferece aos clientes da Braze a capacidade de usar recursos do Intelligent Creative, como cronômetros de contagem regressiva, enquetes e raspadinhas em suas campanhas de mensagens no app e cartões de conteúdo. O Movable Ink e a Braze oferecem uma abordagem mais completa para mensagens dinâmicas orientadas por dados, fornecendo aos usuários elementos em tempo real sobre as coisas que importam.

Comece a [integrar o Movable Ink]({{site.baseurl}}/partners/message_personalization/dynamic_content/visual_and_interactive_content/movable_ink/) em suas campanhas!

## Intelligent Timing

Ao programar uma campanha de mensagens, você pode usar o [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) (anteriormente chamado de Intelligent Delivery) para entregar sua mensagem a cada usuário no momento em que o Braze determina que um indivíduo tem maior probabilidade de engajamento.

As atualizações desse recurso incluem:
- **Esclarecimento sobre os horários de silêncio**: A funcionalidade do Horário de silêncio permanece a mesma, mas a interface do usuário foi ajustada para esclarecimento.
- **Adição do gráfico de prévia**: Agora é possível gerar um gráfico para ver quantos usuários receberão mensagens para cada hora do dia com o Intelligent Timing, bem como qual proporção de usuários tem dados suficientes para calcular um horário ideal.
- **Adição de fallback personalizado**: Agora é possível escolher o fuso local no qual enviar uma mensagem aos usuários quando não houver dados de engajamento suficientes para calcular um horário ideal.

## Exportação do público do Facebook

O Braze oferece a capacidade de exportar manualmente seus usuários da página Braze Segments para criar públicos personalizados do Facebook. Essa é uma exportação única e estática de público e só criará novos [públicos personalizados no Facebook]({{site.baseurl}}/partners/facebook/).

Atualmente disponível para todos os clusters, existe um novo processo de exportação do público do Facebook do Braze, que simplifica o processo com etapas simples de integração. Você não precisará mais colocar os URIs do OAuth Redirect na lista de permissões para enviar públicos personalizados ou mexer nas configurações do aplicativo do Facebook para fazer a integração.

{% alert important %}
Note que todos os clientes que atualmente usam o público do Facebook Custom Audiences devem reintegrar seus segmentos da Braze com essas novas etapas.
{% endalert%}


## Atualizações da API do bloco de conteúdo e do modelo de e-mail

Os endpoints de API [template/email/list]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) e [content_block/list]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) foram atualizados para incluir um novo campo `tags`. Esse campo listará, como uma matriz, todas as tags que se aplicam ao bloco ou modelo de e-mail atual.

## Endereço de remetente personalizado

Ao criar uma mensagem de e-mail no Braze, agora é possível personalizar o endereço do remetente da mensagem na seção **Informações de envio** da composição do e-mail. Você pode usar qualquer uma de nossas [tags de personalização]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) compatíveis

![Personalized From Address]({% image_buster /assets/img/personalized-from-name.png %}){: style="max-width:80%"}

