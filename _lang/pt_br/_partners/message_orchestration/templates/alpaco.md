---
nav_title: Alpaco
article_title: Alpaco
alias: /partners/Alpaco
description: "A integração entre o Braze e a Alpaco permite exportar modelos de e-mail e blocos de conteúdo compatíveis com o Liquid e com a marca para o Braze, prontos para uso em mensagens de e-mail e no app."
page_type: partner
search_tag: Partner
---

# Alpaco

> [A Alpaco](https://alpaco.email/) é uma ferramenta de gestão criativa on-line que oferece um editor de arrastar e soltar para criar conteúdo reutilizável e seguro para a marca no Braze. A integração da Alpaco e do Braze permite exportar blocos de conteúdo, modelos de e-mail e modelos de mensagens no app.

_Essa integração é mantida pela Alpaco._

{% alert note %}
A Alpaco oferece suporte pleno a [variáveis Liquid](https://shopify.github.io/liquid/) e, portanto, tem compatibilidade plena com todas as variáveis Liquid usadas nas suas configurações da Braze.
{% endalert %}

## Pré-requisitos

| Requisito | Descrição |
| ------------| ----------- |
| Conta Alpaco | É necessário ter uma conta na Alpaco para usar essa parceria. |
| Chave da API REST do Braze | Uma chave da API REST da Braze com permissões completas de **modelos**. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Instância do cluster | Sua [instância de cluster]({{site.baseurl}}/api/basics/#endpoints) da Braze se alinha com o dashboard e o endpoint REST da Braze. <br><br> Por exemplo, se o URL do seu dashboard for `https://dashboard-03.braze.com`, seu endpoint será `dashboard-03`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Casos de uso

- Exporte **modelos de e-mail** totalmente projetados para uso em campanhas do Braze e envio de mensagens transacionais.
- Crie e gerencie **blocos de conteúdo modulares** (e.g., cabeçalhos, rodapés, promoções) que podem ser reutilizados em vários canais.
- Crie **mensagens engajadas no app** com a mesma flexibilidade criativa dos e-mails, facilitando o fornecimento de experiências consistentes e de acordo com a marca em todos os canais.
- Ative **a personalização** incluindo Liquid tags com suporte da Braze, como `{{first_name}}` ou `{{custom_attribute}}`.
- Mantenha **a consistência da marca** centralizando o design criativo no Alpaco e empurrando as atualizações para o Braze com uma única exportação.

## Integração

Forneça sua chave da API REST e a instância do cluster da Braze para a equipe de sucesso do cliente da Alpaco. Em seguida, a equipe configurará a integração inicial para você.

{% alert note %}
Essa é uma configuração única e todas as exportações futuras usarão automaticamente essa chave de API.
{% endalert %}

## Exportação de mensagens do Alpaco para o Braze

### Etapa 1: Criar um modelo na Alpaco

Na Alpaco, crie um modelo que expresse a identidade de sua marca. Quando estiver pronto, selecione **Salvar**.

![Alpaco Criar modelo]({% image_buster /assets/img/alpaco/alpaco_1.png %})

### Etapa 2: Redija uma mensagem usando o modelo

Em seguida, acesse o lobby da Alpaco e use seu modelo para criar um e-mail, uma mensagem no app ou um bloco de conteúdo. Para verificar novamente sua mensagem antes de exportar, selecione **Review (Revisar**).

![Criação de e-mail na Alpaco]({% image_buster /assets/img/alpaco/alpaco_2.png %})

### Etapa 3: Exportar sua mensagem para o Braze

Selecione **Exportar** e, em seguida, escolha a integração do Braze e especifique se está exportando um modelo de e-mail ou um bloco de conteúdo.

Se você fizer alterações após a exportação, poderá reexportar o conteúdo do Alpaco para atualizá-lo no Braze.

![Exportar e-mail na Alpaco]({% image_buster /assets/img/alpaco/alpaco_3.png %})

## Uso de modelos e blocos Alpaco no Braze

Dependendo do tipo de conteúdo exportado, o modelo aparecerá em uma das seguintes seções:

- **Modelos e mídias > Modelos de e-mail**
- **Modelos e mídias > Blocos de conteúdo**

Os modelos da Alpaco são ideais para organizações que desejam gerenciar de forma centralizada a consistência da marca. Eles também suportam as tags incorporadas da Braze para facilitar a categorização e o gerenciamento de conteúdo.
