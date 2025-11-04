---
nav_title: Código líquido
article_title: Geração de código Liquid com o BrazeAI
description: "Este artigo abordará como o AI Liquid Assistant funciona e como você pode usá-lo para gerar snippets do Liquid para suas mensagens."
page_type: reference
page_order: 0.0
---

# Geração de código Liquid com o <sup>BrazeAITM</sup>

> O Liquid Assistant do <sup>BrazeAITM</sup> é um assistente de bate-papo desenvolvido pelo <sup>BrazeAITM</sup> que ajuda a gerar o Liquid de que você precisa para personalizar o conteúdo das mensagens.

## Sobre o assistente líquido <sup>BrazeAITM</sup> 

O <sup>BrazeAITM</sup> Liquid Assistant foi projetado para ajudá-lo a escrever um código Liquid eficaz e adaptado às suas necessidades de marketing. Treinada na sintaxe do Liquid e em como os profissionais de marketing utilizam o Liquid em suas mensagens, nossa IA entende as nuances da criação de conteúdo personalizado.

Além disso, ao fornecer ao Liquid Assistant do <sup>BrazeAITM</sup> seus nomes de atributos personalizados (como “favourite_color”) ) e tipos de dados (como booleano e string), o Liquid Assistant do <sup>BrazeAITM</sup> garante que suas mensagens sejam direcionadas com precisão e alinhadas às suas metas. Além disso, se você criar Diretrizes da Marca, o Liquid Assistant da <sup>BrazeAITM</sup> poderá usar as Diretrizes da Marca para personalizar melhor os resultados gerados e personalizar o conteúdo de acordo com a voz da nossa própria marca. As Diretrizes da marca que você criar serão usadas apenas para personalizar o conteúdo para seu próprio uso.

## Canais suportados

Você pode usar o Liquid Assistant do <sup>BrazeAITM</sup> ao criar: 
- Mensagens SMS
- Notificações push
- Mensagens de e-mail em HTML
- Telas

{% alert note %}
O assistente trabalha com mensagens de e-mail e não com modelos. Ele funciona melhor em mensagens de e-mail que já foram criadas.
{% endalert %}

## Geração de código Liquid

Para iniciar o assistente do <sup>BrazeAITM</sup> Liquid, selecione o ícone do assistente de IA no compositor de mensagens.

Compositor de mensagens com o assistente de IA.]({% image_buster /assets/img/ai_liquid/ai_assistant_icon.png %}){: style="max-width:50%;"}

Você pode escolher um dos prompts incluídos ou digitar o seu próprio na caixa de texto.

{% tabs local %}
{% tab use app activity %}
O prompt **Usar atividade do aplicativo** gera código líquido para ajudá-lo a enviar mensagens diferentes com base na última vez em que o aplicativo foi usado. Poderão ser feitas perguntas complementares para que o assistente possa gerar um resultado mais preciso.

\![Exemplo de saída do prompt "Use app activity" (Usar atividade do aplicativo).]({% image_buster /assets/img/ai_liquid/use_app_activity.png %}){: style="max-width:45%;"}
{% endtab %}

{% tab add countdown %}
Esse prompt gerará o código Liquid que envia uma mensagem com o tempo que falta para um evento acontecer. Ele solicitará que você forneça detalhes sobre a data e a hora do evento.

\![Exemplo de saída do prompt "Add countdown" (Adicionar contagem regressiva).]({% image_buster /assets/img/ai_liquid/add_countdown.png %}){: style="max-width:45%;"}
{% endtab %}

{% tab inspire me %}
Esse prompt é exibido quando há conteúdo em sua caixa de mensagem. Ele gera uma lista de opções que você pode escolher para personalizar sua mensagem com o Liquid. 

\![Exemplo de saída do prompt "Inspire me" (Inspire-me).]({% image_buster /assets/img/ai_liquid/inspire_me.png %}){: style="max-width:45%;"}
{% endtab %}

{% tab improve my liquid %}
Esse prompt é exibido quando há conteúdo em seu compositor de mensagens. Selecione-o quando quiser que o assistente torne seu código mais eficiente e mais fácil de ler.

\![Exemplo de saída do prompt "Improve my Liquid".]({% image_buster /assets/img/ai_liquid/improve_my_liquid.png %}){: style="max-width:45%;"}
{% endtab %}
{% endtabs %}

Para gerar seu código Liquid, selecione **Update composer (Atualizar compositor**).

Janela do assistente de IA com avisos fornecidos.]({% image_buster /assets/img/ai_liquid/ai_assistant_window.png %}){: style="max-width:50%;"}
 
Você pode gerar outra mensagem usando o mesmo prompt, selecionando **Regenerate**. Para remover a mensagem e reverter para a anterior, selecione **Undo update (Desfazer atualização**).

## Atributos líquidos {#supported-attributes}

Os atributos a seguir estão atualmente em versão beta para o <sup>BrazeAITM</sup> Liquid Assistant:

| Critério | Tipo de conhecimento
| - | - |
| Líquido (incluindo `for` loops, `if` declarações, matemática e outros) | Codificação |
| Atributos de usuário padrão e standard
| Atributos personalizados que possuem qualquer um desses tipos de dados: {::nomarkdown}<ul><li>Booleanos</li><li>Números</li><li>Cordas</li><li>Matrizes</li><li>Tempo</li></ul>{:/} | Atributos
| Conteúdo conectado | Codificação | Conteúdo conectado
{: .reset-td-br-1 .reset-td-br-2 }

## Práticas recomendadas

Para obter ajuda para escrever prompts eficazes para o Liquid Assistant do <sup>BrazeAITM</sup>, confira nossas práticas recomendadas:

### Usar linguagem natural

O <sup>BrazeAITM</sup> Liquid Assistant é treinado para entender a linguagem natural. Converse com ele como faria com um colega de trabalho ao pedir ajuda. Isso torna mais fácil para o assistente compreender suas necessidades e fornecer assistência precisa.

### Dar contexto

O fornecimento de contexto ajuda o Liquid Assistant do <sup>BrazeAITM</sup> a entender o panorama geral do seu projeto. É útil incluir um contexto como, por exemplo:

- Nome e setor de sua empresa
- Uma campanha na qual você está trabalhando, como a Black Friday ou as vendas de fim de ano
- Sua meta, como aumentar sua taxa de cliques
- Atributos personalizados específicos que você deseja incluir em sua mensagem

A inclusão do contexto em seu prompt ajuda o assistente a adaptar as respostas para atender melhor às suas necessidades. Você também pode incluir detalhes de sua campanha, resumo da mensagem ou documento de brainstorming para que o assistente fique a par de tudo.

### Seja específico

O Liquid Assistant do <sup>BrazeAITM</sup> pode fazer perguntas de acompanhamento, mas fornecer detalhes antecipadamente pode levar a resultados mais precisos mais cedo. Considere incluir detalhes como:

- Quaisquer preferências ou requisitos conhecidos para a mensagem
- Instruções sobre como lidar com situações, como a falta de respostas do destinatário da mensagem ou opções de mensagens alternativas
- Ao solicitar o Liquid que usa o Connected Content, a documentação do ponto de extremidade da API, um exemplo de resposta da API ou ambos

### Seja criativo

Pense fora da caixa com seus prompts para ver como o <sup>BrazeAITM</sup> Liquid Assistant pode aprimorar suas mensagens. Faça experiências com diferentes prompts e ideias, pois a criatividade pode levar a resultados mais envolventes.

## Exemplos de prompts

Aqui estão alguns exemplos para ajudá-lo a começar:

{% tabs local %}
{% tab gaining knowledge %}
- O que é o Liquid e como ele pode me ajudar a aprimorar a personalização de minhas campanhas de marketing no Braze?
- Que tipos de dados posso usar no Liquid para personalizar minhas mensagens de marketing, como informações demográficas ou compras anteriores?
{% endtab %}

{% tab personalizing dynamic content %}
- Criar uma mensagem que mostre conteúdo diferente com base no status de fidelidade do meu cliente. Se não soubermos sobre seu status de fidelidade, envie uma mensagem de fallback.
- Escreva uma mensagem dinâmica que inclua o produto favorito de um usuário e a data da última compra. Se não houver uma última compra, aborte a mensagem.
- Escreva-me um Liquid para incentivar alguém a clicar em minha mensagem que inclua uma contagem regressiva com o tempo restante. Se a oferta tiver expirado, aborte a mensagem.
- Ajude-me a escrever uma mensagem para incentivar os usuários a voltarem e finalizarem a compra se tiverem itens restantes no carrinho.
- Escreva Liquid para personalizar uma mensagem com base no país de um cliente. Quero preencher a mensagem com o nome do país. Se não tivermos nenhum deles, sugira que eles cliquem em um link para atualizar seu perfil.
- Como posso personalizar uma mensagem de boas-vindas com o primeiro nome de um usuário e escrever um texto diferente com base no gênero do usuário?
- Escreva o Liquid para exibir mensagens diferentes com base em um atributo personalizado, “CUSTOM_ATTRIBUTE_NAME“ e seu valor. Há seis opções diferentes que eu poderia enviar. Se não houver nenhum valor para o atributo personalizado, quero enviar uma mensagem de espaço reservado.
{% endtab %}

{% tab handling outliers %}
- Você pode me dar alguns exemplos de como o Liquid é usado em campanhas de marketing para aumentar o engajamento e as taxas de conversão?
- Quais são alguns casos de uso comuns para o Liquid em mensagens de texto para vendas de verão, como lembretes de carrinho abandonado ou promoções personalizadas?
{% endtab %}
{% endtabs %}

{% alert tip %}
Informe-nos se você teve alguma sugestão ou experiência interessante agendando uma [sessão de feedback](https://research.rallyuxr.com/braze/schedule/clxxhw8em0d071ak4b279553s?channel=share) conosco.
{% endalert %}

{% multi_lang_include brazeai/generative_ai/policy.md %}
