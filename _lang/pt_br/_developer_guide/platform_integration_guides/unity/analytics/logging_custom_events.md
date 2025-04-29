---
nav_title: Rastreamento de eventos personalizados
article_title: Rastreamento de Eventos Personalizados para Unity
platform: 
  - Unity
  - iOS
  - Android
page_order: 1
description: "Este artigo de referência cobre como registrar eventos personalizados na plataforma Unity."

---

# Rastreamento de eventos personalizados

> Você pode registrar eventos personalizados no Braze para saber mais sobre os padrões de uso do seu app e para segmentar seus usuários por suas ações no dashboard.

Antes da implementação, certifique-se de revisar exemplos das opções de segmentação oferecidas por eventos personalizados, atributos personalizados e eventos de compra em nossas [Melhores práticas][4]. Recomendamos também que você se familiarize com nossas [convenções de nomenclatura de eventos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

```csharp
AppboyBinding.LogCustomEvent("event name");
```

A Braze também oferece suporte à adição de metadados sobre eventos personalizados, passando um `Dictionary` de propriedades de eventos:

```csharp
AppboyBinding.LogCustomEvent("event name", properties(Dictionary<string, object>));
```

## API REST

Você também pode usar nossa API REST para registrar eventos. Consulte a documentação [da API dos usuários][5] para obter detalhes.

[4]: {{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#best-practices
[5]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
