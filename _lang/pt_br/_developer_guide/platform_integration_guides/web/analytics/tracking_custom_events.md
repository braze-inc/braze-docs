---
nav_title: Rastreamento de eventos personalizados
article_title: Rastreamento de eventos personalizados para a Web
platform: Web
page_order: 2
page_type: reference
description: "Este artigo aborda como rastrear eventos personalizados e adicionar propriedades a esses eventos para a Web."

---

# Rastreamento de eventos personalizados

> Você pode registrar eventos personalizados no Braze para saber mais sobre os padrões de uso do seu app e para segmentar seus usuários por suas ações no dashboard.

Antes da implementação, certifique-se de revisar exemplos das opções de segmentação oferecidas por eventos personalizados, atributos personalizados e eventos de compra em nossas [Melhores práticas]({{site.baseurl}}/developer_guide/platform_wide/getting_started/analytics_overview/#best-practices). Também recomendamos que você se familiarize com nossas [convenções de nomenclatura de eventos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

```javascript
braze.logCustomEvent("YOUR-EVENT-NAME");
```

Consulte a [`logCustomEvent`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent) para saber mais.

## Adição de propriedades {#properties-events}

Opcionalmente, você pode adicionar metadados sobre eventos personalizados passando um objeto de propriedades com seu evento personalizado.

Propriedades são definidas como pares chave-valor. As chaves são strings e os valores podem ser objetos `string`, `numeric`, `boolean` ou [`Date`](http://www.w3schools.com/jsref/jsref_obj_date.asp).

```javascript
braze.logCustomEvent("YOUR-EVENT-NAME", {
  you: "can", 
  pass: false, 
  orNumbers: 42,
  orDates: new Date(),
  or: ["any", "array", "here"],
  andEven: {
     deeply: ["nested", "json"]
  }
});
```

Consulte a [documentação do site`logCustomEvent()` ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent) para obter mais informações.

