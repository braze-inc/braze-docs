## Migração de permissões granulares

{% alert important %}
As permissões granulares estão em acesso antecipado. Quando a migração estiver planejada para sua empresa, seus administradores da Braze receberão e-mails e banners no dashboard notificando-os sobre a [migração de permissões granulares]({{site.baseurl}}/granular_permissions_migration/).
{% endalert %}

Integrações SCIM existentes e [objetos da API SCIM legada]({{site.baseurl}}/scim_api_appendix/?sdktab=legacy%20scim%20api) continuarão a funcionar após a migração de permissões granulares no final de abril. 

Você não precisa tomar nenhuma ação imediata. No entanto, recomendamos que você revise suas integrações para quaisquer permissões que serão granularizadas. Por exemplo, se você estiver enviando `basic_access` na API, sugerimos que atualize sua integração após a granularização para incluir as permissões específicas (por exemplo, `"appGroupPermissions":["view_campaigns","edit_campaigns"]`). A Braze continuará a aceitar strings legadas, como `basic_access`, após a migração de permissões granulares para que as integrações existentes não quebrem.

## Objeto de permissões

O objeto de permissões é um campo encontrado em algumas das solicitações e respostas ao interagir com o recurso do usuário por meio de permissões de ID SCIM.

{% alert note %}
Os grupos de apps foram renomeados como espaços de trabalho na Braze, mas as chaves nesta página ainda fazem referência à terminologia antiga (por exemplo, `appGroup`, `appGroupName`).
{% endalert %}

```
{
  "permissions": {
    "companyPermissions": (required, array),
    "appGroup": (required, array)
  }
}
```

Um objeto de permissões válido é um objeto JSON com os seguintes pares de chave/valor:

| Chave | Obrigatória | Tipo de dados | Descrição |
| --- | --- | --- | --- |
| `companyPermissions` | Opcional | Vetor | Vetor de [strings de permissão em nível de empresa]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_company), em que a presença da string corresponde ao usuário ter a permissão correspondente. |
| `roles` | Opcional | Vetor | Vetor de [objetos de função]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_role-object). |
| `appGroup` | Obrigatória | Vetor | Vetor de [objetos de permissão do espaço de trabalho]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Objeto de permissões do espaço de trabalho

Um objeto de permissão de grupo de apps válido é um objeto JSON com os seguintes pares de chave/valor:

| Chave | Obrigatória | Tipo de dados | Descrição |
| --- | --- | --- | --- |
| `appGroupName`| Opcional | String | Nome do espaço de trabalho. Usado para especificar para qual espaço de trabalho as permissões contidas nesse objeto se destinam. | 
| `appGroupId` | Obrigatório se `appGroupName` estiver ausente | String | ID do espaço de trabalho, servindo como um método alternativo de especificação do espaço de trabalho. |
| `appGroupPermissionSets` | Opcional | Vetor | Vetor com um único [objeto de conjunto de permissões do espaço de trabalho]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-permissions-set-object). |
| `appGroupPermissions` | Obrigatória | Vetor | Vetor de strings de permissão no nível do espaço de trabalho da tabela de [strings de permissão do espaço de trabalho]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_workspace-strings), em que a presença da string corresponde ao usuário ter a permissão correspondente para o espaço de trabalho especificado. |
| `team` | Opcional | Vetor | Vetor de [objetos de permissão da equipe]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_team-permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Objeto do conjunto de permissões do espaço de trabalho {#workspace-permissions-set-object}

Um objeto válido de conjunto de permissões do espaço de trabalho é um objeto JSON com os seguintes pares de chave/valor:

| Chave | Obrigatória | Tipo de dados | Descrição |
| --- | --- | --- | --- |
| `appGroupPermissionSetName` | Opcional | String | Nome do conjunto de permissões do espaço de trabalho que está sendo atribuído ao usuário para esse espaço de trabalho. |
| `appGroupPermissionSetID` | Obrigatório se `appGroupPermissionSetName` estiver ausente | String | ID do espaço de trabalho, servindo como um método alternativo de especificar o conjunto de permissões do espaço de trabalho atribuído ao usuário para esse espaço de trabalho. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Objeto de permissões de equipe

Um objeto de permissão de equipe válido é um objeto JSON com os seguintes pares de chave/valor:

| Chave | Obrigatória | Tipo de dados | Descrição |
| --- | --- | --- | --- |
| `teamName` | Opcional | String | Nome da equipe, que pode ser usado para especificar a qual equipe se destinam as permissões desse objeto. |
| `teamId` | Obrigatório se `teamName` estiver ausente | String | ID da equipe, servindo como um método alternativo de especificar a equipe. |
| `teamPermissions` | Obrigatória | Vetor | Vetor de strings de permissão em nível de equipe da tabela de [strings de permissão de equipes]({{site.baseurl}}/scim_api_appendix/?sdktab=granular%20scim%20api#granularscimapi_team), em que a presença da string corresponde ao usuário ter a permissão correspondente para a equipe especificada. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Objeto de função

Um objeto de função válido é um objeto JSON com os seguintes pares de chave/valor:

| Chave | Obrigatória | Tipo de dados | Descrição |
| --- | --- | --- | --- |
| `roleName` | Opcional | String | Nome da função que está sendo atribuída ao usuário. |
| `roleId` | Obrigatório se `roleName` estiver ausente | String | ID da função, servindo como um método alternativo de especificação da função. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Apêndice

### Strings de permissão da empresa {#company}

| Conforme exibido na interface do usuário | String da API SCIM |
| --- | --- |
| Administrador | `admin` |
| Gerenciar Configurações da Empresa | `manage_company_settings` |
| Criar e excluir espaços de trabalho| `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Strings de permissão do espaço de trabalho {#workspace-strings}

| Nome da permissão | String da API SCIM |
| --- | --- |
| Ver Campanhas | `view_campaigns` |
| Editar Campanhas | `edit_campaigns` |
| Arquivar Campanhas | `archive_campaigns` |
| Ver Canvas | `view_canvases` |
| Editar Canvas | `edit_canvases` |
| Arquivar Canvas | `archive_canvases` |
| Ver regras de limite de frequência | `view_frequency_caps` |
| Editar regras de limite de frequência | `edit_frequency_caps` |
| Ver priorização de mensagens | `view_message_prioritization` |
| Editar priorização de mensagens | `edit_message_prioritization` |
| Ver blocos de conteúdo | `view_content_blocks` |
| Editar blocos de conteúdo | `edit_content_blocks` |
| Arquivar blocos de conteúdo | `archive_content_blocks` |
| Visualizar Feature Flags | `view_feature_flags` |
| Editar Feature Flags | `edit_feature_flags` |
| Arquivar Feature Flags | `archive_feature_flags` |
| Ver Segmentos | `view_segments` |
| Editar Segmentos | `edit_segments` |
| Arquivar Segmentos | `archive_segments` |
| Ver grupo de controle global | `view_global_control_group` |
| Editar grupo de controle global | `edit_global_control_group` |
| Ver modelos de IAM | `view_iam_templates` |
| Editar modelos de IAM | `edit_iam_templates` |
| Arquivar modelos de IAM | `archive_iam_templates` |
| Ver modelos de e-mail | `view_email_templates` |
| Editar modelos de e-mail | `edit_email_templates` |
| Arquivar modelos de e-mail | `archive_email_templates` |
| Ver modelos de webhook | `view_webhook_templates` |
| Editar modelos de webhook | `edit_webhook_templates` |
| Arquivar modelos de webhook | `archive_webhook_templates` |
| Ver modelos de links de e-mail | `view_link_templates` |
| Editar modelos de links de e-mail | `edit_link_templates` |
| Ver ativos da biblioteca de mídia | `view_media_library_assets` |
| Ver locais | `view_locations` |
| Editar locais | `edit_locations` |
| Arquivar locais | `archive_locations` |
| Ver Códigos de Promoção | `view_promotion_codes` |
| Editar Códigos de Promoção | `edit_promotion_codes` |
| Exportar Códigos de Promoção | `export_promotion_codes` |
| Ver Centrais de Preferências | `view_preference_centers` |
| Editar Centrais de Preferências | `edit_preference_centers` |
| Editar Relatórios | `edit_reports` |
| Ver posicionamentos | `view_placements` |
| Editar posicionamentos | `edit_placements` |
| Arquivar posicionamentos | `archive_placements` |
| Ver modelos de banner | `view_banner_templates` |
| Ver Configurações de Múltiplos Idiomas | `view_multi_language_settings` |
| Usar Operator | `use_operator` |
| Ver Agentes do Decisioning Studio | `view_decisioning_studio_agents` |
| Ver público do Decisioning Studio |`view_decisioning_studio_audience` |
| Ver Evento de Conversão do Decisioning Studio | `view_decisioning_studio_conversion_event` |
| Ver proteções do Decisioning Studio | `view_decisioning_studio_guardrails` |
| Lançar Campanhas | `launch_campaigns` |
| Lançar Canvas | `launch_canvases` |
| Editar usuários do dashboard | `edit_dashboard_users` |
| Editar ativos da biblioteca de mídia | `edit_media_library_assets` |
| Excluir ativos da biblioteca de mídia | `delete_media_library_assets` |
| Ver importação de usuários | `view_import_users` |
| Importar usuários	| `import_users` |
| Editar dados de usuários | `edit_user_data` |
| Ver registros de mesclagem de usuários | `view_user_merge_records` |
| Mesclar usuários duplicados | `merge_duplicate_users` |
| Ver chaves de API | `view_api_keys` |
| Editar chaves de API | `edit_api_keys` |
| Ver Grupos Internos | `view_internal_user_groups` |
| Editar Grupos Internos | `edit_internal_user_groups` |
| Excluir Grupos Internos | `delete_internal_user_groups` |
| Ver registro de atividades de envio de mensagem | `view_message_activity_log` |
| Ver registro de usuários de eventos | `view_event_user_log` |
| Ver identificadores de API | `view_api_identifiers` |
| Ver dashboard de uso da API | `view_api_usage_dashboard` |
| Ver limites da API | `view_api_limits` |
| Ver alertas de uso da API | `view_api_usage_alerts` |
| Editar alertas de uso da API | `edit_api_usage_alerts` |
| Ver depurador do SDK | `view_sdk_debugger` |
| Editar depurador do SDK | `edit_sdk_debugger` |
| Lançar blocos de conteúdo | `launch_content_blocks` |
| Editar ingestão de dados na nuvem | `edit_cloud_data_ingestion` |
| Ver configurações do app | `view_app_settings` |
| Editar configurações do app | `edit_app_settings` |
| Ver configurações de push | `view_push_settings` |
| Editar configurações de push | `edit_push_settings` |
| Ver equipes | `view_teams` |
| Editar equipes | `edit_teams` |
| Arquivar equipes | `archive_teams` |
| Ver atributos personalizados | `view_custom_attributes` |
| Editar atributos personalizados | `edit_custom_attributes` |
| Lista de bloqueio de atributos personalizados | `blocklist_custom_attributes` |
| Excluir atributos personalizados | `delete_custom_attributes` |
| Exportar atributos personalizados | `export_custom_attributes` |
| Ver eventos personalizados	 | `view_custom_events` |
| Editar eventos personalizados | `edit_custom_events` |
| Lista de bloqueio de eventos personalizados | `blocklist_custom_events` |
| Excluir eventos personalizados | `delete_custom_events` |
| Exportar eventos personalizados | `export_custom_events` |
| Editar segmentação de propriedades de eventos personalizados | `edit_custom_event_property_segmentation` |
| Ver produtos | `view_products` |
| Editar produtos	 | `edit_products` |
| Lista de bloqueio de produtos | `blocklist_products` |
| Editar segmentação de propriedades de compra | `edit_purchase_property_segmentation` |
| Ver tags | `view_tags` |
| Editar tags | `edit_tags` |
| Excluir tags | `delete_tags` |
| Ver configurações de e-mail	| `view_email_settings` |
| Editar configurações de e-mail | `edit_email_settings` |
| Ver Catálogos | `view_catalogs` |
| Editar Catálogos	 | `edit_catalogs` |
| Exportar Catálogos | `export_catalogs` |
| Excluir Catálogos | `delete_catalogs` |
| Ver Configurações do WhatsApp | `view_whatsapp_settings` |
| Editar Parceiros de Tecnologia | `edit_technology_partners` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Strings de permissão da equipe {#team}

| Nome da permissão | String da API SCIM |
| --- | --- |
| Ver Campanhas | `view_campaigns` |
| Editar Campanhas | `edit_campaigns` |
| Arquivar Campanhas | `archive_campaigns` |
| Ver Canvas | `view_canvases` |
| Editar Canvas | `edit_canvases` |
| Arquivar Canvas | `archive_canvases` |
| Ver regras de limite de frequência | `view_frequency_caps` |
| Editar regras de limite de frequência | `edit_frequency_caps` |
| Ver priorização de mensagens | `view_message_prioritization` |
| Editar priorização de mensagens | `edit_message_prioritization` |
| Ver blocos de conteúdo | `view_content_blocks` |
| Visualizar Feature Flags | `view_feature_flags` |
| Editar Feature Flags | `edit_feature_flags` |
| Arquivar Feature Flags | `archive_feature_flags` |
| Ver Segmentos | `view_segments` |
| Editar Segmentos | `edit_segments` |
| Editar grupo de controle global | `edit_global_control_group` |
| Ver modelos de IAM | `view_iam_templates` |
| Editar modelos de IAM | `edit_iam_templates` |
| Arquivar modelos de IAM | `archive_iam_templates` |
| Ver modelos de e-mail | `view_email_templates` |
| Editar modelos de e-mail | `edit_email_templates` |
| Arquivar modelos de e-mail | `archive_email_templates` |
| Ver modelos de webhook | `view_webhook_templates` |
| Editar modelos de webhook | `edit_webhook_templates` |
| Arquivar modelos de webhook | `archive_webhook_templates` |
| Ver modelos de links de e-mail | `view_link_templates` |
| Editar modelos de links de e-mail | `edit_link_templates` |
| Ver ativos da biblioteca de mídia | `view_media_library_assets` |
| Ver locais | `view_locations` |
| Editar locais | `edit_locations` |
| Arquivar locais | `archive_locations` |
| Ver Códigos de Promoção | `view_promotion_codes` |
| Editar Códigos de Promoção | `edit_promotion_codes` |
| Exportar Códigos de Promoção | `export_promotion_codes` |
| Ver Centrais de Preferências | `view_preference_centers` |
| Editar Centrais de Preferências | `edit_preference_centers` |
| Ver Relatórios | `view_reports` |
| Criar Relatórios | `create_reports` |
| Editar Relatórios | `edit_reports` |
| Ver modelos de banner | `view_banner_templates` |
| Ver Configurações de Múltiplos Idiomas | `view_multi_language_settings` |
| Usar Operator | `use_operator` |
| Ver Agentes do Decisioning Studio | `view_decisioning_studio_agents` |
| Ver Evento de Conversão do Decisioning Studio | `view_decisioning_studio_conversion_event` |
| Lançar Campanhas | `launch_campaigns` |
| Lançar Canvas | `launch_canvases` |
| Editar usuários do dashboard | `edit_dashboard_users` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Strings do departamento

| Conforme exibido na interface do usuário | String da API SCIM |
| --- | --- |
| Agência/Terceiro | `agency` |
| BI/Análise de dados | `bi` |
| Diretoria | `c_suite` |
| Engenharia | `engineering` |
| Financeiro | `finance` |
| Marketing/Editorial | `marketing` |
| Gestão de produto | `pm` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }