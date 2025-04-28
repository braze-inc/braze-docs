---
nav_title: Sobre as recomendações de itens
article_title: Sobre as recomendações de itens
description: "Este artigo de referência descreve diferentes casos de uso para recomendar itens aos clientes usando a Braze."
page_order: 1
---

# Sobre as recomendações de itens

Neste artigo, você aprenderá sobre as diferentes maneiras de sugerir itens nos quais seus clientes estão interessados e se inspirará em casos de uso comuns para criar mecanismos de recomendação usando o Braze.

## Pré-requisitos

Todos os tipos de recomendação exigem que você tenha pelo menos um [catálogo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/) configurado, pois é dele que os itens recomendados são extraídos.

## Tipos de recomendações

Ao se preparar para recomendar itens aos seus clientes, há algumas abordagens que você pode adotar:

- [Personalizada por IA](#ai)
- [Mais popular](#most-popular)
- [Mais recente](#most-recent)
- [Baseado em seleções](#selections-based)
- [Baseado em regras](#rules-based)
- [Tendências](#trending)

### IA Recomendações personalizadas {#ai}

Como parte do recurso de [recomendações de itens de IA][1], as recomendações personalizadas de IA aproveitam o deep learning para prever o que seus usuários provavelmente terão interesse em seguida, com base no que eles demonstraram interesse no passado. Esse método fornece um sistema de recomendação dinâmico e personalizado que se adapta ao comportamento do usuário.

As recomendações personalizadas de IA usam os últimos 6 meses de dados de interação do item, como compras ou eventos personalizados, para criar o modelo de recomendação. Para usuários sem dados suficientes para uma lista personalizada, os itens mais populares servem como fallback para que seus usuários ainda recebam sugestões relevantes.

Com as recomendações de itens de IA, você também pode filtrar ainda mais os itens disponíveis com
[seleções]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/). No entanto, as seleções com Liquid não podem ser usadas em recomendações de IA, portanto, lembre-se disso ao criar suas seleções de catálogo.

Para obter exemplos, consulte a seção [Casos de uso](#use-cases) deste artigo.

{% alert tip %}
As recomendações personalizadas por IA funcionam melhor com centenas ou milhares de itens e, normalmente, com pelo menos 30.000 usuários com dados de compra ou interação. Esse é apenas um guia aproximado e pode variar. Os outros tipos de recomendação podem trabalhar com menos dados.
{% endalert %}

### Recomendações de itens mais populares {#most-popular}

Além do modelo "Personalizado por IA", o recurso de [recomendações de itens por IA][1] também inclui um modelo de recomendação para "Mais populares", que apresenta itens com os quais os usuários mais se engajam.

Com base nos dados de interação que estão sendo rastreados, os casos de uso desse modelo podem incluir recomendações:

- [Itens mais populares](#most-popular-items)
- [Itens preferidos mais populares](#liked-items)
- [Itens mais vistos](#most-viewed-items)
- [Itens populares nos carrinhos dos usuários](#popular-items-in-users-carts)

### Recomendações de itens mais recentes {#most-recent}

Além do modelo "IA Personalizado", o recurso de [recomendações de itens de IA][1] também inclui um modelo de recomendação para "Mais recentes", que apresenta itens com os quais os usuários mais se engajam. Use esse modelo para reduzir o churn, incentivando os usuários desistentes a se engajarem novamente com o conteúdo relevante.

Com base nos dados de interação que estão sendo rastreados, os casos de uso desse modelo podem incluir recomendações:

- [Itens clicados recentemente](#recently-clicked-items)
- [Itens curtidos recentemente](#liked-items)
- [Engajamento recente ou compra de itens](#recently-engaged-with-or-purchased-items)
- [Itens adicionados recentemente ao carrinho](#items-recently-added-to-cart)

### Recomendações de itens em alta {#trending}

Além do modelo "IA Personalizado", o recurso de [recomendações de itens de IA][1] também inclui um modelo de recomendação para "Tendências", que apresenta itens que tiveram o impulso mais positivo quando se trata de interações recentes do usuário. 

Ao contrário do modelo "Mais popular", que apresenta itens com interação consistentemente alta, esse modelo apresenta itens que sofreram um aumento nas interações. Você pode usá-lo para recomendar produtos que estão em ascensão e que estão ganhando força no momento.

Com base nos dados de interação que estão sendo rastreados, os casos de uso desse modelo podem incluir recomendações:

- [Tendência de itens comprados](#trending-purchased-items)
- [Itens favoritos em alta](#trending-liked-items)

### Recomendações baseadas em seleções {#selections-based}

[As seleções]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/) são grupos específicos de dados de catálogo. Ao usar uma seleção, você está basicamente configurando filtros personalizados com base em colunas específicas do seu catálogo. Isso pode incluir filtros por marca, tamanho, local, data de adição e muito mais. Ele lhe dá controle sobre o que está recomendando, permitindo que você defina os critérios que os itens devem atender para serem mostrados aos usuários.

Os três tipos anteriores envolvem a configuração e o treinamento de um modelo de recomendação na Braze. Embora também seja possível usar seleções nesses modelos, também é possível realizar alguns casos de uso de recomendação apenas com seleções de catálogo e personalização Liquid.

Alguns casos de uso incluem recomendações:

- [Novos itens](#new-items)
- [Itens aleatórios](#random-items)

### Recomendações baseadas em regras {#rules-based}

Um mecanismo de [recomendação baseado em regras]({{site.baseurl}}/rules_based_recommendations/) usa dados de usuários e informações de produtos para sugerir itens relevantes aos usuários dentro das mensagens. Ele usa o Liquid e os catálogos do Braze ou o Connected Content para personalizar dinamicamente o conteúdo com base no comportamento e nas atribuições do usuário.

As recomendações baseadas em regras são baseadas em uma lógica fixa que você deve definir manualmente. Isso significa que suas recomendações não se ajustarão ao histórico de compras e aos gostos individuais de um usuário, a menos que você atualize a lógica; portanto, esse método é melhor para recomendações que não precisam de atualizações frequentes.

Alguns casos de uso incluem:

- **Lembretes de reabastecimento:** Enviar lembretes de reabastecimento para itens com um ciclo de uso previsível, como vitaminas mensais ou mantimentos semanais, com base na data da última compra.
- **Compradores de primeira viagem:** Recomendar kits iniciais ou ofertas introdutórias aos compradores de primeira viagem para incentivar uma segunda compra.
Programas de fidelidade: Destaque os produtos que maximizariam os pontos de fidelidade ou as recompensas de um cliente com base em seu saldo de pontos atual.
- **Conteúdo educacional:** Sugerir novos cursos ou conteúdos com base nos tópicos de materiais consumidos ou comprados anteriormente.

## Casos de uso

### Itens que um usuário tem maior probabilidade de comprar em seguida

Preveja e recomende os itens que um usuário provavelmente comprará em seguida, com base em eventos de compra ou eventos personalizados relacionados a compras. Por exemplo:

- Um site de viagens poderia sugerir pacotes de férias, voos ou estadias em hotéis com base no histórico de navegação e nas reservas anteriores de um usuário, antecipando seu próximo destino de viagem e facilitando o planejamento da viagem.
- Uma plataforma de streaming pode analisar os hábitos de visualização para recomendar programas ou filmes que um usuário provavelmente assistirá em seguida, mantendo-o engajado e reduzindo as taxas de churn.

{% details Requisitos %}

- Recomendações de itens de IA
- Catálogo de itens relevantes
- Um método para rastreamento de compras, seja um objeto de compra ou um evento personalizado

{% enddetails %}

{% details Como configurar %}

1. Criar uma [recomendação de item de IA]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/).
2. Defina o **Tipo** como **IA Personalizado**.
3. Selecione seu catálogo.
4. (Opcional) Adicione uma seleção para filtrar sua recomendação para apenas itens relevantes.
5. Escolha como você rastreia atualmente os eventos de compra e a propriedade de evento correspondente.
6. Treine a recomendação.
7. [Use a recomendação no envio de mensagens]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).

{% enddetails %}

### Itens adicionados recentemente ao carrinho

Lembre os usuários de seu interesse em itens que eles adicionaram recentemente ao carrinho, mas que ainda não compraram. Por exemplo, um varejista on-line poderia enviar lembretes ou oferecer descontos por tempo limitado nos itens do carrinho, incentivando os usuários a concluir suas compras antes que as ofertas expirem.

{% details Requisitos %}

- Recomendações de itens de IA
- Catálogo de itens relevantes
- Evento personalizado para adicionar ao carrinho

{% enddetails %}

{% details Como configurar %}

1. Criar uma [recomendação de item de IA]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/).
2. Defina o **Tipo** como **Mais recente**.
3. Selecione seu catálogo.
4. (Opcional) Adicione uma seleção para filtrar sua recomendação para apenas itens relevantes.
5. Escolha **Custom Event (Evento personalizado** ) e selecione na lista o evento personalizado a ser adicionado ao carrinho.
6. Treine a recomendação.
7. [Use a recomendação no envio de mensagens]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).

{% enddetails %}

### Itens apreciados

Incentive os usuários a explorar itens que eles gostaram recentemente ou itens que são popularmente apreciados, com base em um evento personalizado para curtidas. Por exemplo, um aplicativo de streaming de música poderia criar listas de reprodução personalizadas ou sugerir lançamentos de novos álbuns com base nos gêneros ou artistas que um usuário gostou no passado, aumentando o engajamento do usuário e o tempo gasto no app.

{% details Requisitos %}

- Recomendações de itens de IA
- Catálogo de itens relevantes
- Evento personalizado para curtidas

{% enddetails %}

{% details Como configurar %}

1. Criar uma [recomendação de item de IA]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/).
2. Defina o **Tipo** como **Mais recente**.
3. Selecione seu catálogo.
4. (Opcional) Adicione uma seleção para filtrar sua recomendação para apenas itens relevantes.
5. Escolha **Custom Event (Evento personalizado** ) e selecione seu evento personalizado para curtidas na lista.
6. Treine a recomendação.
7. [Use a recomendação no envio de mensagens]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).

{% enddetails %}

### Itens mais populares

Incentive os usuários a explorar itens populares em seu catálogo com base nas compras. Para garantir que apenas o conteúdo relevante seja exibido, recomendamos filtrar com uma seleção. Por exemplo, um serviço de entrega de comida poderia destacar os pratos ou restaurantes mais bem avaliados na área de um usuário, com base na popularidade dos pedidos na plataforma, incentivando a experimentação e a descoberta.

{% details Requisitos %}

- Recomendações de itens de IA
- Catálogo de itens relevantes
- Um objeto de compra ou qualquer evento personalizado

{% enddetails %}

{% details Como configurar %}

1. Criar uma [recomendação de item de IA]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/).
2. Defina o **Tipo** como **Mais popular**.
3. Selecione seu catálogo.
4. (Opcional) Adicione uma seleção para filtrar sua recomendação para apenas itens relevantes. Por exemplo, o serviço de entrega de comida pode ter uma seleção para filtrar o local do restaurante ou o tipo de prato.
5. Escolha como você rastreia eventos atualmente e a propriedade de evento correspondente.
6. Treine a recomendação.
7. [Use a recomendação no envio de mensagens]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).

{% enddetails %}

### Itens mais vistos

Destaque os itens que ganharam atenção em sua base de usuários por meio de visualizações para incentivar o engajamento ou as compras. Por exemplo, um site imobiliário poderia exibir as listagens mais visualizadas na área de pesquisa de um usuário para destacar as propriedades que estão atraindo muita atenção, indicando, potencialmente, bons negócios ou locais desejáveis.

{% details Requisitos %}

- Recomendações de itens de IA
- Catálogo de itens relevantes
- Evento personalizado para exibições

{% enddetails %}

{% details Como configurar %}

1. Criar uma [recomendação de item de IA]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/).
2. Defina o **Tipo** como **Mais popular**.
3. Selecione seu catálogo.
4. (Opcional) Adicione uma seleção para filtrar sua recomendação para apenas itens relevantes.
5. Escolha **Custom Event (Evento personalizado** ) e selecione seu evento personalizado para visualizações na lista.
6. Treine a recomendação.
7. [Use a recomendação no envio de mensagens]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).

{% enddetails %}

### Novos itens

Esse cenário não depende diretamente das ações do usuário, mas sim dos dados do catálogo. É possível filtrar novos itens com base na data de adição ao catálogo e promovê-los por meio de campanhas direcionadas ou Canvas sem a necessidade de treinar um modelo de recomendação.

Por exemplo, uma plataforma de comércio eletrônico de tecnologia poderia alertar os entusiastas da tecnologia sobre os mais recentes gadgets ou as próximas pré-encomendas, usando filtros para direcionamento de itens que foram adicionados recentemente ao catálogo.

{% details Requisitos %}

- Catálogo de itens relevantes com um campo para data adicionada

{% enddetails %}

{% details Como configurar %}

1. Crie uma seleção com base em seu catálogo. Certifique-se de que seu catálogo tenha um campo de tempo (campo com um **tipo de dados** definido como **Tempo**) que corresponda à data em que o item foi adicionado.
2. (Opcional) Adicione filtros, se desejar.
3. Certifique-se de que a opção **Randomize Sort Order** esteja desativada.
4. Em **Sort Field (Campo de classificação**), selecione o campo de data adicionada.
5. Defina **Sort Order (Ordem de classificação** ) como descendente.
6. [Use a seleção no envio de mensagens]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/#using-selections-in-messaging).

{% enddetails %}

### Itens populares nos carrinhos dos usuários

Exiba itens que são adicionados aos carrinhos por muitos outros compradores, fornecendo aos usuários um vislumbre das tendências atuais entre suas ofertas.

Por exemplo, um varejista de moda poderia promover roupas e acessórios que são tendência com base em adições populares aos carrinhos de outros clientes. Em seguida, eles podem criar uma seção dinâmica "Trending Now" em sua página inicial e no app para dispositivos móveis, que é atualizada em tempo real para incentivar os compradores a comprar antes que os itens se esgotem.

{% details Requisitos %}

- Recomendações de itens de IA
- Catálogo de itens relevantes
- Evento personalizado para adicionar ao carrinho

{% enddetails %}

{% details Como configurar %}

1. Criar uma [recomendação de item de IA]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/).
2. Defina o **Tipo** como **Mais popular**.
3. Selecione seu catálogo.
4. (Opcional) Adicione uma seleção para filtrar sua recomendação para apenas itens relevantes.
5. Escolha **Custom Event (Evento personalizado** ) e selecione na lista o evento personalizado a ser adicionado ao carrinho.
6. Treine a recomendação.
7. [Use a recomendação no envio de mensagens]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).

{% enddetails %}

### Itens aleatórios

Para uma experiência diversificada do usuário, a recomendação de itens aleatórios pode introduzir variedade e potencialmente despertar o interesse em áreas menos visitadas do catálogo. Esse método não requer modelos ou eventos específicos, mas usa uma seleção de catálogo para garantir que os itens sejam exibidos aleatoriamente.

Por exemplo, uma livraria on-line poderia oferecer o recurso "Surprise Me" (Surpreenda-me), recomendando um livro aleatório com base nas compras anteriores ou nos hábitos de navegação do usuário, incentivando a exploração fora dos gêneros de leitura habituais.

{% details Requisitos %}

- Catálogo de itens relevantes
- Seleção com a opção **Randomize Sort Order** ativada

{% enddetails %}

{% details Como configurar %}

1. [Crie uma seleção]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/#creating-a-selection) com base em seu catálogo.
2. (Opcional) Adicione filtros, se desejar.
3. Ative a opção **Tornar classificação aleatória**.
4. [Use a seleção no envio de mensagens]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/#using-selections-in-messaging).

{% enddetails %}

### Itens clicados recentemente

Incentive os usuários a revisitar os itens em que clicaram recentemente, com base em um evento personalizado para cliques. Por exemplo, um varejista de moda on-line poderia criar uma recomendação para enviar e-mails de acompanhamento ou notificações por push com roupas pelas quais um usuário demonstrou interesse ao clicar nelas, incentivando-o a revisitar o item e fazer uma compra.

{% details Requisitos %}

- Recomendações de itens de IA
- Catálogo de itens relevantes
- Evento personalizado para cliques

{% enddetails %}

{% details Como configurar %}

1. Criar uma [recomendação de item de IA]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/).
2. Defina o **Tipo** como **Mais recente**.
3. Selecione seu catálogo.
4. (Opcional) Adicione uma seleção para filtrar sua recomendação para apenas itens relevantes.
5. Escolha **Custom Event (Evento personalizado** ) e selecione seu evento personalizado para cliques na lista.
6. Treine a recomendação.
7. [Use a recomendação no envio de mensagens]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).

{% enddetails %}

### Engajamento recente ou compra de itens

Promova itens com os quais os usuários interagiram recentemente, incluindo visualizações, cliques ou compras. Essa abordagem mantém suas recomendações atualizadas e alinhadas com os interesses mais recentes do usuário. Por exemplo:

- **Educação:** Uma plataforma de educação on-line pode incentivar os usuários que assistiram recentemente a um vídeo educativo, mas não se inscreveram em um curso, a conferir cursos semelhantes ou assuntos de interesse para manter o usuário engajado e motivado a começar a aprender.
- **Fitness:** Um app de fitness pode sugerir exercícios ou desafios semelhantes aos que o usuário concluiu recentemente ou com os quais interagiu, mantendo sua rotina de exercícios variada e engajada.
- **Varejista de artigos de decoração:** Depois que um cliente adquire uma ferramenta elétrica, um varejista de reforma residencial pode recomendar acessórios relacionados ou equipamentos de segurança com base na compra recente, aprimorando a experiência e a segurança do usuário.

{% details Requisitos %}

- Recomendações de itens de IA
- Catálogo de itens relevantes
- Um objeto de compra ou qualquer evento personalizado para uma interação de engajamento

{% enddetails %}

{% details Como configurar %}

1. Criar uma [recomendação de item de IA]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/).
2. Defina o **Tipo** como **Mais recente**.
3. Selecione seu catálogo.
4. (Opcional) Adicione uma seleção para filtrar sua recomendação para apenas itens relevantes.
5. Escolha **Custom Event (Evento personalizado** ) e selecione seu evento personalizado para cliques na lista.
6. Treine a recomendação.
7. [Use a recomendação no envio de mensagens]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).

{% enddetails %}

### Tendência de itens comprados

Destaque os itens que seus usuários compraram recentemente com maior frequência. Por exemplo, uma empresa de comércio eletrônico poderia recomendar itens sazonais que os usuários estão começando a estocar durante os preparativos para a próxima estação. 

{% details Requisitos %}

- Recomendações de itens de IA
- Catálogo de itens relevantes
- Um método para rastreamento de compras (um objeto de compra ou um evento personalizado)

{% enddetails %}

{% details Como configurar %}

1. Criar uma [recomendação de item de IA]({{site.baseurl}}/ai_item_recommendations/).
2. Defina o **Tipo** como **Tendência**.
3. Selecione seu catálogo.
4. (Opcional) Adicione uma seleção para filtrar sua recomendação para apenas itens relevantes.
5. Escolha um evento de compra ou um evento personalizado que rastreia as compras, juntamente com a propriedade correspondente.
6. Treine a recomendação.
7. [Use a recomendação no envio de mensagens.]({{site.baseurl}}/user_guide/sage_ai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging)

{% enddetails %}

### Itens favoritos em alta

Destaque itens que seus usuários gostaram recentemente com maior frequência. Por exemplo, um app de música poderia apresentar artistas promissores que tiveram um aumento recente no número de curtidas dos usuários.

{% details Requisitos %}

- Recomendações de itens de IA
- Catálogo de itens relevantes
- Evento personalizado para rastreamento de curtidas

{% enddetails %}

{% details Como configurar %}

1. Criar uma [recomendação de item de IA]({{site.baseurl}}/ai_item_recommendations/).
2. Defina o **Tipo** como **Tendência**.
3. Selecione seu catálogo.
4. (Opcional) Adicione uma seleção para filtrar sua recomendação para apenas itens relevantes.
5. Escolha seu evento personalizado para rastreamento de curtidas, juntamente com a propriedade correspondente.
6. Treine a recomendação.
7. [Use a recomendação no envio de mensagens.]({{site.baseurl}}/user_guide/sage_ai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging/)

{% enddetails %}

[1]: {{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/
