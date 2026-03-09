---
nav_title: Aprovações
article_title: Aprovações
page_order: 1
page_type: reference
description: "Este artigo de referência fornece uma visão geral dos vários status que uma campanha e um canva podem ter e o que eles significam."
tool:
    - Campaigns
    - Canvas
---

# Aprovações para campanhas e canvases

> Use aprovações para adicionar um ponto de verificação final às suas campanhas e canvases antes do lançamento. Com este fluxo de trabalho, você pode verificar e aprovar o conteúdo em todas as seções necessárias da sua mensagem.

## Como funciona?

Você pode revisar os detalhes da sua campanha ou canva na etapa final de edição. 

Para ambos, canvases e campanhas, você deve salvar todas as alterações antes de aprovar, mesmo que sejam suas próprias alterações. Um usuário com as permissões apropriadas deve aprovar cada seção do resumo antes que a mensagem possa ser lançada. O status padrão para cada seção é **Pending Approval**.

{% tabs %}
{% tab campaign %}
Para lançar uma campanha, você deve aprovar estes componentes:

- **Mensagens:** Esta é a mensagem da campanha.
- **Entrega:** Este é o tipo de entrega e determina quando os usuários recebem a campanha.
- **Público-alvo:** Isto determina quem receberá a campanha.
- **Eventos de conversão** Esta é a métrica que você está rastreando para fins de engajamento e relatórios.
{% endtab %}

{% tab canvas %}
Para lançar um canva, você deve aprovar estes componentes principais:

- **Eventos de conversão** Esta é a métrica que você está rastreando para fins de engajamento e relatórios.
- **Cronograma de entrada:** Isto inclui o tipo de cronograma de entrada e quando os usuários entram no canva.
- **Público-alvo:** Isto determina quem irá entrar neste canva.
- **Configurações de Envio:** Estas são as opções de envio para todas as etapas no canva. 
- **Construir Canva:** Esta é a jornada do usuário do canva.
{% endtab %}
{% endtabs %}

## Ativando o fluxo de trabalho de aprovação

Por padrão, a configuração do fluxo de trabalho de aprovação está desativada para Campanhas e canvases. Para ativar este recurso, acesse **Configurações** > **Fluxo de Trabalho de Aprovação** e selecione o toggle aplicável:

- **Usar fluxo de trabalho de aprovação para todas as Campanhas em [seu espaço de trabalho]**
- **Usar fluxo de trabalho de aprovação para todos os canvases em [seu espaço de trabalho]**

{% alert important %}
A aprovação de campanhas não é suportada para [campanhas de API]({{site.baseurl}}/api/api_campaigns) e [campanhas de e-mail de transação]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign).
{% endalert %}

## Definição de permissões de usuário

Depois de ativar o fluxo de trabalho de aprovação, você deve definir as permissões dos usuários para que os usuários da sua empresa possam aprovar ou negar Campanhas e canvases. Ambas as permissões também podem ser aplicadas a Espaços de Trabalho ou [Equipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) ou adicionadas a um [conjunto de permissões]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#permission-sets).

{% tabs %}
{% tab campaign %}
Você deve ter a ["Permissão para Aprovar e Negar Campanhas"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions). Essa permissão controla quem pode atualizar o status de aprovação de uma campanha. Com esta permissão, você pode fazer o seguinte:

- Autoaprovar a Campanha
- Aprovar e lançar a Campanha
- Aprovar, mas não lançar a Campanha (um usuário diferente com a permissão "Enviar Campanhas, canvases" pode lançar a Campanha)
- Nem aprovar nem lançar a Campanha

Depois que os status de aprovação são definidos na etapa **Resumo**, quaisquer alterações subsequentes feitas na Campanha redefinem todos os status de aprovação quando salvos. Isso se aplica a quaisquer alterações feitas em uma Campanha em rascunho ou em uma campanha pós-lançamento. Por exemplo, se você fizer apenas alterações no Público-Alvo, a etapa **Resumo** reverte os status de aprovação de todas as seções de volta ao estado padrão, **Aguardando Aprovação**.

{% endtab %}

{% tab canvas %}
Você deve ter a ["Permissão para Aprovar e Negar canvases"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions). Esta permissão controla quem pode atualizar o status de aprovação de um canva. Com esta permissão, você pode fazer o seguinte:

- Aprovar o Canvas
- Aprovar e lançar o Canva
- Aprovar, mas não lançar o Canvas (um usuário diferente com a permissão "Enviar Campanhas, Canvases" pode lançar o Canvas)
- Nem aprovar nem lançar o Canvas

Após os status de aprovação serem definidos na etapa **Resumo**, quaisquer alterações subsequentes feitas no Canvas redefinem todos os status de aprovação ao serem salvas. Isso se aplica a todas as alterações feitas em um rascunho do Canvas ou em um Canvas pós-lançamento. Por exemplo, se você fizer alterações apenas no público-alvo, a etapa **Resumo** reverte os status de aprovação de todas as seções para o estado padrão, **Aguardando Aprovação**.

{% alert note %}
**Status de aprovação e salvamento**

- Quando você clica em **Aprovar** para uma seção na etapa **Resumo**, essa aprovação é salva imediatamente.
- O botão **Salvar** salva as alterações no conteúdo e configurações do Canvas, não o status de aprovação.

Para evitar perder aprovações:

1. Faça as edições necessárias no Canvas e, em seguida, clique em **Salvar**.
2. Após o Canvas terminar de salvar, aprove as seções relevantes na etapa **Resumo**.
3. Clique em **Salvar** novamente apenas se você fizer alterações adicionais no Canvas após a aprovação. Se você alterar o Canvas e salvar, todos os status de aprovação serão redefinidos para **Aguardando Aprovação**.
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert important %}
Para editar uma Campanha ativa, você precisa da permissão "Aprovar e Negar Campanhas". Um usuário deve aprovar suas alterações porque uma versão em rascunho das Campanhas ainda não está disponível. Esse não é o caso dos Canvas, pois um usuário pode fazer alterações e salvar como rascunho, e outro usuário pode aprovar e iniciar o Canvas.
{% endalert %}