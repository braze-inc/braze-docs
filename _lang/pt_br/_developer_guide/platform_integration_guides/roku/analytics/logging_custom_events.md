---
nav_title: Rastreamento de eventos personalizados
article_title: Rastreamento de eventos personalizados para o Roku
platform: Roku
page_order: 2
page_type: reference
description: "Esta página aborda métodos para registrar eventos personalizados para o Roku por meio do SDK da Braze."

---

# Rastreamento de eventos personalizados

> Você pode registrar eventos personalizados no Braze para saber mais sobre os padrões de uso do seu app e para segmentar seus usuários por suas ações no dashboard. Recomendamos também que você se familiarize com nossas [convenções de nomenclatura de eventos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/).

## Adicionar um evento personalizado

```brightscript
m.Braze.logEvent("YOUR_EVENT_NAME")
```

### Adicionando propriedades

Você pode adicionar metadados sobre eventos personalizados passando um dicionário de propriedades com seu evento personalizado.

As propriedades são definidas como pares de valores-chave.  As chaves são objetos `String` e os valores podem ser `String` ou `Integer`.

```brightscript
m.Braze.logEvent("YOUR_EVENT_NAME", {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})
```
