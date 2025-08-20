---
nav_title: loplat
article_title: loplat
description: "Este artigo de referência descreve a parceria entre o Braze e a loplat, uma plataforma de marketing off-line baseada em local, para permitir que você execute campanhas de marketing de proximidade adicionando contexto de local."
alias: /partners/loplat/
page_type: partner
search_tag: Partner

---

# loplat

> [A Loplat](https://www.loplat.com/) é a principal plataforma off-line baseada em locais. Use o SDK da loplat para aumentar o número de visitantes de sua loja de forma inteligente e executar campanhas de marketing que incentivem as compras na loja. Você pode medir a performance da loja por meio da análise de tráfego após o término da campanha.

_Esta integração é mantida pela Loplat._

## Sobre a integração

A integração do Braze com a loplat permite que você use os serviços de local da loplat (POI da loja e geofence personalizado) para disparar campanhas de marketing de contexto geográfico e criar eventos personalizados usando segmentação off-line. Quando os usuários visitam o local direcionado que você definiu no loplat X, as informações da campanha e do local são enviadas imediatamente para o Braze.

## Pré-requisitos

| Requisito | Descrição |
| --- | --- |
| conta loplat X | É necessário ter uma conta do loplat X para aproveitar essa integração.<br><br>Envie um e-mail para [support@loplat.com](mailto:support@loplat.com) para solicitar uma conta do loplat X. |
| SDK da loplat | O SDK da loplat reconhece as visitas dos usuários à loja, processa eventos de local e distingue se os usuários estão hospedados em um local ou se estão se mudando. Você pode usar o SDK do loplat para analisar o número de pessoas que passam pela sua loja, enviar mensagens push quando os usuários entram na loja etc.<br><br>Observe que o SDK está disponível apenas para Android e iOS. |
| Chave da API REST do Braze | Uma chave da API REST do Braze com as seguintes permissões:<br>- `users.track`<br>- `campaigns.trigger.send`<br>- `campaigns.list`<br>- `canvas.trigger.send`<br>- `canvas.list`<br><br>Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso

As informações do local do evento personalizado fornecidas pela loplat podem ser usadas em suas campanhas para alcançar casos de uso como:

- [Alerta de promoção de duty-free](https://www.loplat.com/loplat-x#usecase)
    - Envie cupons de desconto de lojas duty-free para os usuários que estiverem próximos aos portões de embarque no aeroporto.
- Push de local de estações de carregamento de veículos elétricos (EV)
    - Defina geofences em torno das estações de carregamento de EV e notifique os usuários quando eles estiverem perto da estação e incentive-os a carregar.

## Integração

### Etapa 1: Integrar os SDKs

Integre o SDK da loplat e o SDK da Braze ao seu app usando as etapas fornecidas na documentação da [integração loplat-Braze](https://developers.loplat.com/braze/).

### Etapa 2: Sincronizar os dashboards do Braze e do loplat X e criar uma campanha

Crie uma nova chave de API no dashboard do Braze. Copie a chave de API e cole-a em **Settings > API Settings** (Configurações > Configurações de API) no dashboard da loplat X. Consulte o [Guia do usuário da loplat X](https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e?pvs=25) para obter mais detalhes.

#### Entrega disparada por API

1. Crie uma campanha no Braze ou uma tela que envie com **API-Triggered Delivery** e copie o ID da campanha.
2. Lance a campanha no Braze depois de concluir todas as etapas.
3. Acesse o loplat X e crie uma campanha seguindo as instruções do [guia do usuário do loplat X](https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e#2ed232c885014f19b1870b9fca4230fb).
4. Cole o ID da campanha do Braze nas **Configurações de mensagens da campanha** e inicie a campanha.

![]({% image_buster /assets/img/loplat/loplat_api_triggered_delivery.png %})

#### Entrega baseada em ação

Com a integração, você pode aplicar condições de local enviando informações de geofence, região, nome da marca ou nome da loja. Além disso, você pode adicionar segmentos ou atribuir conversão com o evento personalizado que criou.
1. Crie uma campanha da loplat X seguindo as instruções do [Guia de usuário da loplat X](https://loplatx-user-guide.notion.site/Campaign-integration-b92f8120cbe74d19a3a5f593657b4e8e#f898aa55ef74440aba76dd9a0e3e7598).
2. Adicione um evento personalizado em **Campaign Message Settings (Configurações de mensagens da campanha** ) e inicie a campanha.
3. Acesse o dashboard do Braze e crie uma campanha ou um Canvas que envie com a **entrega baseada em ação**.
4. Selecione o evento personalizado que você criou no loplat X para definir uma ação-gatilho de local.

![]({% image_buster /assets/img/loplat/loplat_action_based_delivery.png %})


