---
nav_title: Excluir usuários
article_title: Excluir usuários
page_order: 4.2
toc_headers: h2
description: "Aprenda como excluir um usuário individual ou um segmento de usuários diretamente pelo dashboard da Braze."
alias: /delete_users/
---

# Excluir usuários

> Aprenda como excluir um usuário individual ou um segmento de usuários diretamente pelo dashboard da Braze.

{% alert important %}
A exclusão de usuários está atualmente em acesso antecipado. Fale com seu gerente de sucesso do cliente se tiver interesse em participar.
{% endalert %}

## Pré-requisitos

Para excluir usuários, você deve ser um administrador ou ter permissões de **Excluir Usuário**.

## Sobre a exclusão de usuários

A exclusão de usuários permite que você gerencie seu banco de dados removendo perfis que não são mais necessários, criados por engano ou que precisam ser excluídos por conformidade (como GDPR ou CCPA).

| Considerações | Informações |
|---------------|---------|
| Tamanho máximo | Você pode excluir até 100 milhões de perfis de usuários ao excluir um segmento. |
| Período de espera | Todas as exclusões de segmentos requerem um período de espera de 7 dias, além do tempo necessário para processar as exclusões. |
| Limites de trabalho | Apenas um segmento pode ser excluído por vez, o que inclui o período de espera de 7 dias. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Excluindo usuários

Você pode excluir um [usuário individual](#delete-individual) ou um [segmento de usuários](#delete-segment) pelo dashboard da Braze:

### Excluindo um usuário individual {#delete-individual}

Para excluir um usuário individual da Braze, acesse **Público** > **Pesquisar Usuários**, depois pesquise e selecione um usuário. Se você estiver excluindo um perfil de usuário duplicado, verifique se selecionou o correto.

![A página 'Pesquisar Usuários' na Braze.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:75%;"}

{% alert warning %}
Exclusões de usuários individuais são permanentes — os perfis não podem ser recuperados após serem excluídos.  
{% endalert %}

Na página do perfil, selecione <i class="fa-solid fa-ellipsis-vertical"></i> **Mostrar opções** > **Excluir Usuário**. Tenha em mente que pode levar alguns minutos para que o usuário seja totalmente excluído na Braze.

![Um usuário na Braze com o menu de reticências verticais aberto, mostrando a opção de excluir o usuário.]({% image_buster /assets/img/audience_management/deleting_users/delete_user.png %}){: style="max-width:85%;"}

### Excluindo um segmento {#delete-segment}

Se você ainda não fez isso, [crie um segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment) contendo os perfis de usuário que deseja excluir. Certifique-se de incluir todos os perfis de usuário se estiver excluindo usuários duplicados.

Na Braze, acesse **Público** > **Gerenciar Público** e selecione a guia **Excluir Usuários**.

![A guia 'Excluir Usuários' na seção 'Gerenciar Público' do dashboard da Braze.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Selecione **Excluir usuários**, escolha o segmento que deseja excluir e selecione **Próximo**.

![Uma janela pop-up com um segmento escolhido para exclusão.]({% image_buster /assets/img/audience_management/deleting_users/choose_segment_to_delete.png %}){: style="max-width:75%;"}

Digite **DELETE** para confirmar sua solicitação e selecione **Excluir usuários**.

![A página de confirmação com 'DELETE' digitado na caixa de confirmação.]({% image_buster /assets/img/audience_management/deleting_users/confirm_segment_delete.png %}){: style="max-width:75%;"}

Os usuários neste segmento não serão excluídos imediatamente. Em vez disso, eles serão marcados como pendentes de exclusão pelos próximos 7 dias. Após esse período, eles serão excluídos e enviaremos um e-mail para informá-lo.

{% alert tip %}
Para garantir que esses usuários exatos sejam excluídos independentemente de mudanças no segmento, um filtro de segmento chamado **Pendente de Exclusão** é criado automaticamente. Você pode [usar este filtro]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#filters) para verificar o status das exclusões pendentes.
{% endalert %}

## Confirmando exclusões de segmento

A Braze envia um e-mail de confirmação com o número de perfis pendentes de exclusão.

Para continuar com a exclusão, faça login na Braze e confirme a solicitação de exclusão.

Se você não confirmar dentro do prazo mostrado no e-mail, a solicitação de exclusão expira e não prossegue.

## Cancelando exclusões de segmentos {#cancel}

Você tem 7 dias para cancelar exclusões de segmentos pendentes. Para cancelar, acesse **Público** > **Gerenciar Público** e selecione a guia **Excluir Usuários**.

![A guia 'Excluir Usuários' na seção 'Gerenciar Público' do dashboard da Braze.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Ao lado de uma exclusão de segmento pendente, selecione <i class="fa-solid fa-eye"></i> para abrir os detalhes do registro de exclusão.

![Uma exclusão de segmento pendente na guia 'Excluir Usuários'.]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

Nos detalhes do registro de exclusão, selecione **Cancelar exclusão**.

![A janela 'Detalhes do Registro de Exclusão' na guia 'Excluir Usuários'.]({% image_buster /assets/img/audience_management/deleting_users/deletion_record_details.png %}){: style="max-width:55%;"}

{% alert tip %}
Quando a exclusão em massa de usuários estiver em andamento, você pode cancelá-la a qualquer momento. No entanto, qualquer usuário já excluído antes do cancelamento não pode ser restaurado.
{% endalert %}

## Verificando o status da exclusão {#status}

Você pode verificar o status de uma exclusão usando [filtros de segmento](#segment-filters), a página [Gerenciar Público](#manage-audience) ou [relatórios de eventos de segurança](#security-event-report).

### Filtros de segmento

Quando você solicita a exclusão de um segmento de usuários, um [filtro de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#filters) chamado **Pendente de Exclusão** é criado automaticamente. Você pode usá-lo para:

- Ver o conjunto exato de usuários vinculados a uma data específica de execução de exclusão.
- Excluir esses usuários de Campaigns para que não recebam mensagens antes da remoção.
- Exportar a lista caso você precise dela para conformidade ou manutenção de registros.

### Gerenciar Público

{% alert note %}
Para obter a lista exata de usuários que serão excluídos, use o [filtro de segmento Pendente de Exclusão](#segment-filters).
{% endalert %}

Acesse **Público** > **Gerenciar Público** e selecione a guia **Excluir Usuários**.

![A guia 'Excluir Usuários' na seção 'Gerenciar Público' do dashboard da Braze.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Nesta página, você pode encontrar as seguintes informações gerais para todas as exclusões atuais e pendentes:

| Campo | Descrição |
|-------|-------------|
| Data da Solicitação | A data em que a solicitação foi originalmente feita. Use-a com o filtro **Pendente de Exclusão** para obter a lista de perfis pendentes de exclusão. |
| Solicitante | O usuário que iniciou a solicitação de exclusão. |
| Nome do Segmento | O nome do segmento usado para selecionar os usuários pendentes de exclusão. |
| Status | Mostra se a solicitação de exclusão está pendente, em andamento ou concluída. |  
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Para mais detalhes sobre uma solicitação específica, selecione <i class="fa-solid fa-eye"></i> para mostrar os detalhes do registro de exclusão. Aqui você também pode [cancelar exclusões de segmentos pendentes](#cancel).

![Uma exclusão de segmento pendente na guia 'Excluir Usuários'.]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

### Relatório de eventos de segurança

Você também pode verificar o status de exclusões anteriores baixando um relatório de eventos de segurança. Para saber mais, veja [Configurações de segurança]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#security-event-report).

## Perguntas frequentes {#faq}

### Posso excluir segmentos com mais de 100 milhões de usuários?

Não. Você não pode excluir segmentos com mais de 100 milhões de usuários. Se precisar de ajuda para excluir um segmento desse tamanho, entre em contato com o [suporte da Braze]({{site.baseurl}}/user_guide/administrative/access_braze/support).

### Parece que não consigo excluir 100 milhões de usuários e estou limitado a excluir apenas 10 milhões. Isso é um bug?

Não, isso não é um bug. Certos clientes estão limitados no número de usuários que podem excluir durante o programa de acesso antecipado (EA).

À medida que o programa EA avança, essa capacidade é projetada para aumentar até que todos os clientes possam excluir até 100 milhões de usuários.

Se você quiser aumentar essa capacidade, entre em contato com seu gerente de conta da Braze. As solicitações são concedidas a critério da equipe de produto.

### A fusão automática de usuários afeta a exclusão de usuários?

Se uma fusão agendada incluir perfis de usuários pendentes de exclusão, a Braze ignora esses perfis e não os mescla. Para mesclar esses perfis, você deve removê-los da exclusão.

### O que acontece com os dados enviados para usuários pendentes de exclusão?

Os dados enviados de sistemas externos ou SDKs ainda são aceitos, mas os usuários serão excluídos conforme programado, independentemente da atividade.

### Canvas e Campaigns disparam para usuários pendentes de exclusão?

Sim. No entanto, você pode adicionar um filtro de inclusão de segmento para excluir todos os usuários com o [filtro de segmento](#segment-filters) **Pendente de Exclusão**.

### Posso recuperar perfis de usuários excluídos?

A exclusão de usuários individuais é permanente.

Você pode [cancelar exclusões de segmento](#cancel) dentro dos primeiros 7 dias. No entanto, qualquer usuário já excluído antes do cancelamento não pode ser restaurado.