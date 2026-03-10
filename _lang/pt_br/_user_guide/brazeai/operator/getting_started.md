---
nav_title: Começar
article_title: Começar a usar o BrazeAI Operator<sup>TM</sup>
page_order: 1
description: "Saiba como acessar e usar o BrazeAI Operator<sup>TM</sup>, o assistente de IA integrado ao dashboard da Braze, incluindo recursos e melhores práticas."
---

# Começar a usar o BrazeAI Operator

> Saiba como acessar e usar o BrazeAI Operator<sup>TM</sup>, seu assistente de IA integrado ao dashboard, incluindo recursos e melhores práticas.

## Acessar o Operator

Abra o Operator em qualquer página do dashboard da Braze.

1. Selecione **BrazeAI Operator<sup>TM</sup>** ao lado do seu perfil de usuário.

![O ícone do BrazeAI Operator ao lado de um perfil de usuário.]({% image_buster /assets/img/operator/operator_icon.png %})

{:start="2"}
2. O painel de chat do Operator será aberto no lado direito da tela.

![O painel de chat do Operator.]({% image_buster /assets/img/operator/operator_chat_panel.png %})

{% alert tip %}
Maximize o painel para leitura mais fácil ou minimize para manter o Operator disponível enquanto trabalha.
{% endalert %}

## Usar o Operator

Descreva o que você quer fazer em linguagem natural. Os prompts podem variar de perguntas simples a solicitações complexas:

- **Simples:** Por que meu Liquid não está renderizando?
- **Complexo:** Como fazer a tag `abort_message` da minha mensagem incluir o atributo de usuário que causou o abort?

O Operator pode fornecer instruções passo a passo, links para a documentação da Braze e explicações em linguagem clara. Perguntas claras e específicas levam a respostas mais úteis. O Operator usa [GPT-5.2](https://platform.openai.com/docs/models/gpt-5.2), que oferece raciocínio forte e é adequado para tarefas complexas e em várias etapas.

## Melhores práticas

Trate o Operator como uma conversa, não como um mecanismo de busca. Prompts curtos e naturais funcionam melhor.

- **Seja específico:** Em vez de "Fale sobre Canvas", tente "Como usar Action Paths no Canvas?".
- **Faça perguntas de acompanhamento:** Se a primeira resposta não atender à sua necessidade, peça esclarecimentos ou detalhes adicionais.
- **Use o contexto da página:** O Operator entende sua localização na Braze. Abra o Operator na página relevante para os resultados mais precisos.

## Personalizar sua experiência

### Aplicar diretrizes de marca

Adicione diretrizes de marca como contexto às consultas do Operator para que as respostas correspondam à voz, tom e personalidade da sua marca. O Operator usa as diretrizes de marca configuradas no seu espaço de trabalho, o que ajuda a garantir mensagens consistentes quando sugere cópias ou explica recursos.

Para configurar diretrizes de marca, vá em **Configurações** > **Diretrizes de marca**. Para mais informações, consulte [Diretrizes de marca]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines/).

![Seleção de diretrizes de marca no painel de chat do Operator.]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

### Aproveitar o contexto da página

O Operator entende automaticamente sua localização na Braze e adapta as respostas a esse contexto. Por exemplo, ao abrir o Operator enquanto constrói um Canvas, ele pode sugerir etapas relevantes ou dar orientação sobre recursos do Canvas sem que você precise explicar onde está no fluxo de trabalho.

Essa consciência de contexto permite que você faça perguntas mais curtas e naturais, como "Como adicionar um atraso?" em vez de "Como adicionar uma etapa de atraso em um fluxo de trabalho do Canvas?".

## Trabalhar com as respostas do Operator

### Começar com sugestões de entrada

Ao abrir o Operator, aparecem sugestões com base em tarefas comuns e na sua página atual. Selecione uma para começar rápido ou digite sua própria pergunta.

### Ver como o Operator pensa

O Operator mostra seu raciocínio em áreas expansíveis rotuladas **Reasoned**. Abra o menu suspenso para expandir essas áreas e ver como o Operator chegou a uma resposta.

![O menu suspenso "Reasoned" recolhido em uma resposta do Operator.]({% image_buster /assets/img/operator/operator_reasoning_collapsed.png %}){:style="max-width:40%"}

### Executar ações com o Operator

O Operator pode sugerir e executar alterações diretamente no dashboard da Braze, por exemplo preencher campos de formulário, ajustar configurações ou gerar conteúdo. Cada alteração sugerida é exibida como um cartão de ação para revisão e aprovação. Para mais detalhes, consulte [Revisar ações]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/).

## Gerenciar sua sessão

### Encerrar uma resposta

Enquanto o Operator gera uma resposta, o botão **Enviar** muda para **Parar**. Selecione **Parar** para encerrar a resposta antes do fim se quiser reformular a pergunta ou se a resposta estiver indo na direção errada.

### Limpar o histórico

Para recomeçar ou remover informações sensíveis da conversa, selecione **Limpar histórico do chat**. Isso exclui o conteúdo atual e redefine o contexto da conversa.

### Dar feedback

Use os botões de polegar para cima ou para baixo abaixo de cada resposta para feedback rápido. Seu feedback ajuda a melhorar as respostas do Operator.

## Próximos passos

- [Revisar ações]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/) – Como revisar e aprovar alterações sugeridas pelo Operator
- [Solução de problemas]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting/) – Problemas comuns e soluções
