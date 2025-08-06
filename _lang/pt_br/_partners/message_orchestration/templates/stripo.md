---
nav_title: Stripo
article_title: Stripo
alias: /partners/stripo
description: "Este artigo de referência descreve a parceria entre a Braze e a Stripo, um construtor de modelos de e-mail de arrastar e soltar que permite criar facilmente e-mails sofisticados com elementos interativos."
page_type: partner
search_tag: Partner

---

# Stripo

> [Stripo](https://stripo.email/) é um criador de e-mail de arrastar e soltar que ajuda você a criar e projetar e-mails responsivos com elementos interativos. Os usuários do Stripo também podem editar em HTML e decidir quais elementos exibir ou ocultar em vários dispositivos através do editor Stripo.

_Essa integração é mantida pela Stripo._

## Sobre a integração

A integração Braze e Stripo permite que você exporte seus e-mails personalizados do Stripo e faça upload deles como templates no Braze.

## Pré-requisitos

| Requisito | Descrição |
| ------------| ----------- |
| Conta Stripo | É necessário ter uma conta Stripo para aproveitar esta parceria. |
| Chave da API REST do Braze | Uma chave da API REST da Braze com permissões completas de **modelos**. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Instância do cluster | Sua [instância de cluster]({{site.baseurl}}/api/basics/#endpoints) da Braze se alinha com o dashboard e o endpoint REST da Braze.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integração

### Etapa 1: Criar e-mail Stripo

Crie um e-mail Stripo na plataforma Stripo e clique em **Exportar**. 

![Stripo Export]({% image_buster /assets/img_archive/stripo_export.png %})

### Etapa 2: Exportar modelo para Braze

Na caixa de diálogo que aparece, selecione **Braze** como seu método de exportação. 

Em seguida, insira seu **nome da conta** (como nome do espaço de trabalho), **chave de API** e sua **instância do cluster**.

![Stripo Form]({% image_buster /assets/img_archive/stripo_form.png %})

{% alert important %}
Esta é uma configuração única, e qualquer exportação no futuro utilizará automaticamente esta chave de API.
{% endalert %}

## Uso

Encontre seu modelo Stripo carregado na seção **Modelos e mídias > Modelos de e-mail** da sua conta Braze. Agora você pode usar este modelo de e-mail para começar a enviar mensagens de e-mail envolventes para seus clientes!


