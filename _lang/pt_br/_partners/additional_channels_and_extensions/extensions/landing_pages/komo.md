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
{% tab Data Capture - Form Submission %}

Quando um usuário enviar um formulário de captura de dados personalizável no Komo, os campos do Komo mapeados na integração do Braze serão passados para o Braze por meio da chamada da API `/users/track/`.

Existem formulários de captura de dados no início ou no final dos cartões.

{% endtab %}
{% tab Market Research - Coming soon %}

A Komo também ativa a capacitação para transmitir dados de pesquisa de marketing capturados quando um usuário responde a uma pergunta de questionário, enquete, teste de personalidade, swiper e similares. Esses dados o capacitarão a aprimorar o perfil de um usuário além dos dados capturados nos envios de formulários.

{% endtab %}
{% endtabs %}

## Integração

### Etapa 1: Publicar um hub e um cartão de engajamento do Komo

Você precisará publicar um Komo Hub com pelo menos um cartão contendo um formulário de captura de dados. Quando publicado, é possível testar a experiência do usuário de ponta a ponta e verificar se a integração está funcionando corretamente.

![Komo Hub.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step1.png %})

### Etapa 2: Adicionar o app Braze Connected 

No Komo, vá para a guia **Company Settings (Configurações da empresa** ) e selecione a seção **Connected Apps (Aplicativos conectados** ). 

Em seguida, localize a integração do Braze na lista e selecione o botão **Connect (Conectar** ) para ativar a integração.

![Integração com o Braze.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step2a.png %}){: style="max-width:50%;"}

![Conecte a integração do Braze Etapa 2b.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step2b.png %})

#### Configurar a integração por meio de um fluxo de trabalho

Agora você precisa configurar um fluxo de trabalho, em um espaço de trabalho, site ou cartão, para sincronizar os dados com o Braze. 

O escopo do fluxo de trabalho dentro do escopo de todo o espaço de trabalho, de um site (que contém muitos cartões) ou de um único cartão depende do fato de você querer que o fluxo de trabalho seja disparado em muitos cartões ou campanhas. 

Depois de criar um fluxo de trabalho, defina seu disparador, procure o Braze no menu de etapas e adicione a etapa "Track User" (Rastrear usuário). 

![Configuração do usuário de rastreamento.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step3a.png %})

A partir daqui, configure os eventos, as atribuições e as inscrições que você deseja sincronizar do Komo para o Braze. 

![Lista de blocos de conteúdo.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step3b.png %})

## Usando a integração

Agora sua integração está funcionando e você pode monitorar cada execução na guia Execuções do fluxo de trabalho. 
