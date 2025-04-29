---
nav_title: Endpoints de API e SDK
article_title: Endpoints de API e SDK
page_order: 1
page_type: reference
description: "Este artigo de referência lista os URLs do dashboard, os endpoints da API e os endpoints do SDK para as instâncias disponíveis da Braze."

---

# Endpoints de API e SDK

> Sua instância da Braze determina a URL necessária para registrar-se na Braze, acessar a API e integrar seu SDK. Saiba mais sobre o SDK da Braze no curso do Braze Learning, [Braze 101](https://learning.braze.com/braze-101).

A Braze gerencia várias instâncias diferentes de nosso dashboard, SDK e endpoints REST, que chamamos de "clusters". Seu gerente de integração da Braze informará em qual cluster você está.

O registro em [dashboard.braze.com](https://dashboard.braze.com) o enviará automaticamente para o endereço correto do cluster.

{% multi_lang_include data_centers.md datacenters='instâncias' %}

{% alert important %}
Ao integrar seu SDK, use o endpoint do SDK. Ao fazer chamadas para nossa API REST, use o endpoint REST.
{% endalert %}

Para obter detalhes sobre como acessar a API, consulte nosso [artigo de visão geral da API]({{site.baseurl}}/api/basics/). 
