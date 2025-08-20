---
nav_title: Voucherify e lista de códigos promocionais
article_title: Lista de Códigos Promocionais da Voucherify e Braze
page_order: 4
alias: /partners/voucherify/promotion/
description: "Este artigo de referência descreve como você pode compartilhar códigos Voucherify usando o snippet de códigos promocionais do Braze."
page_type: partner
search_tag: Partner
---

# Lista de códigos promocionais da Voucherify e Braze

> Além do Conteúdo Conectado e dos atributos personalizados, você pode compartilhar códigos Voucherify usando o snippet de códigos promocionais Braze. Primeiro, exporte os códigos do Voucherify, importe os códigos para o Braze e adicione um trecho de código de e-mail para puxar os códigos da lista de promoções. 

_Essa integração é mantida pela Voucherify._

## Etapa 1: Exportar códigos únicos do Voucherify

No Voucherify, navegue até sua campanha do Voucherify. Em seguida, selecione **Exportar para CSV** e edite o arquivo CSV e remova o nome da coluna para deixar apenas a lista de códigos.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_export_codes.png %}){: style="margin-top:15px;"}

## Etapa 2: Crie uma lista de códigos promocionais

Acessar **Configurações de Dados** > **Códigos Promocionais** e clicar **Criar Lista de Códigos Promocionais**.

Você pode usar o nome da campanha Voucherify para nomear a lista e verificar a consistência dos dados.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_code_list.png %}){: style="max-width:50%;"}

Em seguida, adicione o trecho de código que se refere aos códigos da lista; ele será preenchido com um código único quando a mensagem for enviada.

### Configurações adicionais

Você também pode definir atributos para códigos, como Expiração da Lista e Alertas de Limite; no entanto, nota que o Voucherify gerencia a lógica por trás dos seus códigos, independentemente das configurações da lista.

![Lista de expiração]({% image_buster /assets/img/voucherify/voucherify_promotion_list_expiration.png %})

## Etapa 3: fazer upload do arquivo CSV

Fazer upload do arquivo CSV com códigos Voucherify.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_import_codes.png %})

Confirme que a lista contém apenas códigos (não o cabeçalho da coluna) e clique em **Iniciar Upload**. Quando a importação estiver concluída, clique em **Salvar Lista** para confirmar os detalhes da lista.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_upload_csv.png %}){: style="max-width:50%;"}

## Etapa 4: use o snippet de código em campanhas da Braze

Para usar códigos da lista em uma campanha da Braze, copie o trecho e adicione-o ao corpo do e-mail.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_code_snippet.png %}){: style="max-width:50%;"}

Adicione o trecho de código para exibir um código da lista.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_liquid_email.png %})

Uma vez que a mensagem com o código é enviada, o mesmo código não é usado novamente.

