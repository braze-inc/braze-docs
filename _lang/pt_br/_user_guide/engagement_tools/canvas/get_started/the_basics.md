---
nav_title: Noções básicas de tela
article_title: Fundamentos do Canvas
page_order: 1
page_type: reference
description: "Este artigo de referência aborda os conceitos básicos do Canvas, incluindo várias perguntas que você deve fazer a si mesmo ao configurar seu primeiro Canvas."
tool: Canvas

---

# Noções básicas de tela

> Este artigo de referência aborda os conceitos básicos do Canvas, incluindo várias perguntas que você deve fazer a si mesmo ao configurar seu primeiro Canvas. Também explicaremos os cinco Ws (o quê, quando, quem, por que e onde) da visualização e como isso pode moldar e definir como você pode criar seu Canvas.

## Entendendo a estrutura do Canvas

Antes de começarmos com os detalhes mais refinados da [configuração do Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/), vamos identificar as partes principais que compõem um Canvas.

{% tabs %}
  {% tab Canvas %}
  O Canvas é uma interface unificada na qual os profissionais de marketing criam campanhas com várias mensagens. É um pouco como uma ferramenta de programação visual, permitindo que você crie uma jornada de usuário coesa a partir de uma série de etapas.

  Um exemplo de um Canvas com uma etapa de divisão de decisão em duas jornadas de usuário diferentes, dependendo se o usuário estiver habilitado para push.]({% image_buster /assets/img/canvas_intro/canvas_intro.gif %})

  {% endtab %}

  {% tab Journey %}

  Uma jornada, ou comumente chamada de jornada do usuário, é a experiência de um usuário individual dentro do Canvas.<br><br> \![Um gráfico com a jornada do cliente para um novo usuário. Um usuário anônimo instala um aplicativo, Kat cria uma conta, Kat não abre o aplicativo por uma semana, uma notificação push traz Kat de volta ao aplicativo e, em seguida, Kat usa o aplicativo regularmente.]({% image_buster /assets/img_archive/Journey_2.png %}){: style="max-width:90%;"}

  {% endtab %}

  {% tab Canvas Builder %}
  O construtor do Canvas mapeia as etapas a serem seguidas ao criar seu Canvas. Isso inclui noções básicas, como nomear o Canvas e adicionar equipes. Essencialmente, o construtor do Canvas é a configuração crucial necessária antes de começar a criar seu Canvas. Aqui, você pode controlar a maneira como seus usuários iniciam e concluem a jornada do cliente com opções para editar o [cronograma de entrada]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2b-set-your-canvas-entry-schedule), [o público-alvo]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2c-set-your-target-entry-audience) e [as configurações de envio]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2d-select-your-send-settings).<br><br> O construtor do Canvas na seção Básico para um Canvas chamado "Novo Canvas".]({% image_buster /assets/img_archive/canvas_flow_entry_wizard.png %}){: style="max-width:90%;"}

  {% endtab %}

  {% tab Variants %}
  Uma variante é o caminho que cada cliente segue em sua jornada. O Canvas suporta até oito variantes com um grupo de controle. Você controla qual segmento do seu público-alvo seguirá cada variante.<br><br> \![Selecionando o botão "Add Variant" (Adicionar variante).]({% image_buster /assets/img/canvas_intro/add_canvas_variant.gif %})

  {% endtab %}

  {% tab Steps %}
  Uma etapa do Canvas é um ponto de decisão de marketing: "se isso, então aquilo". Aproveite [os componentes do Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/#about-canvas-components) para criar as etapas de uma jornada do usuário.<br><br> Exemplo de adição de uma etapa de atraso a um Canvas.]({% image_buster /assets/img/canvas_intro/add_canvas_step.gif %}) <br><br> Quando um usuário entra em um Canvas, ele começa na primeira etapa. Cada etapa tem condições que determinam se um usuário pode passar para a próxima etapa. Em uma etapa, você pode definir acionadores ou programar a entrega, refinar a segmentação adicionando filtros ou marcando eventos de exceção e especificar diferentes canais, como notificações push ou eventos de webhook. No Canvas, as etapas ocorrem em uma sequência, o que significa que a primeira etapa ocorre antes que a segunda possa ocorrer. Digamos que temos um Canvas com as seguintes etapas: Atrasar a etapa A com um atraso de 24 horas, enviar a etapa A com uma mensagem push e enviar a etapa B com uma mensagem no aplicativo. O usuário A é mantido em um atraso de 24 horas e, depois de 24 horas, ele receberá uma mensagem push e, em seguida, uma mensagem no aplicativo.

  {% endtab %}
{% endtabs %}

## Criação da jornada do cliente

O uso das cinco perguntas (o quê, quando, quem, por que e onde) da visualização pode ajudar a identificar suas estratégias de envolvimento do cliente para criar uma jornada de mensagem personalizada para cada um dos seus usuários.

### O "quê": Dê um nome ao seu Canvas

> O que você está tentando ajudar o usuário a fazer ou entender?

Nunca subestime o poder do nome. O Braze foi criado para a colaboração, portanto, este é um bom momento para se preparar para comunicar as metas à sua equipe.

Você pode adicionar tags e nomear as etapas e variantes em um Canvas. Para saber mais sobre as jornadas do cliente, confira nosso curso do Braze Learning sobre o [mapeamento dos ciclos de vida do usuário](https://learning.braze.com/mapping-customer-lifecycles).

### O "porquê": Identificar eventos de conversão

> Com base no "o quê", por que você está criando esse Canvas? 

É sempre importante ter uma meta definida em mente, e o Canvas ajuda a entender como está o seu desempenho em relação aos KPIs, como engajamento em sessões, compras e eventos personalizados.

A seleção de pelo menos um [evento de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) lhe dará a capacidade de entender como otimizar o desempenho dentro do Canvas. E se o seu Canvas tiver várias variantes ou um grupo de controle, o Braze usará o evento de conversão para determinar a melhor variação para atingir essa meta.

* **Iniciar sessão**: Quero que meus usuários voltem e se envolvam com o aplicativo.
* **Faça a compra**: Quero que meus usuários comprem.
* **Executar evento personalizado**: Quero que meus usuários executem uma ação específica que estou rastreando como um evento personalizado.
* **Aplicativo de upgrades:** Quero que meus usuários atualizem a versão do aplicativo.

### O "quando": Criar condições iniciais

> Quando um usuário iniciará essa experiência?

Sua resposta determinará os detalhes de quando e como o Canvas será entregue ao cliente. Os usuários podem entrar no seu Canvas de duas maneiras: acionadores programados ou baseados em ações.

{% alert tip %}
Confira [as funcionalidades baseadas em tempo]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/delivery_types/) do Canvas para obter mais estratégias e respostas a perguntas comuns.
{% endalert %}

A entrega programada permite que você envie um Canvas imediatamente para seu público-alvo. Você também pode enviá-la regularmente ou programá-la para um momento específico no futuro. As telas baseadas em ações respondem a comportamentos específicos do cliente à medida que eles ocorrem. Por exemplo, um acionador baseado em ação pode incluir a abertura de um aplicativo, a realização de uma compra, a interação com outra campanha ou o acionamento de qualquer evento personalizado. No momento em que a ação ocorre, você pode fazer com que o Canvas seja enviado aos seus usuários.

### O "quem": Selecione um público

> Quem você está tentando alcançar? 

Para definir seu "quem", você pode usar segmentos predefinidos disponíveis no Canvas. Você também pode adicionar mais filtros para se concentrar ainda mais na conexão com seu público-alvo. Depois de criar esses segmentos, somente os usuários que correspondem aos critérios do público-alvo podem entrar na jornada do Canvas, o que leva a uma experiência mais personalizada. Consulte esta tabela para ver os filtros disponíveis e como eles segmentam seus usuários para se adequarem ao seu caso de uso.

| Filtro              | Descrição                                                                                         |
|---------------------|-----------------------------------------------------------------------------------------------------|
| Dados personalizados         | Segmente usuários com base em eventos e atributos definidos por você. Pode usar recursos específicos de seu produto. |
| Atividade do usuário       | Segmentar os clientes com base em suas ações e compras.                                             |
| Retargeting         | Segmentar os clientes que foram enviados, receberam ou interagiram com Canvases anteriores.               |
| Atividade de marketing  | Segmentar os clientes com base em comportamentos universais, como o último envolvimento.                         |
| Atributos do usuário     | Segmentar os clientes por seus atributos e características constantes.                                 |
| Instalar atribuição | Segmente os clientes por sua primeira fonte, grupo de anúncios, campanha ou anúncio.                                 |

### O "onde": Encontrar meu público

> Onde posso alcançar melhor meu público? 

É aqui que determinamos quais canais de mensagens fazem mais sentido para a jornada do usuário. O ideal é alcançar os usuários onde eles são mais acessíveis. Com isso em mente, você pode usar qualquer um dos seguintes canais com o Canvas:
* [E-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/about/)
* [Empurrar]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/)
* [Mensagens no aplicativo]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/)
* [Cartões de conteúdo]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/)
* [SMS ou MMS]({{site.baseurl}}/about_sms/)
* [Webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/)

### O "como": Crie a experiência completa

> Como posso criar minha jornada do Canvas depois de identificar os cinco Ws?

O "como" resume coletivamente como você criará seu Canvas e como alcançará seus usuários com sua mensagem. Por exemplo, para que uma mensagem seja eficaz, você deve otimizar o tempo de sua mensagem em relação aos fusos horários de seus diferentes usuários.

A resposta a "como" também determina a cadência de envio de um Canvas para seu público-alvo (por exemplo, uma vez por semana ou a cada duas semanas) e quais canais de mensagens devem ser usados para cada Canvas que você criar, conforme descrito em "onde".

## Caso de uso: Fluxo de integração do cliente

Por exemplo, digamos que você seja um profissional de marketing da MovieCanon, uma empresa de serviços de streaming on-line, e esteja encarregado de criar um fluxo de integração para novos usuários do seu aplicativo. Ao fazer referência aos cinco Ws, poderíamos criar o Canvas da seguinte maneira.

* **O que**: O nome do nosso Canvas será "New Onboarding Journey" (Nova jornada de integração).
* **Por que**: O objetivo do nosso Canvas é dar as boas-vindas aos nossos usuários e fazer com que eles continuem interagindo com o aplicativo.
* **Quando**: Depois que um usuário abre o aplicativo pela primeira vez, queremos enviar um e-mail de boas-vindas. 
* **Quem**: Nosso alvo são os novos usuários que estão usando nosso aplicativo pela primeira vez.
* **Onde**: Estamos confiantes de que podemos alcançar novos usuários por meio de seus e-mails, que é a forma como fizemos todas as nossas mensagens anteriores.
* **Como**: Queremos definir um atraso de um dia para não sobrecarregar nossos novos usuários com notificações. Após esse atraso, enviaremos um e-mail com uma lista dos filmes e programas de TV mais populares para incentivá-los a continuar usando o aplicativo.

## Dicas gerais

### Determinar quando e como usar etapas e variantes

Cada Canvas deve ter pelo menos uma variante e pelo menos uma etapa. A partir daí, o céu é o limite - então, como você decide o formato do seu Canvas? É aqui que suas metas, dados e hipóteses entram em ação. O brainstorming de "como" e "onde" ajudará você a mapear o formato e a estrutura corretos do seu Canvas.

### Trabalhar de trás para frente

Algumas metas têm submetas menores. Por exemplo, se o seu objetivo é converter um usuário gratuito em assinante, talvez seja necessária uma página com os serviços de assinatura descritos. O visitante pode precisar ver as opções antes de comprar. Você pode concentrar seus esforços de mensagens em mostrar a eles essa página antes de uma página de checkout. Trabalhar de trás para frente para entender a jornada que um cliente deve percorrer para chegar à sua meta é fundamental para orientá-lo até a conversão.

### Misture suas mensagens

Você já realizou uma campanha semelhante no passado? Ou há um em execução no momento? Tente usar essa única mensagem e adicionar mais personalização a ela. Experimente um novo filtro ou adicione uma mensagem de acompanhamento. À medida que você mistura suas técnicas de mensagens, monitore seu desempenho e continue otimizando, fazendo alterações incrementais.
