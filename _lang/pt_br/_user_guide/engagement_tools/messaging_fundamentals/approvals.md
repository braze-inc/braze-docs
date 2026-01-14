---
nav_title: Aprovações
article_title: Aprovações
page_order: 2
page_type: reference
description: "Este artigo de referência apresenta uma visão geral dos vários status que uma campanha e um Canvas podem ter e o que eles significam."
tool:
    - Campaigns
    - Canvas
---

# Aprovações para campanhas e telas

> O processo de aprovação de campanhas e Canvases adiciona um processo de revisão ao seu fluxo de trabalho antes do lançamento. Dessa forma, você pode verificar se cada seção da final da campanha ou do editor do Canvas foi aprovada para o lançamento.

## Como funciona

Você pode revisar os detalhes de sua campanha ou Canvas na etapa final do editor. Para campanhas, isso é **Review Summary (Resumo da revisão**), e para Canvases, isso é **Summary (Resumo**). 

Se o administrador tiver ativado o fluxo de trabalho de aprovação, cada seção do resumo deverá ser aprovada por um usuário com as permissões adequadas antes que a mensagem possa ser iniciada. O status padrão de cada seção é **Pending Approval (Aprovação pendente**).

{% tabs %}
{% tab campaign %}
Para lançar uma campanha, você deve aprovar esses componentes principais:

- **Mensagens:** Essa é a mensagem da campanha.
- **Entrega:** Esse é o tipo de entrega e determina quando os usuários receberão a campanha.
- **Público-alvo:** Isso determina quem receberá a campanha.
- **Eventos de conversão:** Essa é a métrica que você está monitorando para fins de engajamento e relatórios.
{% endtab %}

{% tab canvas %}
Para lançar um Canvas, você deve aprovar esses componentes principais:

- **Eventos de conversão:** Essa é a métrica que você está monitorando para fins de engajamento e relatórios.
- **Horário de entrada:** Isso inclui o tipo de programação de entrada e quando os usuários devem entrar no Canvas.
- **Público-alvo:** Isso determina quem entrará nesse Canvas.
- **Enviar configurações:** Essas são as opções de envio para todas as etapas do Canvas. 
- **Criar tela:** Essa é a jornada do usuário do Canvas.
{% endtab %}
{% endtabs %}

## Ativação do fluxo de trabalho de aprovação

Por padrão, a configuração do fluxo de trabalho de aprovação é desativada para campanhas e Canvases. Para ativar esse recurso, vá para **Configurações** > **Fluxo de trabalho de aprovação** e selecione o botão de alternância aplicável:
- **Use o fluxo de trabalho de aprovação para todas as campanhas em [seu espaço de trabalho]**
- **Use o fluxo de trabalho de aprovação para todas as telas em [seu espaço de trabalho]**

{% alert important %}
A aprovação da campanha não é compatível com o fluxo de trabalho de criação de [campanhas de API]({{site.baseurl}}/api/api_campaigns) e [campanhas de e-mail transacional]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign).
{% endalert %}

## Definição de permissões de usuário

Depois que o fluxo de trabalho de aprovação for ativado, será necessário definir as permissões de usuário para que os usuários do painel possam aprovar ou negar as campanhas e os Canvases imediatamente. Ambas as permissões também podem ser aplicadas a espaços de trabalho ou [equipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) ou adicionadas a um [conjunto de permissões]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#permission-sets).

{% tabs %}
{% tab campaign %}
Você deve ter a [ permissão "Approve and Deny Campaigns" (Aprovar e recusar campanhas]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions)). Essa permissão controla quem pode atualizar o status de aprovação de uma campanha. É possível autoaprovar componentes de uma campanha.
{% endtab %}

{% tab canvas %}
Você deve ter a [ permissão "Approve and Deny Canvases" (Aprovar e recusar telas]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions)). Um usuário com essa permissão pode executar qualquer uma das seguintes ações no fluxo de trabalho do Canvas:

- Aprovar, mas não lançar o Canvas
- Lançar, mas não aprovar o Canvas
- Aprovar e lançar o Canvas
- Não aprovar ou lançar o Canvas

Depois que os status de aprovação forem definidos na etapa **Resumo**, todas as alterações subsequentes feitas no Canvas redefinirão todos os status de aprovação quando forem salvas. Isso se aplica a todas as alterações feitas em um rascunho do Canvas ou em um Canvas pós-lançamento. Por exemplo, se você só fizer alterações no público-alvo, a etapa **Resumo** reverterá os status de aprovação de todas as seções para o estado padrão, pendente.
{% endtab %}
{% endtabs %}

{% alert important %}
Para editar uma campanha ativa, você precisará da permissão "Approve and Deny Campaigns" (Aprovar e recusar campanhas). Um usuário precisará aprovar suas alterações, pois uma versão preliminar das campanhas ainda não está disponível. Esse não é o caso dos Canvases, pois um usuário pode fazer alterações e salvar como rascunho, e outro usuário pode aprovar e iniciar o Canvas.
{% endalert %}
