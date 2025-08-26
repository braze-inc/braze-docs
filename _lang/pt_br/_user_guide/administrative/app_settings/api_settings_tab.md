---
nav_title: APIs e identificadores
article_title: APIs e identificadores
page_order: 3
page_type: reference
description: "Este artigo aborda a página APIs e identificadores, que exibe as identificações de API para seu espaço de trabalho."

---

# Chaves de API

> A página **APIs e identificadores** é o hub centralizado para gerenciar todas as chaves da API REST em um só lugar. Aqui, você pode acessar o conjunto de chaves de API e identificadores de app de cada espaço de trabalho.

Você pode encontrar a página **APIs e identificadores** em **Configurações**.

### Chaves de API

Esta seção fornece as chaves da API REST do seu espaço de trabalho, os identificadores exclusivos que permitem o acesso aos seus dados para um espaço de trabalho. Uma chave de API REST é necessária em cada solicitação à API da Braze. Para saber mais sobre como criar e usar chaves de API, consulte nossa [visão geral da chave da API REST]({{site.baseurl}}/api/api_key/).

#### Lista de permissões de IP da API

Para maior segurança, você pode especificar uma lista de endereços IP e sub-redes autorizados a fazer solicitações de API REST para uma determinada chave de API REST. Isso é chamado de lista de permissões ou lista de brancos. Para permitir endereços IP ou sub-redes específicos, adicione-os à seção **Lista de permissões de IPs** ao criar uma nova chave da API REST: 

![Seção de lista de permissões de IP da API para criar uma nova chave de API]({% image_buster /assets/img_archive/api-key-ip-whitelisting.png %})

Se você não especificar nenhum, as solicitações poderão ser enviadas de qualquer endereço IP.

{% alert tip %}
Como criar um webhook Braze-to-Braze e usar o allowlisting? Confira nossa lista de [IPs para lista de permissões]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-whitelisting).
{% endalert %}

### Identificadores de app

Esta seção inclui uma lista de identificadores usados para fazer referência a apps específicos em solicitações feitas à API do Braze. Para saber mais sobre identificadores de aplicativos, consulte [Chave de API do identificador de]({{site.baseurl}}/api/identifier_types/) aplicativo.

### Outros identificadores

Para integrar-se à nossa API, você pode pesquisar os identificadores relacionados a quaisquer segmentos, campanhas, cartões de conteúdo e outros que deseja acessar na API externa do Braze. Todas as mensagens devem seguir a codificação [UTF-8](https://en.wikipedia.org/wiki/UTF-8). Depois de selecionar qualquer um deles, o identificador será exibido abaixo do menu suspenso.

Para saber mais, consulte [Tipos de identificadores da API]({{site.baseurl}}/api/identifier_types/).

