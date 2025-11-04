---
page_order: 20
nav_title: Práticas recomendadas
article_title: Práticas recomendadas de envio
description: "Esta página contém práticas recomendadas de push e casos de uso para garantir que suas mensagens push inspirem engajamento em vez de irritação."
channel: push
---

# Práticas recomendadas de envio

As notificações por push são ferramentas poderosas para interagir com os usuários do seu aplicativo, mas devem ser usadas com cuidado para garantir que entreguem mensagens oportunas e relevantes. Antes de enviar sua mensagem push, consulte as práticas recomendadas a seguir para saber o que você deve saber e verificar.

{% alert important %}
Suas mensagens push devem estar dentro das diretrizes das políticas da Apple App Store e da Play Store do Google, especificamente em relação ao uso de mensagens push como anúncios, spam, promoções e muito mais. Saiba mais sobre [as regulamentações de push móvel]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#mobile-push-regulations-for-apps).
{% endalert %}

## Componha sua mensagem push

Como prática recomendada, a Braze recomenda manter cada linha de texto, tanto para o título opcional quanto para o corpo da mensagem, com aproximadamente 30 a 40 caracteres em uma notificação push para celular. Observe que o contador de caracteres no compositor não leva em conta os caracteres líquidos. Isso significa que a contagem final de caracteres de uma mensagem depende de como o Liquid é renderizado para cada usuário. Em caso de dúvida, seja breve e direto.

## Reduzir o tamanho da carga útil da notificação push

O tamanho máximo da carga útil depende da plataforma.

| Plataforma | Tamanho máximo da carga útil |
| --- | --- |
| Web | 3.807 bytes |
| Android | 3.930 bytes |
| iOS | 3.960 bytes |
| Kindle | 5.985 bytes |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Se seu push exceder o tamanho máximo da carga útil, a mensagem não poderá ser enviada. Como prática recomendada, mantenha sua carga útil em algumas centenas de bytes.

### O que é uma carga útil push?

Os provedores de serviços push calculam se a sua notificação push pode ser exibida para um usuário observando o tamanho em bytes de toda a carga útil do push. A carga útil é limitada a **4 KB (4.096 bytes)** para a maioria dos serviços push, incluindo:

- Serviço de notificação por push da Apple (APNs)
- Firebase Cloud Messaging (FCM) do Android
- Empurrar pela Web
- Impulso da Huawei

Esses serviços push recusarão qualquer notificação que exceda esse limite.

A Braze reserva uma parte da carga útil do push para fins de integração e análise. Com isso, nosso tamanho máximo de carga útil é de **3.807 bytes**. Se seu push exceder esse tamanho, a mensagem poderá não ser enviada. Como prática recomendada, mantenha sua carga útil em algumas centenas de bytes.

Os seguintes elementos em seu push compõem a carga útil do push:

- Cópia, como o título e o corpo da mensagem
- Renderização final de qualquer personalização do Liquid
- URLs para imagens (mas não o tamanho da imagem em si)
- URLs para alvos de clique
- Nomes de botões
- Pares de valores-chave

### Dicas para reduzir o tamanho da carga útil

Para reduzir o tamanho da carga útil:

- Mantenha sua mensagem breve. Uma boa diretriz geral é torná-lo acionável e benéfico em menos de 40 caracteres.
- Omita espaços em branco e quebras de linha em sua cópia.
- Considere como o Liquid será renderizado no envio. Como a renderização final de qualquer personalização do Liquid varia de usuário para usuário, o Braze não pode determinar se uma carga útil de push excederá o limite de tamanho quando o Liquid for incluído. Se o Liquid renderizar uma mensagem mais curta, talvez não haja problema. No entanto, se o Liquid resultar em uma mensagem mais longa, o push poderá exceder o limite de tamanho da carga útil. Sempre teste sua mensagem push em um dispositivo real antes de enviá-la aos usuários.
- Considere encurtar os URLs usando um encurtador de URL.

## Otimizar a segmentação

### Colete dados relevantes do usuário

As notificações por push devem ser tratadas com cuidado para que os usuários recebam notificações oportunas e relevantes. A Braze coletará informações úteis sobre dispositivos e uso que podem ser usadas para direcionar segmentos relevantes. Essas informações devem ser complementadas com eventos personalizados e atributos específicos do seu aplicativo. Usando esses dados, você pode direcionar cuidadosamente as mensagens para aumentar as taxas de abertura e diminuir as instâncias de usuários que desativam o push.

### Criar uma página de configurações de notificação

Você pode criar uma página de configurações no seu aplicativo que permita aos usuários informar quais notificações eles desejam receber. Uma abordagem comum é criar um atributo booleano personalizado no Braze correspondente ao status de configuração do aplicativo. Por exemplo, um aplicativo de notícias pode ter configurações de assinatura para notícias de última hora, notícias esportivas ou políticas.

Quando o aplicativo de notícias deseja criar uma campanha direcionada somente a usuários interessados em Política, ele adiciona o filtro de atributo `Subscribes to Politics` ao segmento. Quando definido como true, somente os usuários que se inscreverem para receber notificações as receberão.

Para obter mais informações sobre a configuração de atributos personalizados, consulte os seguintes artigos para [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/#setting-custom-attributes) ou [API REST]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-attributes-object-specification).

## Aumentar os opt-ins e a relevância

### Obter permissão do usuário

As estatísticas gerais para push habilitado estarão relacionadas ao fato de o usuário ter aprovado as notificações com seu sistema operacional. Se os usuários desativarem as notificações no iOS, eles serão automaticamente removidos do nosso sistema, pois a Apple não permitirá que o token push seja enviado.

O Android 13 ou superior exige a obtenção de permissão para que as notificações por push possam ser exibidas. As versões mais antigas do Android assinam as notificações dos usuários por padrão.

### Usuários principais para push

Você só tem uma chance de pedir permissão de push a um usuário e, depois que ele recusa, é muito difícil convencê-lo a reativar o push nas configurações do dispositivo. Por esse motivo, você deve preparar os usuários para o push usando uma mensagem no aplicativo antes de mostrar o prompt do sistema. Consulte [Mensagens in-app do Push Primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) para saber mais sobre como aumentar os opt-ins.

### Adicionar controles de assinatura push

Para evitar que os usuários desativem as notificações no nível do dispositivo, o que remove completamente o token de push em primeiro plano, permita que os usuários controlem a assinatura de push diretamente no aplicativo. Consulte [Atualização dos estados da assinatura push]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions#update-push-subscription-state) para obter mais detalhes.

### Compreender os estados da assinatura push

O estado da assinatura de push não garante que um push será entregue - os usuários também devem estar habilitados para receber notificações. Isso ocorre porque um perfil de usuário pode ter vários dispositivos com diferentes permissões de push em primeiro plano, mas apenas um único estado de assinatura de push.

Se um usuário não tiver um token de push em primeiro plano válido para um aplicativo (ou seja, ele desativa os tokens de push no nível do dispositivo por meio das configurações, optando por não receber notificações), seu estado de assinatura ainda poderá ser considerado `subscribed` para push. No entanto, esse usuário não seria `Foreground Push Enabled for App` no Braze, pois o token de push em primeiro plano não é válido.

Além disso, se um perfil de usuário não tiver um token de push válido ou registrado para outros aplicativos, o filtro `Foreground Push Enabled` na segmentação também será falso.

## Implemente uma política de encerramento para usuários que não respondem

Mesmo quando você envia apenas notificações push relevantes e oportunas, alguns usuários podem não responder a elas e considerá-las spam. Suponha que um usuário apresente um histórico de ignorar repetidamente suas notificações por push. Nesse caso, é uma boa ideia parar de enviar pushs antes que eles fiquem irritados com as comunicações do seu aplicativo ou o desinstalem completamente. 

Para isso, crie uma [política de descontinuidade]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies) que, eventualmente, pare de enviar notificações por push para os usuários que não tiverem uma conta direta ou influenciada aberta por um longo período.

1. Identifique usuários que não respondem com base em aberturas diretas ou influenciadas.
2. Pare gradualmente de enviar notificações push para esses usuários.
3. Antes de remover totalmente as notificações push, envie uma última notificação explicando por que eles não as receberão mais. Isso dá aos usuários a chance de demonstrar seu interesse em continuar os envios abrindo a notificação.
4. Depois que a política de descontinuidade entrar em vigor, use uma [mensagem in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) para lembrar a esses usuários que, embora eles não recebam mais pushs, os canais de mensagens in-app continuarão a fornecer informações interessantes e úteis.

Embora você possa estar relutante em parar de enviar pushes para usuários que originalmente optaram por eles, lembre-se de que outros canais de mensagens podem alcançar esses usuários de forma mais eficaz, especialmente se eles ignoraram seus pushes anteriormente. Se o usuário abrir seus e-mails, as campanhas de e-mail são uma boa maneira de alcançá-lo fora do seu aplicativo. Caso contrário, as mensagens in-app são a melhor maneira de fornecer conteúdo sem correr o risco de o usuário desinstalar o aplicativo.

## Definir eventos de conversão para aberturas de aplicativos

Ao atribuir [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) a uma campanha push, você pode rastrear as aberturas de aplicativos por um determinado período após o recebimento da campanha. A definição de um evento de conversão para aberturas de aplicativos fornece uma visão diferente das estatísticas de resultados que você normalmente recebe após uma campanha push.

Embora todos os resultados de campanhas push dividam as aberturas e aberturas diretas de uma mensagem (que incluem [aberturas]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens/) diretas e [influenciadas]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens/)), o rastreamento de conversões rastreará qualquer tipo de abertura, seja ela direta ou influenciada.

Além disso, ao usar o evento de conversão "abre aplicativo", você está rastreando as aberturas de aplicativos que ocorrem antes desse prazo de conversão (por exemplo, três dias). Isso difere de uma abertura influenciada, pois o tempo que um usuário tem para registrar uma abertura influenciada pode variar de pessoa para pessoa, dependendo do comportamento de envolvimento anterior de cada usuário.

## Artigos relacionados

Não encontrou o que estava procurando? Confira estes artigos adicionais sobre práticas recomendadas:

- [Formatos de mensagens e imagens push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/)
- [Mensagens push primer no aplicativo]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)
- [Capacidade de entrega para dispositivos Android chineses]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/chinese_push_deliverability/)
- [Saiba antes de enviar: canais]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/know_before_send/)
