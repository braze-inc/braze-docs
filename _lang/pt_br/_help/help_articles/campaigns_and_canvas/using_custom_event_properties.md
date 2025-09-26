---
nav_title: Registrando Propriedades de evento personalizado
article_title: Registrando Propriedades de evento personalizado
page_order: 3
page_type: solution
description: "Este artigo de ajuda orienta você por três verificações importantes para garantir que seus eventos personalizados sejam registrados conforme o esperado."
tool: 
- Campaigns
- Canvas
---

# Registrando propriedades de evento personalizado

Existem três verificações importantes a serem realizadas para garantir que seus eventos personalizados estejam sendo registrados conforme o esperado:

* [Estabeleça quais eventos são registrados](#verify-events)
* [Verifique o registro](#verify-log)
* [Verifique os valores](#verify-values)

## Verificar propriedades do evento personalizado

[Propriedades de evento personalizado]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties) são metadados que descrevem eventos personalizados. Várias propriedades podem ser registradas cada vez que um evento personalizado é registrado.

### Verificar eventos

Verifique com seus desenvolvedores quais propriedades de eventos estão sendo rastreadas. Lembre-se de que todas as propriedades do evento diferenciam maiúsculas de minúsculas. Para obter informações adicionais sobre rastreamento de eventos personalizados, confira estes artigos com base na sua plataforma:

* [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/)
* [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/)
* [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/)

### Verificar registro

Para confirmar que as propriedades do evento são rastreadas com sucesso, você pode visualizar todas as propriedades do evento na página de **Eventos Personalizados**.

1. Navegando para **Configurações de Dados** > **Eventos Personalizados**.
2. Localize seu evento personalizado na lista.
3. Para o seu evento, clique em **Gerenciar Propriedades**. Isso mostrará os nomes das propriedades associadas a um evento.

### Verificar valores

Depois de adicionar seu usuário como um usuário teste, siga estas etapas para verificar seus valores: 

1. Execute o evento personalizado dentro do app.
2. Aguarde cerca de 10 segundos para que os dados sejam liberados.
3. Atualize o [registro de usuários de eventos]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) para ver o evento personalizado e o valor da propriedade do evento que foi passado com ele.

Ainda precisa de ajuda? Abra um [ticket de suporte]({{site.baseurl}}/braze_support/).

_Última atualização em 10 de abril de 2023_

