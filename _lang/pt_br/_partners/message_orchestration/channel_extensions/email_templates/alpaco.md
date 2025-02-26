---
nav_title: Alpaco
article_title: Alpaco
alias: /partners/Alpaco
description: "A integração Braze e Alpaco usa a sintaxe da Alpaco para criar e exportar modelos de e-mail orientados por dados para a Braze."
page_type: partner
search_tag: Partner

---

# Alpaco

> [O Alpaco](https://alpaco.email/) é uma ferramenta de marketing por e-mail on-line que oferece um editor de e-mail do tipo arrastar e soltar para um novo nível de controle do design e do resultado. A integração entre o Braze e a Alpaco permite que você exporte para o Braze envios de e-mail com base em dados e na marca. 

{% alert note %}
A Alpaco oferece suporte pleno a [variáveis Liquid](https://shopify.github.io/liquid/) e, portanto, tem compatibilidade plena com todas as variáveis Liquid usadas nas suas configurações da Braze.
{% endalert %}

## Pré-requisitos

| Requisito | Descrição |
| ------------| ----------- |
| Conta Alpaco | É necessário ter uma conta na Alpaco para usar essa parceria. |
| Chave da API REST do Braze | Uma chave da API REST da Braze com permissões completas de **Templates**. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Instância do cluster | Sua [instância de cluster]({{site.baseurl}}/api/basics/#endpoints) da Braze se alinha com o dashboard e o endpoint REST da Braze. <br><br> Por exemplo, se o URL do seu dashboard for `https://dashboard-03.braze.com`, seu endpoint será `dashboard-03`.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integração

Forneça sua chave da API REST e a instância do cluster da Braze para a equipe de sucesso do cliente da Alpaco. Em seguida, a equipe configurará a integração inicial para você.

{% alert note %}
Essa é uma configuração única e todas as exportações futuras usarão automaticamente essa chave de API.
{% endalert %}

## Exportação de e-mails da Alpaco para o Braze

### Etapa 1: Criar um modelo de e-mail na Alpaco

Na plataforma Alpaco, use as diferentes configurações e opções para criar um modelo que expresse a identidade de sua marca. Selecione **Salvar** quando estiver satisfeito com seu modelo.

![Alpaco Criar modelo]({% image_buster /assets/img/alpaco/alpaco_1.png %})

### Etapa 2: Criar um e-mail

Depois que o modelo for criado, navegue até o lobby e crie um e-mail com o modelo. Selecione **Review (Revisar** ) para ter certeza de que tudo está correto.

![Criação de e-mail na Alpaco]({% image_buster /assets/img/alpaco/alpaco_2.png %})

### Etapa 3: Revisar e exportar e-mails para o Braze

Selecione **Exportar** e escolha a integração do Braze para exportar seu modelo de e-mail para o Braze. 

Se quiser implementar alterações no seu modelo de e-mail, faça isso na Alpaco e depois exporte o e-mail de novo para a Braze. Isso atualizará o e-mail no Braze com suas alterações.

![Exportar e-mail na Alpaco]({% image_buster /assets/img/alpaco/alpaco_3.png %})

## Uso de modelos de e-mail da Alpaco no Braze

Para encontrar o e-mail da Alpaco enviado, acesse **Modelos e mídias > Modelos de e-mail** no dashboard da Braze. Agora é possível usar esse modelo para enviar e-mails com a marca e orientados por dados de usuários.

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/
