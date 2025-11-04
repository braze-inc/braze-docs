---
nav_title: Divisão da decisão
article_title: Divisão da decisão 
alias: /decision_split/
page_order: 2
page_type: reference
description: "Este artigo de referência aborda como criar e usar divisões de decisão em seu Canvas."
tool: Canvas

---

# Divisão da decisão 

> O componente Decision Split do Canvas permite que você ofereça experiências personalizadas e em tempo real para seus usuários.

\![Uma etapa de divisão de decisão chamada "Push enabled?" para usuários que não estão habilitados para push e usuários que estão habilitados para push.]({% image_buster /assets/img/decision-split-1.png %}){: style="float:right;max-width:40%;margin-left:15px;margin-top:15px;margin-bottom:15px;"}

Esse componente pode ser usado para criar ramificações do Canvas com base na correspondência de um usuário com uma consulta.

## Criar uma divisão de decisão 

Para criar uma divisão de decisão em seu fluxo de trabalho, adicione uma etapa ao seu Canvas. Em seguida, arraste e solte o componente da barra lateral ou selecione o botão de adição <i class="fas fa-plus-circle"></i> na parte inferior de uma etapa e selecione **Decision Split**.

### Defina sua divisão

Como você deseja dividir seus usuários? Você pode usar [segmentos]({{site.baseurl}}/user_guide/engagement_tools/segments/) e filtros para desenhar a linha. Essencialmente, você está criando uma consulta em `true` ou `false` que avaliará seus usuários e os direcionará para uma etapa ou outra. Você deve usar pelo menos um segmento ou um filtro. Não é necessário usar um segmento e um filtro.

\![Uma etapa de divisão de decisão com o filtro "Foreground Push Enabled is true" selecionado.]({% image_buster /assets/img/define-split-2.png %})

{% alert note %}
Por padrão, os segmentos e filtros de uma etapa de divisão de decisão são verificados logo após o recebimento de uma etapa anterior, a menos que você adicione um atraso.
{% endalert %} 

## Use sua divisão

O uso de uma divisão de decisão pode ajudá-lo a distinguir caminhos para seus usuários com base em seu segmento ou em seus atributos, até mesmo se eles usam determinados canais de mensagens para receber suas mensagens!

Digamos que você esteja criando um fluxo de integração. Você pode começar com um e-mail de boas-vindas ao se inscrever. Então, dois dias depois, você deseja enviar uma mensagem push, mas somente para os usuários que estão habilitados para push. Depois disso, todos os usuários recebem outro e-mail três dias após terem se inscrito. Você também pode usar sua divisão de decisão para enviar uma mensagem in-app aos usuários que não têm o push ativado para incentivá-los a ativar o push.

Se não houver nenhuma etapa seguindo um dos caminhos, os usuários que percorrerem esse caminho sairão do Canvas. 

\![Uma etapa de divisão de decisão chamada "Push enabled?" para usuários que não estão habilitados para push e para aqueles que estão. Os usuários que não estiverem habilitados para push terão um atraso de três dias e receberão uma mensagem por e-mail. Os usuários habilitados para push terão um atraso de 1 dia, receberão uma notificação push seguida de um atraso de 2 dias e, em seguida, receberão a mesma mensagem de e-mail que os usuários que não estão habilitados para push.]({% image_buster /assets/img/use-split-onboarding-3.png %}){: style="max-width:60%"}

## Análises

Consulte a tabela a seguir para ver as descrições das análises para esta etapa:

| Métrico | Descrição |
|---|---|
| _Entrou_ | O número total de vezes que a etapa foi inserida. Se o seu Canvas tiver reelegibilidade e um usuário inserir uma etapa de divisão de decisão duas vezes, duas entradas serão registradas. |
| _Sim_ | O número de entradas que atenderam aos critérios especificados e seguiram pelo caminho "sim". |
| _Não_ | O número de entradas que não atenderam aos critérios especificados e seguiram pelo caminho "não". |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

