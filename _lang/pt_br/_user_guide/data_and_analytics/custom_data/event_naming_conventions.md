---
nav_title: Convenções de nomenclatura de eventos
article_title: Convenções de nomenclatura de eventos
page_order: 10
page_type: reference
description: "Este artigo de referência aborda as convenções adequadas de nomenclatura de eventos e as práticas recomendadas."

---

# Convenções de nomenclatura de eventos

> Garantir a consistência na taxonomia de eventos e atribuições durante a integração com o Braze manterá seus dados limpos e utilizáveis por usuários novos e existentes da plataforma Braze. Isso ajuda a evitar problemas posteriores que podem disparar uma campanha para o público errado ou causar discrepâncias nos resultados devido ao uso do evento errado.

## Práticas recomendadas

- Mantenha sua convenção de nomenclatura clara.
- Use letras maiúsculas e minúsculas e formatação consistente nos nomes dos eventos.
- Evite dar nomes semelhantes aos eventos.
- Evite longas strings de atribuições de eventos, que serão truncadas ou cortadas no dashboard da Braze.

## Convenções de nomenclatura

### Usar grupos de eventos

Use grupos para diferenciar partes de seu produto para nomear eventos. Ao categorizar seu produto em grupos, qualquer usuário pode entender claramente a que o evento se refere e o que ele faz.

### Estrutura de nomenclatura de eventos

A estrutura de nomes mais comum é `group_noun_action`. Os eventos devem ser todos em letras minúsculas para evitar erros de instrumentação e identificação de propriedades.

### Propriedades

Tag um evento e, em seguida, identifique as diferenças usando as propriedades. Isso é útil para eventos que são inerentemente iguais, mas têm pequenas diferenças, como canais para uma campanha. Também podemos ver facilmente como os usuários fluem pelos eventos. Consulte o [objeto de propriedades do evento]({{site.baseurl}}/api/objects_filters/event_object/#event-properties-object) para obter um exemplo e contexto adicional.
