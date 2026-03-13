---
nav_title: Operador
article_title: BrazeAI Operator
page_order: 7
alias: /operator/
toc_headers: h2
description: "Aprenda a acessar e usar o BrazeAI Operator<sup>TM</sup>, um assistente alimentado por IA integrado ao dashboard do Braze, incluindo suas funcionalidades e melhores práticas."
---

# BrazeAI Operator

> O BrazeAI Operator<sup>TM</sup> é um assistente alimentado por IA integrado ao dashboard. O Operator ajuda a realizar tarefas—respondendo perguntas, orientando na configuração, solucionando problemas e gerando ideias.

## Acesse o Operator

Abra o Operator de qualquer página no dashboard do Braze.  

1. Selecione **BrazeAI Operator<sup>TM</sup>** ao lado do seu perfil de usuário.

![O ícone do BrazeAI Operator ao lado de um perfil de usuário.]({% image_buster /assets/img/operator/operator_icon.png %})

{:start="2"}
2\. O painel de chat do Operator se abre no lado direito da tela.

![O painel de chat do Operator.]({% image_buster /assets/img/operator/operator_chat_panel.png %})

{% alert tip %}
Maximize para expandir o painel para uma leitura mais fácil, ou minimize para manter o Operator disponível enquanto trabalha.  
{% endalert %} 

## Use o Operator

Descreva o que você está tentando realizar usando linguagem natural. As solicitações podem variar de perguntas simples a pedidos complexos:

- **Simples:** Por que meu Liquid não está sendo renderizado?
- **Complexo:** Como posso fazer com que a tag `abort_message` da minha mensagem inclua o atributo do usuário que causou a interrupção?

O Operator pode fornecer instruções passo a passo, links para a documentação do Braze e explicações em linguagem simples. Perguntas claras e específicas levam a respostas mais úteis. O Operator usa [GPT-5.2](https://platform.openai.com/docs/models/gpt-5.2), que oferece um raciocínio forte e é adequado para tarefas complexas e de múltiplas etapas. 

## Melhores práticas

Trate o Operador como uma conversa, não como um motor de busca. Prompts curtos e naturais funcionam melhor.

- **Seja específico:** Em vez de "Me fale sobre o Canvas", tente "Como eu uso Jornadas de Ação no Canvas?".  
- **Faça perguntas de acompanhamento:** Se a primeira resposta não atender à sua necessidade, peça esclarecimentos ou detalhes adicionais.
- **Use contexto ciente da página:** O Operador entende sua localização no Braze. Abra o Operador enquanto visualiza a página relevante para obter os resultados mais precisos.

## Personalize sua experiência

### Aplique diretrizes de marca

Adicione diretrizes de marca como contexto às consultas do Operador para que as respostas correspondam à voz, tom e personalidade da sua marca. O Operador usa as diretrizes de marca configuradas no seu espaço de trabalho, o que ajuda a garantir uma comunicação consistente quando sugere textos ou explica recursos.

Para configurar diretrizes de marca, vá para **Configurações** > **Diretrizes de Marca**. Para mais informações, veja [Diretrizes de Marca]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines/).

![Selecionando diretrizes de marca no painel de chat do Operador.]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

### Aproveite o contexto ciente da página

O Operador entende automaticamente sua localização no Braze e adapta as respostas com base nesse contexto. Por exemplo, quando você abre o Operador enquanto constrói um Canvas, ele pode sugerir etapas relevantes ou fornecer orientações sobre os recursos do Canvas sem que você precise explicar onde está no seu fluxo de trabalho.

Essa consciência de contexto significa que você pode fazer perguntas mais curtas e naturais, como "Como eu adiciono uma postergação?" em vez de "Como eu adiciono uma etapa de postergação em um fluxo de trabalho no Canvas?"

## Trabalhe com as respostas do Operador

### Comece com prompts sugeridos

Quando você abre o Operador, prompts sugeridos aparecem com base em tarefas comuns e na sua página atual. Selecione um para começar rapidamente ou digite sua própria pergunta personalizada.

### Entenda como o Operador pensa

O Operador mostra seus passos de raciocínio em seções colapsáveis rotuladas **Raciocinado**. Selecione o dropdown para expandir essas seções e ver como o Operador determinou uma resposta. Isso é útil quando você quer entender a lógica por trás de uma sugestão ou verificar a abordagem.

![O dropdown "Raciocinado" colapsado em uma resposta do Operador.]({% image_buster /assets/img/operator/operator_reasoning_collapsed.png %}){:style="max-width:40%"}

### Aja com o Operador

O Operador pode propor e executar mudanças diretamente no dashboard do Braze, como preencher campos de formulário, atualizar configurações ou gerar conteúdo. Cada mudança proposta é apresentada como um cartão de ação para você revisar e aprovar antes que entre em vigor. Para mais informações sobre como isso funciona, veja [Revisando ações]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/).

## Gerencie sua sessão

### Pare uma resposta

Enquanto o Operador está gerando uma resposta, o botão **Enviar** se torna um botão **Parar**. Selecione **Parar** para encerrar a resposta mais cedo se você precisar reformular sua pergunta ou se a resposta estiver indo na direção errada.

### Limpe seu histórico

Para começar do zero ou remover informações sensíveis da conversa, selecione **Limpar histórico de chat**. Isso remove todo o conteúdo atual e redefine o contexto da conversa.

### Fornecer feedback

Na parte inferior de cada resposta, use os botões de polegar para cima ou para baixo para fornecer feedback rápido. Seu feedback ajuda a melhorar as respostas do Operador ao longo do tempo.

## Privacidade e segurança de dados

### Conformidade com a HIPAA

O Operador de IA utiliza tecnologia de conversa de múltiplas interações que atualmente não é elegível para a política de Retenção Zero de Dados da OpenAI. O Operador de IA usa a política de retenção de dados de Monitoramento de Abuso Modificado da OpenAI, mas o Operador de IA não está coberto pelo Acordo de Associado Comercial (BAA) entre a Braze e a OpenAI. Os usuários não devem solicitar ao Operador de IA que acesse Informações de Saúde Protegidas (PHI) armazenadas na Braze ou enviar PHI a este recurso.

### Provedores de modelos como sub-processadores ou provedores de terceiros

Quando você usa uma integração com um provedor de LLM fornecida pela Braze através dos Serviços Braze ("LLM fornecido pela Braze"), os provedores de tal LLM fornecido pela Braze atuam como Sub-processadores da Braze, sujeitos aos termos do Adendo de Processamento de Dados (DPA) entre você e a Braze. Operador BrazeAI<sup>TM</sup> integra-se com a OpenAI.

### Como os dados são usados com a OpenAI

Para gerar saída de IA através dos recursos BrazeAI que aproveitam a OpenAI ("Saída"), a Braze enviará certas informações ("Entrada") para a OpenAI. A Entrada consiste em seus prompts, o conteúdo exibido no dashboard e dados do espaço de trabalho relevantes para suas consultas. De acordo com [os compromissos da plataforma API da OpenAI](https://openai.com/enterprise-privacy/), os dados enviados para a API da OpenAI via Braze não são usados para treinar ou melhorar os modelos da OpenAI. Entre você e a Braze, a Saída é sua propriedade intelectual. A Braze não reivindicará nenhum direito autoral sobre tal Saída. A Braze não oferece garantia de qualquer tipo em relação a qualquer conteúdo gerado por IA, incluindo a Saída.

## Próximos passos

- [Revisando ações]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/): Saiba como revisar e aprovar as alterações propostas pelo Operador
- [Resolução de Problemas]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting/): Referência a problemas comuns e soluções
