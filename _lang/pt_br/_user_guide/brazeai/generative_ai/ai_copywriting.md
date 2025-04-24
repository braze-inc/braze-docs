---
nav_title: Assistente de Copywriting com IA
article_title: Assistente de Copywriting com IA
page_order: 4
description: "Este artigo de referência aborda o Assistente de Copywriting de IA, recurso que passa um breve nome ou descrição do produto para a ferramenta de geração de cópia GPT da OpenAI para gerar uma cópia de marketing semelhante à humana para uso em seu envio de mensagens."
---

# Assistente de Copywriting com IA

> O assistente de Copywriting de IA passa um breve nome ou descrição do produto para uma ferramenta de geração de cópia GPT de um provedor terceirizado de propriedade da OpenAI para gerar uma cópia de marketing semelhante à humana para uso em seu envio de mensagens. Essa funcionalidade está disponível por padrão para a maioria dos criadores de mensagens no dashboard da Braze.

## Criação de texto {#steps}

Para gerar um texto usando o Assistente de Copywriting de IA, siga estas etapas:

1. Em seu criador de mensagens, selecione <i class="fa-solid fa-wand-magic-sparkles"></i> **Abrir AI Copywriter**.
   * No editor de arrastar e soltar para mensagens no app, selecione um bloco de texto e selecione <i class="fa-solid fa-wand-magic-sparkles" title="IA Copywriter"></i> na barra de ferramentas do bloco.
2. Digite o nome ou a descrição de um produto no campo de entrada.
3. Selecione um comprimento de saída aproximado. Você pode escolher um canal específico para um comprimento de saída com base nas práticas recomendadas específicas do canal ou selecionar entre curto (1 frase), médio (2-3 frases) ou longo (1 parágrafo). 
4. (Opcional) Crie ou aplique uma diretriz da marca para adaptar essa cópia à sua marca. Essas diretrizes são salvas em seu espaço de trabalho e podem ser reutilizadas após serem criadas. Para saber mais, consulte [Criação de diretrizes da marca]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_copywriting/brand_guidelines/).
5. (Opcional) Escolha um tom de mensagem entre as opções disponíveis. Isso determinará o estilo da cópia gerada.
6. (Opcional) Disponível para notificações por push: Selecione **Reference past campaign data (Referência a dados de campanhas** anteriores) para usar suas mensagens push para celular anteriores (campanhas e etapas do Canva) como referência estilística para gerar novas cópias. Quando selecionada, a saída imitará o estilo de suas mensagens anteriores.
7. Selecione o idioma de saída. Isso pode ser diferente do seu idioma de entrada.
8. Selecione **Generate (Gerar**).

Usamos as informações que você fornece para solicitar que a GPT escreva um texto para você. A resposta será obtida da OpenAI e fornecida a você. 

![Modal do Assistente de Copywriting de IA mostrando vários recursos disponíveis"][1]{: style="max-width:70%;"}

{% alert important %}
Filtramos respostas para conteúdo ofensivo que viole a [política de conteúdo](https://beta.openai.com/docs/usage-guidelines/content-policy) da OpenAI.
{% endalert %}

## Uso de dados de campanhas anteriores

Ao usar push como comprimento de saída, se você selecionar **Faz referência a dados de campanhas antigas**, campanhas push móveis anteriores selecionadas aleatoriamente serão enviadas à OpenAI para que a GPT possa usá-las como base para a geração de cópias. Deixe essa caixa desmarcada se não quiser aproveitar esse recurso. Consulte as seções a seguir para saber mais sobre como a Braze e a OpenAI usam seus dados. 

Se usado em conjunto com uma [diretriz]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_copywriting/brand_guidelines/) da marca, tanto a diretriz da marca quanto os dados de campanhas anteriores serão incorporados ao resultado final.

## O que é GPT?

O [GPT](https://openai.com/product/gpt-4) é a ferramenta de geração de linguagem natural de última geração da OpenAI, alimentada por inteligência artificial. Ele pode executar uma variedade de tarefas de linguagem natural, como geração, preenchimento e classificação de textos. Nós o conectamos ao dashboard da Braze para ajudar a inspirar e diversificar sua cópia diretamente enquanto você trabalha.

## Como meus dados são usados e enviados para a OpenAI?

Para gerar uma cópia, a Braze enviará sua consulta à OpenAI. Todas as consultas enviadas pela Braze à OpenAI são anônimas, o que significa que a OpenAI não poderá identificar o remetente da consulta, a menos que você inclua informações exclusivamente identificáveis na entrada fornecida ou nos dados de sua campanha anterior ao ativar a opção "Faz referência a dados de campanhas antigas". De acordo com a [política da OpenAI](https://openai.com/policies/api-data-usage-policies), os dados enviados à API da OpenAI via Braze não são usados para treinar ou aprimorar seus modelos e serão excluídos após 30 dias. Entre você e a Braze, qualquer conteúdo gerado usando GPT é de sua propriedade intelectual. A Braze não fará valer nenhuma reivindicação de propriedade de direitos autorais sobre tal conteúdo e não oferece nenhuma garantia de qualquer tipo com relação a qualquer conteúdo gerado por IA.

## Mais ferramentas de IA

Também é possível [gerar uma imagem usando IA]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#generate-ai) a partir da biblioteca de mídia. Esse recurso usa o [DALL-E 3](https://openai.com/index/dall-e-3/), um sistema de IA da OpenAI que pode criar imagens e arte realistas a partir de uma descrição em linguagem natural.

[1]: {% image_buster /assets/img/ai_copywriter/gpt3.png %} "GPT3"
