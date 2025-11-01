---
nav_title: Convenções de nomenclatura de eventos
article_title: Convenções de nomenclatura de eventos
page_order: 10
page_type: reference
description: "Este artigo de referência aborda as convenções adequadas de nomenclatura de eventos e as práticas recomendadas."

---

# Convenções de nomenclatura de eventos

> Esta página aborda as convenções adequadas de nomenclatura de eventos e as práticas recomendadas. Ao manter a consistência em sua taxonomia de eventos e atributos, você manterá seus dados limpos e utilizáveis para usuários novos e existentes da plataforma Braze. Isso ajuda a evitar problemas posteriores, como o acionamento de uma campanha para o público errado ou a geração de resultados errados após o uso do evento errado.

## Práticas recomendadas

- Mantenha sua convenção de nomenclatura clara.
- Use letras maiúsculas e minúsculas e formatação consistente nos nomes dos eventos.
- Evite dar nomes semelhantes aos eventos.
- Evite longas sequências de atributos de eventos, que serão truncadas ou cortadas no painel do Braze.

## Convenções de nomenclatura

### Usar grupos de eventos

Use grupos para diferenciar partes de seu produto para nomear eventos. Ao categorizar seu produto em grupos, qualquer usuário pode entender claramente a que o evento se refere e o que ele faz.

### Estrutura de nomenclatura de eventos

A estrutura de nomes mais comum é `group_noun_action`. Os eventos devem ser todos em letras minúsculas para evitar erros de instrumentação e identificação de propriedades.

### Propriedades

Marque um evento e, em seguida, identifique as diferenças usando as propriedades. Isso é útil para eventos que são inerentemente iguais, mas têm pequenas diferenças, como canais para uma campanha. Também podemos ver facilmente como os usuários fluem pelos eventos. Consulte o [objeto de propriedades do evento]({{site.baseurl}}/api/objects_filters/event_object/#event-properties-object) para obter um exemplo e contexto adicional.

## Exemplos

Digamos que você faça parte de uma empresa de comércio eletrônico e esteja interessado em rastrear quando os clientes se inscreveram no seu aplicativo e quando assinaram o seu boletim informativo. Aqui estão alguns exemplos de nomes de eventos eficazes:

- `user_signup`
- `newsletter_subscribed`

Esses dois nomes de eventos indicam claramente o evento que estão rastreando. À medida que você criar mais eventos personalizados, certifique-se de manter suas convenções de nomenclatura compreensíveis. Por exemplo, evite usar nomes de eventos como `signup_event_1`, pois isso não é claro e não transmite o que o evento está rastreando, em comparação com `user_signup`.
