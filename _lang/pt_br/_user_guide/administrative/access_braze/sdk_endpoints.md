---
nav_title: Endpoints de API e SDK
article_title: Endpoints de API e SDK
page_order: 1
page_type: reference
description: "Este artigo de referência lista os URLs do dashboard, os endpoints da API e os endpoints do SDK para as instâncias disponíveis da Braze."

---

# Endpoints de API e SDK

> Sua instância da Braze determina a URL necessária para registrar-se na Braze, acessar a API e integrar seu SDK. Saiba mais sobre o SDK da Braze no curso do Braze Learning, [Braze 101][1].

A Braze gerencia várias instâncias diferentes de nosso dashboard, SDK e endpoints REST, que chamamos de "clusters". Seu gerente de integração da Braze informará em qual cluster você está.

O registro em [dashboard.braze.com](https://dashboard.braze.com) o enviará automaticamente para o endereço correto do cluster.

|Instância|URL|Endpoint REST|Endpoint do SDK|
|---|---|---|
|US-01| `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com` | `sdk.iad-01.braze.com` |
|US-02| `https://dashboard-02.braze.com` | `https://rest.iad-02.braze.com` | `sdk.iad-02.braze.com` |
|US-03| `https://dashboard-03.braze.com` | `https://rest.iad-03.braze.com` | `sdk.iad-03.braze.com` |
|US-04| `https://dashboard-04.braze.com` | `https://rest.iad-04.braze.com` | `sdk.iad-04.braze.com` |
|US-05| `https://dashboard-05.braze.com` | `https://rest.iad-05.braze.com` | `sdk.iad-05.braze.com` |
|US-06| `https://dashboard-06.braze.com` | `https://rest.iad-06.braze.com` | `sdk.iad-06.braze.com` |
|US-07| `https://dashboard-07.braze.com` | `https://rest.iad-07.braze.com` | `sdk.iad-07.braze.com` |
|US-08| `https://dashboard-08.braze.com` | `https://rest.iad-08.braze.com` | `sdk.iad-08.braze.com` |
|EU-01| `https://dashboard-01.braze.eu` | `https://rest.fra-01.braze.eu` | `sdk.fra-01.braze.eu` |
|EU-02| `https://dashboard-02.braze.eu` | `https://rest.fra-02.braze.eu` | `sdk.fra-02.braze.eu` |
|AU-01| `https://dashboard.au-01.braze.com`| `https://rest.au-01.braze.com` | `sdk.au-01.braze.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
Ao integrar seu SDK, use o endpoint do SDK. Ao fazer chamadas para nossa API REST, use o endpoint REST.
{% endalert %}

Para saber como acessar a API, consulte o [artigo de visão geral da API][2]. 


[1]: https://learning.braze.com/braze-101
[2]: {{site.baseurl}}/api/basics/