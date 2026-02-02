---
nav_title: Melhorando a baixa latência
article_title: Melhore a baixa latência para cartões de conteúdo como banners
page_order: 10
description: "Este artigo cobre estratégias para garantir que os requisitos de baixa latência sejam atendidos com cartões de conteúdo."
channel:
  - content cards
---

# Melhore a latência para cartões de conteúdo como banners

> Se você está enfrentando latência com a implementação de cartões de conteúdo para casos de uso críticos, como banners na página inicial, revise esta página para estratégias e dicas que ajudem a resolver e acelerar sua renderização.

{% alert tip %}
Você está tentando exibir banners personalizados e proeminentes em seu aplicativo ou site? Experimente [Banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners/), que são projetados para suportar casos de uso de banners de baixa latência.
{% endalert %}

## Use entrada programada em vez de entrada baseada em ação

Cartões baseados em ação em campanhas e canavas exigem processamento em segundo plano. A Braze deve primeiro receber aviso da ação desencadeadora (como uma compra ocorrendo ou uma sessão começando) antes de criar um cartão para um usuário. Como resultado, haverá uma postergação antes que esses cartões fiquem disponíveis.

Cartões baseados em ação introduzirão complexidade adicional ao seu aplicativo, onde você pode se ver continuamente consultando e atualizando para esperar que o cartão esteja disponível. Em vez disso, configure seu cartão para ser `Scheduled Entry`, que atuará como uma janela de disponibilidade para que o cartão esteja sempre disponível para o público-alvo.

Se você programar seus cartões com antecedência, eles estarão prontos, esperando que o usuário abra seu aplicativo e solicite cartões.

## Use a lógica de envio "Na Primeira Impressão"

Juntamente com envios programados, a opção `At First Impression` evitará latência devido à velocidade com que um cartão é criado e armazenado na Braze. O `At Campaign Launch` cria todos os cartões para todos os usuários segmentados com antecedência, o que pode levar tempo para ser concluído. A opção `At First Impression` gerará um cartão para um usuário na primeira vez que for solicitado, como quando um usuário abre seu aplicativo pela primeira vez.

Isso significa que, juntamente com a entrada programada, os cartões estarão disponíveis imediatamente, assim que você precisar deles, seja no início da sessão ou para uma janela de elegibilidade baseada em tempo.

## Lembre-se de que a entrada do Canvas é um pré-requisito para receber cartões.

Ao usar o canva, lembre-se de que um usuário deve primeiro entrar no canva com base nos critérios de entrada configurados, e *então* deve fluir através da etapa da mensagem do cartão de conteúdo. Somente então o cartão estará disponível para seu app ou site. Lembre-se, há uma latência embutida para que o cartão seja criado uma vez que o usuário passe pela etapa e pode haver uma postergação quando o cartão estiver disponível.

## Não atualize os cartões excessivamente

Os cartões de conteúdo são atualizados automaticamente pelo SDK a cada novo início de sessão. Você também pode solicitar manualmente uma atualização do cartão de conteúdo a qualquer momento durante uma sessão ativa.

Chamar o método `requestContentCardsRefresh` e atualizar com muita frequência pode levar a limitações de taxa. Se seu app se tornar temporariamente limitado por taxa, você pode não conseguir atualizar os cartões quando precisar ou em um momento crítico no engajamento do usuário com seu app.

Para evitar que isso aconteça, chame este método de atualização apenas em momentos importantes no ciclo de vida do usuário, como após um usuário fazer uma compra ou após um usuário atualizar seu nível de inscrição.

## Evite incluir Conteúdo Conectado

Conteúdo Conectado enriquece os cartões de conteúdo com dados de API de primeira ou terceira parte. No entanto, quando incluído em uma mensagem de cartão de conteúdo, bloqueará a disponibilidade do cartão até que a solicitação de rede de Conteúdo Conectado possa ser concluída. Em alguns casos, isso fará com que os SDKs tentem novamente alguns segundos depois, em um esforço para não atrasar a lógica de renderização do seu app, que pode esperar que o SDK conclua sua tarefa de atualização.

Se você precisar usar Conteúdo Conectado, agende esses cartões com antecedência e use a opção `At Campaign Launch` para que os cartões sejam pré-criados antes da próxima sessão de um usuário. Observe que esses cartões não estarão disponíveis imediatamente, pois a Braze escreve todos os cartões para todos os usuários elegíveis.
