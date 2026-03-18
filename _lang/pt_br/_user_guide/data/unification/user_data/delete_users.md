---
nav_title: Excluir usuários
article_title: Excluir usuários
page_order: 4.2
toc_headers: h2
description: "Aprenda como excluir um usuário individual ou um segmento de usuários diretamente através do painel do Braze."
alias: /delete_users/
hidden: true
---

# Excluir usuários

> Aprenda como excluir um usuário individual ou um segmento de usuários diretamente através do painel do Braze.

{% alert important %}
O acesso antecipado para este recurso está temporariamente fechado. Entre em contato com seu gerente de sucesso do cliente para mais detalhes.
{% endalert %}

## Pré-requisitos

Você deve ser um administrador para excluir usuários.

## Sobre a exclusão de usuários

A exclusão de usuários permite que você gerencie seu banco de dados removendo perfis que não são mais necessários, criados por engano ou que precisam ser excluídos por conformidade (como GDPR ou CCPA).

| Considerações | Informações |
|---------------|---------|
| Tamanho máximo | Você pode excluir até 100 milhões de perfis de usuários ao excluir um segmento. |
| Período de espera | Todas as exclusões de segmentos requerem um período de espera de 7 dias, além do tempo necessário para processar as exclusões. |
| Limites de trabalho | Apenas um segmento pode ser excluído por vez, o que inclui o período de espera de 7 dias. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Excluindo usuários

Você pode excluir um [usuário individual](#delete-individual) ou um [segmento de usuários](#delete-segment) através do painel do Braze:

### Excluindo um {#delete-individual} individual

Para excluir um usuário individual do Braze, acesse **público** > **Pesquisar Usuários**, em seguida, pesquise e selecione um usuário. Se você estiver excluindo um perfil de usuário duplicado, verifique se você selecionou o correto.

![A página 'Pesquisar Usuários' no Braze.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:75%;"}

{% alert warning %}
Exclusões de usuários individuais são permanentes—os perfis não podem ser recuperados após serem excluídos.  
{% endalert %}

Na página do perfil deles, selecione <i class="fa-solid fa-ellipsis-vertical"></i> **Mostrar opções** > **Excluir Usuário**. Tenha em mente que pode levar alguns minutos para que o usuário seja totalmente excluído no Braze.

![Um usuário no Braze com o menu de reticências verticais aberto, mostrando a opção de excluir o usuário.]({% image_buster /assets/img/audience_management/deleting_users/delete_user.png %}){: style="max-width:85%;"}

### Excluindo um segmento {#delete-segment}

Se você ainda não fez, [crie um segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment) contendo os perfis de usuário que deseja excluir. Certifique-se de incluir todos os perfis de usuário se estiver excluindo usuários duplicados.

No Braze, acesse **público** > **Gerenciar Público**, e então selecione a aba **Excluir Usuários**.

![A aba 'Excluir Usuários' na seção 'Gerenciar Público' do painel do Braze.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Selecione **Excluir usuários**, escolha o segmento que deseja excluir e, em seguida, selecione **Próximo**.

![Uma janela pop-up com um segmento escolhido para exclusão.]({% image_buster /assets/img/audience_management/deleting_users/choose_segment_to_delete.png %}){: style="max-width:75%;"}

Digite **EXCLUIR** para confirmar sua solicitação, e então selecione **Excluir usuários**.

![A página de confirmação com 'EXCLUIR' digitado na caixa de confirmação.]({% image_buster /assets/img/audience_management/deleting_users/confirm_segment_delete.png %}){: style="max-width:75%;"}

Os usuários neste segmento não serão excluídos imediatamente. Em vez disso, eles serão marcados como pendentes de exclusão pelos próximos 7 dias. Após esse tempo, eles serão excluídos e nós enviaremos um e-mail para informá-lo.

{% alert tip %}
Para garantir que esses usuários exatos sejam excluídos independentemente das mudanças de segmento, um filtro de segmento chamado **Pendente de Exclusão** é criado automaticamente. Você pode [usar este filtro]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#filters) para verificar o status das exclusões pendentes.
{% endalert %}

## Confirmando exclusões de segmento

O Braze envia um e-mail de confirmação com o número de perfis pendentes de exclusão.

Para continuar com a exclusão, faça login no Braze e confirme a solicitação de exclusão.

Se você não confirmar dentro do prazo mostrado no e-mail, a solicitação de exclusão expira e não prossegue.

## Cancelando exclusões de segmentos {#cancel}

Você tem 7 dias para cancelar exclusões de segmentos pendentes. Para cancelar, acesse **Audience** > **Gerenciar Público**, em seguida, selecione a guia **Excluir Usuários**.

![A aba 'Excluir Usuários' na seção 'Gerenciar Público' do painel do Braze.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Ao lado de uma exclusão de segmento pendente, selecione <i class="fa-solid fa-eye"></i> para abrir os detalhes do registro de exclusão.

![Uma exclusão de segmento pendente na guia 'Excluir Usuários'.]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

Nos detalhes do registro de exclusão, selecione **Cancelar exclusão**.

![A janela 'Detalhes do Registro de Exclusão' na guia 'Excluir Usuários'.]({% image_buster /assets/img/audience_management/deleting_users/deletion_record_details.png %}){: style="max-width:55%;"}

{% alert tip %}
Quando a exclusão em massa de usuários estiver em andamento, você pode cancelá-la a qualquer momento. No entanto, qualquer usuário já excluído antes do cancelamento não pode ser restaurado.
{% endalert %}

## Verificando o status da exclusão {#status}

Você pode verificar o status de uma exclusão usando [filtros de segmento](#segment-filters), a página [gerenciar público](#manage-audience) ou [relatórios de eventos de segurança](#security-event-report).

### Filtros de segmento

Quando você solicita a exclusão de um segmento de usuários, um [filtro de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#filters) chamado **Exclusão Pendente** é criado automaticamente. Você pode usá-lo para:

- Ver o conjunto exato de usuários vinculados a uma data específica de execução de exclusão.
- Excluir esses usuários de campanhas para que não recebam mensagens antes da remoção.
- Exportar a lista se você precisar dela para conformidade ou manutenção de registros.

### Gerenciar público

{% alert note %}
Para obter a lista exata de usuários que serão excluídos, use o [filtro de segmento de Exclusão Pendente](#segment-filters) em vez disso.
{% endalert %}

Acesse **Audience** > **Gerenciar Público**, em seguida, selecione a guia **Excluir Usuários**.

![A aba 'Excluir Usuários' na seção 'Gerenciar Público' do painel do Braze.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Nesta página, você pode encontrar as seguintes informações gerais para todas as exclusões atuais e pendentes:

| Campo | Descrição |
|-------|-------------|
| Data da Solicitação | A data em que a solicitação foi originalmente feita. Use-o com o filtro **Pending Deletion** para obter a lista de perfis pendentes de exclusão. |
| Solicitante | O usuário que iniciou a solicitação de exclusão. |
| Nome do segmento | O nome do segmento usado para selecionar os usuários pendentes de exclusão. |
| Status | Mostra se a solicitação de exclusão está pendente, em andamento ou concluída. |  
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Para mais detalhes sobre uma solicitação específica, selecione <i class="fa-solid fa-eye"></i> para mostrar os detalhes do registro de exclusão. Aqui você também pode [cancelar exclusões de segmentos pendentes](#cancel).

![Uma exclusão de segmento pendente na guia 'Excluir Usuários'.]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

### Relatório de eventos de segurança

Você também pode verificar o status de exclusões anteriores baixando um relatório de eventos de segurança. Para saber mais, veja [Configurações de segurança]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#security-event-report).

## Perguntas frequentes {#faq}

### Posso excluir segmentos com mais de 100 milhões de usuários?

Não. Você não pode excluir segmentos com mais de 100 milhões de usuários. Se precisar de ajuda para excluir um segmento desse tamanho, entre em contato com [support@braze.com](mailto:support@braze.com).

### Parece que não consigo excluir 100 milhões de usuários e estou limitado a excluir apenas 10 milhões. Isso é um bug?

Não, isso não é um bug. Certos clientes estão limitados no número de usuários que podem excluir durante o programa de acesso antecipado (EA).

À medida que o programa EA avança, essa capacidade é projetada para aumentar até que todos os clientes possam excluir até 100 milhões de usuários.

Se você quiser aumentar essa capacidade, entre em contato com seu gerente de conta da Braze. As solicitações são concedidas a critério da equipe de produto.

### A fusão automática de usuários afeta a exclusão de usuários?

Se uma fusão agendada incluir perfis de usuários pendentes de exclusão, a Braze ignora esses perfis e não os mescla. Para mesclar esses perfis, você deve removê-los da exclusão.

### O que acontece com os dados enviados para usuários pendentes de exclusão?

Os dados enviados de sistemas externos ou SDKs ainda são aceitos, mas os usuários serão excluídos conforme programado, independentemente da atividade.

### As Canvases e campanhas dispararão para usuários pendentes de exclusão?

Sim. No entanto, você pode adicionar um filtro de inclusão de segmento para excluir todos os usuários com o **Pending Deletion** [filtro de segmento](#segment-filters).

### Posso recuperar perfis de usuários excluídos?

A exclusão de usuários individuais é permanente.

Você pode [cancelar exclusões de segmento](#cancel) dentro dos primeiros 7 dias após. No entanto, qualquer usuário já excluído antes do cancelamento não pode ser restaurado.
