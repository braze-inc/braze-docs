---
nav_title: Exclusão de usuários
article_title: Exclusão de usuários
page_order: 4.2
toc_headers: h2
description: "Saiba como excluir um usuário individual ou um segmento de usuários diretamente no painel do Braze." 
---

# Exclusão de usuários

> Saiba como excluir um usuário individual ou um segmento de usuários diretamente no painel do Braze.

{% alert important %}
Esse recurso está atualmente em acesso antecipado. Entre em contato com seu gerente de sucesso do cliente se estiver interessado em participar.
{% endalert %}

## Pré-requisitos

Para excluir usuários, você precisa ser um administrador ou ter permissões para **Excluir usuário**.

## Sobre a exclusão de usuários

A exclusão de usuários permite que você gerencie seu banco de dados removendo perfis que não são mais necessários, criados por engano ou que precisam ser excluídos para fins de conformidade (como GDPR ou CCPA).

| Considerações | Detalhes |
|---------------|---------|
| Tamanho máximo | É possível excluir até 100 milhões de perfis de usuário ao excluir um segmento. |
| Período de espera | Todas as exclusões de segmentos exigem um período de espera de 7 dias mais o tempo necessário para processar as exclusões. |
| Limites de trabalho | Apenas um segmento pode ser excluído de cada vez, o que inclui o período de espera de 7 dias. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Exclusão de usuários

Você pode excluir um [usuário individual](#delete-individual) ou um [segmento de usuários](#delete-segment) por meio do painel do Braze:

### Exclusão de um indivíduo {#delete-individual}

Para excluir um usuário individual do Braze, vá para **Audience** > **Search Users** e, em seguida, procure e selecione um usuário. Se estiver excluindo um perfil de usuário duplicado, verifique se selecionou o perfil correto.

\![A página "Pesquisar usuários" no Braze.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:75%;"}

{% alert warning %}
As exclusões de usuário único são permanentes - os perfis não podem ser recuperados depois de serem excluídos.  
{% endalert %}

Na página de perfil do usuário, selecione <i class="fa-solid fa-ellipsis-vertical"></i> **Mostrar opções** > **Excluir usuário**. Lembre-se de que pode levar alguns minutos para que o usuário seja totalmente excluído no Braze.

\![Um usuário no Braze com o menu de elipses verticais aberto, mostrando a opção de excluir o usuário.]({% image_buster /assets/img/audience_management/deleting_users/delete_user.png %}){: style="max-width:85%;"}

### Exclusão de um segmento {#delete-segment}

Se ainda não o fez, [crie um segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment) que contenha os perfis de usuário que deseja excluir. Certifique-se de incluir todos os perfis de usuário se estiver excluindo usuários duplicados.

No Braze, vá para **Audience** > **Manage Audience** e selecione a guia **Delete Users (Excluir usuários** ).

A guia "Delete Users" (Excluir usuários) na seção "Manage Audience" (Gerenciar público) do painel do Braze.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Selecione **Excluir usuários**, escolha o segmento que deseja excluir e, em seguida, selecione **Avançar**.

\![Uma janela pop-up com um segmento escolhido para exclusão.]({% image_buster /assets/img/audience_management/deleting_users/choose_segment_to_delete.png %}){: style="max-width:75%;"}

Digite **DELETE** para confirmar a solicitação e selecione **Delete users (Excluir usuários**).

\![A página de confirmação com "DELETE" digitado na caixa de confirmação.]({% image_buster /assets/img/audience_management/deleting_users/confirm_segment_delete.png %}){: style="max-width:75%;"}

Os usuários desse segmento não serão excluídos imediatamente. Em vez disso, eles serão marcados como pendentes de exclusão pelos próximos 7 dias. Após esse período, eles serão excluídos e nós lhe enviaremos um e-mail para informá-lo.

{% alert tip %}
Para garantir que esses usuários exatos sejam excluídos independentemente das alterações no segmento, um filtro de segmento chamado **Pending Deletion (Exclusão pendente** ) é criado automaticamente. Você pode [usar esse filtro]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#filters) para verificar o status das exclusões pendentes.
{% endalert %}

## Cancelamento de exclusões de segmentos {#cancel}

Você tem 7 dias para cancelar as exclusões de segmentos pendentes. Para cancelar, vá para **Audience** > **Manage Audience** e selecione a guia **Delete Users (Excluir usuários** ).

A guia "Delete Users" (Excluir usuários) na seção "Manage Audience" (Gerenciar público) do painel do Braze.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Ao lado de uma exclusão de segmento pendente, selecione <i class="fa-solid fa-eye"></i> para abrir os detalhes do registro de exclusão.

\![Uma exclusão de segmento pendente na guia "Excluir usuários".]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

Nos detalhes do registro de exclusão, selecione **Cancelar exclusão**.

A janela "Detalhes do registro de exclusão" na guia "Excluir usuários".]({% image_buster /assets/img/audience_management/deleting_users/deletion_record_details.png %}){: style="max-width:55%;"}

{% alert tip %}
Quando a exclusão de usuários em massa estiver em andamento, você poderá cancelá-la a qualquer momento. No entanto, os usuários já excluídos antes do cancelamento não podem ser restaurados.
{% endalert %}

## Verificação do status da exclusão {#status}

Você pode verificar o status de uma exclusão usando [filtros de segmento](#segment-filters), a página [gerenciar público](#manage-audience) ou [relatórios de eventos de segurança](#security-event-report).

### Filtros de segmento

Quando você solicita a exclusão de um segmento de usuários, um [filtro de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#filters) chamado **Pending Deletion (Exclusão pendente** ) é criado automaticamente. Você pode usá-lo para:

- Veja o conjunto exato de usuários vinculados a uma data específica de execução de exclusão.
- Exclua esses usuários das campanhas para que eles não recebam mensagens antes da remoção.
- Exporte a lista se precisar dela para fins de conformidade ou manutenção de registros.

### Gerenciar o público

{% alert note %}
Para obter a lista de usuários exatos que serão excluídos, use o [filtro de segmento Pending Deletion (Exclusão pendente](#segment-filters) ).
{% endalert %}

Vá para **Audience** > **Manage Audience** e selecione a guia **Delete Users (Excluir usuários** ).

A guia "Delete Users" (Excluir usuários) na seção "Manage Audience" (Gerenciar público) do painel do Braze.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Nesta página, você pode encontrar as seguintes informações gerais sobre todas as exclusões atuais e pendentes:

| Campo | Descrição |
|-------|-------------|
| Data da solicitação | A data em que a solicitação foi feita originalmente. Use-o com o filtro **Pending Deletion (Exclusão pendente** ) para obter a lista de perfis com exclusão pendente. |
| Solicitante | O usuário que iniciou a solicitação de exclusão. |
| Nome do segmento | O nome do segmento usado para selecionar os usuários com exclusão pendente. |
| Status | Mostra se a solicitação de exclusão está pendente, em andamento ou concluída. |  
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Para obter mais detalhes sobre uma solicitação específica, selecione <i class="fa-solid fa-eye"></i> para mostrar os detalhes do registro de exclusão. Aqui você também pode [cancelar as exclusões de segmentos pendentes](#cancel).

\![Uma exclusão de segmento pendente na guia "Excluir usuários".]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

### Relatório de eventos de segurança

Você também pode verificar o status de exclusões anteriores fazendo o download de um relatório de eventos de segurança. Para obter mais informações, consulte [Configurações de segurança]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#security-event-report).

## Perguntas frequentes {#faq}

### Posso excluir segmentos com mais de 100 milhões de usuários?

Não. Não é possível excluir segmentos com mais de 100 milhões de usuários. Se precisar de ajuda para excluir um segmento desse tamanho, entre em contato com [o suporte@braze.com](mailto:support@braze.com).

### A fusão automatizada de usuários afeta a exclusão de usuários?

Se uma mesclagem agendada incluir perfis de usuários com exclusão pendente, o Braze ignorará esses perfis e não os mesclará. Para mesclar esses perfis, você deve removê-los da exclusão.

### O que acontece com os dados enviados aos usuários que aguardam a exclusão?

Os dados enviados de sistemas externos ou SDKs ainda são aceitos, mas os usuários serão excluídos conforme programado, independentemente da atividade.

### Os Canvases e as campanhas serão acionados para usuários com exclusão pendente?

Sim. No entanto, você pode adicionar um filtro de inclusão de segmento para excluir todos os usuários com o [filtro de segmento](#segment-filters) **Pending Deletion**.

### Posso recuperar perfis de usuário excluídos?

A exclusão de usuários individuais é permanente.

Você pode [cancelar as exclusões de segmentos](#cancel) nos primeiros 7 dias após. No entanto, os usuários já excluídos antes do cancelamento não poderão ser restaurados.
