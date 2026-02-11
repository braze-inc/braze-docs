---
nav_title: "Objetos e apêndice da API do SCIM"
article_title: Objetos e Apêndice da API SCIM
page_order: 8
page_type: reference
description: "Este artigo explica os diferentes objetos e o apêndice da API do SCIM."
hidden: true
permalink: "/scim_api_appendix/"
---

# Objetos e apêndice da API do SCIM

## Objeto de permissões

O objeto de permissões é um campo encontrado em algumas das solicitações e respostas ao fazer interface com o recurso do usuário por meio de permissões de ID SCIM.

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
| `companyPermissions` | Opcional | Vetor | Matriz de strings de permissão no nível da empresa da tabela de [strings de permissão da empresa](#company), na qual a presença da string corresponde ao usuário que tem a permissão correspondente. |
| `roles` | Opcional | Vetor | Vetor de [objetos de função](#role-object). |
| `appGroup` | Obrigatória | Vetor | Vetor de [objetos de permissão do espaço de trabalho](#workspace-permission-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Objeto de permissões do espaço de trabalho {#workspace-permission-object}

Um objeto de permissão de grupo de apps válido é um objeto JSON com os seguintes pares de chave/valor:

| Chave | Obrigatória | Tipo de dados | Descrição |
| --- | --- | --- | --- |
| `appGroupName`| Opcional | String | Nome do espaço de trabalho. Usado para especificar para qual espaço de trabalho as permissões contidas nesse objeto se destinam. | 
| `appGroupId` | Obrigatório se `appGroupName` estiver ausente | String | ID do espaço de trabalho, servindo como um método alternativo de especificação do espaço de trabalho. |
| `appGroupPermissionSets` | Opcional | Vetor | Vetor com um único [objeto de conjunto de permissões de espaço de trabalho](#workspace-permissions-set-object). |
| `appGroupPermissions` | Obrigatória | Vetor | Vetor de strings de permissão no nível do espaço de trabalho da tabela de [strings de permissão do espaço de trabalho](#workspace-strings), na qual a presença da string corresponde ao usuário que tem a permissão correspondente para o espaço de trabalho especificado. |
| `team` | Opcional | Vetor | Vetor de [objetos de permissão da equipe](#team-permissions-object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Objeto do conjunto de permissões do espaço de trabalho {#workspace-permissions-set-object}

Um objeto válido de conjunto de permissões de espaço de trabalho é um objeto JSON com os seguintes pares de valores-chave:

| Chave | Obrigatória | Tipo de dados | Descrição |
| --- | --- | --- | --- |
| `appGroupPermissionSetName` | Opcional | String | Nome do conjunto de permissões do espaço de trabalho que está sendo atribuído ao usuário para esse espaço de trabalho. |
| `appGroupPermissionSetID` | Obrigatório se `appGroupPermissionSetName` estiver ausente | String | ID do espaço de trabalho, servindo como um método alternativo de especificar o conjunto de permissões do espaço de trabalho atribuído ao usuário para esse espaço de trabalho. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Objeto de permissões de equipe

Um objeto de permissão de equipe válido é um objeto JSON com os seguintes pares de valores-chave:

| Chave | Obrigatória | Tipo de dados | Descrição |
| --- | --- | --- | --- |
| `teamName` | Opcional | String | Nome da equipe, que pode ser usado para especificar a qual equipe se destinam as permissões desse objeto. |
| `teamId` | Obrigatório se `teamName` estiver ausente | String | ID da equipe, servindo como um método alternativo de especificar a equipe. |
| `teamPermissions` | Obrigatória | Vetor | Matriz de strings de permissão em nível de equipe da tabela de [strings de permissão de equipes](#team), na qual a presença da string corresponde ao usuário que tem a permissão correspondente para a equipe especificada. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Objeto de função

Um objeto de função válido é um objeto JSON com os seguintes pares de valores-chave:

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
| Pode gerenciar configurações da empresa | `manage_company_settings` |
| Pode adicionar/remover espaços de trabalho| `add_remove_app_groups` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Strings de permissão do espaço de trabalho {#workspace-strings}

| Nome da permissão | String da API SCIM |
| --- | --- |
| Administrador | `admin` |
| Campanhas de acesso, canvas, cartões, segmentos, biblioteca de mídia | `basic_access` |
| Aprovar e rejeitar canvas | `approve_deny_campaigns` |
| Enviar campanhas, canvas | `send_campaigns_canvases` |
| Publicar cartões | `publish_cards` |
| Editar segmentos | `edit_segments` |
| Exportar dados de usuários | `export_user_data` |
| Ver IPI | `view_pii` |
| Ver perfis de usuário em conformidade com IPI | `view_user_profile` |
| Gerenciar usuários do dashboard | `manage_dashboard_users` |
| Gerenciar ativos da biblioteca de mídia | `manage_media_library` |
| Ver dados de uso | `view_usage_data` |
| Importação e atualização de dados de usuários | `import_update_user_data` |
| Ver informações de faturamento | `view_billing_details` |
| Acessar console de desenvolvedores | `dev_console` |
| Lançar blocos de conteúdo | `launch_content_blocks` |
| Gerenciar integrações externas | `manage_external_integrations` |
| Gerenciar apps | `manage_apps` |
| Gerenciar equipes | `manage_teams` |
| Gerenciar eventos, atributos, compras | `manage_events_attributes_purchases` |
| Gerenciar tags | `manage_tags` |
| Gerenciar configurações de e-mail | `manage_email_settings` |
| Gerenciar grupos de inscrição | `manage_subscription_groups` |
| Gerenciar configurações de aprovação | `manage_approval_settings` |
| Permissão para gerenciar catálogos do dashboard | `manage_catalogs_dashboard_permission` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Strings de permissão da equipe {#team}

| Nome da permissão | String da API SCIM |
| --- | --- |
| Administrador | `admin` |
| Campanhas de acesso, canvas, cartões, segmentos, biblioteca de mídia | `basic_access` |
| Aprovar e rejeitar canvas | `approve_deny_campaigns` |
| Enviar campanhas, canvas | `send_campaigns_canvases` |
| Publicar cartões | `publish_cards` |
| Editar segmentos | `edit_segments` |
| Exportar dados de usuários | `export_user_data` |
| Ver perfil do usuário | `view_user_profile` |
| Gerenciar usuários do dashboard | `manage_dashboard_users` |
| Gerenciar ativos da biblioteca de mídia | `manage_media_library` |
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
