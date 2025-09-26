---
nav_title: Dyspatch
article_title: Dyspatch
alias: /partners/dyspatch
description: "Este artigo de referência descreve a parceria entre Braze e Dyspatch, um construtor de e-mail de arrastar e soltar que permite criar e-mails bonitos, responsivos e envolventes sem a necessidade de escrever código."
page_type: partner
search_tag: Partner

---

# Dyspatch

> [Dyspatch](https://www.dyspatch.io) oferece um construtor de e-mail intuitivo de arrastar e soltar usado para criar e-mails bonitos, responsivos e envolventes sem precisar escrever código. Colabore com sua equipe para criar e aprovar e-mails na Dyspatch e, em seguida, exportá-los para uso na Braze, tudo em apenas algumas etapas! 

_Essa integração é mantida pela Dyspatch._

## Sobre a integração

A integração Dyspatch e Braze permite simplificar o ciclo de vida da criação de e-mails exportando modelos de e-mail Dyspatch diretamente para o Braze.

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta da Dyspatch | Uma [conta Dyspatch](https://www.dyspatch.io/login/) com uma [função de proprietário ou administrador](https://docs.dyspatch.io/administration/dyspatch_roles/) é necessária para aproveitar esta parceria. |
| chave da API REST Braze | Uma chave da API REST da Braze com permissões completas de **modelos**. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integração

A integração Braze e Dyspatch permite que você exporte modelos de e-mail Dyspatch diretamente para sua biblioteca de mídia Braze ou baixe seu modelo e faça o upload manualmente. 

### Etapa 1: Crie a integração Braze

No portal de administração do Dyspatch, abra o menu suspenso do seu nome de usuário e selecione **Integrações**. Crie uma nova integração, selecione **Braze**, e insira sua chave de API do Braze.

No campo **Localize Exports By** (Encontrar exportações por), você pode escolher como gostaria de gerenciar a localização. Este campo permite que você [localize seus modelos de e-mail](https://docs.dyspatch.io/localization/localizing_a_template/) e os exporte para a Braze para enviar e-mails personalizados por idioma ou localidade com facilidade. 

![Modelo de exportação da Dyspatch]({% image_buster /assets/img/dyspatch/dyspatch_integration_create.png %}){: style="max-width:50%;"}

### Etapa 2: Exportar modelo para Braze

Depois de concluir um e-mail na Dyspatch, para enviar seu modelo para a Braze, visualize o modelo de e-mail publicado e clique em **Download/Export** (Baixar/exportar) e depois em **Export to integration** (Exportar para integração).

Se você quiser fazer upload do seu modelo manualmente, visualize o modelo de e-mail publicado e clique em **Baixar/Exportar** e depois em **Baixar HTML**. Em seguida, na seção **modelos e mídias > Modelos de e-mail** da sua conta Braze, selecione **Do arquivo** para fazer upload do seu modelo.

![Modelo de exportação da Dyspatch]({% image_buster /assets/img/dyspatch/dyspatch_export.gif %})

{% alert important %}
Não selecione **CSS Inline** na seção **Informações de Envio** para qualquer modelo de e-mail Dyspatch no Braze. A Dyspatch cuida disso, garantindo que seus e-mails sejam robustos, responsivos e prontos para enviar.
{% endalert %}

### Uso

Encontre seu modelo Dyspatch carregado na seção **modelos e mídias > modelos de e-mail** da sua conta Braze. Agora você pode usar este modelo de e-mail para começar a enviar mensagens de e-mail envolventes para seus clientes!


