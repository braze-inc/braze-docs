---
nav_title: Recomendações de itens
article_title: Recomendações de itens em Braze
page_order: 15
search_rank: 1
description: "Saiba tudo sobre os mecanismos de recomendação de itens no Braze."
---

# Recomendações de itens

> Aprimore seu jogo de recomendação com o Braze criando um mecanismo de recomendação que pode sugerir aos seus usuários itens e conteúdo que eles realmente desejam. Desde a personalização de experiências com IA até a criação de seus próprios mecanismos com Liquid ou Connected Content, você encontrará tudo o que precisa para fazer com que cada recomendação seja importante.

## Pré-requisitos

Antes de criar ou usar recomendações de itens no Braze, você precisará [criar pelo menos um catálogo - somente]({{site.baseurl}}/user_guide/data/activation/catalogs/create/)os itens desse catálogo serão recomendados aos usuários.

## Tipos e casos de uso

### IA personalizada {#ai}

Como parte do recurso de [recomendações de itens de IA]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/), as recomendações personalizadas de IA aproveitam o aprendizado profundo para prever o que seus usuários provavelmente terão interesse em seguida, com base no que eles demonstraram interesse no passado. Esse método fornece um sistema de recomendação dinâmico e personalizado que se adapta ao comportamento do usuário.

As recomendações personalizadas de IA usam os últimos 6 meses de dados de interação de itens, como compras ou eventos personalizados, para criar o modelo de recomendação. Para os usuários que não têm dados suficientes para uma lista personalizada, os itens mais populares servem como um recurso para que seus usuários ainda recebam sugestões relevantes.

Com as recomendações de itens de IA, você também pode filtrar ainda mais os itens disponíveis com
[seleções]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/). No entanto, as seleções com Liquid não podem ser usadas em recomendações de IA, portanto, lembre-se disso ao criar suas seleções de catálogo.

{% alert tip %}
As recomendações personalizadas por IA funcionam melhor com centenas ou milhares de itens e, normalmente, com pelo menos 30.000 usuários com dados de compra ou interação. Esse é apenas um guia aproximado e pode variar. Os outros tipos de recomendação podem trabalhar com menos dados.
{% endalert %}

#### Casos de uso

Com base nos dados de interação que estão sendo rastreados, os casos de uso desse modelo podem incluir:

{% tabs local %}
{% tab Most likely to purchase next %}
Preveja e recomende os itens que um usuário provavelmente comprará em seguida, com base em eventos de compra ou eventos personalizados relacionados a compras. Por exemplo:

- Um site de viagens poderia sugerir pacotes de férias, voos ou estadias em hotéis com base no histórico de navegação e nas reservas anteriores de um usuário, antecipando seu próximo destino de viagem e facilitando o planejamento da viagem.
- Uma plataforma de streaming pode analisar os hábitos de visualização para recomendar programas ou filmes que um usuário provavelmente assistirá em seguida, mantendo-o envolvido e reduzindo as taxas de rotatividade.

{% details Requirements %}
- Recomendações de itens de IA
- Catálogo de itens relevantes
- Um método para rastrear compras, seja um objeto de compra ou um evento personalizado
{% enddetails %}

{% details Setting it up %}
1. Criar uma [recomendação de item de IA]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Defina o **Tipo** como **AI Personalizado**.
3. Selecione seu catálogo.
4. (Opcional) Adicione uma seleção para filtrar sua recomendação para apenas itens relevantes.
5. Escolha como você rastreia atualmente os eventos de compra e a propriedade de evento correspondente.
6. Treine a recomendação.
7. [Use a recomendação nas mensagens]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}
{% endtab %}
{% endtabs %}

### Item mais popular {#most-popular}

O modelo de recomendação "Mais popular" apresenta itens com os quais os usuários mais se envolvem.

#### Casos de uso

Com base nos dados de interação que estão sendo rastreados, os casos de uso desse modelo podem incluir recomendações:

{% tabs local %}
{% tab most popular %}
Incentive os usuários a explorar itens populares em seu catálogo com base nas compras. Para garantir que apenas o conteúdo relevante seja exibido, recomendamos filtrar com uma seleção. Por exemplo, um serviço de entrega de alimentos poderia destacar os pratos ou restaurantes mais bem avaliados na área de um usuário, com base na popularidade dos pedidos na plataforma, incentivando a experimentação e a descoberta.

{% details Requirements %}
- Recomendações de itens de IA
- Catálogo de itens relevantes
- Um objeto de compra ou qualquer evento personalizado
{% enddetails %}

{% details Setting it up %}
1. Criar uma [recomendação de item de IA]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Defina o **Tipo** como **Mais popular**.
3. Selecione seu catálogo.
4. (Opcional) Adicione uma seleção para filtrar sua recomendação para apenas itens relevantes. Por exemplo, o serviço de entrega de comida pode ter uma seleção para filtrar a localização do restaurante ou o tipo de prato.
5. Escolha como você rastreia atualmente os eventos e a propriedade de evento correspondente.
6. Treine a recomendação.
7. [Use a recomendação nas mensagens]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}
{% endtab %}

{% tab most liked %}
Incentive os usuários a explorar itens que eles gostaram recentemente ou itens que são popularmente apreciados, com base em um evento personalizado para curtidas. Por exemplo, um aplicativo de streaming de música poderia criar listas de reprodução personalizadas ou sugerir lançamentos de novos álbuns com base nos gêneros ou artistas que um usuário gostou no passado, aumentando o envolvimento do usuário e o tempo gasto no aplicativo.

{% details Requirements %}
- Recomendações de itens de IA
- Catálogo de itens relevantes
- Evento personalizado para curtidas
{% enddetails %}

{% details Setting it up %}
1. Criar uma [recomendação de item de IA]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Defina o **Tipo** como **Mais recente**.
3. Selecione seu catálogo.
4. (Opcional) Adicione uma seleção para filtrar sua recomendação para apenas itens relevantes.
5. Escolha **Custom Event (Evento personalizado** ) e selecione seu evento personalizado para curtidas na lista.
6. Treine a recomendação.
7. [Use a recomendação nas mensagens]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}
{% endtab %}

{% tab most viewed %}
Destaque os itens que ganharam atenção em sua base de usuários por meio de visualizações para incentivar o envolvimento ou as compras. Por exemplo, um site de imóveis poderia exibir as listagens mais visualizadas na área de pesquisa de um usuário para destacar as propriedades que estão atraindo muita atenção, o que pode indicar bons negócios ou locais desejáveis.

{% details Requirements %}
- Recomendações de itens de IA
- Catálogo de itens relevantes
- Evento personalizado para exibições
{% enddetails %}

{% details Setting it up %}
1. Criar uma [recomendação de item de IA]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Defina o **Tipo** como **Mais popular**.
3. Selecione seu catálogo.
4. (Opcional) Adicione uma seleção para filtrar sua recomendação para apenas itens relevantes.
5. Escolha **Custom Event** e selecione seu evento personalizado para visualizações na lista.
6. Treine a recomendação.
7. [Use a recomendação nas mensagens]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}
{% endtab %}

{% tab popular in cart %}
Exiba itens que são adicionados aos carrinhos por muitos outros compradores, proporcionando aos usuários uma visão das tendências atuais entre suas ofertas.

Por exemplo, um varejista de moda poderia promover roupas e acessórios que são tendência com base em adições populares aos carrinhos de outros clientes. Em seguida, eles podem criar uma seção dinâmica "Trending Now" em sua página inicial e no aplicativo móvel, que é atualizada em tempo real para incentivar os compradores a comprar antes que os itens se esgotem.

{% details Requirements %}
- Recomendações de itens de IA
- Catálogo de itens relevantes
- Evento personalizado para adicionar ao carrinho
{% enddetails %}

{% details Setting it up %}
1. Criar uma [recomendação de item de IA]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Defina o **Tipo** como **Mais popular**.
3. Selecione seu catálogo.
4. (Opcional) Adicione uma seleção para filtrar sua recomendação para apenas itens relevantes.
5. Escolha **Custom Event (Evento personalizado** ) e selecione na lista o evento personalizado a ser adicionado ao carrinho.
6. Treine a recomendação.
7. [Use a recomendação nas mensagens]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}
{% endtab %}
{% endtabs %}

### Item mais recente {#most-recent}

O modelo de recomendação "Mais recente" apresenta itens com os quais os usuários mais se envolvem. Use esse modelo para reduzir a rotatividade, incentivando os usuários inativos a se envolverem novamente com o conteúdo relevante.

#### Casos de uso

Com base nos dados de interação que estão sendo rastreados, os casos de uso desse modelo podem incluir recomendações:

{% tabs local %}
{% tab Recently clicked %}
Incentive os usuários a revisitar os itens em que clicaram recentemente, com base em um evento personalizado para cliques. Por exemplo, um varejista de moda on-line poderia criar uma recomendação para enviar e-mails de acompanhamento ou notificações push com roupas pelas quais um usuário demonstrou interesse ao clicar nelas, incentivando o usuário a revisitar o item e fazer uma compra.

{% details Requirements %}
- Recomendações de itens de IA
- Catálogo de itens relevantes
- Evento personalizado para cliques
{% enddetails %}

{% details Setting it up %}
1. Criar uma [recomendação de item de IA]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Defina o **Tipo** como **Mais recente**.
3. Selecione seu catálogo.
4. (Opcional) Adicione uma seleção para filtrar sua recomendação para apenas itens relevantes.
5. Escolha **Custom Event** e selecione seu evento personalizado para cliques na lista.
6. Treine a recomendação.
7. [Use a recomendação nas mensagens]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}

{% endtab %}
{% tab Recently liked %}
Incentive os usuários a explorar itens que eles gostaram recentemente ou itens que são popularmente apreciados, com base em um evento personalizado para curtidas. Por exemplo, um aplicativo de streaming de música poderia criar listas de reprodução personalizadas ou sugerir lançamentos de novos álbuns com base nos gêneros ou artistas que um usuário gostou no passado, aumentando o envolvimento do usuário e o tempo gasto no aplicativo.

{% details Requirements %}
- Recomendações de itens de IA
- Catálogo de itens relevantes
- Evento personalizado para curtidas
{% enddetails %}

{% details Setting it up %}
1. Criar uma [recomendação de item de IA]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Defina o **Tipo** como **Mais recente**.
3. Selecione seu catálogo.
4. (Opcional) Adicione uma seleção para filtrar sua recomendação para apenas itens relevantes.
5. Escolha **Custom Event (Evento personalizado** ) e selecione seu evento personalizado para curtidas na lista.
6. Treine a recomendação.
7. [Use a recomendação nas mensagens]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}
{% endtab %}

{% tab Recently engaged %}
Promova itens com os quais os usuários interagiram recentemente, incluindo visualizações, cliques ou compras. Essa abordagem mantém suas recomendações atualizadas e alinhadas com os interesses mais recentes do usuário. Por exemplo:

- **Educação:** Uma plataforma de educação on-line pode incentivar os usuários que assistiram recentemente a um vídeo educativo, mas não se inscreveram em um curso, a conferir cursos semelhantes ou assuntos de interesse para manter o usuário envolvido e motivado a começar a aprender.
- **Fitness:** Um aplicativo de condicionamento físico pode sugerir exercícios ou desafios semelhantes aos que o usuário concluiu recentemente ou com os quais interagiu, mantendo sua rotina de exercícios variada e envolvente.
- **Varejista de artigos de decoração:** Depois que um cliente adquire uma ferramenta elétrica, um varejista de reforma residencial pode recomendar acessórios relacionados ou equipamentos de segurança com base na compra recente, aprimorando a experiência e a segurança do usuário.

{% details Requirements %}
- Recomendações de itens de IA
- Catálogo de itens relevantes
- Um objeto de compra ou qualquer evento personalizado para uma interação de engajamento
{% enddetails %}

{% details Setting it up %}
1. Criar uma [recomendação de item de IA]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Defina o **Tipo** como **Mais recente**.
3. Selecione seu catálogo.
4. (Opcional) Adicione uma seleção para filtrar sua recomendação para apenas itens relevantes.
5. Escolha **Custom Event** e selecione seu evento personalizado para cliques na lista.
6. Treine a recomendação.
7. [Use a recomendação nas mensagens]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}
{% endtab %}

{% tab Recently added %}
Lembre os usuários de seu interesse em itens que eles adicionaram recentemente ao carrinho, mas que ainda não compraram. Por exemplo, um varejista on-line poderia enviar lembretes ou oferecer descontos por tempo limitado nos itens do carrinho, incentivando os usuários a concluir suas compras antes que as ofertas expirem.
{% details Requirements %}

- Recomendações de itens de IA
- Catálogo de itens relevantes
- Evento personalizado para adicionar ao carrinho
{% enddetails %}

{% details Setting it up %}
1. Criar uma [recomendação de item de IA]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Defina o **Tipo** como **Mais recente**.
3. Selecione seu catálogo.
4. (Opcional) Adicione uma seleção para filtrar sua recomendação para apenas itens relevantes.
5. Escolha **Custom Event (Evento personalizado** ) e selecione na lista o evento personalizado a ser adicionado ao carrinho.
6. Treine a recomendação.
7. [Use a recomendação nas mensagens]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}
{% endtab %}
{% endtabs %}

### Item de tendência {#trending}

O modelo de recomendação "Trending" (Tendências) apresenta itens que mostraram o impulso mais positivo em interações recentes do usuário. Calculamos isso usando uma análise ponderada de aproximadamente 10 semanas de histórico de eventos, com a maior ponderação aplicada às duas semanas mais recentes, aproximadamente. Para evitar que pequenas flutuações afetem a qualidade da recomendação, aplicamos um limite de atividade e técnicas de suavização estatística.

Ao contrário do modelo "Mais popular", que apresenta itens com interação consistentemente alta, esse modelo apresenta itens que sofreram um aumento nas interações. Você pode usá-lo para recomendar produtos que estão em ascensão e que estão tendo maior tração no momento.

#### Casos de uso

Com base nos dados de interação que estão sendo rastreados, os casos de uso desse modelo podem incluir recomendações:

{% tabs local %}
{% tab Trending purchased %}
Destaque os itens que seus usuários compraram recentemente com maior frequência. Por exemplo, uma empresa de comércio eletrônico poderia recomendar itens sazonais que os usuários estão começando a estocar durante os preparativos para a próxima estação. 

{% details Requirements %}
- Recomendações de itens de IA
- Catálogo de itens relevantes
- Um método para rastrear compras (um objeto de compra ou um evento personalizado)
{% enddetails %}

{% details Setting it up %}
1. Criar uma [recomendação de item de IA]({{site.baseurl}}/ai_item_recommendations/).
2. Defina o **Tipo** como **Tendência**.
3. Selecione seu catálogo.
4. (Opcional) Adicione uma seleção para filtrar sua recomendação para apenas itens relevantes.
5. Escolha um evento de compra ou um evento personalizado que rastreie compras, juntamente com a propriedade correspondente.
6. Treine a recomendação.
7. [Use a recomendação nas mensagens.]({{site.baseurl}}/user_guide/sage_ai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging)
{% enddetails %}
{% endtab %}

{% tab Trending liked %}
Destaque itens que seus usuários gostaram recentemente com maior frequência. Por exemplo, um aplicativo de música poderia apresentar artistas promissores que tiveram um aumento recente nas curtidas dos usuários.

{% details Requirements %}
- Recomendações de itens de IA
- Catálogo de itens relevantes
- Evento personalizado para rastrear curtidas
{% enddetails %}

{% details Setting it up %}
1. Criar uma [recomendação de item de IA]({{site.baseurl}}/ai_item_recommendations/).
2. Defina o **Tipo** como **Tendência**.
3. Selecione seu catálogo.
4. (Opcional) Adicione uma seleção para filtrar sua recomendação para apenas itens relevantes.
5. Escolha seu evento personalizado para rastrear curtidas, juntamente com a propriedade correspondente.
6. Treine a recomendação.
7. [Use a recomendação nas mensagens.]({{site.baseurl}}/user_guide/sage_ai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging/)
{% enddetails %}
{% endtab %}
{% endtabs %}

### Baseado em seleções {#selections-based}

[As seleções]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) são grupos específicos de dados de catálogo. Ao usar uma seleção, você está basicamente configurando filtros personalizados com base em colunas específicas do seu catálogo. Isso pode incluir filtros para marca, tamanho, local, data de adição e muito mais. Ele lhe dá controle sobre o que está recomendando, permitindo que você defina os critérios que os itens devem atender para serem mostrados aos usuários.

Os três tipos anteriores envolvem a configuração e o treinamento de um modelo de recomendação no Braze. Embora também seja possível usar seleções nesses modelos, você também pode realizar alguns casos de uso de recomendação apenas com seleções de catálogo e personalização do Liquid.

#### Casos de uso

Com base nos dados de interação que estão sendo rastreados, os casos de uso desse modelo podem incluir recomendações:

{% tabs local %}
{% tab New items %}
Esse cenário não depende diretamente das ações do usuário, mas sim dos dados do catálogo. Você pode filtrar novos itens com base na data de adição ao catálogo e promovê-los por meio de campanhas direcionadas ou Canvases sem a necessidade de treinar um modelo de recomendação.

Por exemplo, uma plataforma de comércio eletrônico de tecnologia poderia alertar os entusiastas da tecnologia sobre os gadgets mais recentes ou sobre as próximas pré-encomendas, usando filtros para direcionar os itens que foram adicionados recentemente ao catálogo.

{% details Requirements %}
- Catálogo de itens relevantes com um campo para data adicionada
{% enddetails %}

{% details Setting it up %}
1. Crie uma seleção com base em seu catálogo. Certifique-se de que seu catálogo tenha um campo de tempo (campo com um **tipo de dados** definido como **Tempo**) que corresponda à data em que o item foi adicionado.
2. (Opcional) Adicione filtros, se desejar.
3. Certifique-se de que a opção **Randomize Sort Order** esteja desativada.
4. Em **Sort Field (Campo de classificação**), selecione o campo de data adicionada.
5. Defina **Sort Order** como descendente.
6. [Use a seleção em mensagens]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/#using-selections-in-messaging).
{% enddetails %}
{% endtab %}

{% tab Random items %}
Para uma experiência diversificada do usuário, a recomendação de itens aleatórios pode introduzir variedade e potencialmente despertar o interesse em áreas menos visitadas do catálogo. Esse método não exige modelos ou eventos específicos, mas usa uma seleção de catálogo para garantir que os itens sejam exibidos aleatoriamente.

Por exemplo, uma livraria on-line poderia oferecer o recurso "Surpreenda-me", recomendando um livro aleatório com base nas compras anteriores ou nos hábitos de navegação do usuário, incentivando a exploração fora dos gêneros de leitura habituais.

{% details Requirements %}
- Catálogo de itens relevantes
- Seleção com a opção **Randomize Sort Order** ativada
{% enddetails %}

{% details Setting it up %}
1. [Crie uma seleção]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/#creating-a-selection) com base em seu catálogo.
2. (Opcional) Adicione filtros, se desejar.
3. Ative a opção **Randomize Sort Order**.
4. [Use a seleção em mensagens]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/#using-selections-in-messaging).
{% enddetails %}
{% endtab %}
{% endtabs %}

### Baseado em regras {#rules-based}

Um mecanismo de [recomendação baseado em regras]({{site.baseurl}}/rules_based_recommendations/) usa dados do usuário e informações do produto para sugerir itens relevantes aos usuários nas mensagens. Ele usa o Liquid e os catálogos Braze ou o Connected Content para personalizar dinamicamente o conteúdo com base no comportamento e nos atributos do usuário.

As recomendações baseadas em regras são baseadas em uma lógica fixa que você deve definir manualmente. Isso significa que suas recomendações não se ajustarão ao histórico de compras e aos gostos individuais de um usuário, a menos que você atualize a lógica; portanto, esse método é melhor para recomendações que não precisam de atualizações frequentes.

#### Casos de uso

Com base nos dados de interação que estão sendo rastreados, os casos de uso desse modelo podem incluir:

- **Lembretes de reabastecimento:** Enviar lembretes de reabastecimento para itens com um ciclo de uso previsível, como vitaminas mensais ou mantimentos semanais, com base na última data de compra.
- **Compradores de primeira viagem:** Recomendar kits iniciais ou ofertas introdutórias aos compradores de primeira viagem para incentivar uma segunda compra.
Programas de fidelidade: Destaque os produtos que maximizariam os pontos de fidelidade ou as recompensas do cliente com base em seu saldo de pontos atual.
- **Conteúdo educacional:** Sugerir novos cursos ou conteúdos com base nos tópicos de materiais consumidos ou comprados anteriormente.

{% multi_lang_include brazeai/recommendations/ai.md section="Plan-specific features" %}

## Perguntas frequentes {#faq}

### O que faz com que os itens "Mais populares" sejam misturados às recomendações de outros modelos?

Quando nosso mecanismo de recomendação seleciona uma lista para você, ele primeiro prioriza as seleções personalizadas com base no modelo específico que você escolheu, como "Mais recente" ou "Personalizado por IA". Se esse modelo não puder preencher a lista completa de 30 recomendações por qualquer motivo, alguns dos itens mais populares entre todos os usuários serão adicionados para garantir que cada usuário sempre tenha um conjunto completo de recomendações.

Isso acontece em algumas condições específicas:

- O modelo encontra menos de 30 itens que correspondem aos seus critérios.
- Os itens relevantes não estão mais disponíveis ou em estoque.
- Os itens não atendem aos critérios de seleção atuais, talvez devido a uma alteração no estoque ou nas preferências do usuário.

### As recomendações existentes são treinadas semanalmente após a atualização para o Item Recommendations Pro?

Sim, mas somente após a próxima atualização programada. As recomendações existentes não mudam para treinamento semanal e previsão diária imediatamente após a atualização para o Item Recommendations Pro. No entanto, eles adotarão o novo cronograma automaticamente em seu próximo ciclo de retreinamento. Por exemplo, se uma recomendação foi treinada pela última vez em 1º de fevereiro e está definida para ser treinada novamente a cada 30 dias, ela adotará a nova programação semanal após a próxima atualização em 2 de março.