---
nav_title: Shopify checkout.liquid
page_order: 7
description: "Este artigo explica a descontinuação do Shopify checkout.liquid, incluindo o impacto na sua integração com a Shopify e orientações para desenvolvedores."
page_type: update

---

# Descontinuação do Shopify checkout.liquid

Shopify informou a todos os comerciantes sobre a descontinuação de `checkout.liquid`, e a migração para [Checkout Extensibility](https://www.shopify.com/enterprise/blog/checkout-extensibility-winter-editions), uma nova base para criar experiências de checkout personalizadas. 

Shopify descontinuará `checkout.liquid` em duas fases:

1. **[13 de agosto de 2024](#phase-one-august-13-2024):** Prazo para fazer upgrade das suas páginas de informações, envio e pagamento.
2. **[28 de agosto de 2025](#phase-two-august-28-2025):** Prazo para fazer upgrade das suas páginas de agradecimento e status do pedido, incluindo seus aplicativos que usam tags de script e scripts adicionais.

Para obter informações gerais sobre como fazer upgrade para a Extensibilidade do Checkout, consulte [o guia de upgrade da Shopify](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-extensibility).

## Impacto na sua integração

A integração Braze e Shopify usa [Shopify ScriptTags](https://shopify.dev/docs/apps/build/online-store/script-tag-legacy) para carregar a Braze Web SDK para sites não headless. Estamos planejando lançar uma nova versão da integração antes do prazo de 2025 para apoiar todos os clientes antes que `checkout.liquid` seja totalmente descontinuado. 

Para as próximas mudanças em 13 de agosto de 2024, verifique os detalhes abaixo para ver se você será impactado pela sua equipe de desenvolvimento.

### Fase um: 13 de agosto de 2024

A integração padrão da Braze e Shopify não usa as páginas de informações, envio e pagamento dentro da experiência de checkout. Como resultado, a integração padrão não será afetada. 

#### Shopify Plus

Para os clientes do Shopify Plus, quaisquer trechos de código SDK personalizados que modifiquem `checkout.liquid` para as páginas de informações, envio ou pagamento se tornarão inativos após esta data. Por exemplo, o código personalizado que registra eventos dessas páginas não funcionará mais. Se você tiver código SDK personalizado, consulte nosso [guia do desenvolvedor](#developer-guidance) para migração.

#### Não-Shopify Plus

Para clientes que não são do Shopify Plus, se você precisar personalizar as páginas de informações, pagamento e envio, você [precisa fazer upgrade para o Shopify Plus](https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/checkout-extensibility#eligibility) e então seguir as [orientações do desenvolvedor](#developer-guidance).

### Fase dois: 28 de agosto de 2025

Shopify vai descontinuar o suporte para [ScriptTags](https://shopify.dev/docs/apps/build/online-store/script-tag-legacy) em páginas `checkout.liquid`, que são usadas na integração. Em resposta, estamos ativamente construindo uma nova versão da integração com a Shopify, que planejamos lançar bem antes do prazo de agosto de 2025. Fique atento para saber mais da equipe de produtos da Braze. 

## Orientação para desenvolvedores

Esta orientação se aplica aos clientes do Shopify Plus que adicionaram trechos de código SDK personalizados às páginas de informações, envio ou pagamento em `checkout.liquid`. Se você não fez essas personalizações, pode desconsiderar esta orientação.

Você não poderá mais adicionar trechos de código SDK personalizados às páginas de informações, envio ou pagamento em `checkout.liquid`. Em vez disso, você precisará adicionar trechos de código SDK personalizados às páginas de agradecimento ou de status do pedido. Isso permite que você reconcilie os usuários que concluíram o checkout.
1. Carregue o SDK web da Braze nas páginas de agradecimento e status do pedido.
2. Recuperar o e-mail do usuário.
3. Ligue para `setEmail`.

{% raw %}
```java
braze.getUser().setEmail(<email address>);
```
{% endraw %}

{: start="4"}
4\. No Braze, mescle os perfis de usuário no e-mail.

Se você encontrar perfis de usuário duplicados, pode usar nossa [ferramenta de mesclagem em massa]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users#bulk-merging) para ajudar a simplificar seus dados. 
