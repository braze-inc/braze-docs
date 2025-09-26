---
nav_title: Aprovações
article_title: Aprovações
page_order: 2
page_type: reference
description: "Este artigo de referência oferece uma visão geral dos vários status que uma campanha e uma tela podem ter e o que significam."
tool:
    - Campaigns
    - Canvas
---

# Aprovações para campanhas e telas

> O processo de aprovação de campanhas e Canvas adiciona um processo de revisão ao seu fluxo de trabalho antes do lançamento. Dessa forma, você pode verificar se cada seção da final da campanha ou do editor do Canva foi aprovada para o lançamento.

## Como funciona?

Você pode revisar os detalhes de sua campanha ou do Canva na etapa final do editor. Para campanhas, isso é **Resumo da revisão**, e para telas, isso é **Resumo**. 

Se o administrador tiver ativado o fluxo de trabalho de aprovação, cada seção do resumo deverá ser aprovada por um usuário com as permissões apropriadas antes que a mensagem possa ser iniciada. O status padrão de cada seção é **Pending Approval (Aprovação pendente**).

{% tabs %}
{% tab campanha %}
Para lançar uma campanha, você deve aprovar esses componentes principais:

- **Envio de mensagens:** Essa é a mensagem da campanha.
- **Entrega:** Esse é o tipo de entrega e determina quando os usuários receberão a campanha.
- **Público-alvo:** Isso determina quem receberá a campanha.
- **Eventos de conversão:** Essa é a métrica que você está rastreando para fins de engajamento e relatórios.
{% endtab %}

{% tab canvas %}
Para lançar um Canva, você deve aprovar esses componentes principais:

- **Eventos de conversão:** Essa é a métrica que você está rastreando para fins de engajamento e relatórios.
- **Cronograma de entrada:** Isso inclui o tipo de programação de entrada e quando os usuários devem entrar no Canva.
- **Público-alvo:** Isso determina quem entrará nessa tela.
- **Enviar configurações:** Essas são as opções de envio para todas as etapas do Canva. 
- **Construir canvas:** Essa é a jornada do usuário do Canva.
{% endtab %}
{% endtabs %}

## Ativação do fluxo de trabalho de aprovação

Por padrão, a configuração do fluxo de trabalho de aprovação é desativada para campanhas e telas. Para ativar esse recurso, acesse **Configurações** > **Fluxo de trabalho de aprovação** e selecione o botão de alternância aplicável:
- **Use o fluxo de trabalho de aprovação para todas as campanhas em [seu espaço de trabalho]**
- **Use o fluxo de trabalho de aprovação para todas as telas em [seu espaço de trabalho]**

{% alert important %}
A aprovação da campanha não é suportada no fluxo de trabalho de criação de [campanhas de API]({{site.baseurl}}/api/api_campaigns) e [campanhas de e-mail de transação]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign).
{% endalert %}

## Definição de permissões de usuário

Depois que o fluxo de trabalho de aprovação for ativado, será necessário definir as permissões de usuário para que os usuários do dashboard possam aprovar ou negar as campanhas e os Canvas imediatamente. Ambas as permissões também podem ser aplicadas a espaços de trabalho ou [equipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) ou adicionadas a um [conjunto de permissões]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#permission-sets).

{% tabs %}
{% tab campanha %}
Você deve ter a [ permissão "Approve and Deny Campaigns" (Aprovar e recusar campanhas]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions)). Essa permissão controla quem pode atualizar o status de aprovação de uma campanha. É possível autoaprovar componentes de uma campanha.
{% endtab %}

{% tab canvas %}
Você deve ter a [ permissão "Approve and Deny Canvases" (Aprovar e recusar telas]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions)). Um usuário com essa permissão pode realizar qualquer uma das seguintes ações no fluxo de trabalho do Canva:

- Aprovar, mas não lançar o Canva
- Lançar, mas não aprovar o Canva
- Aprovar e lançar o Canva
- Não aprovar ou lançar o canva

Depois que os status de aprovação forem definidos na etapa **do Resumo**, todas as alterações subsequentes feitas no Canva redefinirão todos os status de aprovação quando forem salvas. Isso se aplica a todas as alterações feitas em um rascunho do Canvas ou em um Canvas pós-lançamento. Por exemplo, se você só fizer alterações no público-alvo, a etapa **Resumo** reverterá os status de aprovação de todas as seções para o estado padrão, pendente.
{% endtab %}
{% endtabs %}

{% alert important %}
Para editar uma campanha ativa, você precisará da permissão "Approve and Deny Campaigns" (Aprovar e recusar campanhas). Um usuário precisará aprovar suas alterações, pois uma versão preliminar das campanhas ainda não está disponível. Esse não é o caso dos Canvas, pois um usuário pode fazer alterações e salvar como rascunho, e outro usuário pode aprovar e iniciar o Canvas.
{% endalert %}
