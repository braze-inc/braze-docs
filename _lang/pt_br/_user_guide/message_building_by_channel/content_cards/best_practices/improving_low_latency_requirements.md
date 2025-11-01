---
nav_title: Melhoria da baixa latência
article_title: Aprimoramento da baixa latência para cartões de conteúdo como banners
page_order: 10
description: "Este artigo aborda estratégias para garantir que os requisitos de baixa latência sejam atendidos com os Content Cards."
channel:
  - content cards
---

# Melhorar a latência dos Content Cards como banners

> Se você estiver enfrentando latência com sua implementação de Content Cards para casos de uso críticos, como banners de página inicial, consulte esta página para obter estratégias e dicas para ajudar a resolver e acelerar a renderização.

{% alert tip %}
Está tentando exibir banners personalizados e de destaque em seu aplicativo ou site? Experimente [os Banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners/), que foram criados para oferecer suporte a casos de uso de banners de baixa latência.
{% endalert %}

## Usar entrada programada em vez de entrada baseada em ação

Os cartões baseados em ação, tanto nas campanhas quanto nos Canvases, exigem processamento em segundo plano. A Braze deve primeiro receber uma notificação da ação desencadeadora (como a ocorrência de uma compra ou o início de uma sessão) antes de criar um cartão para um usuário. Como resultado, haverá um atraso na disponibilização desses cartões.

Os cartões baseados em ações introduzirão uma complexidade adicional ao seu aplicativo, no qual você poderá ter que fazer pesquisas e atualizações contínuas para esperar que o cartão esteja disponível. Em vez disso, configure seu cartão para ser `Scheduled Entry`, que funcionará como uma janela de disponibilidade para que o cartão esteja sempre disponível para o público-alvo.

Se você programar seus cartões com antecedência, eles estarão prontos, esperando que o usuário abra seu aplicativo e solicite cartões.

## Use a lógica de envio "At First Impression" (na primeira impressão)

Juntamente com os envios programados, a opção `At First Impression` evitará a latência devido à velocidade com que um cartão é criado e armazenado no Braze. O `At Campaign Launch` cria antecipadamente todos os cartões para todos os usuários segmentados, o que pode levar algum tempo para ser concluído. A opção `At First Impression` gerará um cartão para um usuário na primeira vez em que ele for solicitado, como quando um usuário abre seu aplicativo pela primeira vez.

Isso significa que, juntamente com a entrada programada, os cartões estarão disponíveis imediatamente, assim que você precisar deles, seja no início da sessão ou em uma janela de elegibilidade baseada em tempo.

## Lembre-se de que a inscrição no Canvas é um pré-requisito para receber cartões

Ao usar o Canvas, lembre-se de que um usuário deve primeiro entrar no Canvas com base em seus critérios de entrada configurados e *, em seguida,* deve passar pela etapa de mensagem do Content Card. Só então o cartão estará disponível para seu aplicativo ou site. Lembre-se de que há uma latência embutida para a criação do cartão quando o usuário passa pela etapa e pode atrasar quando o cartão estiver disponível.

## Não atualize os cartões excessivamente

Os Content Cards são atualizados automaticamente pelo SDK a cada início de nova sessão. Você também pode solicitar manualmente uma atualização do Content Card a qualquer momento durante uma sessão ativa.

A chamada do método `requestContentCardsRefresh` e a atualização muito frequente podem levar à limitação da taxa. Se o seu aplicativo ficar temporariamente com a taxa limitada, talvez não seja possível atualizar os cartões quando for necessário ou em um momento crítico do envolvimento do usuário com o aplicativo.

Para evitar que isso aconteça, chame esse método de atualização somente em momentos importantes do ciclo de vida do usuário, como depois que um usuário fizer uma compra ou depois que um usuário fizer upgrade de seu nível de assinatura.

## Evite incluir conteúdo conectado

O Connected Content enriquece os Content Cards com dados de API próprios ou de terceiros. No entanto, quando incluído em uma mensagem de Content Card, ele bloqueará a disponibilidade do cartão até que a solicitação da rede Connected Content possa ser concluída. Em alguns casos, isso fará com que os SDKs tentem novamente alguns segundos depois, em um esforço para não atrasar a lógica de renderização do seu aplicativo, que pode esperar que o SDK conclua a tarefa de atualização.

Se for necessário usar o Connected Content, agende esses cartões com antecedência e use a opção `At Campaign Launch` para que os cartões sejam pré-criados antes da próxima sessão do usuário. Observe que esses cartões não estarão disponíveis imediatamente, pois o Braze grava todos os cartões para todos os usuários qualificados.
