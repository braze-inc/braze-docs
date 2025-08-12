---
nav_title: Janeiro
page_order: 12
noindex: true
page_type: update
description: "Este artigo contém notas de versão de janeiro de 2018."
---
# Janeiro de 2018

## CSS inlining

Agora você pode ativar ou desativar [o CSS inlining]({{site.baseurl}}/user_guide/message_building_by_channel/email/css_inline/#css-inlining) para mensagens de e-mail individuais acessando **as Configurações de e-mail**.

## Novos filtros de segmento

Agora você pode criar segmentos usando os seguintes filtros:
- Recebeu uma etapa do canva
- Etapa do canva aberta/clicada
- Última etapa do canva específica recebida

{% alert update %}
A partir de março de 2019, `Received Canvas Step` foi renomeado para `Received Message from Canvas Step`, e `Last Received Specific Canvas Step` foi renomeado para `Last Received Message from Specific Canvas Step`.
{% endalert %}

## Exportação de usuários usando o ID do dispositivo

Esse endpoint agora aceita um identificador de dispositivo como parâmetro, o que permite [exportar perfis de usuários anônimos]({{site.baseurl}}/developer_guide/rest_api/export/#users-by-identifier-endpoint).

É possível usar o ID do dispositivo para exportar todos os perfis de usuário desse dispositivo.

## Atualização dos relatórios de engajamento

Estatísticas adicionais, como **a taxa de abertura de push** e **a taxa de conversão**, agora estão disponíveis nos [relatórios de engajamento]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#engagement-reports).

## Certificados push da Apple: Uso de arquivos .p8

Agora é possível usar um [arquivo p8]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#recommended-option-using-a-p8-file-authentication-tokens) ao fazer upload de um certificado Apple Push, garantindo que suas credenciais push do iOS nunca expirem.


