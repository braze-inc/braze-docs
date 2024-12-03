---
nav_title: Aprovação e permissões do Canva
article_title: Aprovação e permissões do Canva 
page_order: 0.5
alias: "/canvas_approval/"
description: "Este artigo de referência aborda como aprovar Canvas antes do lançamento e descreve as permissões de usuário relacionadas."
tool: Canvas
---

# Aprovação e permissões do Canva

> A aprovação do Canva adiciona um processo de revisão ao seu fluxo de trabalho antes do lançamento. Dessa forma, você pode verificar se cada confirmação foi aprovada para iniciar o Canva.

## Ativação da aprovação do Canva

Para ativar o fluxo de trabalho de aprovação do Canva, acesse **Configurações** > **Fluxo de trabalho de aprovação** em **Configurações do local de trabalho**. Por padrão, esse recurso está desativado.

![As configurações do Fluxo de trabalho de aprovação, onde a opção de usar o fluxo de trabalho de aprovação para campanhas e Canvas está ativada.][1]

{% alert tip %}
Certifique-se de verificar se tem as [permissões de usuário]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions) adequadas para aprovar Canvas.
{% endalert %}

### Definição de permissões de usuário

Depois que o fluxo de trabalho de aprovação do Canvas tiver sido ativado, acesse **Configurações** > **Usuários da empresa** e selecione **Aprovar e recusar telas** para permitir que usuários específicos aprovem e recusem telas imediatamente. Essa permissão também pode ser aplicada a espaços de trabalho ou [equipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/), ou adicionada a um [conjunto de permissões]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#permission-sets).

Um usuário com essa permissão pode realizar qualquer uma das seguintes ações no fluxo de trabalho do Canva:
- Aprovar, mas não lançar o Canva
- Lançar, mas não aprovar o Canva
- Aprovar e lançar o Canva
- Não aprovar ou lançar o canva

![Um exemplo de uma caixa de seleção não marcada para a permissão Aprovar e negar telas, o que significa que esse usuário não tem permissão para aprovar ou negar telas.][3]{: style="max-width:70%" }

{% alert important %}
Para editar uma campanha ativa, você precisará da permissão "Approve and Deny Campaigns" (Aprovar e recusar campanhas). Um usuário precisará aprovar suas alterações, pois uma versão preliminar das campanhas ainda não está disponível. Esse não é o caso dos Canvas, pois um usuário pode fazer alterações e salvar como rascunho, e outro usuário pode aprovar e iniciar o Canvas.
{% endalert %}

## Uso de aprovações

Quando tiver a permissão "Approve and Deny Canvases" (Aprovar e recusar telas), você terá acesso à etapa do **Resumo** do construtor de telas. Essa página fornece um resumo dos principais detalhes do Canvas com a opção de aprovar ou negar esses detalhes, incluindo eventos de conversão, programação de entrada e o tipo e a quantidade de componentes em seu Canvas. Note que o estado padrão da aprovação do Canva é **Aprovação pendente**.

Depois que os status de aprovação forem definidos na etapa **do Resumo**, todas as alterações subsequentes feitas no Canva redefinirão todos os status de aprovação quando forem salvas. Isso se aplica a todas as alterações feitas em um rascunho do Canvas ou em um Canvas pós-lançamento. Por exemplo, se você só fizer alterações no público-alvo, a etapa **Resumo** reverterá os status de aprovação de todas as seções para o estado padrão, pendente.

![Um exemplo do fluxo de trabalho de aprovação do Canva em que os detalhes dos eventos de conversão e do cronograma de entrada foram marcados como aprovados.][2]{: style="max-width:85%" }

Depois que cada seção for aprovada, o botão **Launch** estará disponível e você poderá iniciar o Canva.

[1]: {% image_buster /assets/img_archive/canvas_approval.png %}
[2]: {% image_buster /assets/img_archive/canvas_approval_summary.png %}
[3]: {% image_buster /assets/img_archive/canvas_approval_user_permissions.png %}