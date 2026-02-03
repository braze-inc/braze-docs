---
nav_title: Stensul
article_title: Stensul
alias: /partners/stensul
description: "Este artigo de referência descreve a parceria entre o Braze e a Stensul, uma plataforma de e-mail corporativo para a criação de modelos de e-mail responsivos a dispositivos móveis em todos os canais."
page_type: partner
search_tag: Partner

---

# Stensul

> [A Stensul](https://stensul.com/) fornece aos profissionais de marketing de e-mail ferramentas para criar e-mails responsivos a dispositivos móveis e de acordo com a marca na Stensul antes de enviá-los ao Braze em tempo real para a criação de campanhas.

_Essa integração é mantida pela Stensul._

## Sobre a integração

A integração da Braze com a Stensul permite exportar seus e-mails da Stensul formatados em HTML e fazer upload deles como modelos na Braze.

## Pré-requisitos

| Requisito | Descrição |
| ------------| ----------- |
| Conta da Stensul | É necessário ter uma conta da Stensul para usar a parceria. |
| chave da API REST Braze | Uma chave da API REST da Braze com permissões completas de **modelos**. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Instância do cluster | Sua [instância de cluster]({{site.baseurl}}/api/basics/#endpoints) da Braze se alinha com o dashboard e o endpoint REST da Braze.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integração

Forneça sua chave da API REST e a instância do cluster da Braze para a equipe de sucesso do cliente da Stensul. Em seguida, a equipe configurará a integração inicial para você.

{% alert important %}
Essa é uma configuração única e todas as exportações futuras utilizarão automaticamente essa chave de API.
{% endalert %}

### Etapa 1: criar o e-mail na Stensul

Crie um e-mail na Stensul usando a plataforma Stensul e clique em **Complete** (Concluir).

![Opções de salvamento da Stensul]({% image_buster /assets/img_archive/stensul_save_options.png %})

### Etapa 2: Exportar modelo para o Braze
Na nova caixa de diálogo que aparece na página de conclusão, selecione **Upload to ESP** (Fazer upload para o provedor de serviços de e-mail).

![Opções de upload do Stensul]({% image_buster /assets/img_archive/stensul_upload_options.png %})

Em seguida, digite o **nome do modelo**, o **assunto** e o **pré-cabeçalho** do e-mail e selecione **Upload**. Em seguida, você receberá uma confirmação de que o upload foi bem-sucedido e um histórico de uploads anteriores do arquivo, se aplicável.

![Sucesso no upload do Stensul]({% image_buster /assets/img_archive/stensul_upload_success.png %})

## Uso

Encontre o modelo Stensul feito upload na seção **Modelos** da sua conta Braze ** & Media > Email Templates**. Agora você pode usar este modelo de e-mail para começar a enviar mensagens de e-mail envolventes para seus clientes!


