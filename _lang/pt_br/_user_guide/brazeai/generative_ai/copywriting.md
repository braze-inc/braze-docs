---
nav_title: Redação publicitária
article_title: Assistente de Copywriting com IA
page_order: 2.1
description: "Este artigo de referência aborda o Assistente de Copywriting de IA, recurso que passa um breve nome ou descrição do produto para a ferramenta de geração de cópia GPT da OpenAI para gerar uma cópia de marketing semelhante à humana para uso em seu envio de mensagens."
---

# Gerar texto com BrazeAI

> O assistente de Copywriting de IA passa um breve nome ou descrição do produto para uma ferramenta de geração de cópia GPT de um provedor terceirizado de propriedade da OpenAI para gerar uma cópia de marketing semelhante à humana para uso em seu envio de mensagens. Essa funcionalidade está disponível por padrão para a maioria dos criadores de mensagens no dashboard da Braze.

## Gerando texto

### Etapa 1: Lançar redator de IA

Em seu criador de mensagens, selecione <i class="fa-solid fa-wand-magic-sparkles"></i> **Abrir AI Copywriter**.

No editor de arrastar e soltar para mensagens no app, selecione um bloco de texto e selecione <i class="fa-solid fa-wand-magic-sparkles" title="IA Copywriter"></i> na barra de ferramentas do bloco.

### Etapa 2: Insira os detalhes

Insira um nome ou descrição do produto no campo de entrada e, em seguida, selecione um comprimento de saída aproximado.

Você pode escolher um canal específico para um comprimento de saída com base nas práticas recomendadas específicas do canal ou selecionar entre curto (1 frase), médio (2-3 frases) ou longo (1 parágrafo).

### Etapa 3: Personalize ainda mais (opcional)

Para personalizar ainda mais seu texto, você pode:

- **Aplicar diretrizes de marca:** Após [gerar diretrizes de marca com BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/generative_ai/brand_guidelines), você pode usá-las para ajudar a gerar seu texto.
- **Escolher um tom:** Cada tom gerará texto em um estilo diferente. Escolha o tom que melhor combina com a voz da sua marca.
- **Referenciar dados de campanhas passadas**: Quando ativado, as notificações push móveis anteriores enviadas através de suas campanhas ou etapas do Canvas são usadas como referência estilística para gerar seu novo texto. Para saber mais, veja [Usando dados de campanhas passadas](#past-campaign-data).
- **Traduzir texto automaticamente:** Você pode escolher um idioma de saída diferente para seu texto. O conteúdo gerado será exibido nesse idioma.

### Etapa 4: Gere seu texto

Quando você terminar, selecione **Gerar**. Usaremos as informações que você fornecer para solicitar ao GPT que escreva o texto para você. A resposta será obtida da OpenAI e fornecida a você. Para saber mais, veja [Como meus dados são usados e enviados para a OpenAI?](#ai-policy).

![Modal do Assistente de Copywriting de IA mostrando vários recursos disponíveis"]({% image_buster /assets/img/ai_copywriter/gpt3.png %} "GPT3"){: style="max-width:70%;"}

{% alert important %}
Filtramos respostas para conteúdo ofensivo que viole a [política de conteúdo](https://beta.openai.com/docs/usage-guidelines/content-policy) da OpenAI.
{% endalert %}

## Sobre dados de campanhas passadas {#past-campaign-data}

Ao usar push como seu comprimento de saída, se você selecionar **Referenciar dados de campanhas passadas**, campanhas de push móvel anteriores selecionadas aleatoriamente serão enviadas para a OpenAI para que o GPT possa usá-las como base para sua geração de texto. Atualmente, o redator de IA enviará campanhas de push para a OpenAI que não têm sintaxe Liquid. Deixe essa caixa desmarcada se não quiser aproveitar esse recurso. Consulte as seções a seguir para saber mais sobre como a Braze e a OpenAI usam seus dados. 

Se usado em conjunto com uma [diretriz]({{site.baseurl}}/user_guide/brazeai/generative_ai//brand_guidelines/) da marca, tanto a diretriz da marca quanto os dados de campanhas anteriores serão incorporados ao resultado final.

{% multi_lang_include brazeai/generative_ai/policy.md %}
