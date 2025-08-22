---
nav_title: Regras de envio de mensagens
article_title: Regras de envio de mensagens
page_order: 1
page_type: reference
description: "Esta página aborda como usar regras de envio de mensagens no fluxo de trabalho de aprovação para campanhas e telas com um grande volume de envio."
---

# Regras de envio de mensagens

> Use regras de envio de mensagens em seu fluxo de trabalho de aprovação para limitar o número de usuários alcançáveis antes que seja necessária uma aprovação adicional - dessa forma, você pode revisar suas campanhas e Canvas antes de direcionar um público maior.

## Como funciona?

As regras de envio de mensagens se aplicam a um espaço de trabalho e são compostas por um tipo de mensagem e um número máximo de usuários acessíveis.

- **Tipo de mensagem:** Define a que tipo de mensagem a regra será aplicada: campanha, Canva ou ambos, Canvas e campanhas.
- **Máximo de usuários acessíveis:** Determina o tamanho do público que exigirá uma aprovação adicional.

### Tipos de mensagens compartilhadas e usuários com alcance máximo

Podem existir duas regras com o mesmo número de usuários acessíveis para o mesmo tipo de mensagem. Por exemplo, é possível definir um máximo de 10.000 usuários para o Canvas e 10.000 usuários para o Canvas e as campanhas. 

### Aprovadores separados

Duas regras podem compartilhar o mesmo usuário máximo para que você possa organizar e separar suas regras por aprovadores. Por exemplo, você cria as duas regras a seguir:

- Regra A para o Canvas com um máximo de 100.000 usuários com aprovadores na sua equipe jurídica
- Regra B para o Canvas com um máximo de 100.000 usuários com aprovadores na sua equipe de marketing 

### Não há usuários acessíveis sobrepostos

Não é possível definir regras com um número sobreposto de usuários para o mesmo tipo de mensagem. Por exemplo, a seguinte regra de envio de mensagens **não pode** ser definida: 

- Regra C para o Canva com um máximo de 10.000 usuários 
- Regra D para o Canva com um máximo de 1.000.000 de usuários

## Criação de uma regra de envio de mensagens

### Pré-requisitos

Somente os administradores do Braze podem definir regras de envio de mensagens, mas qualquer usuário do Braze pode ser um aprovador de regras de envio de mensagens (incluindo usuários sem permissões gerais de aprovação).

### Etapa 1: Adicionar uma regra

{% alert note %}
Você pode criar até cinco regras de envio de mensagens.
{% endalert %}

1. Acesse **Configurações** > **Fluxo de trabalho de aprovação** > **Regras de envio de mensagens**.
2. Selecione **Criar regra**.
3. Dê um nome a essa regra (por exemplo, "Todas as inscrições de usuários").
4. Para o **tipo de mensagem**, selecione **Campanha**, **Canvas** ou **Ambos os Canvas e Campanhas** para aplicar a regra de aprovação.
5. Insira um número para o **máximo de usuários acessíveis**. Para saber mais, consulte [Estatísticas do público]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users#audience-statistics).
6. Selecione **Salvar**.

![Um exemplo de regra de envio de mensagens "Regra 1" para campanhas com 100.000 usuários como máximo. Há um usuário que pode aprovar o Canva e a campanha a ser lançada.]({% image_buster /assets/img/target_population_approval_example.png %}){: style="max-width:90%;"}

### Etapa 2: Determinar o lançamento com aprovação (opcional)

Selecione **Permitir lançamento com aprovação**. Em seguida, em **Com aprovação de**, selecione os aprovadores que têm permissão para aprovar o Canva ou a campanha se o máximo for atingido.

Observe os seguintes detalhes sobre o envio de mensagens com aprovação:

- Se o máximo for atingido e um aprovador for selecionado, o usuário do Braze com a permissão de aprovação poderá selecionar **Aprovado** no menu suspenso de aprovação do **público-alvo**.
- Se o máximo for atingido e uma aprovação não for selecionada, o Canva ou a campanha será impedida de ser lançada.

![A etapa "Resumo" do fluxo de trabalho do Canva que mostra que você precisa de uma aprovação para iniciar.]({% image_buster /assets/img/non_approver_banner.png %}){: style="max-width:90%;"}

## Perguntas frequentes

### Tenho que reconfigurar minhas permissões para usar regras de envio de mensagens?

Não. Qualquer usuário, independentemente de suas permissões atuais, pode ser selecionado como aprovador de público-alvo.

### Como as regras de envio de mensagens se relacionam com a etapa de público-alvo?

As regras de envio de mensagens não levam em conta detalhes como eventos de gatilho. Por exemplo, uma campanha pode ter como alvo todos os seus usuários. No entanto, a campanha é disparada por um evento, portanto, o número real de usuários que a recebem é menor.

### Alguma coisa será alterada automaticamente quando as regras de envio de mensagens forem ativadas?

Não. Depois que esse recurso for ativado, você deverá inserir manualmente o número máximo de usuários e selecionar os aprovadores para usar o recurso.

