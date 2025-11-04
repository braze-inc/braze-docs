---
nav_title: Zapier
article_title: Zapier
alias: /partners/zapier/
description: "Este artigo de referência descreve a parceria entre o Braze e o Zapier, uma ferramenta da Web de automação que permite compartilhar dados entre apps da Web e usar essas informações para automatizar ações."
page_type: partner
search_tag: Partner

---
# Integração com o Zapier

> [O Zapier](https://zapier.com/) é uma ferramenta da Web de automação que permite compartilhar dados entre apps da Web e, em seguida, usar essas informações para automatizar ações. 

A parceria entre a Braze e a Zapier usa a API e os [webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#creating-a-webhook) da Braze para se conectar a aplicativos de terceiros, como Google Workplace, Slack, Salesforce, WordPress etc., para automatizar várias ações.

## Pré-requisitos

| Solicitações | Descrição |
|---|---|
| Conta Zapier | É necessário ter uma conta da Zapier para usar a parceria. |
| endpoint REST do Braze | Sua URL de endpoint REST. Seu endpoint dependerá da [URL do Braze para sua instância]({{site.baseurl}}/api/basics/#api-definitions). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

No exemplo da Zapier a seguir, enviaremos informações do WordPress para a Braze usando um webhook POST. Essas informações poderão ser usadas para criar um Braze Canvas.

### Etapa 1: Criar um disparo do Zapier

Usando a terminologia da Zapier, um "zap" é um fluxo de trabalho automatizado que conecta seus apps e serviços. A primeira parte de qualquer zap é designar um gatilho. Depois que seu zap for ativado, a Zapier executará automaticamente as respectivas ações sempre que seu gatilho for detectado.

Usando nosso exemplo do WordPress, na plataforma Zapier, configuraremos nosso zap para disparar quando uma nova postagem do WordPress for adicionada e selecionaremos **Published** e **Posts** como **Post Status** e **Post Type**. 

![Na plataforma Zapier, em um zap, selecione o gatilho para ser um "novo comentário", "qualquer webhook" ou "nova postagem". Para este exemplo, selecionamos "new post" (nova postagem). ] [5]

![Na plataforma Zapier, em um zap, configure o gatilho selecionando o status e o tipo de postagem desejados. Para este exemplo, "Published" (Publicados) e "Posts" (Postagens) estão selecionados.] [6]

### Etapa 2: Adicionar um webhook de ação

Em seguida, defina a ação do zap. Quando seu zap estiver ativado e seu disparador for detectado, a ação ocorrerá automaticamente.

Continuando com nosso exemplo, queremos enviar uma solicitação POST como JSON para um endpoint da Braze. Isso pode ser feito selecionando a opção **Webhooks** em **Apps**.

![]({% image_buster /assets/img_archive/zapier3.png %})

### Etapa 3: configure o POST da Braze

Ao configurar seu webhook, use as seguintes configurações e forneça seu endpoint REST da Braze no URL do webhook. Quando terminar, selecione **Publicar**.

- **Método**: POST
- **URL do webhook**: `https://rest.iad-01.braze.com/canvas/trigger/send`
- **Passagem de dados**: Falso
- **Não flutuar**: Não
- **Cabeçalho da solicitação**:
  - **Content-Type**: application/json
  - **Autorização**: portador SUA-CHAVE-DA-API
- **Dados**: 

```json
{
  "canvas_id": "your_canvas_identifier",
  "recipients": [
    {
      "external_user_id": "external_user_identifier",
      "canvas_entry_properties":{
        "string_property": "Your example string",
        "example_integer_property": 1
      }
    }
  ]
}
```

![]({% image_buster /assets/img/zapier.png %}){: style="max-width:70%;"}

### Etapa 4: Criar uma campanha no Braze

Depois de configurar seu zap com êxito, você poderá personalizar suas campanhas do Braze ou Canvas com dados do WordPress usando a formatação Liquid para exibir as informações em suas mensagens.

[5]: {% image_buster /assets/img_archive/zapier1.png %}
[6]: {% image_buster /assets/img_archive/zapier2.png %}
