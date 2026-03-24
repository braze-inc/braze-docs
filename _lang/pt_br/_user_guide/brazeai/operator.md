---
nav_title: Operator
article_title: BrazeAI Operator
page_order: 7
alias: /operator/
toc_headers: h2
description: "Aprenda a acessar e usar o BrazeAI Operator<sup>TM</sup>, um assistente alimentado por IA integrado ao dashboard da Braze, incluindo suas funcionalidades e melhores práticas."
---

# BrazeAI Operator

> O BrazeAI Operator<sup>TM</sup> é um assistente alimentado por IA integrado ao dashboard. O Operator ajuda a realizar tarefas—respondendo perguntas, orientando na configuração, solucionando problemas e gerando ideias.

## Acesse o Operator

Abra o Operator de qualquer página no dashboard da Braze.  

1. Selecione **BrazeAI Operator<sup>TM</sup>** ao lado do seu perfil de usuário.

![O ícone do BrazeAI Operator ao lado de um perfil de usuário.]({% image_buster /assets/img/operator/operator_icon.png %})

{:start="2"}
2. O painel de chat do Operator se abre no lado direito da tela.

![O painel de chat do Operator.]({% image_buster /assets/img/operator/operator_chat_panel.png %})

{% alert tip %}
Maximize para expandir o painel e facilitar a leitura, ou minimize para manter o Operator disponível enquanto trabalha.  
{% endalert %} 

## Use o Operator

Descreva o que você está tentando realizar usando linguagem natural. As solicitações podem variar de perguntas simples a pedidos complexos:

- **Simples:** Por que meu Liquid não está sendo renderizado?
- **Complexo:** Como posso fazer com que a tag `abort_message` da minha mensagem inclua o atributo do usuário que causou a interrupção?

O Operator pode fornecer instruções passo a passo, links para a documentação da Braze e explicações em linguagem simples. Perguntas claras e específicas levam a respostas mais úteis. O Operator usa o [GPT-5.2](https://platform.openai.com/docs/models/gpt-5.2), que oferece raciocínio avançado e é adequado para tarefas complexas e de múltiplas etapas. 

## Melhores práticas

Trate o Operator como uma conversa, não como um mecanismo de busca. Prompts curtos e naturais funcionam melhor.

- **Seja específico:** Em vez de "Me fale sobre o Canvas", tente "Como eu uso jornadas de ação no Canvas?".  
- **Faça perguntas de acompanhamento:** Se a primeira resposta não atender à sua necessidade, peça esclarecimentos ou informações adicionais.
- **Use o contexto da página:** O Operator entende sua localização na Braze. Abra o Operator enquanto visualiza a página relevante para obter os resultados mais precisos.

## Personalize sua experiência

### Aplique diretrizes da marca

Adicione diretrizes da marca como contexto às consultas do Operator para que as respostas correspondam à voz, ao tom e à personalidade da sua marca. O Operator usa as diretrizes da marca configuradas no seu espaço de trabalho, o que ajuda a garantir uma comunicação consistente quando sugere textos ou explica recursos.

Para configurar diretrizes da marca, acesse **Configurações** > **Diretrizes da Marca**. Para mais informações, veja [Diretrizes da Marca]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines/).

![Selecionando diretrizes da marca no painel de chat do Operator.]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

### Aproveite o contexto da página

O Operator entende automaticamente sua localização na Braze e adapta as respostas com base nesse contexto. Por exemplo, quando você abre o Operator enquanto constrói um Canvas, ele pode sugerir etapas relevantes ou fornecer orientações sobre os recursos do Canvas sem que você precise explicar onde está no seu fluxo de trabalho.

Essa consciência de contexto significa que você pode fazer perguntas mais curtas e naturais, como "Como eu adiciono uma postergação?" em vez de "Como eu adiciono uma etapa de postergação em um fluxo de trabalho no Canvas?"

## Trabalhe com as respostas do Operator

### Comece com prompts sugeridos

Quando você abre o Operator, prompts sugeridos aparecem com base em tarefas comuns e na sua página atual. Selecione um para começar rapidamente ou digite sua própria pergunta personalizada.

### Entenda como o Operator pensa

O Operator mostra seus passos de raciocínio em seções recolhíveis rotuladas **Raciocinado**. Selecione o dropdown para expandir essas seções e ver como o Operator chegou a uma resposta. Isso é útil quando você quer entender a lógica por trás de uma sugestão ou verificar a abordagem.

![O dropdown "Raciocinado" recolhido em uma resposta do Operator.]({% image_buster /assets/img/operator/operator_reasoning_collapsed.png %}){:style="max-width:40%"}

### Aja com o Operator

O Operator pode propor e executar mudanças diretamente no dashboard da Braze, como preencher campos de formulário, atualizar configurações ou gerar conteúdo. Cada mudança proposta é apresentada como um cartão de ação para você revisar e aprovar antes que entre em vigor. Para mais informações sobre como isso funciona, veja [Revisando ações]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/).

## Gerencie sua sessão

### Pare uma resposta

Enquanto o Operator está gerando uma resposta, o botão **Enviar** se torna um botão **Parar**. Selecione **Parar** para encerrar a resposta antecipadamente se você precisar reformular sua pergunta ou se a resposta estiver indo na direção errada.

### Limpe seu histórico

Para começar do zero ou remover informações sensíveis da conversa, selecione **Limpar histórico de chat**. Isso remove todo o conteúdo atual e redefine o contexto da conversa.

### Forneça feedback

Na parte inferior de cada resposta, use os botões de polegar para cima ou para baixo para fornecer feedback rápido. Seu feedback ajuda a melhorar as respostas do Operator ao longo do tempo.

## Privacidade e segurança de dados

### Conformidade com a HIPAA

O Operator de IA utiliza tecnologia de conversa de múltiplas interações que atualmente não é elegível para a política de Retenção Zero de Dados da OpenAI. O Operator de IA usa a política de retenção de dados de Monitoramento de Abuso Modificado da OpenAI, mas o Operator de IA não está coberto pelo Acordo de Associado Comercial (BAA) entre a Braze e a OpenAI. Os usuários não devem solicitar ao Operator de IA que acesse Informações de Saúde Protegidas (PHI) armazenadas na Braze ou enviar PHI a este recurso.

### Provedores de modelos como subprocessadores ou provedores terceiros

Quando você usa uma integração com um provedor de LLM fornecida pela Braze por meio dos Serviços Braze ("LLM fornecido pela Braze"), os provedores de tal LLM fornecido pela Braze atuam como subprocessadores da Braze, sujeitos aos termos do Adendo de Processamento de Dados (DPA) entre você e a Braze. O BrazeAI Operator<sup>TM</sup> integra-se com a OpenAI.

### Como os dados são usados com a OpenAI

Para gerar saída de IA por meio dos recursos da BrazeAI que utilizam a OpenAI ("Saída"), a Braze enviará certas informações ("Entrada") para a OpenAI. A Entrada consiste nos seus prompts, no conteúdo exibido no dashboard e nos dados do espaço de trabalho relevantes para suas consultas. De acordo com os [compromissos da plataforma de API da OpenAI](https://openai.com/enterprise-privacy/), os dados enviados para a API da OpenAI via Braze não são usados para treinar ou melhorar os modelos da OpenAI. Entre você e a Braze, a Saída é sua propriedade intelectual. A Braze não reivindicará nenhum direito autoral sobre tal Saída. A Braze não oferece garantia de qualquer tipo em relação a qualquer conteúdo gerado por IA, incluindo a Saída.

## Próximos passos

- [Revisando ações]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/): Saiba como revisar e aprovar as alterações propostas pelo Operator
- [Abrir tickets de suporte]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets/): Abra tickets de suporte diretamente pelo Operator
- [Resolução de problemas]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting/): Consulte problemas comuns e soluções