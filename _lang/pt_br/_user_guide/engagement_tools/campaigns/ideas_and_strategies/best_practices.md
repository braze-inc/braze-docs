---
nav_title: Práticas recomendadas
article_title: Práticas recomendadas de campanha
page_order: 0
description: "Este artigo fornece as práticas recomendadas para criar e personalizar suas campanhas."
tool: Campaign

---

# Práticas recomendadas de campanha

## Quatro T's da Braze

A Braze recomenda que você envie apenas dados de clientes que pretenda utilizar na plataforma da Braze. Considere a filosofia dos "Quatro T's da Braze" para garantir que você só envie dados que serão usados:

- **Direcione** seu público criando [segmentos de público]({{site.baseurl}}/user_guide/engagement_tools/segments/).
- **Acione** suas mensagens com entrega [baseada em ação]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery#action-based-delivery) ou [acionada por API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/).
- **Modele** e personalize suas mensagens com a [lógica condicional do Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid).
- **Acompanhe** a eficácia de suas campanhas com o [rastreamento de conversões]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/).

Isso permite otimizar os dados enviados ao Braze e agilizará sua capacidade de enviar mensagens aos usuários, ao mesmo tempo em que garante o não rastreamento de pontos de dados que sua equipe pode não considerar úteis a longo prazo. 

## Direcionamento de usuários

Ao desenvolver suas campanhas ao longo do tempo, você poderá notar lapsos em seu público. Nesse ponto crucial, é possível direcionar [os usuários inativos]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/) com uma campanha especializada usando a segmentação. 

### Identifique seu público

Aproveite os segmentos e filtros a seu favor, definindo seu público. Considere quem é o público-alvo de sua campanha e de suas mensagens. Com essas informações importantes, você pode criar [campanhas em vários]({{site.baseurl}}/user_guide/engagement_tools/campaigns/faq/#how-do-you-create-a-multichannel-campaign) canais que ofereçam a flexibilidade de criar suas mensagens em canais diferentes para atender às preferências de notificação do seu público.

Também é importante entender seus [usuários ativos]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/active_user_campaigns/) para mostrar seu apreço aos usuários consistentes.

## Campanhas multicanais

### Reconhecimento de recursos

Se o seu objetivo é atrair seus usuários para um novo recurso ou versão do app, use uma estratégia multicanal com foco em canais dentro do app. [Mensagens dentro do app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) e [Cartões de Conteúdo]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/) são geralmente menos disruptivos se um usuário não deseja atualizar imediatamente. 

Não se esqueça de incluir [deep linking]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) para a loja de aplicativos apropriada.

Persuadir os usuários a atualizar o aplicativo ou a mudar a forma como usam o aplicativo pode ser difícil, portanto, informe-os sobre todos os benefícios da nova versão ou dos novos recursos e como isso melhorará a experiência deles com o aplicativo. 

### Enviar tempo

O momento certo é fundamental! Quando seu objetivo for convencer os usuários a atualizar seu app, espere até que eles tenham uma experiência positiva no app para perguntar aos usuários. Para manter o público engajado, evite o envio repetitivo de mensagens que possam parecer intrusivas.

Com o tempo, seus usuários podem esquecer certos recursos ou não perceber novos recursos. Quando novos recursos forem adicionados, não deixe de informar seus usuários por meio de [mensagens no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/). Se os usuários não estiverem se engajando com os principais recursos do aplicativo, talvez seja melhor lembrá-los quando estiverem se engajando com seu app e quando esse novo recurso seria útil. Nosso artigo sobre [aceitação de dados]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/) tem mais informações sobre como garantir que seu pedido esteja de acordo com as expectativas de fluxo de trabalho dos usuários. 

## Classificações altas

Obter classificações de cinco estrelas na loja de aplicativos está na lista de desejos de todo profissional de marketing para mobile. Obter avaliações positivas, no entanto, não é uma tarefa fácil, pois exige trabalho extra dos usuários. Aplicando nossa funcionalidade de maneiras inteligentes, podemos ajudá-lo a aumentar o engajamento de seus clientes.

### Direcionamento a usuários avançados

Os usuários avançados podem ser defensores do seu app. Muitas vezes, eles interagem com seu aplicativo de forma consistente e podem fornecer feedback para melhorar seu app. Embora sejam diferentes de aplicativo para aplicativo, os usuários avançados tendem a ter o seguinte:

- Registrou muitas sessões
- Usou o app recentemente
- Gastou dinheiro e fez compras

Para garantir classificações mais altas, peça aos usuários avançados que avaliem seu app na loja de aplicativos, pois é mais provável que eles tenham coisas boas a dizer. Por exemplo, você pode criar um segmento chamado "Power users" com esses filtros:
- Usou esses apps mais de 10 vezes nos últimos 14 dias
- Gastou mais de 50 dólares

![Um exemplo de um segmento que visa usuários avançados de um app.]({% image_buster /assets/img_archive/ratings_power_users.png %})

Visitar a app store leva tempo por parte dos seus usuários. Para maximizar a probabilidade de que eles façam um esforço extra, solicite uma classificação ou avaliação depois que eles tiverem uma experiência positiva com seu app. Por exemplo, pergunte a eles depois de terem superado um nível de jogo ou feito uma compra usando um código de desconto. Nosso artigo sobre [aceitação de dados]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states) tem mais informações sobre maneiras de garantir que sua solicitação esteja de acordo com as expectativas de fluxo de trabalho dos usuários.

## Agendamento de suas campanhas

Ao editar programações de campanhas ou públicos, observe as seguintes práticas recomendadas:

- **Campanhas de programação única:** Você pode editar a campanha até o horário de envio programado.
- **Campanhas programadas recorrentes:** Você pode editar a campanha até o horário de envio programado.
- **Campanhas de fuso local:** Não faça edições 24 horas antes do horário programado de envio.
- **Campanhas com tempo de envio ideal:** Não faça edições 24 horas antes da meia-noite do dia em que a campanha está programada para ser enviada.

{% alert note %}
Editar uma campanha ativa e mudar a entrega para o **Tempo de envio local** fará com que um novo lote de mensagens seja enfileirado, o que significa que seus usuários receberão a mensagem duas vezes devido à mensagem sendo enfileirada duas vezes. Para evitar isso, primeiro pare a campanha original, depois lance uma duplicata após atualizar o cronograma.
{% endalert %}

