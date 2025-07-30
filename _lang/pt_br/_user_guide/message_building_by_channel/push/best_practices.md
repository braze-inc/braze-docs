---
page_order: 20
nav_title: Práticas recomendadas
article_title: Práticas recomendadas de push
description: "Esta página contém as melhores práticas e casos de uso de push para garantir que suas mensagens de push inspirem engajamento em vez de aborrecimento."
channel: push
---

# push melhores práticas

Notificações por push são ferramentas poderosas para engajar os usuários do seu app, mas devem ser usadas com cuidado para garantir que entreguem mensagens oportunas e relevantes. Antes de enviar sua mensagem push, consulte as seguintes melhores práticas para coisas que você deve saber e verificar.

{% alert important %}
Suas mensagens push devem estar dentro das diretrizes da Apple App Store e das políticas da Google Play Store, especificamente no que diz respeito ao uso de mensagens push como anúncios, spam, promoções e mais. Saiba mais sobre [regulamentações de push móvel]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#mobile-push-regulations-for-apps).
{% endalert %}

## Crie sua mensagem push

Como prática recomendada, a Braze recomenda manter cada linha de texto, tanto para o título opcional quanto para o corpo da mensagem, com aproximadamente 30 a 40 caracteres em uma notificação por push para celular. Nota que o contador de caracteres no criador não conta os caracteres Liquid. Isso significa que a contagem final de caracteres de uma mensagem depende de como Liquid renderiza para cada usuário. Em caso de dúvida, seja breve e direto.

## Otimize o direcionamento

### Coletar dados de usuários relevantes

Notificações por push devem ser tratadas com cuidado para direcionar os usuários com notificações oportunas e relevantes. Braze coletará informações úteis do dispositivo e de uso que podem ser usadas para segmentar segmentos relevantes. Esta informação deve ser complementada com eventos personalizados e atributos específicos para o seu app. Usando esses dados, você pode direcionar cuidadosamente as mensagens para aumentar as taxas de abertura e diminuir as instâncias de usuários desativando push.

### Criar uma página de configurações de notificações

Você pode criar uma página de configurações no seu app que permite aos usuários dizer quais notificações eles querem receber. Uma abordagem comum é criar um atributo personalizado booleano no Braze correspondente ao status da configuração do app. Por exemplo, um app de notícias pode ter configurações de inscrição para notícias de última hora, notícias esportivas ou política.

Quando o app de notícias deseja criar uma campanha direcionada apenas para usuários interessados em Política, eles adicionam o filtro de atributo `Subscribes to Politics` ao segmento. Quando definido como verdadeiro, apenas os usuários que se inscrevem para notificações as receberão.

Para saber mais sobre como definir atributos personalizados, consulte os seguintes artigos para [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/#setting-custom-attributes) ou [REST API]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-attributes-object-specification).

## Aumente as inscrições e a relevância

### Obter permissão do usuário

As estatísticas gerais para push habilitado estarão relacionadas a se o usuário aprovou notificações com seu sistema operacional. Se os usuários desativarem as notificações no iOS, eles serão automaticamente removidos do nosso sistema, pois a Apple não permitirá que o token por push seja enviado.

A partir do Android 13, os apps precisam obter permissão antes que as notificações por push possam ser exibidas. Versões mais antigas do Android irão inscrever os usuários em notificações por padrão.

### Usuários principais para push

Você só tem uma chance de pedir permissão de push a um usuário, e depois que ele recusa, é muito difícil convencê-lo a reativar o push nas configurações do dispositivo. Por isso, você deve preparar os usuários para push usando uma mensagem no app antes de mostrar o prompt do sistema. Para saber mais sobre como aumentar as adesões, consulte [Push primer em mensagens no app]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

### Adicionar controles de inscrição push

Para evitar que os usuários desativem as notificações no nível do dispositivo, o que remove completamente seu token por push em primeiro plano, permita que os usuários controlem sua inscrição de push diretamente no seu app. Para saber mais, consulte [Atualização de estados de inscrição de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions#update-push-subscription-state).

### Estados de inscrição de push

O estado da inscrição push não garante que um push será entregue—os usuários também devem estar habilitados para push para receber notificações. Isso ocorre porque um perfil de usuário pode ter vários dispositivos com diferentes permissões de push em primeiro plano, mas apenas um único estado de inscrição de push.

Se um usuário não tiver um token por push válido em primeiro plano para um app (ou seja, eles desativam tokens por push no nível do dispositivo através das configurações, optando por não receber notificações), seu estado de inscrição ainda pode ser considerado `subscribed` para push. No entanto, este usuário não seria `Push Enabled for App` na Braze, pois o token por push em primeiro plano não é válido.

Além disso, se um perfil de usuário não tiver um token por push válido ou registrado para quaisquer outros aplicativos, seu filtro `Push Enabled` na segmentação também será falso.

## Implementar uma política de pôr do sol para usuários não responsivos

Mesmo quando você envia apenas notificações por push relevantes e oportunas, alguns usuários ainda podem não respondê-las e achá-las spam. Suponha que um usuário mostre um histórico de repetidamente ignorar suas notificações por push. Nesse caso, é uma boa ideia parar de enviar notificações antes que eles fiquem irritados com as comunicações do seu app ou desinstalá-lo completamente. 

Para fazer isso, crie uma [política de sunset]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies) que eventualmente pare de enviar notificações por push para usuários que não tiveram uma abertura direta ou influenciada por um longo tempo.

1. Identifique usuários não responsivos com base em aberturas diretas ou por influência.
2. Pare gradualmente de enviar notificações por push para esses usuários.
3. Antes de remover as notificações por push completamente, envie uma última notificação explicando por que eles não as receberão mais. Isso dá aos usuários a chance de demonstrar seu interesse em continuar recebendo notificações ao abrir essa notificação.
4. Após a política de sunset entrar em vigor, use uma [mensagem no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) para lembrar esses usuários de que, embora eles não recebam mais pushes, os canais de envio de mensagens no app continuarão a fornecer informações interessantes e úteis.

Embora você possa estar relutante em parar de enviar notificações push para os usuários que originalmente optaram por recebê-las, lembre-se de que outros canais de envio de mensagens podem alcançar esses usuários de forma mais eficaz, especialmente se eles já ignoraram suas notificações push anteriormente. Se o usuário abrir seus e-mails, campanhas de e-mail são uma boa maneira de alcançá-los fora do seu app. Se não, as mensagens no app são a melhor maneira de entregar conteúdo sem arriscar que o usuário desinstale seu app.

## Definir eventos de conversão para aberturas de app

Ao atribuir [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) a uma campanha de push, você pode rastrear aberturas de app por um determinado período após o recebimento da campanha. Definir um evento de conversão para aberturas de app fornece um insight diferente das estatísticas de resultados que você normalmente recebe após uma campanha de push.

Embora todos os resultados da campanha de push dividam as aberturas diretas e aberturas de uma mensagem (que incluem tanto aberturas diretas quanto [aberturas por influência]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens/)), o rastreamento de conversão rastreará qualquer tipo de abertura, seja direta ou por influência.

Além disso, ao usar o evento de conversão "abre o app", você está rastreando aberturas de app que ocorrem antes do prazo de conversão (por exemplo, três dias). Isso difere de uma abertura influenciada, pois o tempo que um usuário tem para registrar uma abertura influenciada pode variar de pessoa para pessoa, dependendo do comportamento de engajamento passado de cada usuário.

## Artigos relacionados

Não encontrou o que estava procurando? Confira estes artigos adicionais sobre melhores práticas:

- [Push message and image formats]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/)
- [Mensagens no app de push primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)
- [Entregabilidade para dispositivos Android chineses]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/chinese_push_deliverability/)
- [Saiba antes de enviar: canais]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/know_before_send/)
