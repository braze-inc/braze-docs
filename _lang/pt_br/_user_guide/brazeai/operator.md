---
nav_title: Operador
article_title: Operador BrazeAI
page_order: 0.7
alias: /operator/
description: "Este artigo de referência aborda o BrazeAI Operator, um assistente com IA incorporado ao dashboard do Braze."
---

# Operador <sup>BrazeAITM</sup> 

> O <sup>BrazeAITM</sup> Operator é um assistente com IA incorporado ao dashboard do Braze. O operador fornece respostas, orientação para solução de problemas e práticas recomendadas em seu fluxo de trabalho.

{% alert important %}
O <sup>BrazeAITM</sup> Operator está em uma versão beta privada com funcionalidade limitada. Para obter ajuda para começar, entre em contato com o gerente de sucesso do cliente.
{% endalert %}

## Sobre o operador

O Operator é um assistente de IA incorporado no dashboard do Braze. Ele responde a perguntas, sugere as próximas etapas e o orienta nas tarefas - tudo dentro do seu fluxo de trabalho.

Durante a versão beta, o Operator suporta apenas o modo **Ask**. Você pode:

- Obtenha respostas da documentação da Braze
- Solucionar problemas usando [o contexto com reconhecimento de página](#page-aware-context)
- Aprenda as melhores práticas e orientações sobre integração

### Modelar provedores como subprocessadores ou provedores terceirizados

Quando o Cliente utilizar uma integração com um provedor de LLM fornecido pela Braze por meio dos Serviços Braze ("LLM fornecido pela Braze"), os provedores de tal LLM fornecido pela Braze atuarão como Subprocessadores da Braze, sujeitos aos termos do Adendo de Processamento de Dados (DPA) entre o Cliente e a Braze. O BrazeAI Operator se integra ao OpenAI.

Se o Cliente optar por trazer sua própria chave de API para integrar-se ao Braze IA Operator, o provedor da própria inscrição LLM do Cliente será considerado um Provedor Terceirizado, conforme definido no contrato entre o Cliente e o Braze. 

### Como meus dados são usados e enviados para a OpenAI?

Para gerar resultados de IA por meio dos recursos de IA do Braze que o Braze identifica como aproveitando a OpenAI ("Resultado"), o Braze enviará seus prompts, o conteúdo exibido no dashboard e os dados do espaço de trabalho relevantes para suas consultas, conforme aplicável ("Entrada") para a OpenAI. De acordo com [os compromissos da plataforma API da OpenAI](https://openai.com/enterprise-privacy/), os dados enviados à API da OpenAI via Braze não são usados para treinar ou aprimorar os modelos da OpenAI. Entre você e a Braze, a saída é sua propriedade intelectual. A Braze não fará nenhuma reivindicação de propriedade de direitos autorais sobre tais Produtos. A Braze não oferece nenhuma garantia de qualquer tipo com relação a qualquer conteúdo gerado por IA em geral, incluindo o Resultado.

## Como acessar o Operador

Você pode abrir o Operator em qualquer página do dashboard do Braze.  

1. Selecione **<sup>BrazeAITM</sup> Operator**, ao lado do seu perfil de usuário.

![O ícone do Operador BrazeAI ao lado de um perfil de usuário.]({% image_buster /assets/img/operator/operator_profile.png %}){:style="max-width:60%"}

{: start="2"}
2\. O painel de bate-papo do Operator será aberto no lado direito da tela.

![O painel de bate-papo do Operator.]({% image_buster /assets/img/operator/operator_panel.png %})

{% alert tip %}
Tente maximizar para expandir o painel e facilitar a leitura, ou minimizá-lo para manter o Operator disponível enquanto você continua trabalhando.  
{% endalert %} 

## Como falar com a operadora

Use prompts para se comunicar com a Operadora. A melhor abordagem é falar naturalmente, como faria com um colega de trabalho ou um amigo. Seus prompts podem variar de perguntas simples a solicitações complexas:

- **Simples:** Como posso garantir que os usuários não recebam e-mails de abandono de carrinho enquanto ainda estiverem comprando no site?
- **Complexo:** Como posso fazer com que a tag `abort_message` da minha mensagem inclua a atribuição do usuário que causou a interrupção?

O operador pode fornecer instruções passo a passo, links para documentos do Braze e explicações em linguagem simples. Quanto mais clara e específica for sua pergunta, mais útil será a resposta. 

### Melhores práticas

Pense no Operator como uma conversa, não como um mecanismo de busca. Geralmente, os prompts curtos e naturais funcionam melhor.

- **Seja específico:** Em vez de "Tell me about Canvas" (Fale-me sobre o Canvas), tente "How do I use Action Jornadas of Action in Canvas?" (Como usar jornadas de ação no Canvas?).  
- **Use follow-ups:** Se a primeira resposta não for a que você precisa, faça perguntas esclarecedoras. O operador pode refinar as respostas.
- **Confie no contexto:** O operador sabe em que página você está no Braze. Abra o Operator enquanto estiver na página em que está trabalhando para obter os resultados mais relevantes.

## Recursos

O Operator inclui os seguintes recursos durante a versão beta:

### Modelos GPT

Você pode selecionar entre esses modelos de GPT para usar em diferentes tipos de solicitação com o Operator:

- [GPT-5 nano](https://platform.openai.com/docs/models/gpt-5-nano)
- [GPT-5 mini](https://platform.openai.com/docs/models/gpt-5-mini)
- [GPT-5](https://platform.openai.com/docs/models/gpt-5)
- [GPT-5.1](https://platform.openai.com/docs/models/gpt-5.1) (padrão)

![Menu suspenso para a escolha de diferentes modelos de GPT.]({% image_buster /assets/img/operator/operator_model.png %}){:style="max-width:70%"}

### Contexto com reconhecimento de página

O Operator entende a página em que você está trabalhando no Braze e pode adaptar as respostas com base nesse contexto. Por exemplo, se você abrir o Operator durante a criação de um Canvas, ele poderá sugerir etapas ou fornecer orientações relevantes para o Canvas sem que você precise explicar onde está. 

### Sugestões

Ao abrir o Operator, você verá alguns prompts sugeridos para ajudá-lo a começar. Selecione uma para começar ou digite sua própria pergunta.

### Visualizando o raciocínio

O operador mostra suas etapas de raciocínio em seções recolhíveis rotuladas como **Reasoned**. Selecione o menu suspenso para expandir essas seções e ver como o Operador chegou a uma resposta.

![O menu suspenso para "Reasoned" foi ampliado com mais detalhes sobre como o Operador respondeu.]({% image_buster /assets/img/operator/operator_reasoning.png %}){:style="max-width:50%"}

### Ações sugeridas

Em alguns casos, o Operator recomendará as próximas etapas e fornecerá links diretos para as páginas relevantes em seu dashboard do Braze. Por exemplo, se você perguntar sobre as taxas de bounce de e-mail, a Operator poderá vinculá-lo à página **do Deliverability Center**. Esses atalhos ajudam você a agir mais rapidamente sem precisar navegar manualmente.

### Interrupção da geração

Enquanto o operador estiver gerando uma resposta, o botão **Enviar** se torna um botão **Parar**. Se quiser encerrar a resposta mais cedo, selecione **Stop (Parar**).

### Limpando o histórico de bate-papo

Para redefinir sua conversa, selecione **Limpar histórico de bate-papo**. Isso remove o conteúdo atual para que você possa começar do zero.

### Maximização e minimização do painel

Você pode usar o botão **maximizar** para expandir o Operator para facilitar a leitura ou **minimizar** para manter o painel escondido enquanto você continua trabalhando no Braze.

### Envio de feedback

Na parte inferior de cada resposta, use os botões de polegar para cima ou polegar para baixo para fornecer feedback rápido. Isso ajuda a melhorar as respostas do operador.

## Solução de problemas

| Problema | Solução de problemas |
| --- | --- |
| Sem resposta | Tente atualizar a página e reabrir o painel do operador. |
| Respostas fora do tópico | Reformule sua pergunta de forma mais específica. Mencione o recurso ou o fluxo de trabalho sobre o qual você está perguntando. |
| Envio de mensagens de erro | Se a Operadora não conseguir transmitir o conteúdo para você, talvez apareça a mensagem "Tente novamente". A operadora pode estar temporariamente indisponível ou sua conexão foi interrompida. Tente novamente após alguns minutos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Limitações

O Operator foi projetado para ajudá-lo a navegar no Braze e a trabalhar com mais eficiência, mas há alguns limites atuais que devem ser lembrados:

### Sem acesso aos seus dados

Embora o Operator tenha acesso ao contexto do trabalho que você está fazendo no Braze, ele não pode consultar ou retornar respostas sobre os dados da sua empresa armazenados no Braze. Por exemplo, ele **não** pode responder a solicitações como:

- "Dê-me uma lista de todas as minhas campanhas de e-mail do ano passado."
- "Mostre-me quais segmentos tiveram o maior engajamento no último trimestre."
- "Analisar minha performance no Canva e sugerir melhorias."

### Estabilidade beta

Como uma versão beta privada, o Operator pode apresentar erros ocasionais, interrupções ou recursos incompletos.

Se não tiver certeza de que uma pergunta é suportada, tente formulá-la em termos de como o Operator pode ajudá-lo a navegar ou realizar ações dentro do dashboard do Braze, em vez de extrair análises ou dados históricos.

### Número de mensagens enviadas

Há um limite de quantas mensagens você pode enviar ao Operador. Recomendamos usar o GPT-5 mini ou GPT-5 nano padrão para suas consultas e usar o GPT-5 criteriosamente para tarefas mais complexas.
