---
nav_title: Mailizio
article_title: Mailizio
alias: /partners/mailizio
description: "Este artigo de referência descreve a parceria entre o Braze e a Mailizio, uma plataforma de criação e gerenciamento de e-mails que permite que você crie conteúdo reutilizável e seguro para a marca e o exporte para o Braze."
page_type: partner
search_tag: Partner

---

# Mailizio

> [O Mailizio](https://mailizio.com/) é uma plataforma de criação e gerenciamento de e-mails que facilita a criação de conteúdo reutilizável e seguro para a marca usando um editor visual intuitivo. Com a integração da Mailizio ao Braze, você pode exportar seus blocos de conteúdo e modelos de e-mail e, em seguida, gerar automaticamente mensagens no app a partir desses mesmos ativos, ativando uma implantação de campanha rápida e totalmente controlada.

_Essa integração é mantida pela Mailizio._

## Sobre a integração

A integração entre o Mailizio e o Braze permite que você crie modelos dinâmicos de e-mail usando o editor do Mailizio, aproveite as variáveis do Liquid usadas nas configurações do Braze e envie-os para o Braze para agilizar a execução da campanha.

## Casos de uso

- Envie modelos de e-mail prontos para envio diretamente para o Braze para campanhas e mensagens transacionais.
- Crie módulos de conteúdo reutilizáveis (cabeçalhos, rodapés, promoções e outros) para otimizar a produção em várias campanhas e canais.
- Gere mensagens no app a partir de e-mails: O Mailizio identifica seções relevantes do seu e-mail e permite exportar o HTML para uso em suas campanhas in-app.
- Personalize em escala com variáveis Liquid compatíveis com o Braze em e-mails e mensagens no app.
- Mantenha a consistência de sua marca gerenciando ativos criativos no Mailizio e atualizando-os no Braze com uma única exportação.

## Pré-requisitos

| Requisito | Descrição |                          
| ----------- | ----------- |  
| Conta Mailizio | É necessário ter uma conta Mailizio para aproveitar essa parceria. |  
| Chave da API REST do Braze | Uma chave da API REST da Braze com permissões completas de **modelos**.<br><br>Você pode criar uma chave da API REST do Braze no dashboard do Braze em **Configurações** > Chaves de API. |  
| Endpoint REST  do Braze | [Sua URL de endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Seu endpoint depende do URL do Braze para sua instância. |  
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integração

Forneça sua chave da API REST do Braze e a instância do cluster para o gerente de sucesso do cliente do Mailizio. A equipe do Mailizio configura a integração inicial para você.

{% alert important %}
Essa é uma configuração única, e todas as exportações no futuro utilizarão automaticamente essa chave de API.
{% endalert %}

### Etapa 1: Criar um e-mail no Mailizio

No Mailizio, use o editor de arrastar e soltar para criar um e-mail que reflita a identidade de sua marca e, em seguida, clique em **Salvar** para preservar seu trabalho.

![captura de tela do editor de arrastar e soltar]({% image_buster /assets/img/mailizio/screenshot_1.png %})

### Etapa 2: Exportar seu modelo de e-mail para o Braze

Quando estiver pronto, clique em **Exportar boletim informativo**. Na janela pop-up, selecione **Braze-email** e confirme a exportação.

Se você atualizar seu conteúdo posteriormente, exporte-o novamente do Mailizio para atualizá-lo no Braze.

![captura de tela do modal de exportação]({% image_buster /assets/img/mailizio/screenshot_2.png %})

{% alert important %}  
Você pode criar e exportar blocos de conteúdo da mesma forma usando o editor **de módulos** do Mailizio.  
{% endalert %}

## Uso

Localize o modelo Mailizio feito upload na seção **Templates & Media > Email Templates** da sua conta Braze. Agora você pode usar este modelo de e-mail para começar a enviar mensagens de e-mail envolventes para seus clientes!
