---
nav_title: QA de Conteúdo
article_title: Controle de qualidade do conteúdo com IA
page_order: 4
description: "Este artigo de referência aborda como realizar a garantia de qualidade do conteúdo de sua mensagem com IA diretamente do criador de mensagens."
---

# QA de Conteúdo com BrazeAI<sup>TM</sup>

> Aprenda a fazer QA do seu conteúdo com BrazeAI<sup>TM</sup>, para que você possa identificar erros de ortografia, problemas gramaticais, tom inadequado ou linguagem ofensiva—antes de enviar.

## Recursos suportados

Os seguintes recursos são suportados para ajudar a melhorar a qualidade do seu conteúdo:

| Recurso                     | Descrição |
|----------------------------|-------------|
| Verificação de ortografia e gramática | Verifica automaticamente se há erros de ortografia e gramática em sua mensagem. Ele sugere correções e fornece recomendações para melhorar a precisão geral do conteúdo. |
| Análise de tom              | Avalia o tom da mensagem para identificar possíveis problemas. Isso ajuda a garantir que o tom pretendido se alinhe ao estilo de comunicação desejado e ajuda a evitar mal-entendidos ou ofensas não intencionais. |
| Detecção de linguagem ofensiva | Examina sua mensagem em busca de qualquer linguagem potencialmente ofensiva ou inadequada, permitindo que você revise seu conteúdo e mantenha uma comunicação respeitosa. |
| Verificação de conteúdo acidental   | Detecta qualquer inclusão de código, linguagem de marcação ou mensagens de teste que possam ter sido adicionadas involuntariamente, incluindo qualquer código Liquid que não foi renderizado para um usuário teste. |
| Suporte multilíngue     | Embora não seja oficialmente suportado pela OpenAI, o GPT pode entender [várias línguas](https://openai.com/research/gpt-4#:~:text=GPT%2D4%203%2Dshot%20accuracy%20on%20MMLU%20across%20languages). Tenha em mente que o Braze não passa nenhuma informação sobre o idioma ou localidade do seu texto quando é enviado para a OpenAI, então seus resultados podem variar dependendo do idioma que você está escrevendo. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Usando BrazeAI<sup>TM</sup> para QA de conteúdo

{% alert note %}
Este recurso está disponível apenas para canais de SMS, push Android e push iOS neste momento.
{% endalert %}

1. Após compor uma mensagem de push móvel ou SMS, navegue até a aba **Teste**.
2. Localize a seção **Controle de qualidade do conteúdo com IA**.
3. Clique em **Test Content (Testar conteúdo**).

![QA de Conteúdo com a seção de IA da aba Teste.]({% image_buster /assets/img/content_qa_ai.png %})

## Melhores práticas

Considere o seguinte, para que você possa aproveitar ao máximo o QA de Conteúdo com IA:

- **Revise sua mensagem:** Embora o verificador de conteúdo possa ajudar a identificar erros, ainda é essencial revisar seu conteúdo manualmente. Confie nas sugestões geradas pela IA como um guia útil, mas use seu julgamento para garantir a precisão.
- **Compreender a análise do tom:** Os resultados da análise de tom são subjetivos e baseados no entendimento do modelo IA. Embora eles possam fornecer insights úteis, considere o tom pretendido e o contexto da conversa para fazer os ajustes apropriados.
- **Verifique novamente a linguagem ofensiva sinalizada:** A detecção de linguagem ofensiva foi projetada para ser robusta, mas pode ocasionalmente sinalizar falsos positivos. Analise cuidadosamente as seções sinalizadas e faça as alterações apropriadas conforme necessário.

{% multi_lang_include brazeai/generative_ai/policy.md %}
