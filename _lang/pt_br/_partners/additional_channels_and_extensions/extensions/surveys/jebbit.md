---
nav_title: Jebbit
article_title: Jebbit
description: "Este artigo de referência descreve a parceria entre o Braze e o Jebbit, uma PaaS que permite passar e-mails e atribuições de usuários de suas campanhas do Jebbit como dados de usuários para o Braze em tempo real."
alias: /partners/jebbit/
page_type: partner
search_tag: Partner

---

# Jebbit

> A [Jebbit](https://www.jebbit.com/) é uma PaaS que permite criar experiências de engajamento para que os usuários capturem dados primários.

_Essa integração é mantida pelo Jebbit._

## Sobre a integração

A integração entre a Braze e a Jebbit permite passar e-mails e atribuições de usuários das suas campanhas da Jebbit como dados de usuários para a Braze em tempo real. Esses dados podem então ser usados para impulsionar iniciativas de marketing, como campanhas de e-mail personalizadas e disparos. 

## Pré-requisitos

| Requisito | Descrição |
|---|---|
|Conta da Jebbit | É necessário ter uma conta da Jebbit para usar a parceria. |
| Chave da API REST do Braze | Uma chave da API REST da Braze com todas as permissões de dados de usuários. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
|Ponto de extremidade REST do Braze | Sua URL de endpoint REST. Seu endpoint dependerá do [URL da Braze para [sua instância]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

Ao solicitar a integração com a Jebbit, avise-nos caso seja necessário cumprir algum prazo rígido. Além disso, confirme se você tem os atributos mapeados nas experiências da Jebbit que gostaria de passar para a Braze.

### Etapa 1: Fornecer credenciais da API

Forneça suas credenciais de API ao Jebbit em um arquivo de texto por meio de uma solicitação de arquivo do Dropbox.
Envie seu arquivo usando o seguinte [URL do Dropbox](https://www.dropbox.com/request/RqKQHkJHXw1cFBKbXpZx).

### Etapa 2: confirme o envio do teste

Um engenheiro da Jebbit atribuído à sua integração fará o push de um envio de teste da Jebbit para a Braze, dando a você a oportunidade de ver como os dados ficarão no ambiente da Braze. Essa é a etapa final da ativação da integração. Agora que seus dados da Jebbit estão configurados, use-os para conduzir suas iniciativas de marketing.

{% alert note %}
A ID de atribuição que você definiu no Jebbit é como o nome do campo de atribuição será mostrado no Braze.
{% endalert %}

## Personalização

Atualmente, damos suporte especificamente aos pontos de extremidade [de dados de usuários]({{site.baseurl}}/api/endpoints/user_data/), mas é possível dar suporte a solicitações de diferentes pontos de extremidade.

Os nomes dos campos de atributos também podem ser personalizados de acordo com sua preferência.

Se quiser adicionar outros atributos da Jebbit à Braze, mapeie o novo atributo na sua conta da Jebbit. A atribuição será exibida automaticamente no Braze à medida que você coletar dados para esse atributo.

