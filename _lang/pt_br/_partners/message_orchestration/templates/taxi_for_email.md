---
nav_title: Taxi for Email
article_title: Taxi for Email
alias: /partners/taxi_for_email
description: "Este artigo de referência descreve a parceria entre o Braze e o Taxi for Email, uma ferramenta de marketing de e-mail on-line que permite que os clientes do Braze criem modelos de e-mail inteligentes usando sua interface de arrastar e soltar e uma sintaxe simples, porém poderosa."
page_type: partner
search_tag: Partner

---

# Taxi for Email

> [O Taxi for Email](http://taxiforemail.com/) é uma ferramenta de marketing por e-mail on-line que oferece um editor visual de e-mail intuitivo do tipo arrastar e soltar. O Taxi incentiva as equipes a colaborar facilmente em campanhas de e-mail, permitindo que redatores e editores tenham acesso e recursos necessários para criar e-mails, tudo sem código.

_Essa integração é mantida pelo Taxi for Email._

## Sobre a integração

A integração entre o Braze e o Taxi aproveita a sintaxe simples e poderosa do Taxi para criar e exportar modelos de e-mail inteligentes para o Braze. 

## Pré-requisitos

| Requisito | Descrição |
| ------------| ----------- |
| Taxi para conta de e-mail | É necessário ter uma conta do Taxi for Email para aproveitar essa parceria. |
| Chave da API REST do Braze | Uma chave da API REST da Braze com permissões completas de **modelos**. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Ponto de extremidade do Braze | [Seu endpoint Braze]({{site.baseurl}}/api/basics/#endpoints) está alinhado com o URL do dashboard Braze.<br><br> Por exemplo, se o URL do dashboard for `https://dashboard-03.braze.com`, seu endpoint será `dashboard-03`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integração

### Etapa 1: Crie um modelo de e-mail para o Taxi

Crie um modelo de táxi na plataforma Taxi. Depois que o modelo for criado, navegue até **as Configurações da organização** e selecione a guia **ESP Connectors (Conectores ESP** ).

### Etapa 2: Criar conector Braze

1. Na caixa de diálogo exibida, selecione o botão **Add New (Adicionar novo)** e, em seguida, selecione **Braze** na lista suspensa. 
2. Selecione **Braze** para editar as configurações do conector Braze.
3. Digite o endpoint e a chave de API da Braze.

Seu campo de conector mudará de cor depois que os detalhes com as permissões corretas forem fornecidos. Se esse campo não for alterado, verifique se seus campos estão alinhados com os requisitos listados.

## Uso

Encontre o modelo de Taxi feito upload na seção **Modelos e mídias > Modelos de e-mail** da sua conta Braze. Agora você pode usar esse modelo de e-mail para começar a enviar mensagens de e-mail envolventes para seus clientes!


