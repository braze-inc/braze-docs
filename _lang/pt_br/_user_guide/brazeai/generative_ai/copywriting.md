---
nav_title: Redação publicitária
article_title: Assistente de Copywriting com IA
page_order: 2.1
description: "Este artigo de referência aborda o Assistente de Copywriting de IA, recurso que passa um breve nome ou descrição do produto para a ferramenta de geração de texto GPT da OpenAI para gerar textos de marketing semelhantes aos humanos para uso no seu envio de mensagens."
---

# Gerar texto com BrazeAI

> O Assistente de Copywriting de IA passa um breve nome ou descrição do produto para uma ferramenta de geração de texto GPT de um provedor terceirizado de propriedade da OpenAI para gerar textos de marketing semelhantes aos humanos para uso no seu envio de mensagens. Essa funcionalidade está disponível por padrão para a maioria dos criadores de mensagens no dashboard da Braze.

## Gerando texto

### Etapa 1: Abrir o redator de IA

No seu criador de mensagens, selecione <i class="fa-solid fa-wand-magic-sparkles"></i> **Abrir AI Copywriter**.

No editor de arrastar e soltar para mensagens no app, selecione um bloco de texto e selecione <i class="fa-solid fa-wand-magic-sparkles" title="AI Copywriter"></i> na barra de ferramentas do bloco.

### Etapa 2: Insira os detalhes

Insira um nome ou descrição do produto no campo de entrada e, em seguida, selecione um comprimento de saída aproximado.

Você pode escolher um canal específico para um comprimento de saída com base nas práticas recomendadas específicas do canal ou selecionar entre curto (1 frase), médio (2-3 frases) ou longo (1 parágrafo).

### Etapa 3: Personalize ainda mais (opcional)

Para personalizar ainda mais seu texto, você pode:

- **Aplicar diretrizes da marca:** Após [gerar diretrizes da marca com BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/generative_ai/brand_guidelines), você pode usá-las para ajudar a gerar seu texto.
- **Escolher um tom:** Cada tom gerará texto em um estilo diferente. Escolha o tom que melhor combina com a voz da sua marca.
  
  Selecionar um tom adiciona uma instrução de estilo ao prompt enviado para a OpenAI, então o resultado exato pode variar de acordo com a entrada, o comprimento do canal, as diretrizes da marca e o modelo. 
  
  Veja o que cada tom faz por padrão:
  - **Formal:** Linguagem mais profissional e polida. Frases completas, linguagem mais cortês, gírias mínimas.
  - **Direto:** Mais direto e conciso. Menos adjetivos, menos "enrolação de marketing", chamadas para ação mais claras.
  - **Casual:** Mais descontraído e conversacional. Frases mais amigáveis, palavras mais simples, energia mais leve.
  - **Pessoal:** Mais individual e empático. Usa mais "você", pode parecer mais personalizado, especialmente se você adicionar personalização como {% raw %}`{{${first_name}}}`{% endraw %} à mensagem que está criando.
  - **Chamativo:** Mais atraente e impactante. Frases mais marcantes, energia mais alta, ganchos e CTAs mais fortes (geralmente soa mais "promocional" do que os outros tons).
  - **Sofisticado:** Linguagem mais elevada e refinada. Menos casual, posicionamento mais "premium".
  - **Profissional:** Empresarial e claro. Mais moderno e acessível do que o Formal, mas ainda mantendo autoridade.
  - **Passivo:** Linguagem mais suave e menos insistente. Menos comandos diretos, frases mais sugestivas.
  - **Urgente:** Enfatiza imediatismo e sensibilidade ao tempo. CTAs mais fortes, prazos, sinais de escassez.
  - **Empolgante:** Mais energético e entusiasmado. Enfatiza emoção positiva e celebração (geralmente mais focado em hype do que a abordagem baseada em ganchos do tom Chamativo).
 
  
- **Referenciar dados de campanhas anteriores**: Quando ativado, as notificações por push anteriores enviadas por meio das suas campanhas ou etapas do Canvas são usadas como referência estilística para gerar seu novo texto. Para saber mais, consulte [Usando dados de campanhas anteriores](#past-campaign-data).
- **Traduzir texto automaticamente:** Você pode escolher um idioma de saída diferente para seu texto. O conteúdo gerado será exibido nesse idioma.

### Etapa 4: Gere seu texto

Quando terminar, selecione **Gerar**. Usaremos as informações que você fornecer para solicitar ao GPT que escreva o texto para você. A resposta será obtida da OpenAI e fornecida a você. Para saber mais, consulte [Como meus dados são usados e enviados para a OpenAI?](#ai-policy).

![Modal do Assistente de Copywriting de IA mostrando vários recursos disponíveis"]({% image_buster /assets/img/ai_copywriter/gpt3.png %} "GPT3"){: style="max-width:70%;"}

{% alert important %}
Filtramos respostas com conteúdo ofensivo que viole a [política de conteúdo](https://beta.openai.com/docs/usage-guidelines/content-policy) da OpenAI.
{% endalert %}

## Sobre dados de campanhas anteriores {#past-campaign-data}

Ao usar push como seu comprimento de saída, se você selecionar **Referenciar dados de campanhas anteriores**, campanhas de push para celular anteriores selecionadas aleatoriamente serão enviadas para a OpenAI para que o GPT possa usá-las como base para a geração de texto. Atualmente, o redator de IA enviará campanhas de push para a OpenAI que não têm sintaxe Liquid. Deixe essa caixa desmarcada se não quiser aproveitar esse recurso. Consulte as seções a seguir para saber mais sobre como a Braze e a OpenAI usam seus dados. 

Se usado em conjunto com uma [diretriz da marca]({{site.baseurl}}/user_guide/brazeai/generative_ai//brand_guidelines/), tanto a diretriz da marca quanto os dados de campanhas anteriores serão incorporados ao resultado final.

{% multi_lang_include brazeai/generative_ai/policy.md %}