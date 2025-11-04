---
nav_title: Mencione-me
article_title: Integração do Mention Me com o Braze
description: Guia de configuração da integração Mention Me
alias: /partners/mention_me/
page_type: partner
search_tag: Partner
---

# Mencione-me

> Juntos, [o Mention Me](https://www.mention-me.com/) e o Braze podem ser sua porta de entrada para atrair clientes premium e promover uma fidelidade inabalável à marca. Ao integrar perfeitamente os dados primários de referência ao Braze, você pode oferecer experiências omnicanal altamente personalizadas direcionadas aos fãs da sua marca.

_Essa integração é mantida pela Mention Me._

## Pré-requisitos

Antes de começar, você precisará do seguinte:

| Pré-requisito          | Descrição                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Uma conta Mention Me   | É necessário ter uma conta [Mention Me](https://mention-me.com/login) para aproveitar essa parceria.                                                                     |
| Uma chave da API REST da Braze  | Uma chave da API REST da Braze com as permissões `users.track` e `templates.email.create`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Um endpoint Braze REST | [Seu URL do ponto de extremidade REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Seu endpoint dependerá do URL do Braze para sua instância.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso

* Envie dados de contato e aceitação de clientes indicados pelo Mention Me para o Braze em tempo real
* Use os dados de referência para criar lembretes por e-mail de cupons
* Aprimoramento da performance de outros canais de marketing, usando dados de referência para segmentar e direcionar clientes de alto valor

## Quais dados são enviados do Mention Me para o Braze?

Quando você configurar essa integração, o Mention Me criará automaticamente as atribuições e os eventos de seus clientes - portanto, não há necessidade de fazer isso antes.

Os endereços de e-mail de seus clientes no Braze serão usados para vincular eventos relevantes e atributos personalizados. O Mention Me enviará eventos e atributos de perfil de contato para qualquer cliente potencial ou existente que disparar esse evento por meio do Mention Me, independentemente de seu status de aceitação.

Para obter mais detalhes, consulte [Atribuições e eventos do perfil de contato](https://help.mention-me.com/hc/en-gb/articles/26677937177501-What-Mention-Me-data-is-sent-to-Braze).

## Integração do Mention Me

{% alert tip %}
Para obter um passo a passo completo, consulte a [documentação de configuração do Braze da Mention Me](https://help.mention-me.com/hc/en-gb/articles/26151773368221-How-to-setup-Braze-with-Mention-Me).
{% endalert %}

Para integrar o Mention Me com o Braze:

1. No Mention Me, acesse a página de [integração do Braze](https://mention-me.com/merchant/~/integrations/braze) e selecione **Connect (Conectar**).
2. Selecione **Create New Authorization (Criar nova autorização)**, adicione a [chave de API criada anteriormente](#prerequisites) e selecione sua instância do Braze.
3. Escolha um ou mais países com os quais você gostaria de sincronizar.
4. Quando terminar, selecione **Connect**.
