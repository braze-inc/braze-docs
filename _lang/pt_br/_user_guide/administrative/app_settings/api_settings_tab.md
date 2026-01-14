---
nav_title: APIs e identificadores
article_title: APIs e identificadores
page_order: 3
page_type: reference
description: "Este artigo aborda a página APIs e identificadores, que exibe as identificações de API para seu espaço de trabalho."

---

# Chaves de API

> A página **APIs e identificadores** é o seu hub centralizado para gerenciar todas as suas chaves de API REST em um só lugar. Aqui, você pode acessar o conjunto de chaves de API e identificadores de aplicativos de cada espaço de trabalho.

Você pode encontrar a página **APIs e identificadores** em **Configurações**.

### Chaves de API

Esta seção fornece as chaves da API REST do seu espaço de trabalho, os identificadores exclusivos que permitem o acesso aos dados de um espaço de trabalho. Uma chave de API REST é necessária em cada solicitação à API do Braze. Para obter mais informações sobre como criar e usar chaves de API, consulte nossa [visão geral da chave de API REST]({{site.baseurl}}/api/api_key/).

#### Lista de permissões de IP da API

Para maior segurança, você pode especificar uma lista de endereços IP e sub-redes autorizados a fazer solicitações de API REST para uma determinada chave de API REST. Isso é chamado de lista de permissões ou lista branca. Para permitir endereços IP ou sub-redes específicos, adicione-os à seção **Whitelist IPs (IPs da lista branca)** ao criar uma nova chave de API REST: 

\![Seção de lista branca de IPs da API na criação de uma nova chave de API]({% image_buster /assets/img_archive/api-key-ip-whitelisting.png %})

Se você não especificar nenhum, as solicitações poderão ser enviadas de qualquer endereço IP.

{% alert tip %}
Como criar um webhook Braze-to-Braze e usar o allowlisting? Confira nossa lista de [IPs para colocar na lista de permissões]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-whitelisting).
{% endalert %}

### Identificadores de aplicativos

Esta seção inclui uma lista de identificadores usados para fazer referência a aplicativos específicos em solicitações feitas à API do Braze. Para saber mais sobre identificadores de aplicativos, consulte [Chave da API do identificador de aplicativos]({{site.baseurl}}/api/identifier_types/).

### Outros identificadores

Para integrar-se à nossa API, você pode pesquisar os identificadores relacionados a quaisquer segmentos, campanhas, cartões de conteúdo e outros que você deseja acessar a partir da API externa do Braze. Todas as mensagens devem seguir a codificação [UTF-8](https://en.wikipedia.org/wiki/UTF-8). Depois de selecionar qualquer um deles, o identificador será exibido abaixo do menu suspenso.

Para obter mais informações, consulte [Tipos de identificadores de API]({{site.baseurl}}/api/identifier_types/).

