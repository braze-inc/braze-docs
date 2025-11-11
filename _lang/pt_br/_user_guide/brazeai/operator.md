---
nav_title: Operador
article_title: Operador BrazeAI
page_order: 0.7
alias: /operator/
description: "Este artigo de referência cobre o Operador BrazeAI, um assistente alimentado por IA integrado ao painel da Braze."
---

# Operador BrazeAI<sup>TM</sup>

> O Operador BrazeAI<sup>TM</sup> é um assistente alimentado por IA integrado ao painel da Braze. O operador ajuda você a encontrar respostas, solucionar problemas e aprender as melhores práticas sem sair do seu fluxo de trabalho.

{% alert important %}
O Operador BrazeAI<sup>TM</sup> está atualmente em uma beta privada com funcionalidade limitada. Para ajuda para começar, entre em contato com seu gerente de sucesso do cliente.
{% endalert %}

## Sobre o Operador

O operador é seu assistente de IA integrado no painel da Braze. Ele ajuda você a se mover mais rápido respondendo perguntas, sugerindo próximos passos e orientando você em tarefas—tudo sem sair do seu fluxo de trabalho.

Durante a beta, o operador suporta apenas o modo **Ask**. Você pode:

- Obter respostas da documentação da Braze
- Solucionar problemas usando [contexto ciente da página](#page-aware-context)
- Aprender melhores práticas e orientações de integração

## Como acessar o Operador

Você pode abrir o Operador de qualquer página no painel da Braze.  

1. Selecione **BrazeAI<sup>TM</sup> Operador**, ao lado do seu perfil de usuário.

\![O ícone do Operador BrazeAI ao lado de um perfil de usuário.]({% image_buster /assets/img/operator/operator_profile.png %}){:style="max-width:60%"}

{: start="2"}
2\. O painel de chat do Operador será aberto no lado direito da tela.

\![O painel de chat para o Operador.]({% image_buster /assets/img/operator/operator_panel.png %})

{% alert tip %}
Tente maximizar para expandir o painel para uma leitura mais fácil, ou minimizá-lo para manter o Operador disponível enquanto você continua trabalhando.  
{% endalert %}

## Como falar com o Operador

Use prompts para se comunicar com o Operador. A melhor abordagem é falar naturalmente—como você faria com um colega de trabalho ou um amigo. Seus prompts podem variar de perguntas simples a solicitações complexas:

- **Simples:** Como posso garantir que os usuários não recebam e-mails de abandono de carrinho enquanto ainda estão no site fazendo compras?
- **Complexo:** Como posso fazer com que a tag `abort_message` da minha mensagem inclua o atributo do usuário que causou a interrupção?

O Operador pode fornecer instruções passo a passo, links para a documentação do Braze e explicações em linguagem simples. Quanto mais clara e específica for sua pergunta, mais útil será a resposta. 

### Melhores práticas

Pense no Operador como uma conversa, não como um motor de busca. Prompts curtos e naturais geralmente funcionam melhor.

- **Seja específico:** Em vez de "Fale-me sobre o Canvas", tente "Como uso os Caminhos de Ação no Canvas?".  
- **Use acompanhamentos:** Se a primeira resposta não for o que você precisa, faça perguntas de esclarecimento. O operador pode refinar as respostas.
- **Confie no contexto:** O operador sabe em qual página você está no Braze. Abra o operador enquanto você está na página com a qual está trabalhando para obter os resultados mais relevantes.

## Recursos

O operador inclui os seguintes recursos durante a versão beta:

### Contexto ciente da página

O operador entende a página em que você está trabalhando atualmente no Braze e pode adaptar as respostas com base nesse contexto. Por exemplo, se você abrir o operador enquanto constrói um Canvas, ele pode sugerir etapas ou fornecer orientações relevantes ao Canvas, sem que você precise explicar onde está. 

### Sugestões de prompts

Quando você abrir o operador, verá alguns prompts sugeridos para ajudá-lo a começar. Selecione um para começar ou digite sua própria pergunta.

### Visualizando raciocínio

O operador mostra suas etapas de raciocínio em seções colapsáveis rotuladas **Raciocinado**. Selecione o menu suspenso para expandir essas seções e ver como o operador chegou a uma resposta.

\![Menu suspenso para "Raciocinado" expandido com mais detalhes sobre como o operador respondeu.]({% image_buster /assets/img/operator/operator_reasoning.png %}){:style="max-width:60%"}

### Ações sugeridas

Em alguns casos, o Operador recomendará os próximos passos e fornecerá links diretos para as páginas relevantes no seu painel do Braze. Por exemplo, se você perguntar sobre taxas de rejeição de e-mail, o Operador pode linká-lo para a sua página **Centro de Entregabilidade**. Esses atalhos ajudam você a agir mais rápido sem precisar navegar manualmente.

### Parando a geração

Enquanto o Operador está gerando uma resposta, o botão **Enviar** se torna um botão **Parar**. Se você quiser encerrar a resposta mais cedo, selecione **Parar**.

### Limpando o histórico de chat

Para redefinir sua conversa, selecione **Limpar histórico de chat**. Isso remove o conteúdo atual para que você possa começar do zero.

### Maximizando e minimizando o painel

Você pode usar o botão **maximizar** para expandir o Operador para uma leitura mais fácil, ou **minimizar** para manter o painel escondido enquanto você continua trabalhando no Braze.

### Enviando feedback

Na parte inferior de cada resposta, use os botões de polegar para cima ou para baixo para fornecer feedback rápido. Isso ajuda a melhorar as respostas do Operador.

## Solução de problemas

| Problema | Solução de problemas |
| --- | --- |
| Sem resposta | Tente atualizar a página e reabrir o painel do Operador. |
| Respostas fora do tópico | Reformule sua pergunta de forma mais específica. Mencione o recurso ou fluxo de trabalho sobre o qual você está perguntando. |
| Mensagens de erro | Se o Operator não conseguir transmitir conteúdo para você, pode aparecer um prompt de "Tente novamente". O Operator pode estar temporariamente indisponível ou sua conexão foi interrompida. Tente novamente após alguns minutos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Limitações

O Operator foi projetado para ajudá-lo a navegar no Braze e realizar o trabalho de forma mais eficiente, mas existem alguns limites atuais a serem considerados:

### Sem acesso aos seus dados

Embora o Operator tenha acesso ao contexto do trabalho que você está fazendo no Braze, ele não pode consultar ou retornar respostas sobre os dados da sua empresa armazenados no Braze. Por exemplo, ele **não pode** responder a solicitações como:

- "Me dê uma lista de todas as minhas campanhas de e-mail do ano passado."
- "Mostre-me quais segmentos tiveram o maior engajamento no último trimestre."
- "Analise meu desempenho no Canvas e sugira melhorias."

### Estabilidade beta

Como uma beta privada, o Operator pode ter erros ocasionais, interrupções ou recursos incompletos.

Se você não tiver certeza se uma pergunta é suportada, tente formulá-la em termos de como o Operator pode ajudá-lo a navegar ou realizar ações dentro do painel do Braze, em vez de puxar análises ou dados históricos.
