---
nav_title: Caso de uso
article_title: Caso de uso Impulsionar a descoberta de conteúdo após a exibição
description: "Este exemplo mostra como uma marca fictícia usa as recomendações de itens da Braze IA para fornecer conteúdo personalizado e sugestões de produtos nos principais momentos do cliente."
page_type: tutorial
---

# Caso de uso: Promova a descoberta de conteúdo após a visualização

> Este exemplo mostra como uma marca fictícia usa as recomendações de itens da Braze IA para fornecer conteúdo personalizado e sugestões de produtos nos principais momentos do cliente. Saiba como a lógica de recomendação pode melhorar o engajamento, aumentar as conversões e reduzir o esforço manual.

Digamos que Camila seja gerente de CRM da MovieCanon, uma plataforma de streaming que apresenta filmes e séries com curadoria. 

O objetivo de Camila é manter o engajamento dos espectadores depois que eles terminam de assistir a algo. Historicamente, as mensagens "Você também pode gostar" do MovieCanon eram baseadas em uma ampla correspondência de gêneros e enviadas em momentos arbitrários - muitas vezes horas ou dias após uma sessão. O engajamento era baixo, e sua equipe sabia que poderia fazer melhor.

Usando [as recomendações de itens por IA]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/), Camila configura um sistema para recomendar automaticamente novos títulos com base no histórico de exibição de cada espectador, entregue imediatamente após o usuário terminar um filme ou episódio. É uma maneira mais inteligente e pessoal de ajudar os usuários a descobrir o conteúdo que eles realmente desejam assistir e mantê-los engajados na plataforma.

![Mensagem no app com a seguinte mensagem: "A seguir, só para você. Porque você assistiu a "Nomads of the Sun", com uma imagem, nome do título, descrição e CTA para "Assistir agora" ou "Pular" para a próxima recomendação.]({% image_buster /assets/img/ai_use_cases/recommendation_rendered.png %})

Este tutorial explica como a Camila:

- Uma mensagem personalizada disparada quando um usuário termina de assistir a algo
- Recomendações personalizadas de acordo com as preferências do espectador - extraídas automaticamente do catálogo do MovieCanon e inseridas na mensagem 

## Etapa 1: Criar um modelo de previsão de churn

A Camila começa criando uma recomendação que apresentará títulos relevantes sempre que um usuário terminar de assistir a algo. Ela quer que seja dinâmico, para que os usuários recebam sugestões diferentes com base no que assistiram recentemente.

1. No dashboard do Braze, Camila navega até **Recomendações de itens de IA**.
2. Ela cria uma nova recomendação e a nomeia "Post-viewing suggestions" (Sugestões pós-visualização).
3. Para o tipo de recomendação, ela escolhe **IA Personalizada**, para que cada usuário veja recomendações personalizadas com base em comportamentos anteriores.
4. Ela seleciona **Não recomendar itens com os quais os** usuários **já interagiram anteriormente** para que os usuários não recebam recomendações de algo que já assistiram. 
5. Ela seleciona o catálogo que contém a biblioteca de conteúdo atual do MovieCanon. Camila não adiciona uma seleção de catálogo, pois deseja que todos os itens do catálogo sejam itens elegíveis para recomendação.
6. Camila vincula a recomendação ao evento personalizado `Watched Content`, que rastreia as visualizações concluídas, e define o **Nome da propriedade** como o título do conteúdo.
7. Ela cria a recomendação.

## Etapa 2: Configure uma mensagem no app

Depois que a recomendação termina o treinamento, Camila cria um fluxo de envio de mensagens que chega ao usuário no momento certo: imediatamente após ele terminar um título. A mensagem inclui uma lista de três sugestões personalizadas extraídas diretamente do catálogo.

1. Camila cria uma campanha de mensagens no app usando o editor de arrastar e soltar.
2. Ela define o disparo para seu evento personalizado: `Watched Content`.
3. Ela cria uma mensagem no app de várias páginas com imagens de título, nomes e uma CTA "Assista agora".

![Modal "Add Personalization" aberto no editor do Braze, com "Item recommendation" selecionado como o tipo de personalização.]({% image_buster /assets/img/ai_use_cases/recommendation_add_personalization.png %})

{: start="4"}

4. No corpo da mensagem, Camila usa o [modal Add Personalization]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#inserting-pre-formatted-variables) para adicionar variáveis como o nome, a descrição e a miniatura do título recomendado usando o Liquid, que preenche dinamicamente o conteúdo do catálogo. Ela modelou um atributo personalizado para o site `Last Watched Movie` para que os usuários saibam que essa recomendação se baseia no histórico de relógios. 

![Editor de mensagens no app com Liquid bruto para modelar em campos específicos de itens do catálogo da recomendação.]({% image_buster /assets/img/ai_use_cases/recommendation_liquid.png %})

{% details Show Liquid used in image %}

{% raw %}

```liquid
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].name }}
```

```liquid
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].description }}
```

```liquid
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].thumbnail }}
```

{% endraw %}

{% enddetails %}

{: start="5"}

5. Em seguida, Camila duplica sua página e incrementa a matriz Liquid {% raw %} (`{{ items[0]}}` a `{{items[1]}}`) {% endraw %} em cada variável para modelar o próximo item da lista de recomendações.

## Etapa 3: Medir e otimizar

Com a campanha ativa, Camila monitora as taxas de abertura, as CTRs e o comportamento de visualização de acompanhamento. Ela compara a performance com campanhas anteriores de recomendação estática e vê um maior engajamento e mais sessões de conteúdo por usuário.

Ela também planeja fazer testes A/B:

- Tempo (imediato versus 10 minutos após a observação)
- Layout do conteúdo (carrossel versus lista)
- Variações de CTA ("Assistir agora" versus "Adicionar à fila")

Ao combinar o envio de mensagens orientado por eventos com recomendações de itens por IA, o Camila transforma a descoberta de conteúdo em uma experiência automática e personalizada. O MovieCanon mantém os usuários engajados sem adivinhações, fornecendo conteúdo relevante no momento certo para aumentar a profundidade da sessão e reduzir o churn.





