---
nav_title: Práticas recomendadas
article_title: Práticas recomendadas de campanha
page_order: 0
description: "Este artigo fornece as práticas recomendadas para criar e personalizar suas campanhas."
tool: Campaign

---

# Práticas recomendadas de campanha

## Quatro T's da brasagem

A Braze recomenda que você envie apenas dados de clientes que pretenda utilizar na plataforma Braze. Considere a filosofia dos "Quatro T's do Braze" para garantir que você só envie dados que serão usados:

- **Direcione** seu público-alvo criando [segmentos de público-alvo]({{site.baseurl}}/user_guide/engagement_tools/segments/).
- **Acione** suas mensagens com entrega [baseada em ação]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery#action-based-delivery) ou [acionada por API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/).
- **Crie modelos** e personalize suas mensagens com a [lógica condicional do Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid).
- **Acompanhe** a eficácia de suas campanhas com o [controle de conversões]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/).

Isso permite que você otimize os dados enviados ao Braze e simplificará sua capacidade de enviar mensagens aos seus usuários, ao mesmo tempo em que evita o rastreamento de pontos de dados que sua equipe pode não considerar úteis a longo prazo. 

## Segmentação de usuários

À medida que você desenvolve suas campanhas ao longo do tempo, pode notar lapsos em seu público. Nesse ponto crucial, você pode segmentar os [usuários que estão perdendo o interesse]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/) com uma campanha especializada usando a segmentação. 

### Identifique seu público-alvo

Aproveite os segmentos e filtros a seu favor, definindo seu público-alvo. Considere quem é o público-alvo de sua campanha e de suas mensagens. Com essas informações importantes, você pode criar [campanhas multicanais]({{site.baseurl}}/user_guide/engagement_tools/campaigns/faq/#how-do-you-create-a-multichannel-campaign) que oferecem a flexibilidade de criar suas mensagens em diferentes canais para atender às preferências de notificação do seu público.

Também é importante entender seus [usuários ativos]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/active_user_campaigns/) para mostrar seu apreço pelos usuários consistentes.

## Campanhas multicanais

### Reconhecimento de recursos

Se o seu objetivo é atrair os usuários para um novo recurso ou versão do aplicativo, use uma estratégia multicanal com foco nos canais in-app. [As mensagens in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) e [os Content Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/) geralmente são menos perturbadores se o usuário não quiser fazer a atualização imediatamente. 

Não se esqueça de incluir [links diretos]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) para a loja de aplicativos apropriada.

Persuadir os usuários a atualizar o aplicativo ou a mudar a forma como usam o aplicativo pode ser difícil, portanto, informe-os sobre todos os benefícios da nova versão ou dos novos recursos e como isso melhorará a experiência deles com o aplicativo. 

### Enviar tempo

O momento certo é fundamental! Quando o seu objetivo for convencer os usuários a atualizar o aplicativo, espere até que eles tenham uma experiência positiva com o aplicativo para perguntar aos usuários. Para manter seu público-alvo envolvido, evite mensagens repetitivas que possam parecer intrusivas.

Com o tempo, seus usuários podem esquecer certos recursos ou não perceber novos recursos. Quando novos recursos forem adicionados, não deixe de informar seus usuários por meio de [mensagens no aplicativo]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/). Se os usuários não estiverem interagindo com os principais recursos do aplicativo, talvez seja melhor lembrá-los quando eles estiverem interagindo com o aplicativo e quando esse novo recurso for útil. Nosso artigo sobre [opt-in de dados]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/) tem mais informações sobre como garantir que sua solicitação esteja de acordo com as expectativas de fluxo de trabalho dos usuários. 

## Classificações altas

Obter classificações de cinco estrelas na loja de aplicativos está na lista de desejos de todo profissional de marketing móvel. Obter avaliações positivas, no entanto, não é uma tarefa fácil, pois exige trabalho extra dos usuários. Ao aplicar nossa funcionalidade de maneiras inteligentes, podemos ajudá-lo a aumentar o envolvimento do cliente.

### Segmentação de usuários avançados

Os usuários avançados podem ser defensores do seu aplicativo. Muitas vezes, eles interagem com seu aplicativo de forma consistente e podem fornecer feedback para aprimorá-lo. Embora sejam diferentes de aplicativo para aplicativo, os usuários avançados tendem a ter o seguinte:

- Registrou muitas sessões
- Usou o aplicativo recentemente
- Gastou dinheiro e fez compras

Para garantir classificações mais altas, peça aos seus usuários avançados que avaliem seu aplicativo na loja de aplicativos, pois é mais provável que eles tenham ótimas coisas a dizer. Por exemplo, você pode criar um segmento chamado "Power users" com esses filtros:
- Usou esses aplicativos mais de 10 vezes nos últimos 14 dias
- Gastou mais de 50 dólares

\![Um exemplo de um segmento que tem como alvo os usuários avançados de um aplicativo.]({% image_buster /assets/img_archive/ratings_power_users.png %})

Visitar a loja de aplicativos leva tempo para os usuários. Para maximizar a probabilidade de que eles façam um esforço extra, solicite uma classificação ou avaliação depois que eles tiverem uma experiência positiva com seu aplicativo. Por exemplo, pergunte a eles depois de terem superado um nível de jogo ou feito uma compra usando um código de desconto. Nosso artigo sobre [opt-in de dados]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states) tem mais informações sobre maneiras de garantir que sua solicitação esteja de acordo com as expectativas de fluxo de trabalho dos usuários.

## Agendamento de suas campanhas

Ao editar programações de campanhas ou públicos, observe as seguintes práticas recomendadas:

- **Campanhas de programação única:** Você pode editar a campanha até o horário de envio programado.
- **Campanhas programadas recorrentes:** Você pode editar a campanha até o horário de envio programado.
- **Campanhas de tempo de envio local:** Não faça edições 24 horas antes do horário de envio programado.
- **Campanhas com tempo de envio ideal:** Não faça edições 24 horas antes da meia-noite do dia em que a campanha está programada para ser enviada.

{% alert note %}
Editar uma campanha ativa e alterar a entrega para **Hora de envio local** fará com que um novo lote de mensagens seja enfileirado, o que significa que seus usuários receberão a mensagem duas vezes, pois a mensagem será enfileirada duas vezes. Para evitar isso, primeiro interrompa a campanha original e, em seguida, inicie uma duplicada após atualizar o cronograma.
{% endalert %}

