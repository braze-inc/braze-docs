---
nav_title: Pontos de extremidade de API e SDK
article_title: Pontos de extremidade de API e SDK
page_order: 1
page_type: reference
description: "Este artigo de referência lista os URLs do painel, os pontos de extremidade da API e os pontos de extremidade do SDK para as instâncias disponíveis do Braze."

---

# Pontos de extremidade de API e SDK

> Sua instância do Braze determina a URL necessária para fazer login no Braze, acessar a API e integrar seu SDK. Saiba mais sobre o Braze SDK em nosso curso Braze Learning, [Braze 101](https://learning.braze.com/braze-101).

O Braze gerencia várias instâncias diferentes para nosso painel, SDK e pontos de extremidade REST, que chamamos de "clusters". Seu gerente de integração do Braze informará em qual cluster você está.

Fazer login em [dashboard.braze.com](https://dashboard.braze.com) o enviará automaticamente para o endereço correto do cluster.

{% multi_lang_include data_centers.md datacenters='instances' %}

{% alert important %}
Ao integrar seu SDK, use o ponto de extremidade do SDK. Ao fazer chamadas para nossa API REST, use o ponto de extremidade REST.
{% endalert %}

Para obter detalhes sobre como acessar a API, consulte nosso [artigo de visão geral da API]({{site.baseurl}}/api/basics/). 
