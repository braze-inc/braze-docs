---
nav_title: Komo
article_title: Komo
description: "Este artigo de referência descreve a parceria entre o Braze e a Komo, uma plataforma de engajamento com clientes especializada em gamificação, conteúdo interativo, competições, prêmios e fidelidade. Por meio dessa integração, os dados primários e de terceiros capturados na Komo podem ser publicados na Braze."
alias: /partners/komo/
page_type: partner
search_tag: Partner

---

# Komo

> [A Komo](https://komo.tech/) é uma plataforma de engajamento com clientes especializada em gamificação, conteúdo interativo, competições, prêmios e fidelidade.

_Essa integração é mantida pela Komo._

## Sobre a integração

A integração entre a Braze e a Komo permite coletar dados primários e de terceiros por meio dos hubs de engajamento da Komo. Esses hubs são microsites dinâmicos que oferecem conteúdo interativo e recursos de gamificação. Os dados de usuários coletados desses hubs são então transmitidos para a API do Braze.

- Ingestão em tempo real na Braze de dados primários e de dados voluntários de usuários coletados da Komo
- Ingerir dados de pesquisas de marketing e de preferências dos usuários quando eles respondem a pesquisas, enquetes e perguntas de questionários
- Crie progressivamente perfis de usuário no Braze ao longo do tempo, à medida que o usuário continua a se engajar e a compartilhar mais dados sobre si mesmo
- Padronize a aparência dos e-mails de transação enviados pelo Braze

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Komo | Você precisará de uma conta Komo ativa para aproveitar essa parceria. Visite o [Komo](https://komo.tech/) para iniciar um teste agora. |
| Chave da API REST do Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST do Braze | [Sua URL de endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Seu endpoint dependerá do URL do Braze para sua instância.<br><br>Por exemplo, deve ficar parecido com: https://rest.iad-03.braze.com |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Casos de uso

{% tabs local %}
{% tab Captura de dados - Envio de formulários %}

Quando um usuário enviar um formulário de captura de dados personalizável no Komo, os campos do Komo mapeados na integração do Braze serão passados para o Braze por meio da chamada da API `/users/track/`.

Existem formulários de captura de dados no início ou no final dos cartões.

{% endtab %}
{% tab Pesquisa de mercado - em breve %}

Em breve, a Komo adicionará a capacidade de transmitir dados de pesquisa de marketing capturados quando um usuário responder a uma pergunta de questionário, enquete, teste de personalidade, swiper etc. Esses dados o capacitarão a aprimorar o perfil de um usuário além dos dados capturados nos envios de formulários.

{% endtab %}
{% endtabs %}

## Integração

### Etapa 1: Publicar um hub e um cartão de engajamento do Komo

Você precisará publicar um hub de engajamento da Komo com pelo menos um cartão contendo um formulário de captura de dados. Quando publicado, é possível testar a experiência do usuário de ponta a ponta e verificar se a integração está funcionando corretamente.

![]({% image_buster /assets/img/komo/komo_hub_publish.png %})

### Etapa 2: Adicionar a integração do Braze

No Komo, vá para a guia **Hub Settings (Configurações do hub)** e selecione a seção **Integrations (Integrações** ). Em seguida, localize a integração do Braze na lista e selecione o botão **Connect (Conectar** ) para ativar a integração.

![]({% image_buster /assets/img/komo/komo_hub_settings_integrations.png %})

![]({% image_buster /assets/img/komo/komo_hub_settings_braze_connect.png %})

#### Configurar o mapeamento de usuários

A primeira coisa que você precisará configurar é como mapear os usuários capturados no Komo para os usuários no Braze. Se estiver capturando o `braze_id` ou `external_id` por um campo na Komo, poderá selecionar a chave apropriada; caso contrário, selecione a opção mais comum, que é um alias de usuário de e-mail ou telefone.

![]({% image_buster /assets/img/komo/komo_hub_settings_braze_key.png %}){: style="max-width:65%;"}

Em seguida, você precisará definir um mapa dos campos da Komo que deseja transferir para as atribuições da Braze. O Komo captura uma grande quantidade de dados, portanto, somente os campos mapeados na integração do Braze serão enviados ao Braze.

![]({% image_buster /assets/img/komo/komo_hub_settings_braze_settings.png %}){: style="max-width:65%;"}

Por fim, adicione sua chave de API e o URL do ponto de extremidade REST e clique em **Salvar** para ativar a integração.

## Usando a integração

Depois que a integração for concluída, você poderá usar os dados do Komo enviados ao Braze para criar segmentos para direcionamento.


