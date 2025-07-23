---
nav_title: Controle de qualidade do conteúdo com IA
article_title: Controle de qualidade do conteúdo com IA
page_order: 10
description: "Este artigo de referência aborda como realizar a garantia de qualidade do conteúdo de sua mensagem com IA diretamente do criador de mensagens."
---

# Controle de qualidade do conteúdo com IA

> Saiba como realizar a garantia de qualidade do conteúdo de suas mensagens com IA diretamente do criador de mensagens.

O Content QA with IA usa os recursos do GPT e do OpenAI para realizar verificações no conteúdo da sua mensagem, garantindo que ela siga os padrões de qualidade ao identificar elementos ineficazes, como erros de ortografia, problemas gramaticais, tom inadequado e linguagem ofensiva. Você pode acessar esse recurso na guia **Teste** ao criar uma mensagem push, SMS ou no app em uma campanha ou no Canva.

## Principais recursos

O Controle de qualidade do conteúdo com IA oferece os seguintes recursos principais para aprimorar a qualidade do conteúdo de suas mensagens:

- **Verificação ortográfica e gramatical:** Verifica automaticamente se há erros de ortografia e gramática em sua mensagem. Ele sugere correções e fornece recomendações para melhorar a precisão geral do conteúdo.
- **Análise de tom:** Avalia o tom da mensagem para identificar possíveis problemas. Isso ajuda a garantir que o tom pretendido se alinhe ao estilo de comunicação desejado e ajuda a evitar mal-entendidos ou ofensas não intencionais.
- **Detecção de linguagem ofensiva:** Examina sua mensagem em busca de qualquer linguagem potencialmente ofensiva ou inadequada, permitindo que você revise seu conteúdo e mantenha uma comunicação respeitosa.
- **Verificação acidental de conteúdo:** Detecta qualquer inclusão de código, linguagem de marcação ou mensagens de teste que possam ter sido adicionadas de forma não intencional, incluindo qualquer código Liquid que não tenha sido renderizado para um usuário teste.

## Acessando o controle de qualidade do conteúdo com IA

{% alert note %}
O controle de qualidade de conteúdo com IA só está disponível para canais push e SMS no momento.
{% endalert %}

Para acessar o verificador de conteúdo, siga estas etapas:

1. Depois de criar uma mensagem push ou SMS, navegue até a guia **Teste**.
2. Localize a seção **Controle de qualidade do conteúdo com IA**.
3. Clique em **Test Content (Testar conteúdo**).

![Conteúdo da seção QA com IA da guia Teste.][1]{: style="max-width:60%"}

### Suporte a idiomas

O GPT é capaz de entender [vários idiomas](https://openai.com/research/gpt-4#:~:text=GPT%2D4%203%2Dshot%20accuracy%20on%20MMLU%20across%20languages), embora a OpenAI não ofereça suporte oficial a eles. A Braze não passa nenhuma informação adicional sobre o idioma ou a região de sua cópia quando o conteúdo da mensagem é enviado à OpenAI; portanto, cabe ao GPT fazer essa determinação.

Os resultados podem variar dependendo do idioma em que você está escrevendo.

## Dicas para uso eficaz

Considere as seguintes dicas para aproveitar ao máximo o recurso Controle de qualidade do conteúdo com IA:

- **Revise sua mensagem:** Embora o verificador de conteúdo possa ajudar a identificar erros, ainda é essencial revisar seu conteúdo manualmente. Confie nas sugestões geradas pela IA como um guia útil, mas use seu julgamento para garantir a precisão.
- **Compreender a análise do tom:** Os resultados da análise de tom são subjetivos e baseados no entendimento do modelo IA. Embora eles possam fornecer insights úteis, considere o tom pretendido e o contexto da conversa para fazer os ajustes apropriados.
- **Verifique novamente a linguagem ofensiva sinalizada:** A detecção de linguagem ofensiva foi projetada para ser robusta, mas pode ocasionalmente sinalizar falsos positivos. Analise cuidadosamente as seções sinalizadas e faça as alterações apropriadas conforme necessário.

## Como meus dados são usados e enviados para a OpenAI?

Para verificar o conteúdo de sua mensagem, a Braze a enviará para a plataforma de API da OpenAI. Todas as consultas enviadas à OpenAI pela Braze são anônimas, o que significa que a OpenAI não poderá identificar de quem a consulta foi enviada, a menos que você inclua informações exclusivamente identificáveis no conteúdo da mensagem que fornecer. Conforme detalhado nos [Compromissos da Plataforma de API da OpenAI](https://openai.com/policies/api-data-usage-policies), os dados enviados à API da OpenAI via Braze não são usados para treinar ou melhorar seus modelos e serão excluídos após 30 dias. Certifique-se de aderir às políticas da OpenAI relevantes para você, que podem incluir [a Política de Uso](https://openai.com/policies/usage-policies) e a [Política de Compartilhamento e Publicação](https://openai.com/policies/sharing-publication-policy). A Braze não oferece nenhuma garantia de qualquer tipo com relação a qualquer conteúdo gerado por IA.

[1]: {% image_buster /assets/img/content_qa_ai.png %}
