---
nav_title: Criação de canais
article_title: Criação de posicionamentos de cartão de banner para o SDK do Braze
hidden: true
description: "Este artigo de referência aborda os cartões de banner e como integrar esse recurso no Braze SDK."
platform:
  - iOS
  - Android
  - Web
  
---

# Criação de posicionamentos de cartões de banner

> Antes de lançar uma campanha de cartão de banner em seu app, você precisará criar um posicionamento no dashboard do Braze. Os posicionamentos são locais que você define em seu app e que podem exibir cartões de banner.

{% alert important %}
Os cartões de banner estão atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar desse acesso antecipado.
{% endalert %}

## Pré-requisitos

Essas são as versões mínimas do SDK para começar a usar os cartões de banner:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.6.0 %}

## Criação de um posicionamento

### Etapa 1: Criar um novo posicionamento

Acesse **Settings** > **Banner Cards Placements** e selecione **Create Placement**).

![Seção de posicionamentos de cartão de banner para criar IDs de posicionamento.]({% image_buster /assets/img/banner_cards/create_placement.png %})

### Etapa 2: Preencha os detalhes

Dê um nome à sua colocação e atribua a ela uma **ID de posicionamento**. Opcionalmente, você pode adicionar uma descrição para sua colocação.

Trabalhe com sua equipe de marketing para criar essa ID. Essa é a ID que será referenciada no código do seu aplicativo, e sua equipe de marketing usará a ID para atribuir uma campanha ao local no seu app. 

{% alert important %}
Evite editar seu ID de posicionamento após o lançamento, pois isso pode interromper a integração com seu app ou site.
{% endalert %}

![Os detalhes de posicionamento que designam um cartão de banner serão exibidos na barra lateral esquerda para campanhas de promoção de vendas na primavera.]({% image_buster /assets/img/banner_cards/placement_details_example.png %})

Para obter etapas sobre como lançar uma campanha de cartão de banner, consulte [Criação de um cartão de banner]({{site.baseurl}}/create_banner_card/).

## Próximos passos

Agora que você criou os posicionamentos de seu cartão de banner, você pode:

- [Integrar cartões de banner]({{site.baseurl}}/developer_guide/banner_cards/integration/)
- [Criar cartões de banner]({{site.baseurl}}/create_banner_card/)
