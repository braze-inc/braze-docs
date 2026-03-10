---
nav_title: Código Liquid
article_title: Gerar código Liquid com BrazeAI
description: "Este artigo abordará como o IA Liquid Assistant funciona e como você pode usá-lo para gerar snippets do Liquid para o envio de mensagens."
page_type: reference
page_order: 0.0
---

# Gerar código Liquid com BrazeAI

> O Liquid Assistant do <sup>BrazeAITM</sup> é um assistente de bate-papo desenvolvido pelo <sup>BrazeAITM</sup> que ajuda a gerar o Liquid de que você precisa para personalizar o conteúdo das mensagens.

## Sobre o assistente Liquid BrazeAI<sup>TM</sup>

O Liquid Assistant da <sup>BrazeAI™</sup> foi projetado para ajudar na formulação de um código Liquid eficaz e adaptado às suas necessidades de marketing. Treinada na sintaxe do Liquid e em como os profissionais de marketing utilizam o Liquid em suas mensagens, nossa IA entende as nuances da elaboração de conteúdo personalizado.

Além disso, ao fornecer ao Assistente Liquid BrazeAI<sup>TM</sup> os nomes dos seus atributos personalizados (como “favourite_color”)) e tipos de dados (como booleano e string), nosso Assistente Liquid BrazeAI<sup>TM</sup> garante que suas mensagens sejam precisamente direcionadas e alinhadas com seus objetivos. Além disso, se você criar diretrizes da marca, o Liquid Assistant da <sup>BrazeAITM</sup> poderá usar as diretrizes da marca para personalizar melhor os resultados gerados e personalizar o conteúdo de acordo com a voz da nossa própria marca. As diretrizes da marca que você criar serão usadas apenas para personalizar o conteúdo para seu próprio uso.

## Canais suportados

Você pode usar o Liquid Assistant do <sup>BrazeAITM</sup> ao criar: 
- Envio de mensagens SMS
- Notificações por push
- Envio de mensagens de e-mail em HTML
- Canvas

{% alert note %}
O assistente funciona em mensagens de e-mail e não em templates. Funciona melhor em mensagens de e-mail que já estão construídas.
{% endalert %}

## Geração de código Liquid

Para iniciar o Liquid Assistant da <sup>BrazeAI™</sup>, selecione o ícone do assistente de IA no criador de mensagens.

![Criador de mensagens com o assistente de IA.]({% image_buster /assets/img/ai_liquid/ai_assistant_icon.png %}){: style="max-width:50%;"}

Você pode escolher um dos prompts incluídos ou inserir o seu próprio na caixa de texto.

{% tabs local %}
{% tab use app activity %}
O prompt **Usar atividade do aplicativo** gera código Liquid para ajudá-lo a enviar mensagens diferentes com base na última vez em que o aplicativo foi usado. Poderão ser feitas perguntas complementares para que o assistente possa gerar um resultado mais preciso.

![Exemplo de saída do prompt "Use app activity" (Usar atividade do app).]({% image_buster /assets/img/ai_liquid/use_app_activity.png %}){: style="max-width:45%;"}
{% endtab %}

{% tab add countdown %}
Esse prompt gerará o código Liquid que envia uma mensagem com o tempo que falta para um evento acontecer. Ele solicitará que você forneça detalhes sobre a data e a hora do evento.

![Exemplo de saída do prompt "Add countdown" (Adicionar contagem regressiva).]({% image_buster /assets/img/ai_liquid/add_countdown.png %}){: style="max-width:45%;"}
{% endtab %}

{% tab inspire me %}
Esse prompt aparece quando há conteúdo em sua caixa de mensagens. Ele gera uma lista de opções que você pode escolher para personalizar sua mensagem com o Liquid. 

![Exemplo de saída do prompt "Inspire-me".]({% image_buster /assets/img/ai_liquid/inspire_me.png %}){: style="max-width:45%;"}
{% endtab %}

{% tab improve my liquid %}
Esse prompt é exibido quando há conteúdo em seu criador de mensagens. Selecione-o quando quiser que o assistente torne seu código mais eficiente e mais fácil de ler.

![Exemplo de saída do prompt "Improve my Liquid" (Melhorar meu Liquid).]({% image_buster /assets/img/ai_liquid/improve_my_liquid.png %}){: style="max-width:45%;"}
{% endtab %}
{% endtabs %}

Para gerar seu código Liquid, selecione **Atualizar criador**.

![Janela do assistente de IA com prompts fornecidos.]({% image_buster /assets/img/ai_liquid/ai_assistant_window.png %}){: style="max-width:50%;"}
 
Você pode gerar outra mensagem usando o mesmo prompt, selecionando **Regenerate**. Para remover a mensagem e reverter para a anterior, selecione **Undo update (Desfazer atualização**).

## Atributos Liquid {#supported-attributes}

Os seguintes atributos estão atualmente em beta para o Assistente Liquid BrazeAI<sup>TM</sup>:

| Critério | Tipo de conhecimento | 
| - | - | 
| Liquid (incluindo loops `for`, declarações `if`, matemática e outros) | Codificação |
| Atributos de usuário padrão e padrão | Atributos |
| Atributos personalizados que têm qualquer um desses tipos de dados: {::nomarkdown}<ul><li>Booleanos</li><li>Números</li><li>Strings</li><li>Matrizes</li><li>Horário</li></ul>{:/} | Atributos |
| Conteúdo conectado | Codificação |
{: .reset-td-br-1 .reset-td-br-2 }

## Melhores práticas

Para ajuda na redação de prompts eficazes para o Assistente Liquid BrazeAI<sup>TM</sup>, confira nossas melhores práticas:

### Usar linguagem natural

O Liquid Assistant da <sup>BrazeAI™</sup> é treinado para entender a linguagem natural. Converse com ele como faria com um colega de trabalho ao pedir ajuda. Isso torna mais fácil para o assistente compreender suas necessidades e fornecer assistência precisa.

### Dar contexto

O fornecimento de contexto ajuda o Liquid Assistant da <sup>BrazeAI™</sup> a entender o panorama geral do seu projeto. É útil incluir um contexto como, por exemplo:

- Nome e setor de sua empresa
- Uma campanha na qual você está trabalhando, como a Black Friday ou as vendas de fim de ano
- Seu objetivo, como aumentar sua taxa de cliques
- Atributos personalizados específicos que deseja incluir em sua mensagem

A inclusão do contexto em seu prompt ajuda o assistente a adaptar as respostas para atender melhor às suas necessidades. Você também pode incluir detalhes de sua campanha, resumo de mensagens ou documento de envio de mensagens para que o assistente fique a par de tudo.

### Seja específico

O Liquid Assistant da <sup>BrazeAI™</sup> pode fazer perguntas de acompanhamento, mas fornecer detalhes antecipadamente pode agilizar a geração de resultados mais precisos. Considere incluir detalhes como:

- Quaisquer preferências ou requisitos conhecidos para a mensagem
- Instruções sobre como lidar com situações, como a falta de respostas do destinatário da mensagem ou opções de mensagem fallback
- Ao solicitar o Liquid que usa o conteúdo conectado, a documentação do endpoint da API, uma amostra da resposta da API ou ambos

### Seja criativo

Pense fora da caixa com seus prompts para ver como o Liquid Assistant da <sup>BrazeAI™</sup> pode aprimorar seu envio de mensagens. Faça experiências com diferentes prompts e ideias, pois a criatividade pode levar a resultados mais engajados.

## Exemplos de prompts

Aqui estão alguns exemplos para ajudar você a começar:

{% tabs local %}
{% tab gaining knowledge %}
- O que é o Liquid e como ele pode me ajudar a aprimorar a personalização de minhas campanhas de marketing na Braze?
- Que tipos de dados posso usar no Liquid para personalizar minhas mensagens de marketing, como informações demográficas ou compras anteriores?
{% endtab %}

{% tab personalizing dynamic content %}
- Criar uma mensagem que mostre conteúdo diferente com base no status de fidelidade de meu cliente. Se não soubermos seu status de fidelidade, envie uma mensagem fallback.
- Escreva uma mensagem dinâmica que inclua o produto favorito de um usuário e a data da última compra. Se não houver uma última compra, aborte a mensagem.
- Escreva-me um Liquid para incentivar alguém a clicar em minha mensagem que inclua uma contagem regressiva com o tempo restante. Se a oferta tiver expirado, aborte a mensagem.
- Ajude-me a escrever uma mensagem para incentivar os usuários a voltarem e finalizarem a compra se tiverem itens restantes no carrinho.
- Escreva Liquid para personalizar uma mensagem com base no país de um cliente. Quero preencher a mensagem com o nome do país. Se não tivermos nenhum deles, sugira que ele clique em um link para atualizar seu perfil.
- Como posso personalizar uma mensagem de boas-vindas com o nome de um usuário e escrever um texto diferente com base no gênero do usuário?
- Escreva Liquid para exibir mensagens diferentes com base em um atributo personalizado, “CUSTOM_ATTRIBUTE_NAME“ e seu valor. Há seis opções diferentes que eu poderia enviar. Se não houver nenhum valor do atributo personalizado, quero enviar uma mensagem de espaço reservado.
{% endtab %}

{% tab handling outliers %}
- Você pode me dar alguns exemplos de como o Liquid é usado em campanhas de marketing para aumentar o engajamento e as taxas de conversão?
- Quais são alguns casos de uso comuns para a Liquid em mensagens de texto para vendas de verão, como lembretes de abandono de carrinho ou promoções personalizadas?
{% endtab %}
{% endtabs %}

{% alert tip %}
Informe-nos se você teve alguma sugestão ou experiência interessante agendando uma [sessão de feedback](https://research.rallyuxr.com/braze/schedule/clxxhw8em0d071ak4b279553s?channel=share) conosco.
{% endalert %}

{% multi_lang_include brazeai/generative_ai/policy.md %}
