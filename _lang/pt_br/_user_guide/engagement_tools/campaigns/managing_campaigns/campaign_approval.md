---
nav_title: Aprovação de campanhas
article_title: Aprovação de campanhas
alias: "/campaign_approval/"
page_order: 0
page_type: reference
description: "Esta página fornece uma visão geral do processo de aprovação da campanha."
tool: Campaigns
---

# Aprovação de campanhas

> A aprovação da campanha adiciona um processo de revisão ao seu fluxo de trabalho antes de lançar uma campanha. Esse recurso adiciona estados que estão disponíveis na etapa do fluxo de trabalho de confirmação de campanha. Você pode se certificar de que cada confirmação seja aprovada para lançar a campanha.

{% alert important %}
A aprovação da campanha não é suportada no fluxo de trabalho de criação de campanhas de API e campanhas de e-mail de transação.
{% endalert %}

## Ativação da aprovação da campanha

Por padrão, a configuração de aprovação de campanha está desativada. Para ativar esse recurso, vá para **Configurações** > **Fluxo de trabalho de aprovação**.

{% alert note %}
Se você estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), poderá encontrar essa página em **Gerenciar configurações** > **Fluxo de trabalho de aprovação**.
{% endalert %}

## Uso de aprovações

Depois que a aprovação da campanha for ativada, você deverá ter a permissão "Approve and Deny Campaigns" (Aprovar e recusar campanhas). Essa permissão controla quem pode atualizar o status de aprovação de uma campanha. Essa permissão também pode ser aplicada a espaços de trabalho ou [equipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) ou adicionada a um [conjunto de permissões]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#permission-sets).

Na etapa **Revisar resumo** do fluxo de trabalho de criação de campanha, use a opção de aprovação para aprovar ou negar os principais componentes de sua campanha: **Mensagens**, **envio**, **público-alvo** e **eventos de conversão**. O estado padrão da aprovação da campanha é **Aprovação pendente**. Note que é possível autoaprovar componentes de uma campanha.

![][1]

Quando cada seção for aprovada, o botão **Launch** será ativado e você poderá lançar sua campanha! 

[1]: {% image_buster /assets/img_archive/campaign_approval_example.png %} 
