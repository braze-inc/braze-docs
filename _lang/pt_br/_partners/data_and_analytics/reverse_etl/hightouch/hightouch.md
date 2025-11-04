---
nav_title: Hightouch
article_title: Hightouch
description: "Este artigo de referência descreve a parceria entre a Braze e o Hightouch, uma plataforma para sincronizar os dados de seus clientes de seu data warehouse com ferramentas de negócios."
page_type: partner
search_tag: Partner

---

# Hightouch

> [O Hightouch](https://hightouch.io) é uma plataforma moderna de integração de dados que o capacita a sincronizar dados de clientes, produtos ou proprietários de seu data warehouse ou data lake com qualquer app de sua escolha, tudo sem a assistência das equipes de TI ou de engenharia.

A integração entre a Braze e o Hightouch permite que você crie campanhas melhores na Braze com dados atualizados de clientes de seu data warehouse. Ao sincronizar automaticamente os dados de clientes no Braze, você não precisa mais se preocupar com a consistência dos dados e pode se concentrar na criação de experiências de clientes de classe mundial. 

Essa integração também permite a [importação de coortes de usuários para o Braze]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/hightouch/hightouch_cohort_import/), enviando campanhas direcionadas com base em dados que podem existir apenas em seu data warehouse.

## Pré-requisitos

| Requisito | Descrição |
|---|---|
| Conta Hightouch | É necessário ter uma conta Hightouch para aproveitar essa parceria.
| chave da API REST Braze | Uma chave da API REST da Braze com as permissões `users.track` e `users.export.ids`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Ponto de extremidade REST do Braze  | Sua URL de endpoint REST. Seu endpoint dependerá do [URL do Braze para sua instância]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints).<br><br>O Hightouch requer o nome do cluster em que sua instância do Braze está localizada. Por exemplo, se seu endpoint da Braze for `https://rest.iad-01.braze.com`, você só precisará de `iad-01`.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso

* Sincronize dados de usuários e contas no Braze para criar campanhas hiperpersonalizadas.
* Atualize automaticamente seus segmentos da Braze com dados novos de seu warehouse.
* Ofereça melhores experiências trazendo dados de outros pontos de contato do cliente para o Braze.
* Importe coortes de usuários para a Braze, o que lhe permite enviar campanhas e canvas direcionados. 

## Integração

### Etapa 1: Crie seu destino Hightouch Braze

1. Na plataforma Hightouch, na seção **Destinations** (Destinos), clique em **Add destination** (Adicionar destino).
2. Selecione **Braze** na lista de destinos disponíveis.
3. Forneça seu endpoint REST da Braze (excluindo "https://rest.") e sua chave da API REST da Braze.<br><br>![]({% image_buster /assets/img/hightouch/hightouch_braze_setup.png %})

### Etapa 2: Sincronização de objetos e eventos

O Hightouch suporta a sincronização de objetos de usuário e eventos.

| Destino | Descrição | Modos suportados |
|---|---|---|
| Objeto | Sincroniza registros com objetos como usuários ou organizações em seus destinos.| Upsert ou atualização |
| Eventos | Sincroniza registros como eventos para o seu destino; isso geralmente ocorre na forma de uma chamada de faixa. | Rastrear evento ou rastrear compra |

{% alert note %}
Consulte o [Hightouch](https://hightouch.com/docs/destinations/braze#syncing-and-data-point-consumption) para saber mais sobre como as sincronizações afetam o consumo de pontos de dados do Braze.
{% endalert %}

#### Sincronização de objetos do Braze

É possível sincronizar objetos Hightouch (campos de usuário) com os campos padrão ou personalizados equivalentes do Braze. Também é possível realizar a correspondência de registros para ajudar a unificar os dados entre as duas plataformas.

#### Sincronização de eventos do Braze

A Hightouch permite rastrear dados de eventos e compras e sincronizá-los com a Braze. Várias opções podem ser definidas no Hightouch que afetarão o comportamento de sincronização, como a configuração de dados de rastreamento e a definição de comportamento de usuário inexistente.

{% alert important %}
Mais instruções sobre a sincronização de objetos e eventos podem ser encontradas na [documentação do Hightouch](https://hightouch.io/docs/destinations/braze/).
{% endalert %}



## Demonstração da integração

<div class="video-container">
    <iframe width="560" height="315" src="https://drive.google.com/file/d/1KQdCwZzV88hXMx7AMWgh8izqkldtNv5p/preview" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


