---
nav_title: Código personalizado e ponte JavaScript
article_title: Código personalizado e ponte JavaScript para Banners
page_order: 2
page_type: reference
description: "Aprenda a usar HTML personalizado em Banners e a ponte JavaScript para registrar cliques e disparar ações do Braze."
channel:
  - banners
---

# Código personalizado e ponte JavaScript para Banners

> Quando você usa o bloco de editor **Código Personalizado** no criador de Banners, deve chamar `brazeBridge.logClick()` de dentro do seu HTML personalizado para registrar cliques. Os Banners usam a mesma ponte JavaScript que mensagens HTML dentro do aplicativo, então os mesmos métodos e padrões se aplicam.

Se você usar HTML personalizado no design do seu Banner, o SDK do Braze não pode anexar automaticamente ouvintes de cliques a elementos dentro do seu código personalizado. Você deve chamar explicitamente `brazeBridge.logClick()` para qualquer elemento clicável (links, botões e similares) que você deseja rastrear na análise de campanhas.

Por exemplo, para registrar um clique quando um usuário toca em um botão no seu HTML personalizado:

```html
<button onclick="brazeBridge.logClick()">
  Click me
</button>
```

Para a referência completa da ponte JavaScript, incluindo todos os métodos disponíveis e opções de rastreamento de cliques, veja a seção abaixo.

## Ponte JavaScript {#javascript-bridge}

{% include javascript_bridge/reference.md %}
