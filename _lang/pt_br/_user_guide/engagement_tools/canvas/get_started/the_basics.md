---
nav_title: Noções básicas sobre canvas
article_title: Noções básicas sobre canvas
page_order: 1
page_type: reference
description: "Este artigo de referência aborda os conceitos básicos do Canvas, incluindo várias perguntas que você deve fazer a si mesmo ao configurar seu primeiro Canvas."
tool: Canvas

---

# Noções básicas de canvas

> Este artigo de referência aborda os conceitos básicos do Canvas, incluindo várias perguntas que você deve fazer a si mesmo ao configurar seu primeiro Canvas. Também explicaremos os cinco Ws (o quê, quando, quem, por que e onde) da visualização e como isso pode moldar e definir como você pode criar seu Canva.

## Entendendo a estrutura do Canva

Antes de começarmos com os detalhes da [configuração do Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/), vamos identificar as partes principais que compõem um Canvas.

{% tabs %}
  {% tab Canvas %}
  O Canva é uma interface unificada na qual os profissionais de marketing criam campanhas com várias mensagens. É um pouco como uma ferramenta de programação visual, que lhe permite criar uma jornada de usuário coesa a partir de uma série de etapas.

  ![Um exemplo de um Canva com uma etapa de divisão de decisão em duas jornadas de usuário diferentes, dependendo da capacitação do usuário.]({% image_buster /assets/img/canvas_intro/canvas_intro.gif %})

  {% endtab %}

  {% tab Jornada %}

  Uma jornada, ou comumente chamada de jornada do usuário, é a experiência de um usuário individual dentro do Canva.<br><br> ![Um gráfico com a jornada do cliente para um novo usuário. Um usuário anônimo instala um aplicativo, Kat cria uma conta, Kat não abre o aplicativo por uma semana, uma notificação por push traz Kat de volta ao aplicativo e, em seguida, Kat usa o aplicativo regularmente.]({% image_buster /assets/img_archive/Journey_2.png %}){: style="max-width:90%;"}

  {% endtab %}

  {% tab Criador de canvas %}
  O construtor do Canvas mapeia as etapas a serem seguidas ao criar seu Canvas. Isso inclui noções básicas, como nomear o Canva e adicionar equipes. Essencialmente, o criador de canvas é a configuração crucial necessária antes de começar a criar seu canva. Aqui, é possível controlar a forma como os usuários iniciam e concluem a jornada do cliente com opções para editar o [cronograma de entrada]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2b-set-your-canvas-entry-schedule), [o público-alvo]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2c-set-your-target-entry-audience) e [as configurações de envio]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2d-select-your-send-settings).<br><br> ![O construtor do Canvas na seção Noções básicas para um Canvas chamado "Novo canva".]({% image_buster /assets/img_archive/canvas_flow_entry_wizard.png %}){: style="max-width:90%;"}

  {% endtab %}

  {% tab Variantes %}
  Uma variante é a jornada que cada cliente segue em sua jornada. O Canva suporta até oito variantes com um grupo de controle. Você controla qual segmento do seu público seguirá cada variante.<br><br> ![Selecionando o botão "Adicionar variante".]({% image_buster /assets/img/canvas_intro/add_canvas_variant.gif %})

  {% endtab %}

  {% tab Etapas %}
  Uma etapa do canva é um ponto de decisão de marketing: "se isso, então aquilo". Aproveite [os componentes do Canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/#about-canvas-components) para criar as etapas de uma jornada do usuário.<br><br> ![Exemplo de adição de uma etapa do canva.]({% image_buster /assets/img/canvas_intro/add_canvas_step.gif %}) <br><br> Quando um usuário entra em um Canva, ele começa na primeira etapa. Cada etapa tem condições que determinam se um usuário pode passar para a próxima etapa. Em uma etapa, você pode definir disparadores ou programar a entrega, refinar o direcionamento adicionando filtros ou marcando eventos de exceção e especificar diferentes canais, como notificações por push ou eventos de webhook. No Canva, as etapas ocorrem em uma sequência, o que significa que a primeira etapa ocorre antes que a segunda possa ocorrer. Digamos que tenhamos um Canvas com as seguintes etapas: Atrasar a etapa A com uma postergação de 24 horas, enviar a etapa A com uma mensagem push e enviar a etapa B com uma mensagem no app. O usuário A é mantido em uma postergação de 24 horas e, depois de 24 horas, receberá uma mensagem push e, em seguida, uma mensagem no app.

  {% endtab %}
{% endtabs %}

## Criação da jornada do cliente

O uso dos cinco Ws (o que, quando, quem, por que e onde) da visualização pode ajudar a identificar suas estratégias de engajamento do cliente para criar uma jornada de mensagens personalizada para cada um dos seus usuários.

### O "quê": Dê um nome à sua tela

> O que você está tentando ajudar o usuário a fazer ou entender?

Nunca subestime o poder do nome. O Braze foi criado para a colaboração, portanto, este é um bom momento para se preparar para a comunicação de metas com a sua equipe.

Você pode adicionar tags e nomear as etapas e variantes em um Canvas. Para saber mais sobre as jornadas dos clientes, confira nosso curso do Braze Learning sobre o [mapeamento dos ciclos de vida dos usuários](https://learning.braze.com/mapping-customer-lifecycles).

### O "porquê": Identificar eventos de conversão

> Com base no "o quê", por que você está criando esse Canva? 

É sempre importante ter uma meta definida em mente, e o Canva ajuda a entender como está o seu desempenho em relação aos KPIs, como engajamento em sessões, compras e eventos personalizados.

A seleção de pelo menos um [evento de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) lhe dará a capacidade de entender como otimizar a performance dentro do Canva. E se a sua tela tiver várias variantes ou um grupo de controle, o Braze usará o evento de conversão para determinar a melhor variação para atingir essa meta.

* **Iniciar sessão**: Quero que meus usuários voltem e se engajem com o app.
* **Fazer compra**: Quero que meus usuários comprem.
* **Executar evento personalizado**: Quero que meus usuários realizem uma ação específica que estou rastreando como um evento personalizado.
* **App de upgrades:** Quero que meus usuários façam upgrade da versão do app.

### O "quando": Criar condições iniciais

> Quando um usuário iniciará essa experiência?

Sua resposta determinará os detalhes de quando e como o Canva será entregue ao cliente. Os usuários podem entrar no seu Canva de duas maneiras: disparos programados ou baseados em ações.

{% alert tip %}
Dê uma olhada em [Funcionalidades baseadas em tempo]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/delivery_types/) para o Canva para obter mais estratégias e respostas a perguntas comuns.
{% endalert %}

A entrega programada permite que você envie um Canva imediatamente para seu público-alvo. Você também pode enviá-la regularmente ou programá-la para um momento específico no futuro. As telas baseadas em ações respondem a comportamentos específicos do cliente à medida que eles ocorrem. Por exemplo, um gatilho baseado em ação pode incluir a abertura de um app, a realização de uma compra, a interação com outra campanha ou o disparo de qualquer evento personalizado. No momento em que a ação ocorre, você pode fazer com que o Canva seja enviado aos seus usuários.

### O "quem": Selecionar um público

> Quem você está tentando alcançar? 

Para definir seu "quem", você pode usar segmentos predefinidos disponíveis no Canva. Você também pode adicionar mais filtros para se concentrar ainda mais na conexão com seu público-alvo. Depois de criar esses segmentos, somente os usuários que correspondem aos critérios do público-alvo podem entrar na jornada do Canva, o que leva a uma experiência mais personalizada. Consulte esta tabela para ver os filtros disponíveis e como eles segmentam seus usuários para se adequarem ao seu caso de uso.

| Filtrar              | Descrição                                                                                         |
|---------------------|-----------------------------------------------------------------------------------------------------|
| Dados personalizados         | Segmente os usuários com base em eventos e atribuições definidas por você. Pode usar recursos específicos de seu produto. |
| Atividade do usuário       | Segmentar os clientes com base em suas ações e compras.                                             |
| Redirecionamento         | Segmente os clientes que foram enviados, receberam ou interagiram com Canvas anteriores.               |
| Atividade de marketing  | Segmentar os clientes com base em comportamentos universais, como o último engajamento.                         |
| Atributos do usuário     | Segmentar os clientes por seus atributos e características constantes.                                 |
| Instalar atribuição | Segmente os clientes por sua primeira fonte, grupo de anúncios, campanha ou anúncio.                                 |

### O "onde": Encontrar meu público

> Onde posso alcançar melhor meu público? 

É aqui que determinamos quais canais de envio de mensagens fazem mais sentido para a jornada do usuário. O ideal é alcançar os usuários onde eles são mais acessíveis. Com isso em mente, você pode usar qualquer um dos seguintes canais com o canva:
* [E-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/about/)
* [Push]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/)
* [Mensagem no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/)
* [Cartões de conteúdo]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/)
* [SMS ou MMS]({{site.baseurl}}/about_sms/)
* [Webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/)

### O "como": Crie a experiência completa

> Como posso criar minha jornada do canva depois de identificar os cinco Ws?

O "como" resume coletivamente como você criará seu Canva e como alcançará seus usuários com sua mensagem. Por exemplo, para que uma mensagem seja eficaz, você deve otimizar o momento do envio de mensagens em relação aos fusos horários de seus diferentes usuários.

A resposta a "como" também determina a cadência de envio de um Canvas para seu público (por exemplo, uma vez por semana ou quinzenalmente) e quais canais de envio de mensagens devem ser usados para cada Canvas que você criar, conforme descrito em "onde".

## Caso de uso: Fluxo de integração do cliente

Por exemplo, digamos que você seja um profissional de marketing da MovieCanon, uma empresa de serviços de streaming on-line, e esteja encarregado de criar um fluxo de integração para novos usuários do seu app. Ao fazer referência aos cinco Ws, poderíamos criar o canva da seguinte maneira.

* **O que**: O nome de nosso canva será Nova jornada de integração.
* **Por que**: O objetivo do nosso Canva é dar as boas-vindas aos nossos usuários e fazer com que eles continuem se engajando no app.
* **Quando**: Depois que um usuário abre o app pela primeira vez, queremos enviar um e-mail de boas-vindas. 
* **Quem**: Estamos direcionando para novos usuários que estão usando nosso app pela primeira vez.
* **Onde**: Estamos confiantes de que podemos alcançar novos usuários por meio de seus e-mails, que é como fizemos todos os nossos envios de mensagens anteriores.
* **Como**: Queremos definir uma postergação de um dia para não sobrecarregar nossos novos usuários com notificações. Após essa postergação, enviaremos um e-mail com uma lista dos filmes e programas de TV mais populares para incentivá-los a continuar usando o app.

## Dicas gerais

### Determinar quando e como usar etapas e variantes

Cada Canva deve ter pelo menos uma variante e pelo menos uma etapa do canva. A partir daí, o céu é o limite - então, como você decide o formato de sua tela? É aqui que suas metas, dados e hipóteses entram em ação. O brainstorming de "como" e "onde" o ajudará a mapear a forma e a estrutura corretas do seu Canva.

### Trabalhar de trás para frente

Algumas metas têm submetas menores. Por exemplo, se o seu objetivo é converter um usuário gratuito em uma inscrição, talvez seja necessária uma página com os serviços de inscrição descritos. O visitante pode precisar ver as opções antes de comprar. Você pode concentrar seus esforços de envio de mensagens em mostrar a eles essa página antes de uma página de checkout. Acessar o passado para entender a jornada que um cliente deve percorrer para chegar ao seu objetivo é fundamental para orientá-lo até a conversão.

### Diversifique seu envio de mensagens

Você já realizou uma campanha semelhante no passado? Ou há algum em andamento? Tente usar essa única mensagem e adicionar mais personalização a ela. Experimente um novo filtro ou adicione uma mensagem de acompanhamento. Ao diversificar as técnicas de envio de mensagens, monitore sua performance e continue otimizando, fazendo alterações incrementais.
