---
nav_title: "Aprovações do público-alvo"
article_title: "Aprovações do público-alvo"
permalink: "/target_approvals/"
hidden: true
description: "Este artigo descreve como usar aprovações de público-alvo para campanhas e Canvas com um grande volume de envio."
---

# Aprovação do público-alvo

> Esta página aborda como configurar aprovações de público-alvo para suas regras de envio de mensagens. Usando a aprovação do público-alvo, você pode definir limites de volume para campanhas e Canvas para exigir aprovação adicional para suas regras de envio de mensagens. Dessa forma, você pode ter uma revisão adicional quando um público maior for o alvo de seu envio de mensagens.

{% alert important %}
A aprovação do público-alvo está atualmente em acesso antecipado. Entre em contato com o gerente da sua conta Braze se estiver interessado em participar do acesso antecipado.
{% endalert %}

## Pré-requisito

Antes de poder configurar a aprovação do público-alvo, os fluxos de trabalho de aprovação do Canva e da campanha devem estar ativados.

Para ativar os fluxos de trabalho de aprovação do Canva e da campanha, acesse **Configurações** > **Fluxo de trabalho de aprovação** > **Aprovações sempre ativas**. 

## Direcionamento da aprovação do público-alvo

1. Acesse **Configurações** > **Fluxo de trabalho de aprovação** > **Regras de envio de mensagens**.
2. Selecione **Criar regra**.
3. Dê um nome à sua regra para identificá-la rapidamente (por exemplo, "Todas as inscrições de usuários").
4. Para **Objeto**, selecione **Campanha**, **Canvas** ou **Ambos os Canvas e Campanhas** para aplicar a regra de aprovação.
5. Digite um número para o **Limite de usuários acessíveis**. Para saber mais, consulte [Estatísticas do público]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users#audience-statistics).
6. Selecione **Salvar**.

![Um exemplo de regra de envio de mensagens "Regra 1" para Canvas e campanhas com 100.000 usuários como limite. Há três usuários que podem aprovar o Canva e a campanha a ser lançada.][1]

Você pode definir até cinco regras de envio de mensagens. Ao configurar sua regra de envio de mensagens, podem existir duas regras com o mesmo limite de volume para o mesmo objeto. Por exemplo, é possível definir um limite de 10.000 usuários para o Canva e de 10.000 usuários para o Canva e as campanhas. 

Da mesma forma, se você configurar dois limites de 10.0000 usuários para o Canva com diferentes aprovadores, essa regra poderá ser salva. Dessa forma, você pode organizar e separar seus aprovadores (como a equipe jurídica e a equipe de design) em regras específicas.

Observe que não é possível definir regras com limites de volume sobrepostos para o mesmo objeto. Por exemplo, a seguinte regra de envio de mensagens **não pode** ser definida: uma regra com um limite de 10.000 usuários para o Canvas e outra regra com um limite de 1.000.000 de usuários para o Canvas.

### Seleção de aprovadores

{% alert important %}
Opcionalmente, você pode selecionar aprovadores que, se o limite for atingido, terão permissão para aprovar o Canva ou a campanha. Se você não selecionar aprovadores, o lançamento do Canva ou da campanha será bloqueado.
{% endalert %}

Somente os administradores do Braze podem definir regras de envio de mensagens, mas qualquer usuário do Braze pode ser um aprovador de público-alvo (incluindo usuários sem permissões gerais de aprovação). 

Se um limite for atingido e um aprovador for selecionado, o usuário com a permissão de aprovação poderá selecionar **Aprovado** no menu suspenso de aprovação do **público-alvo**.

### Regras no Canva e nas campanhas

A aprovação do público-alvo controla quem pode aprovar a etapa do **público-alvo** de um Canva e de uma campanha. Se uma regra for atendida, mas os aprovadores não estiverem selecionados, o botão **Iniciar** ou **Atualizar** do Canva ou da campanha será desativado.

![A etapa "Resumo" do fluxo de trabalho do Canva que mostra que você precisa de uma aprovação para iniciar.][2]

## Perguntas frequentes

### Alguma coisa será alterada automaticamente quando esse recurso for ativado?

Não. Depois que esse recurso for ativado, você deverá inserir manualmente um limite de volume e selecionar aprovadores para usar o recurso.

### Preciso reconfigurar minhas permissões para usar esse recurso?

Não. Você não precisa alterar as permissões existentes. Qualquer usuário, independentemente de suas permissões atuais, pode ser selecionado como aprovador de público-alvo.

### O mesmo limite se aplica a todos os espaços de trabalho?

Não. Você deve configurar regras de envio de mensagens para cada espaço de trabalho.

### O público-alvo foi aprovado com base na etapa Público-alvo?

Sim. A aprovação do público-alvo não leva em conta detalhes como os eventos de gatilho. Por exemplo, uma campanha pode ser direcionada a todos os seus usuários; no entanto, a campanha é disparada por um evento, portanto, o número real de usuários que a recebem é menor.

[1]: {% image_buster /assets/img/target_population_approval_example.png %}
[2]: {% image_buster /assets/img/non_approver_banner.png %}