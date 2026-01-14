---
nav_title: "Envio de e-mail para o amor"
article_title: Envio de e-mail para o amor
description: "Saiba como integrar o Braze ao Email Love, um plug-in do Figma que o capacita a criar e exportar e-mails HTML responsivos e acessíveis diretamente do Figma."
alias: /partners/email_love/
page_type: partner
search_tag: Partner

---

# Envio de e-mail para o amor

> [O Email Love](https://emaillove.com/) é um plug-in do Figma que permite projetar e exportar e-mails HTML responsivos e acessíveis diretamente do Figma. O recurso Exportar para o Braze do Email Love usa a API do Braze para fazer upload de seus modelos de e-mail para o Braze sem problemas.

## Pré-requisitos

| Requisito            | Descrição                                                      |
|------------------------|------------------------------------------------------------------|
| **Envio de e-mail Conta do amor** | É necessário ter uma conta de envio de e-mail para aproveitar essa parceria. |
| **Chave da API REST do Braze** | Uma chave da API REST do Braze com a permissão completa `Templates` ativada. Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

## Usando o E-mail Love com o Braze

### Etapa 1: Executar o plug-in

Para criar seu modelo de e-mail, primeiro será necessário carregar o plug-in. Para obter instruções mais detalhadas, consulte a documentação do Email Love para [fazer upload de seu e-mail para o Braze](https://help.emaillove.com/exporting-an-email-design/6rcR6LPWq6BoYseKZf41nS/uploading-your-email-to-braze-/3ZcmGaGz6a8azeZQxWgKzm).

### Etapa 2: Crie seu primeiro quadro

No plug-in, selecione o botão **[+ No Template Selected]** para criar um novo quadro para o design de seu e-mail.

### Etapa 3: Crie o modelo com os componentes pré-construídos do Email Love

Selecione o quadro que você criou e comece a adicionar componentes (cabeçalhos, blocos de conteúdo, CTAs e rodapés) da biblioteca de **ativos** do plug-in para estruturar seu e-mail.

![Componentes pré-construídos do e-mail Love.]({% image_buster /assets/img/email_love/emaillove1_content.png %})

### Etapa 4: Personalizar os componentes

Modifique os componentes usando as ferramentas do Figma para ajustar seu texto, imagens, cores e elementos de layout para alinhar o design do modelo com sua marca. Se você adicionar um componente de rodapé, um ink de cancelamento de inscrição do Braze será automaticamente incluído quando você exportar.

![Personalize os componentes no Figma.]({% image_buster /assets/img/email_love/emaillove2_components.png %})

### Etapa 5: Exportar seu modelo de e-mail para o Braze

1. Quando terminar, selecione o quadro que deseja exportar. Note que você precisará usar um rodapé de envio de e-mail que contenha um ink de cancelamento de inscrição para que a exportação funcione.
2. Selecione o botão **Exportar** no plug-in e selecione **Braze** no menu suspenso.
3. Copie e cole sua chave de API na caixa **Braze API Key** no plug-in Email Love Figma.
4. Selecione o botão **Set API Key (Definir chave de API** ).
5. Selecione **Change Instance ID (Alterar ID da Instância**) e, em seguida, selecione o ID da instância do Braze.

![Exportação de um modelo para o Braze a partir do plug-in Email Love.]({% image_buster /assets/img/email_love/emaillove3_exportbraze.png %}){: style="max-width:50%;"}

### Etapa 6: Edite seu e-mail no Braze

No Braze, acesse **Modelos** > **Editar modelos** > **Editar mensagem**. Dentro do editor de modelos, você pode editar o HTML do e-mail ou usar o **editor Rich Text** na guia **Classic**.

## Suporte e solução de problemas

Para obter instruções mais detalhadas, consulte a documentação do Email Love sobre a [exportação de um design de e-mail](https://help.emaillove.com/exporting-an-email-design/6rcR6LPWq6BoYseKZf41nS/uploading-your-email-to-braze-/3ZcmGaGz6a8azeZQxWgKzm). Para obter suporte adicional, entre em contato com a equipe de suporte do Email Love.
