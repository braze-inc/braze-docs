---
nav_title: Redação
article_title: Assistente de Copywriting com IA
page_order: 2.1
description: "Este artigo de referência aborda o Assistente de Copywriting de IA, recurso que passa um breve nome ou descrição do produto para a ferramenta de geração de cópia GPT da OpenAI para gerar uma cópia de marketing semelhante à humana para uso em seu envio de mensagens."
---

# Geração de cópia com o <sup>BrazeAITM</sup>

> O assistente de Copywriting de IA passa um breve nome ou descrição do produto para uma ferramenta de geração de cópia GPT de um provedor terceirizado de propriedade da OpenAI para gerar uma cópia de marketing semelhante à humana para uso em seu envio de mensagens. Essa funcionalidade está disponível por padrão para a maioria dos criadores de mensagens no dashboard da Braze.

## Geração de cópia

### Etapa 1: Redator de IA de lançamento

Em seu criador de mensagens, selecione <i class="fa-solid fa-wand-magic-sparkles"></i> **Abrir AI Copywriter**.

No editor de arrastar e soltar para mensagens no app, selecione um bloco de texto e selecione <i class="fa-solid fa-wand-magic-sparkles" title="IA Copywriter"></i> na barra de ferramentas do bloco.

### Etapa 2: Insira os detalhes

Digite o nome ou a descrição de um produto no campo de entrada e selecione um comprimento de saída aproximado.

Você pode escolher um canal específico para um comprimento de saída com base nas práticas recomendadas específicas do canal ou selecionar entre curto (1 frase), médio (2-3 frases) ou longo (1 parágrafo).

### Etapa 3: Personalize-o ainda mais (opcional)

Para personalizar ainda mais sua cópia, você pode:

- **Aplique as diretrizes da marca:** Depois de [gerar as diretrizes da marca com o <sup>BrazeAITM</sup>]({{site.baseurl}}/user_guide/brazeai/generative_ai/brand_guidelines), você pode usá-las para ajudar a gerar seu texto.
- **Escolha um tom:** Cada tom gerará uma cópia em um estilo diferente. Escolha o tom que melhor corresponda à voz de sua marca.
- **Consulte os dados de campanhas anteriores**: Quando ativada, as notificações por push para celular anteriores enviadas por meio de suas campanhas ou etapas do Canva são usadas como referência estilística para gerar sua nova cópia. Para saber mais, consulte [Uso de dados de campanhas anteriores](#past-campaign-data).
- **Tradução automática de cópia:** Você pode escolher um idioma de saída diferente para sua cópia. O conteúdo gerado será enviado para esse idioma.

### Etapa 4: Gerar sua cópia

Quando terminar, selecione **Generate (Gerar**). Usaremos as informações que você fornecer para solicitar que a GPT escreva um texto para você. A resposta será obtida da OpenAI e fornecida a você. Para saber mais, consulte [Como meus dados são usados e enviados para a OpenAI?](#ai-policy)

![Modal do Assistente de Copywriting de IA mostrando vários recursos disponíveis"]({% image_buster /assets/img/ai_copywriter/gpt3.png %} "GPT3"){: style="max-width:70%;"}

{% alert important %}
Filtramos respostas para conteúdo ofensivo que viole a [política de conteúdo](https://beta.openai.com/docs/usage-guidelines/content-policy) da OpenAI.
{% endalert %}

## Sobre dados de campanhas anteriores {#past-campaign-data}

Ao usar push como comprimento de saída, se você selecionar **Faz referência a dados de campanhas antigas**, campanhas push móveis anteriores selecionadas aleatoriamente serão enviadas à OpenAI para que a GPT possa usá-las como base para a geração de cópias. Deixe essa caixa desmarcada se não quiser aproveitar esse recurso. Consulte as seções a seguir para saber mais sobre como a Braze e a OpenAI usam seus dados. 

Se usado em conjunto com uma [diretriz]({{site.baseurl}}/user_guide/brazeai/generative_ai//brand_guidelines/) da marca, tanto a diretriz da marca quanto os dados de campanhas anteriores serão incorporados ao resultado final.

{% multi_lang_include brazeai/generative_ai/policy.md %}
