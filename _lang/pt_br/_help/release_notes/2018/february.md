---
nav_title: Fevereiro
page_order: 11
noindex: true
page_type: update
description: "Este artigo contém notas de versão de fevereiro de 2018."
---
# Fevereiro de 2018

## Contagem de ícones de notificação de push do iOS

Agora você pode [atualizar a contagem de emblemas][89] no criador de push do Braze.
Para cada mensagem por push, você pode especificar a contagem de ícones de notificação que a notificação dispara.

## Exportação de usuários via API usando endereços de e-mail

Agora é possível [exportar dados de perfis de usuários via API][88], especificando endereços de e-mail.
Essa exportação inclui todos os perfis associados a esse endereço de e-mail.

## APIs de modelos de e-mail

Agora você pode criar e atualizar [modelos de e-mail via API][87]. Cada modelo terá um **email_template_id** que pode ser referenciado em outras chamadas de API.

## Permissões de chaves da API REST

Agora você pode criar [várias chaves da API REST][86] e configurar permissões de acesso para cada uma delas. Cada chave pode ser configurada para conceder acesso a determinados endpoints.

Você também pode especificar uma [lista de permissões de endereços IP][85] e sub-redes que têm permissão para fazer solicitações de API REST para uma determinada chave da API REST.

[85]: {{site.baseurl}}/developer_guide/rest_api/basics/#api-ip-whitelisting
[86]: {{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys
[87]: {{site.baseurl}}/developer_guide/rest_api/email_templates/#email-templates
[88]: {{site.baseurl}}/developer_guide/rest_api/export/#user-export
[89]: {{site.baseurl}}/help/best_practices/utilizing_badge_count/#utilizing-badge-count
