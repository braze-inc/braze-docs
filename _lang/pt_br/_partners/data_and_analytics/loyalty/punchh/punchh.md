---
nav_title: Punchh
article_title: Punchh
page_order: 1
description: "Este artigo de referência descreve a parceria entre a Braze e a Punchh, uma plataforma de fidelidade e engajamento. Com ela, você pode sincronizar dados entre as duas plataformas. Os dados publicados no Braze estarão disponíveis para segmentação e poderão sincronizar os dados de usuários de volta à Punchh por meio de modelos de webhook configurados no Braze."
page_type: partner
search_tag: Partner

---

# Punchh

> [A Punchh](https://punchh.com/) é uma plataforma de fidelidade e engajamento líder do setor que ativa as marcas para oferecer programas de fidelidade do cliente omnicanal, tanto na loja quanto digitalmente. 

_Essa integração é mantida pela Punchh._

## Sobre a integração

A integração do Braze e da Punchh permite que você sincronize dados para fins de presente e fidelidade nas duas plataformas. Os dados publicados no Braze estarão disponíveis para segmentação e poderão sincronizar os dados de usuários de volta à Punchh por meio de webhooks do Braze.

## Quais são os benefícios?

- Ingerir dados de fidelidade da Punchh para o Braze em tempo real. 
- Use e estratifique os poderosos dados de público da Braze para oferecer experiências significativas e dinâmicas em vários canais (app, celular, web, e-mail e SMS).
  - Os clientes abriram os e-mails? Os clientes abriram o app perto de uma loja?
- Padronize a aparência dos e-mails de transação enviados pelo Braze.
- Crie jornadas que permitam testes A/B e otimização à medida que você avança.

## Pré-requisitos

| Requisito | Descrição |
|---|---|
| Conta Punchh | Você precisa ter uma conta ativa no Punchh para aproveitar essa parceria. |
| chave da API REST Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST do Braze | [Sua URL de endpoint REST.]({{site.baseurl}}/api/basics/#endpoints) Seu endpoint depende do URL do Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## O que mais devo saber?

#### Antes de integrar

- Ao utilizar a integração do Braze, serão necessárias duas campanhas, uma no Punchh e a segunda no Braze. Por exemplo, se você enviar uma campanha com uma oferta anexada, a campanha de presentes será configurada no Punchh, e a notificação poderá ser enviada pelo Braze.
- Os convidados já devem existir em Punchh e Braze. A Punchh filtrará qualquer cliente que ainda não seja um cliente de fidelidade.

#### Pontos importantes a serem notados

- A Punchh adicionou a capacidade de desativar o envio de atributos padrão de usuários para o Braze, para que o cliente não incorra em excedentes de pontos de dados. Isso é configurado durante a configuração do adaptador.
- Se estiver usando segmentos personalizados em campanhas recorrentes, o nome da campanha deve ser usado em vez do ID da campanha, pois os IDs mudam a cada vez que a campanha é executada.
- Os canais de comunicação disponíveis em cada campanha de envio de mensagens da Punchh incluem mensagens ricas, notificações por push, SMS e envio de e-mail.
- Depois que os usuários forem enviados para um segmento personalizado da Punchh do Braze, eles não poderão ser removidos. Somente novos hóspedes podem ser adicionados a um segmento personalizado existente. Se os hóspedes precisarem ser removidos de um segmento personalizado da Punchh existente, será necessário criar uma nova campanha de webhook no Braze para enviar os usuários a um novo segmento personalizado da Punchh.

## Integração

A Punchh oferece vários pontos de extremidade disponíveis aos clientes do Braze para ajudar a adicionar IDs externos à plataforma Punchh usando os seguintes pontos de extremidade da API da Punchh. Depois que as IDs externas forem adicionadas, crie um adaptador no Punchh, forneça suas credenciais do Braze e selecione os eventos que deseja sincronizar. Em seguida, você pode pegar o ID do segmento do Punchh e usá-lo para criar um webhook do Punchh para disparar a sincronização do cliente em uma jornada do Canva.

Observe que o Punchh `user_id` e o Braze `external_id` precisam estar disponíveis em uma das plataformas para que a integração seja sincronizada corretamente. 
- Os eventos enviados da Punchh para o Braze incluirão o Braze `external_id` como identificador. Se a Punchh estiver configurada para usar o `external_source_id`, esse valor será definido como o Braze `external_id`. Caso contrário, a integração terá como padrão a configuração do Punchh `user_id` como Braze `external_id`.
- Para enviar webhooks do Braze para o Punchh, o Punchh `user_id` deve estar disponível no perfil do usuário do Braze. Se a Punchh `user_id` não for usada como Braze `external_id`, ela deverá ser definida como um atributo personalizado "punchh_user_id". 

### Etapa 1: Configurar endpoints externos de ingestão de ID (opcional)

As IDs externas do Braze podem ser adicionadas usando os seguintes endpoints para usuários novos e existentes do Punchh.

{% alert important %}
Os valores dos campos `external_source` e `external_source_id` devem ser exclusivos da Punchh e não devem estar associados a perfis existentes.
{% endalert %}

1. Novos usuários do Punchh<br>
Crie novos usuários no Punchh com um ponto de extremidade de fazer login no Punchh usando os campos `external_source` e `external_source_id`. A Punchh permite que identificadores externos sejam enviados com um perfil de usuário por meio de um dos seguintes pontos de extremidade de inscrição:
- [API de inscrição móvel](https://developers.punchh.com/docs/dev-portal-mobile/2e67abf6f8e12-sign-up-register)
- [API de inscrição por SSO](https://developers.punchh.com/docs/dev-portal-online-ordering/58f18dfdd2a3d-signup-with-email-and-password)<br><br>
2. Usuários existentes da Punchh <br>
Atualize o `external_source_id` para os usuários existentes da Punchh. O Punchh permite que identificadores externos sejam adicionados a um perfil por meio de um ponto de extremidade de atualização da API do usuário: 
- [Atualização do usuário móvel](https://developers.punchh.com/docs/dev-portal-mobile/c9b928e35a6f3-update-user-profile)
- [Atualização do usuário SSO](https://developers.punchh.com/docs/dev-portal-online-ordering/eef4eef6c97a0-update-user-information)
- [Atualização do usuário do dashboard](https://developers.punchh.com/docs/dev-portal-platform-functions/6351feaf591aa-update-a-user)
<br><br>
{% tabs local %}
{% tab Exemplo de API de inscrição de usuário %}
Este exemplo permite enviar identificadores externos com um perfil de usuário no momento em que se faz o login. Isso é feito enviando `external_source` como "customer_id" e `external_source_id` como "111111111111111111" como um tipo de dados string.

```json
curl --location --request POST 'https://server_name_goes_here.punchh.com/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'x-pch-digest: SIGNATURE' \
--header 'Accept-Timezone: Etc/UTC' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--data-raw '{
    "client":"CLIENT",
    "user" : {
      "email": "test@example.com",
      "password": "PASSWORD",
      "first_name":"FIRST_NAME",
      "last_name":"LAST_NAME",
      "terms_and_conditions":"true",
      "anniversary":"2014-02-02",
      "zip_code":"94497",
      "birthday":"2004-02-02",
      "external_source":"customer_id",
      "external_source_id":"111111111111111111"
      }
}'
```
{% endtab %}
{% tab Exemplo de API de atualização de usuário %}
Este exemplo permite que você atualize identificadores externos com um perfil de usuário. Isso é feito enviando `external_source` como "customer_id" e `external_source_id` como "111111111111111111" como um tipo de dados string.

```json
curl --location --request PUT 'https://server_name_goes_here.punchh.com/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--header 'x-pch-digest: SIGNATURE' \
--header 'Authorization: Bearer ACCESS_TOKEN' \
--data-raw '{
    "client":"CLIENT",
    "user": {
        "external_source":"customer_id",
        "external_source_id":"111111111111111111"
    }
}'
```
{% endtab %}
{% endtabs %}

{% alert note %}
**Configuração da plataforma:** Para ativar os identificadores externos no Punchh, no painel do Punchh, navegue até **Cockpit** > **Dashboard** > **External User Identifier (Identificador de usuário externo**).
{% endalert %}

### Etapa 2: Configuração do adaptador de Braze em Punchh

#### Eventos disponíveis para sincronização {#available-events-to-sync}

1. **Convidado:** Disparado em qualquer inscrição, atualização do perfil do convidado, desativação ou exclusão
2. **Check-in de fidelidade:** Disparado para transações de fidelidade ou ganhos por meio da leitura do código de barras do recibo
3. **Check-in de presentes:** Disparado para pontos concedidos em uma campanha
4. **Redenção:** Disparado no caso de qualquer resgate de recompensas, excluindo os cupons Punchh, pois eles seriam enviados separadamente como eventos de cupom, incluindo a emissão e o resgate
5. **Recompensas:** Disparado a partir de recompensas oferecidas por campanhas, atividades, conversão de pontos em recompensas ou ofertas de administradores
6. **Notificações de transação:** Disparado após a atividade transacional de um usuário no sistema Punchh (por exemplo, expiração de pontos)
7. **Notificações de marketing:** Disparado com base em diferentes configurações de campanha no Punchh para um segmento associado de usuários

{% alert note %}
Consulte a documentação da Punchh para saber como podem ser as cargas úteis desses eventos disponíveis.
{% endalert %}

Trabalhe com seu gerente de implementação da Punchh para configurar esse adaptador.

Para configurar a integração do Braze e do Punchh, faça o seguinte:

1. No painel do Punchh, navegue até **Cockpit** > **Dashboard** > **Principais recursos** > **Ativar gerenciamento de webhook** e ative a opção **Ativar gerenciamento de webhook**.<br><br>
2. Em seguida, ative os adaptadores navegando até **Configurações** > **Gerenciador de webhooks** > **Configurações** > **guia Mostrar adaptadores** e ative **a guia Mostrar adaptadores**.<br><br>
3. Navegue até o **Webhooks Manager** na guia **Settings (Configurações)**, selecione a guia **Adapters (Adaptadores** ) e clique em **Create Adapter (Criar adaptador**). <br><br>![]({% image_buster /assets/img/punchh/punchh1.png %})<br><br>
4. Preencha o nome do adaptador, a descrição e o e-mail do administrador. Selecione **Braze** como seu adaptador e forneça seu ponto de extremidade da API REST do Braze e a chave de API do Braze.<br><br>
5. Em seguida, selecione os eventos disponíveis que gostaria de ativar. Uma lista desses eventos pode ser encontrada em [Eventos disponíveis para sincronização](#available-events-to-sync).<br><br>![]({% image_buster /assets/img/punchh/punchh3.png %})<br><br>
6. Clique em **Submit** para ativar o webhook.

## Criar o webhook Punchh no Braze

O Braze pode adicionar usuários a um segmento da Punchh por meio de webhooks que utilizam os segmentos personalizados da Punchh.

1. Crie um segmento personalizado na Punchh e note o endereço `custom_segment_id` presente no URL do dashboard do segmento da Punchh, conforme mostrado abaixo. Podem ser usados os criadores de segmentos clássicos ou beta. No entanto, a versão beta é recomendada, pois a versão clássica acabará sendo descontinuada.<br><br>Na plataforma Punchh, navegue até **Convidado** > **Segmento** > **Lista personalizada** > **Nova lista personalizada**.<br><br>![]({% image_buster /assets/img/punchh/update1.png %})<br><br>

2. Crie uma campanha de webhook no Braze usando o endpoint Punchh para adicionar um usuário a um segmento personalizado como o URL do webhook. Aqui você pode fornecer o `custom_segment_id` extraído do URL e o `user_id` como pares de valores-chave.<br><br>![]({% image_buster /assets/img/punchh/punchh4.png %})<br><br>

3. Esse webhook pode ser configurado como uma campanha singular ou como uma etapa de um Canva. Como alternativa, se o webhook que adiciona usuários a esse segmento específico do Punchh for usado em várias campanhas ou Canvas, ele poderá ser configurado como um [modelo]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template#creating-a-webhook-template).<br><br>
A chave `user_id` no webhook mapeia o ID de usuário da Punchh. Esse identificador precisará ser adicionado a todos os webhooks criados no Braze para adicionar usuários a um segmento personalizado da Punchh. O atributo personalizado `punch_user_id` pode ser preenchido dinamicamente como o valor da chave `user_id` usando o [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#pre-formatted-variables). Você pode inserir a variável de atributo personalizado `punchh_user_id` usando o ícone azul de "mais", localizado no canto superior direito de qualquer campo de texto de modelo.<br><br>![]({% image_buster /assets/img/punchh/update3.png %}){: style="max-width:65%;"}<br><br>![]({% image_buster /assets/img/punchh/update4.png %}){: style="max-width:65%;"}<br><br>

4. Depois que o webhook é salvo, ele pode ser usado para sincronizar usuários, conforme mostrado abaixo. Por exemplo, 136 hóspedes seriam adicionados ao segmento personalizado Punch quando essa campanha do webhook Braze fosse lançada.<br><br>![Um exemplo de sincronização de usuários usando o webhook salvo devido à integração do Braze e do Punchh.]({% image_buster /assets/img/punchh/punchh6.png %})

Para saber mais sobre como os webhooks são usados no Braze, consulte [Criando um webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/). 

## Campanhas de casos de uso

### Configuração da campanha e do Canva

#### Como gerenciar os gatilhos

Os casos de uso para envio de mensagens do Braze acionados por eventos da Punchh enviados ao Braze, como eventos de recompensas ou eventos de convidados, podem ser criados como [campanhas baseadas em ações]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery#action-based-delivery) ou Canvas disparados pelo evento relevante da Punchh.

A adição de um gatilho abre a lista de eventos criados no Braze. Escolha o evento que deve disparar a campanha ou o Canva a ser enviado ao usuário que registrou o evento.

![]({% image_buster /assets/img/punchh/update5.png %})

Filtros de propriedade podem ser adicionados para filtrar ainda mais o evento-gatilho. Por exemplo, a mensagem só deve ser disparada quando um cliente disparar o evento "checkins_gift" em que a propriedade do evento aprovada é `true`. Esse é um recurso opcional que pode não ser aplicável a todos os casos de uso. 

#### Segmentação

Em muitos casos, as campanhas do Braze e as Canvas que são disparadas por eventos da Punchh podem ser definidas para um público "Todos os usuários", pois a segmentação dos usuários que disparam esses eventos será determinada na Punchh. No entanto, os clientes que desejam refinar ainda mais o público de usuários que receberão o envio de mensagens do Braze disparado pelo evento podem fazê-lo adicionando filtros e segmentos adicionais na seção **Públicos-alvo** do criador da campanha ou no **Público de entrada** do criador do Canvas. 

### Casos de uso

{% tabs local %}
{% tab Inscrição %}
#### Campanha de inscrição

Ao utilizar a configuração do Braze para uma campanha de inscrição com uma oferta anexada, será necessário configurar uma campanha de presentes de inscrição no Punchh e uma mensagem de boas-vindas no Braze. 

A Punchh recomenda que uma postergação de execução seja adicionada à campanha de mensagens, para que o Braze possa disparar primeiro a mensagem de boas-vindas com base no evento do convidado. Se quiser enviar uma mensagem de acompanhamento informando ao usuário que ele foi presenteado, poderá disparar essa mensagem com base no evento de recompensas.

No caso de uma campanha de inscrição, todas as pessoas que se inscreveram podem ser usadas para o segmento; portanto, não será necessário um segmento personalizado do Braze.

Configurações da Punchh necessárias:
- Campanha: inscrição 
- Segmento: Todos inscreveram-se
- Recompensa: Escolha do cliente
Eventos necessários:
- Evento de recompensa
- Evento para convidados
Considerações:
- Atraso na execução, recomendamos que o hóspede adicione uma postergação de 5 a 10 minutos

![Um segmento de usuário é configurado na Punchh, e os clientes se inscrevem em um programa de fidelidade. Depois disso, o evento do convidado, se disparado, e a campanha de mensagens do Braze é disparada. Em seguida, a campanha de presentes de inscrição do Punchh é acionada após 10 minutos, disparando o evento de recompensas e a mensagem opcional de acompanhamento.]({% image_buster /assets/img/punchh/usecase3.png %})
{% endtab %}

{% tab Braze bem-vindo %}
#### Campanha de boas-vindas do Braze

Quando um novo usuário inscreve-se, a Punchh envia ao Braze um evento Guest que cria o usuário e envia um atributo personalizado `signup_channel`, que pode ser usado para disparar a campanha de boas-vindas do Braze.

Para configurar a campanha de boas-vindas do Braze, siga estas etapas:

1. No Braze, crie uma campanha baseada em ações.
2. Para o disparo, selecione **Alterar valor de atributo personalizado** com o atributo personalizado `signup_channel` definido como **Qualquer valor novo**.
3. Continue criando sua campanha e envie-a quando estiver pronta!

{% endtab %}
{% tab Oferta em massa %}
#### Campanha de oferta em massa

Ao utilizar uma campanha de oferta em massa para presentear, uma campanha de oferta em massa precisará ser configurada no Punchh e uma campanha de mensagens no Braze.

Se você quiser utilizar um segmento do Braze para sua campanha ou enviar uma comunicação do Braze antes de presentear os convidados na plataforma Punchh, será necessário um [segmento personalizado do Punchh]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#step-3-create-punchh-webhook-in-braze) para a campanha de presentes do Punchh. 

A criação do segmento de usuários para receber essa oferta no Braze só é recomendada quando se usam atribuições indisponíveis no Punchh. Caso contrário, a segmentação da Punchh poderá ser usada, e a campanha de mensagens do Braze será criada como uma campanha baseada em ação, disparada pelos usuários que receberem suas recompensas (o evento de recompensa disparado pela Punchh).

Configurações da Punchh necessárias:
- Campanha: Oferta em massa
- Segmento: Lista personalizada ou escolha do cliente
- Recompensa: Escolha do cliente

**Usando o Punchh para segmentação e oferta de presentes e o Braze para envio de mensagens:**<br>
Por exemplo, uma recompensa de US$ 2 de desconto é enviada a um segmento configurável no Punchh com envio de mensagens pelo Braze.<br>
![Um segmento de usuário pode ser configurado na Punchh, e os usuários recebem um presente por meio de uma campanha de oferta em massa da Punchh. Em seguida, um evento de recompensa é disparado, e a campanha de mensagens da Braze é disparada.]({% image_buster /assets/img/punchh/usecase6.png %}){: style="max-width:80%;"}

**Usando a segmentação e o envio de mensagens do Braze e o Punchh para presentear:**<br>
Por exemplo, uma recompensa de US$ 2 de desconto e o envio de mensagens para um segmento com atribuições não disponíveis no Punchh.<br>
![Um segmento de usuário pode ser configurado na Braze e, em seguida, uma mensagem pode ser enviada de um segmento Braze para Braze. Em seguida, os usuários são enviados para o segmento personalizado da Punchh por meio de um webhook do Braze com o segmento e o ID do usuário. Depois disso, o usuário recebe um presente por meio da campanha de oferta em massa da Punchh com um segmento personalizado. Depois disso, o evento-gatilho é disparado.]({% image_buster /assets/img/punchh/usecase5.png %}){: style="max-width:80%;"}

**Usar a segmentação Braze e o Punchh para presentes ou envio de mensagens, ou ambos:**<br>
Por exemplo, uma recompensa de $2 de desconto é enviada a um segmento com atribuições não disponíveis no Punchh, mas não é necessário o envio de mensagens, ou as mensagens podem ser enviadas por meio do Punchh (note que todos os convidados devem estar presentes no Punchh).<br>
![Um segmento de usuário pode ser configurado no Braze, e os usuários são enviados ao segmento personalizado da Punchh por meio de um webhook do Braze com o segmento e o ID do usuário. Depois disso, o usuário recebe um presente por meio da campanha de oferta em massa da Punchh com um segmento personalizado. Depois disso, o evento-gatilho é disparado.]({% image_buster /assets/img/punchh/usecase4.png %})

{% endtab %}
{% tab Oferta recorrente em massa %}
#### Campanha de oferta em massa recorrente

Ao utilizar uma campanha de oferta em massa recorrente para presentear, será necessário configurar uma campanha de oferta em massa no Punchh e uma campanha de mensagens no Braze. Um segmento personalizado da Punchh será necessário se o cliente quiser usar a segmentação do Braze (recomendado somente se estiver utilizando atributos indisponíveis na Punchh). Caso contrário, a segmentação Punchh pode ser usada, e a campanha de mensagens do Braze será disparada com base no evento de recompensas.

Configurações da Punchh necessárias:
- Campanha: oferta recorrente em massa
- Segmento: Lista personalizada ou escolha do cliente
- Recompensa: Escolha do cliente
Considerações:
- Os IDs e os nomes das campanhas são enviados à Braze como uma propriedade do evento. Se você quiser usar um identificador de campanha Punchh no Braze para filtrar ainda mais o público que está recebendo a campanha, o nome da campanha deverá ser usado, pois os IDs da campanha serão alterados diariamente.

{% endtab %}
{% tab Oferta de pós check-in com notificação %}
#### Campanha de oferta pós-check-in com notificação

Ao utilizar uma campanha de oferta pós-check-in, o Braze enviará a notificação sobre o presente e, quando o hóspede fizer um check-in, ele será presenteado com a campanha pós-check-in da Punchh. Portanto, uma campanha de oferta pós-check-in precisará ser configurada no Punchh e uma campanha de mensagens no Braze (para notificar os clientes sobre a campanha).

Configurações da Punchh necessárias:
- Campanha: Oferta pós-check-in
- Segmento: Lista personalizada
- Recompensa: Escolha do cliente

Por exemplo, um envio de e-mail notificando os hóspedes a visitarem o local neste fim de semana para ganhar pontos em dobro em um segmento com atribuições não disponíveis no Punchh. A Punchh presenteará esse segmento com pontos após um check-in qualificado e envio opcional de mensagens do Braze. 

![Um segmento de usuário é configurado no Braze, e as mensagens são enviadas do Braze após a campanha de check-in. Em seguida, os usuários qualificados são enviados para o segmento personalizado da Punchh por meio do webhook do Braze com o segmento e o ID do usuário. Por fim, o usuário qualificado no segmento personalizado faz o check-in e recebe o brinde e a mensagem opcional por meio da campanha pós-check-in]({% image_buster /assets/img/punchh/update7.png %})

{% endtab %}
{% tab Oferta de pós check-in sem notificação %}
#### Campanha de oferta pós-check-in sem notificação

Ao utilizar uma campanha de oferta pós-check-in que não notifique previamente os clientes, a campanha oferecerá (envio de mensagens opcional) e disparará qualquer notificação no Braze. Portanto, uma campanha de oferta pós-check-in deve ser configurada no Punchh; no entanto, não é necessário ter uma lista personalizada. Em vez disso, você pode escolher o segmento que deseja no Punchh. 

Configurações da Punchh necessárias:
- Campanha: Oferta pós-check-in
- Segmento: Escolha do cliente
- Recompensa: Escolha do cliente

Por exemplo, uma campanha Braze de surpresa e prazer é enviada a um segmento disponível em Punchh, agradecendo aos clientes pela visita e recompensando-os com US$ 2 de desconto em sua próxima visita.

![Um segmento de usuário qualificado pode ser configurado no Punchh, e um usuário qualificado faz o check-in e recebe um presente por meio de uma campanha pós-check-in do Punchh. Depois disso, um evento de recompensa é disparado, e a mensagem de recall é enviada notificando os convidados sobre a recompensa enviada pela Braze.]({% image_buster /assets/img/punchh/usecase2.png %})

{% endtab %}
{% tab Aniversário %}
#### Campanha de aniversário 

Ao utilizar uma campanha de aniversário, o usuário receberá primeiro o presente de aniversário da campanha Punchh. Esse presente (evento de recompensa) dispara campanha de mensagens na Braze que notifica o usuário sobre o presente. Portanto, não é necessária uma lista personalizada. Em vez disso, você pode escolher o segmento e a configuração de aniversário no Punchh.

Configurações da Punchh necessárias:
- Campanha: Campanha de aniversário
- Segmento: Escolha do cliente
- Recompensa: Escolha do cliente
Considerações:
- Presentear no mês de inscrição
- Duração da vida útil (por quanto tempo a recompensa de aniversário é válida?)
- Campanhas recorrentes, programação necessária 

![Um segmento opcional pode ser criado na Punchh, e um usuário qualificado recebe recompensas por meio de uma campanha de aniversário da Punchh. Depois disso, um evento de recompensa é disparado, e a mensagem de recall é enviada notificando os convidados sobre a recompensa enviada pela Braze.]({% image_buster /assets/img/punchh/usecase1.png %})

{% endtab %}
{% tab Recall %}
#### Campanha de recall

Ao direcionar os usuários com base na inatividade, uma campanha de recall pode ser usada. O cliente pode criar o segmento e a campanha no Punchh, mas utilizar o Braze para o envio de mensagens.

Se você quiser usar a segmentação criada no Braze, um [segmento Punchh personalizado]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#step-3-create-punchh-webhook-in-braze) baseado em inatividade poderá ser anexado a uma campanha de oferta em massa recorrente.

Configurações da Punchh necessárias:
- Campanha: Campanha de recall
- Segmento: Escolha do cliente
- Recompensa: Escolha do cliente
Considerações:
- A campanha é executada em um cronograma

![Um segmento opcional pode ser criado na Punchh, e um usuário qualificado recebe recompensas por meio de uma campanha de recall da Punchh. Depois disso, um evento de recompensa é disparado, e a mensagem de recall é enviada notificando os convidados sobre a recompensa enviada pela Braze.]({% image_buster /assets/img/punchh/usecase.png %})

{% endtab %}
{% endtabs %}


