---
nav_title: Foursquare
article_title: Foursquare
alias: /partners/foursquare/
description: "Este artigo de referência descreve a parceria entre o Braze e o Foursquare, uma plataforma de dados de localização, fornecendo disparo de eventos em tempo real com base no local."
page_type: partner
search_tag: Partner

---

# Foursquare

{% multi_lang_include video.html id="G2ZoJqZGqrU" align="right" %}

> [O Foursquare](https://foursquare.com/) é uma plataforma de dados de localização que fornece direcionamento de dados de localização em suas campanhas no Braze. Use o Pilgrim SDK do Foursquare nos apps iOS e Android para fornecer disparos de eventos em tempo real com base no local, permitindo que você aproveite os poderosos recursos de direcionamento geográfico do Foursquare para enviar mensagens relevantes e personalizadas com o Braze.



## Pré-requisitos

| Requisito | Descrição |
|---|---|
| Conta do Foursquare | É necessário ter uma conta no Foursquare para aproveitar essa parceria. |
| Chave da API REST do Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Espaço de trabalho do Braze e IDs de aplicativos | O espaço de trabalho do Braze e os IDs do app podem ser encontrados no [console do desenvolvedor]({{site.baseurl}}/api/api_key/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integração

Para integrar as duas plataformas, é necessário integrar os dois SDKs e mapear os campos de usuário correspondentes. Após a integração do SDK da Pilgrim, você receberá eventos de local no dispositivo ou em um webhook. 

### Etapa 1: Mapear campos de ID de usuário

Para mapear corretamente os campos entre os dois SDKs, defina o mesmo ID de usuário em ambos os sistemas usando o [método`changeUser`]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#setting-user-ids) no SDK da Braze e o método `setUserId` de [`PilgrimUserInfo`](https://developer.foursquare.com/docs/pilgrim-sdk/advanced-setup-guide#custom-user-data) no SDK da Pilgrim.

### Etapa 2: Configurar o console do Pilgrim


Encontre os IDs do espaço de trabalho e do app no console de desenvolvedor do Braze. Em seguida, insira sua chave da API REST da Braze e os IDs do app no Foursquare Pilgrim Console.

Depois de configurar o Pilgrim Console, o SDK do Pilgrim registrará os eventos locais e os encaminhará para a Braze, permitindo que você redirecione e segmente clientes qualificados. Consulte [o site do desenvolvedor do Foursquare](https://developer.foursquare.com/) para obter mais detalhes.

{% alert important %}
O SDK do Pilgrim requer que você ative os serviços locais.
{% endalert %}

## Envio de mensagens

Depois que a integração estiver configurada, você poderá configurar uma campanha ou uma tela que atuará a partir de eventos locais gerados pelo SDK da Pilgrim. Essa rota de integração é ideal para envio de mensagens em tempo real logo após os usuários entrarem em um local de interesse ou para comunicação de acompanhamento com postergação após a saída, como uma nota de agradecimento ou um lembrete.

Para enviar uma campanha de mensagens com base em um local definido:
- Crie uma campanha ou canva na Braze que envie com a **entrega baseada em ação**
- Para seu disparo, use um evento personalizado de `arrival` com um filtro de propriedade de evento para `locationType`, conforme mostrado na captura de tela a seguir.

![Uma campanha baseada em ação na etapa de entrega mostrando "chegada" selecionada como a opção "executar evento personalizado", em que "locationType" é igual a "casa".]({% image_buster /assets/img_archive/action-based-campaign.png %})

## Redirecionamento

Para redirecionar seus usuários, use o SDK do Pilgrim para definir um atributo personalizado `last_location` nos perfis de usuário dos usuários da Braze. Em seguida, é possível usar a comparação `matches regex` para redirecionar os usuários que foram a um determinado local no mundo real, por exemplo, segmentando todos os usuários que estiveram recentemente em uma pizzaria.

![Uma campanha baseada em ações na etapa de usuários direcionados mostrando "last_location" igual a "Pizza Place".]({% image_buster /assets/img_archive/last-location-segment.png %})

Também é possível segmentar os usuários no Braze que visitaram um determinado tipo de local com base no site `primaryCategoryId` do Foursquare em um determinado período de tempo. Para aproveitar esse ponto de dados para seus casos de uso de redirecionamento, registre `primaryCategoryId` como uma propriedade de evento durante o processo de segmentação do público. Para identificar os usuários e as propriedades usadas pela API do Foursquare e pelo Pilgrim SDK, consulte [o site do desenvolvedor do Foursquare](https://developer.foursquare.com/).


