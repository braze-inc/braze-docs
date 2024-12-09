---
nav_title: Cartões de conteúdo
article_title: Cartões de conteúdo no Canvas
page_order: 1
page_type: reference
description: "Este artigo de referência descreve os recursos e as nuances específicas do uso dos cartões de conteúdo como um canal de envio de mensagens no Canva."
tool: Canvas
channel: content cards

---

# Cartões de conteúdo no Canvas

> Os cartões de conteúdo podem ser enviados a seus clientes como parte de sua jornada no canva. Este artigo descreve os recursos e as nuances específicas do uso dos cartões de conteúdo como um canal de envio de mensagens no Canva.

Assim como em outros canais de envio de mensagens do Canva, os cartões de conteúdo serão enviados para o dispositivo do usuário quando ele atender ao público e aos critérios de direcionamento especificados para a etapa do canva. Depois que o cartão de conteúdo for enviado, ele estará disponível no feed de cada usuário elegível na próxima vez que o feed de cartões for atualizado.

![][1]

Duas opções que mudarão a forma como a etapa do cartão de conteúdo interagirá com o Canva são seu [comportamento de](#advancement-behavior-options) [expiração](#content-card-expiration) e [avanço](#advancement-behavior-options).

## Expiração do cartão de conteúdo {#content-card-expiration}

Ao criar um novo cartão de conteúdo, você pode escolher quando ele deve expirar do feed do usuário com base no tempo de envio. A contagem regressiva para a expiração de um cartão de conteúdo começa quando o usuário chega à etapa de mensagens no Canva em que o cartão é enviado. O cartão estará ativo no feed do usuário a partir desse momento até expirar. Um cartão pode existir no feed de um usuário por até 30 dias. 

### Datas de expiração relativas versus absolutas

Você tem duas maneiras de definir quando um cartão deve desaparecer do feed de um usuário: uma data relativa ou uma data absoluta. Veja a seguir como cada um deles funciona:

#### Datas relativas

Ao escolher uma data relativa, como "Remover cartões enviados após 5 dias no feed de um usuário", é possível definir uma data de expiração máxima de 30 dias.

#### Datas absolutas

Quando você escolhe uma data absoluta, como "Remove sent cards on December 1, 2023 at 4 pm" (Remover cartões enviados em 1º de dezembro de 2023 às 16h), há algumas nuances envolvidas.

Embora seja possível especificar uma duração de expiração maior que 30 dias, o cartão de conteúdo existirá no feed de um usuário por no máximo 30 dias. Especificar uma duração superior a 30 dias permite levar em conta qualquer postergação antes de disparar a etapa Mensagem, mas não estende a vida útil máxima do cartão no feed do usuário.

Tenha cuidado ao definir uma data de expiração com mais antecedência do que 30 dias após o lançamento do Canva. Se um usuário chegar à etapa Mensagem mais de 30 dias antes da data de expiração especificada, o cartão não será enviado.

### Comportamento de expiração

O cartão de conteúdo permanece disponível no feed do usuário até atingir sua data de expiração, mesmo que o usuário avance para etapas subsequentes na jornada do Canva. Se você não quiser que o cartão de conteúdo esteja ativo quando as próximas etapas do canva forem entregues, certifique-se de que a expiração seja mais curta do que a postergação nas etapas subsequentes.

Após a expiração de um cartão de conteúdo, ele será automaticamente removido do feed do usuário durante a próxima atualização, mesmo que ele ainda não o tenha visualizado.

## Opções de comportamento de avanço {#advancement-behavior-options}

{% alert important %}
A partir de 28 de fevereiro de 2023, não será mais possível criar ou duplicar canvas usando o editor original. Esta seção está disponível para referência ao entender como o comportamento de avanço funciona para etapas com cartões de conteúdo.
{% endalert %}

{% alert note %}
No Canvas Flow, os componentes de mensagem avançam automaticamente todos os usuários que entram na etapa do canva. Não há necessidade de especificar o comportamento de avanço de mensagens, o que simplifica a configuração da etapa geral. Se quiser implementar a opção **Advance when message sent**, adicione uma [jornada do público]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) separada para filtrar os usuários que não receberam a etapa anterior.
{% endalert %}

A opção Advancement Behavior (Comportamento de avanço) permite controlar quando um usuário deve avançar para a próxima etapa elegível. As etapas que enviam [apenas cartões de conteúdo](#steps-with-in-content-cards-only) têm opções de avanço diferentes das [etapas com vários tipos de mensagens](#steps-with-multiple-message-channels) (push, e-mail etc.). Para os cartões de conteúdo em um fluxo de trabalho do Canvas Flow, essa opção é definida para sempre avançar imediatamente o público.

### Etapas somente com cartões de conteúdo {#steps-with-in-content-cards-only}

Se uma etapa contiver apenas cartões de conteúdo (e nenhum outro canal de envio de mensagens), você poderá controlar o comportamento de avanço com as seguintes opções:

| Opção | Descrição |
|---|---|
| Avançar quando uma mensagem for enviada | Os usuários avançarão para as próximas etapas do Canva quando o cartão de conteúdo tiver sido enviado com sucesso. Use essa opção quando quiser que os usuários avancem apenas se o cartão for enviado e não for abortado. |
| Avançar público imediatamente | Os usuários avançarão para as próximas etapas do Canva quando houver tentativa de envio do cartão de conteúdo. Se o cartão for abortado e não for enviado, os usuários ainda avançarão para a próxima etapa. Use essa opção quando quiser que os usuários avancem, independentemente de o cartão de conteúdo ser enviado com êxito ou abortado. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][2]

### Componentes com vários canais {#steps-with-multiple-message-channels}

Os componentes do canva com um cartão de conteúdo e outro canal de envio de mensagens têm as seguintes opções de avanço:

| Opção | Descrição |
|---|---|
| Avançar quando uma mensagem for enviada | Os usuários avançarão para as próximas etapas do canva quando pelo menos um dos tipos de mensagem nessa etapa tiver sido enviado com êxito.|
| Avançar público imediatamente | Quando essa opção for selecionada, todos no público do componente avançarão para as próximas etapas após o envio das mensagens, independentemente de terem visto a mensagem notada ou não.  <br> <br> _Os usuários devem corresponder ao segmento do componente e aos critérios de filtro para avançar para as próximas etapas._ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][3]

## Relatórios e análise de dados

Depois de iniciar uma etapa dos cartões de conteúdo no Canva, você pode começar a analisar várias métricas diferentes para essa etapa. Essas métricas incluem o número de mensagens enviadas, destinatários únicos, taxas de conversão, receita total e muito mais.

![][4]

Para saber mais sobre as métricas disponíveis e suas definições, consulte nosso [Glossário de métricas de relatórios][6].

## Casos de uso

#### Ofertas promocionais

Adicione cartões ao feed de um usuário à medida que ele se qualifica para promoções e anúncios específicos. Por exemplo, se um usuário se tornar elegível para uma nova oferta depois de executar uma ação ou fazer uma compra, usando o Canva, você poderá enviar a ele um cartão de conteúdo, além de outros canais de envio de mensagens, para que, na próxima vez que ele abrir o app, a oferta esteja disponível para ele.

#### Caixa de entrada de notificações por push

Há ocasiões em que um usuário pode descartar uma notificação por push ou excluir um e-mail, mas você quer lembrá-lo ou promover a oferta caso ele mude de ideia.

Usando o Canva, é possível adicionar um componente que envia um Content Card e uma notificação por push para oferecer aos usuários uma "caixa de entrada" persistente de cartões que se alinham às mensagens promocionais enviadas via push. 

#### Vários feeds com base em categorias

É possível separar seus cartões de conteúdo em vários feeds com base em categorias, como diferentes tópicos que os usuários podem navegar, ou feeds transacionais e de marketing. Para saber mais sobre como criar vários feeds usando pares de valores-chave, consulte nosso guia para [Personalização dos feeds do cartão de conteúdo][7].


[1]: {% image_buster /assets/img_archive/content-cards-in-canvas.png %}
[2]: {% image_buster /assets/img_archive/content-cards-in-canvas-single-channel.png %}
[3]: {% image_buster /assets/img_archive/content-cards-in-canvas-multiple-channels.png %}
[4]: {% image_buster /assets/img_archive/content-cards-in-canvas-analytics.png %}
[6]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/
[7]: {{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds