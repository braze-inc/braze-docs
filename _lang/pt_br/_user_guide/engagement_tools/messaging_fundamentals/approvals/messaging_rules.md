---
nav_title: Regras de mensagens
article_title: Regras de mensagens
page_order: 1
page_type: reference
description: "Esta página aborda como usar regras de mensagens no fluxo de trabalho de aprovação para campanhas e Canvases com um grande volume de envio."
---

# Regras de mensagens

> Use regras de mensagens em seu fluxo de trabalho de aprovação para limitar o número de usuários alcançáveis antes que seja necessária uma aprovação adicional - dessa forma, você pode revisar suas campanhas e Canvases antes de atingir um público maior.

## Como funciona

As regras de mensagens se aplicam a um espaço de trabalho e são compostas por um tipo de mensagem e um número máximo de usuários acessíveis.

- **Tipo de mensagem:** Define a que tipo de mensagem a regra será aplicada: campanha, Canvas ou ambos, Canvas e campanhas.
- **Máximo de usuários acessíveis:** Determina o tamanho do público que exigirá uma aprovação adicional.

### Tipos de mensagens compartilhadas e usuários com alcance máximo

Podem existir duas regras com o mesmo número de usuários acessíveis para o mesmo tipo de mensagem. Por exemplo, você pode definir um máximo de 10.000 usuários para o Canvas e 10.000 usuários para o Canvas e as campanhas. 

### Aprovadores separados

Duas regras podem compartilhar o mesmo usuário máximo para que você possa organizar e separar suas regras por aprovadores. Por exemplo, você cria as duas regras a seguir:

- Regra A para o Canvas com um máximo de 100.000 usuários com aprovadores em sua equipe jurídica
- Regra B para o Canvas com um máximo de 100.000 usuários com aprovadores na sua equipe de marketing 

### Não há usuários acessíveis sobrepostos

Não é possível definir regras com um número sobreposto de usuários para o mesmo tipo de mensagem. Por exemplo, a seguinte regra de mensagens **não pode** ser definida: 

- Regra C para o Canvas com um máximo de 10.000 usuários 
- Regra D para o Canvas com um máximo de 1.000.000 de usuários

## Criação de uma regra de mensagens

### Pré-requisitos

Somente os administradores do Braze podem definir regras de mensagens, mas qualquer usuário do Braze pode ser um aprovador de regras de mensagens (incluindo usuários sem permissões gerais de aprovação).

### Etapa 1: Adicionar uma regra

{% alert note %}
Você pode criar até cinco regras de mensagens.
{% endalert %}

1. Vá para **Configurações** > **Fluxo de trabalho de aprovação** > **Regras de mensagens**.
2. Selecione **Criar regra**.
3. Dê um nome a essa regra (por exemplo, "Todas as assinaturas de usuário").
4. Para o **tipo de mensagem**, selecione **Campanha**, **Tela** ou **Ambas as telas e campanhas** para aplicar a regra de aprovação.
5. Insira um número para o **máximo de usuários acessíveis**. Para obter mais informações, consulte [Estatísticas de público]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users#audience-statistics).
6. Selecione **Salvar**.

\![Um exemplo de regra de mensagens "Regra 1" para campanhas com 100.000 usuários como máximo. Há um usuário que pode aprovar o Canvas e a campanha a ser lançada.]({% image_buster /assets/img/target_population_approval_example.png %}){: style="max-width:90%;"}

### Etapa 2: Determinar o lançamento com aprovação (opcional)

Selecione **Permitir lançamento com aprovação**. Em seguida, para **Com aprovação de**, selecione os aprovadores que têm permissão para aprovar o Canvas ou a campanha se o máximo for atingido.

Observe os detalhes a seguir sobre o lançamento de mensagens com aprovação:

- Se o máximo for atingido e um aprovador for selecionado, o usuário do Braze com a permissão de aprovação poderá selecionar **Aprovado** no menu suspenso de aprovação do **Público-alvo**.
- Se o máximo for atingido e uma aprovação não for selecionada, o Canvas ou a campanha será impedido de ser lançado.

A etapa "Resumo" do fluxo de trabalho do Canvas que mostra que você precisa de uma aprovação para iniciar.]({% image_buster /assets/img/non_approver_banner.png %}){: style="max-width:90%;"}

## Perguntas frequentes

### Preciso reconfigurar minhas permissões para usar as regras de mensagens?

Não. Qualquer usuário, independentemente de suas permissões atuais, pode ser selecionado como aprovador de população-alvo.

### Como as regras de mensagens se relacionam com a etapa Público-alvo?

As regras de mensagens não levam em conta detalhes como o acionamento de eventos. Por exemplo, uma campanha pode ter como alvo todos os seus usuários. No entanto, a campanha é acionada por eventos, portanto, o número real de usuários que a recebem é menor.

### Alguma coisa será alterada automaticamente quando as regras de mensagens forem ativadas?

Não. Depois que esse recurso for ativado, você deverá inserir manualmente o número máximo de usuários e selecionar os aprovadores para usar o recurso.

