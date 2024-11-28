---
nav_title: Arquivamento de mensagem
article_title: Arquivamento de mensagem
alias: "/message_archiving/"
page_order: 0
page_type: reference
description: "Este artigo de referência aborda o arquivamento de mensagens, um recurso que permite salvar uma cópia das mensagens enviadas aos usuários."

---

# Arquivamento de mensagens

> O arquivamento de mensagens permite salvar uma cópia das mensagens enviadas aos usuários para fins de arquivamento ou conformidade no bucket S3 da AWS, no contêiner do Azure Blob Storage ou no bucket do Google Cloud Storage. <br><br> Este artigo aborda como configurar o arquivamento de mensagens, referências de cargas úteis JSON e perguntas frequentes.

O arquivamento de mensagens está disponível como um recurso complementar. Para começar a usar o arquivamento de mensagens, entre em contato com o gerente de sucesso do cliente do Braze.

## Como funciona?

Quando esse recurso estiver ativado, se você tiver conectado um bucket de armazenamento em nuvem ao Braze e o tiver marcado como o destino padrão de exportação de dados, o Braze gravará um arquivo JSON compactado em gzip no bucket de armazenamento em nuvem para cada mensagem enviada a um usuário por meio dos canais selecionados (e-mail, SMS ou push). 

Esse arquivo conterá os campos definidos em [Referências de arquivo](#file-references) e refletirá os modelos finais de mensagens enviadas ao usuário. Todos os valores de modelo definidos em sua campanha (por exemplo, {% raw %}`{{${first_name}}}`{% endraw %}) mostrarão o valor final que o usuário recebeu com base nas informações de perfil. Isso permite que você retenha uma cópia da mensagem enviada para atender aos requisitos de conformidade, auditoria ou suporte ao cliente.

Se você configurar credenciais para vários provedores de armazenamento em nuvem, o arquivamento de mensagens só será exportado para aquele explicitamente marcado como o destino padrão de exportação de dados. Se nenhum padrão explícito for fornecido e um bucket S3 da AWS estiver conectado, o arquivamento de mensagens fará upload para esse bucket.

{% alert important %}
A ativação desse recurso afetará a velocidade de entrega de suas mensagens, pois o upload do arquivo é realizado imediatamente antes do envio da mensagem para manter a precisão. Isso introduz latência adicional no pipeline de envio da Braze, afetando as velocidades de envio.
{% endalert %}

O JSON será salvo em seu bucket de armazenamento usando a seguinte estrutura de chave:

`sent_messages/channel/(one of: md5, e164 phone number, email, or push token)/(campaign_id OR canvas_step_id)/DispatchId.json.gz`

Um arquivo de exemplo pode ter a seguinte aparência:

`sent_messages/email/819baa08d8d7e77e19d4666f5fc6050b/ee965cb2-8934-4b0a-acf1-91c899c2f915/651fd10b282850b39e1169c13975234b.json.gz`

{% alert note %}
**Está tendo problemas para encontrar seus tokens por push em seus buckets?**<br>
O Braze faz o downcase de seus tokens por push antes de fazermos o hash deles. Isso faz com que o token por push `Test_Push_Token12345` seja baixado para `test_push_token12345` na jornada da chave com o hash `32b802170652af2b5624b695f34de089`.
{% endalert %}

## Configuração do arquivamento de mensagens

Esta seção o orienta na configuração do arquivamento de mensagens para o seu espaço de trabalho. Antes de continuar, confirme se sua empresa comprou e ativou o arquivamento de mensagens.

### Etapa 1: Conecte um bucket de armazenamento em nuvem

Se ainda não tiver feito isso, conecte um bucket de armazenamento em nuvem à Braze. Para obter etapas, consulte a documentação de nossos parceiros sobre o [Amazon S3]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3/), o [Azure Blob Storage]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/microsoft_azure_blob_storage_for_currents/) ou o [Google Cloud Storage]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/google_cloud_storage_for_currents/).

### Etapa 2: Selecione canais de envio de mensagens

A página de configurações de **envio de mensagens** controla quais canais salvarão uma cópia das mensagens enviadas em seu bucket de armazenamento na nuvem.

Para selecionar canais:

1. Acesse **Configurações** > **Arquivamento de mensagens**.
2. Selecione seus canais.
3. Selecione **Salvar alterações**.

![A página de Arquivamento de mensagens tem três canais para seleção: E-mail, Push e SMS.][1]

{% alert note %}
Se você não vir o **envio de mensagens** em **Configurações**, confirme se sua empresa comprou e ativou o arquivamento de mensagens.
{% endalert %}

## Referências de arquivos

A seguir, referências da carga útil JSON entregue ao seu bucket de armazenamento em nuvem sempre que uma mensagem é enviada. Consulte nosso repositório de exemplos de código para obter [arquivos de amostra de arquivo de mensagens](https://github.com/braze-inc/braze-examples/tree/main/message-archiving).

{% tabs %}
{% tab E-mail %}

```json
{
  "version" : 1, //numerical version of the json structure
  "to": ToAddress, ("customer@example.com")
  "subject": SubjectLine ("20% off coupon inside!"),
  "from_name": DisplayName ("Braze"),
  "from_address": FromAddress ("no-reply@braze.com"),
  "html_body": HtmlBody,
  "plaintext_body": PlainTextBody,
  "amp_body": AMPEmailBody,
  "extras": Extra hash—for SendGrid users, this will be passed to SendGrid as Unique Arguments,
  "headers": HashOfHeaders,
  "sent_at": UnixTimestamp,
  "dispatch_id": DispatchIdFromBraze,
  "campaign_id": CampaignApiId, // may not be available
  "canvas_id": CanvasApiId, // may not be available
  "canvas_step_id": CanvasStepApiId, // may not be available
  "canvas_variation_id" : CanvasVariationApiId, // may not be available
  "message_variation_id": MessageVariationApiId, // may not be available,
  "attachments": Array of JSON Objects containing 'bytes' and 'file_name', // may not be available
  "user_id": String,
  "campaign_name": String, // will only be available if the message is from a campaign
  "canvas_name": String, // will only be available if the message is a from Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

O campo `extras` mencionado nessa carga útil é dos pares de valores chave adicionados no campo **Extras de e-mail** ao enviar um e-mail. Para enviar dados de volta ao Currents, consulte [Extras de mensagens]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/).

![]({% image_buster /assets/img_archive/email_extras.png %}){: style="max-width:60%" }

{% endtab %}
{% tab SMS %}

```json
{
  "version" : 1 //numerical version of the json structure
  "to": PhoneNumber, ("+15555555555"),
  "body": Body ("Hi there!"),
  "subscription_group": SubscriptionGroupExternalId,
  "provider": StringOfProviderName,
  "media_urls": ArrayOfString,
  "sent_at": UnixTimestamp,
  "dispatch_id": DispatchIdFromBraze,
  "campaign_id": CampaignApiId, // may not be available
  "canvas_id": CanvasApiId, // may not be available
  "canvas_step_id": CanvasStepApiId, // may not be available
  "canvas_variation_id" : CanvasVariationApiId, // may not be available
  "message_variation_id": MessagVariationApiId, // may not be available
  "user_id": String,
  "campaign_name": String, // will only be available if the message is from a campaign
  "canvas_name": String, // will only be available if the message is a from Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

{% endtab %}
{% tab Push %}

```json
{
  "version" : 1, //numerical version of the json structure
  "to": PushToken,
  "payload": JsonOfEntirePushPayload,
  "platform": ios/android/web/kindle,
  "app_id": ApiKeyOfApp,
  "sent_at": UnixTimestamp,
  "dispatch_id": DispatchIdFromBraze,
  "campaign_id": CampaignApiId, // may not be available
  "canvas_id": CanvasApiApiId, // may not be available
  "canvas_step_id": CanvasStepApiId, // may not be available
  "canvas_variation_id" : CanvasVariationApiId, // may not be available
  "message_variation_id": MessagVariationApiId, // may not be available
  "user_id": String,
  "campaign_name": String, // will only be available if the message is from a campaign
  "canvas_name": String, // will only be available if the message is a from Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

{% endtab %}
{% endtabs %}

## Perguntas frequentes

### Quais modelos não estão incluídos na carga útil?

As modificações feitas depois que a mensagem sair do Braze não serão refletidas no arquivo salvo em seu bucket de armazenamento em nuvem. Isso inclui modificações feitas por nossos parceiros de entrega de e-mail, como o envolvimento de links para rastreamento de cliques e a inserção de pixels de rastreamento.

### O que são mensagens sob o valor "unassociated" (não associado) na jornada da campanha?

Quando uma mensagem é enviada fora de uma campanha ou do Canva, a ID da campanha no nome do arquivo será "desassociada". Isso ocorrerá quando você enviar mensagens de teste do dashboard, quando o Braze enviar respostas automáticas de SMS ou quando as mensagens enviadas por meio da API não especificarem um ID de campanha.

### Como faço para obter mais informações sobre esse envio?

Você pode usar o `external_id` ou o `dispatch_id` em conjunto com o `user_id` para fazer referência cruzada da mensagem modelada com nossos dados de Currents para encontrar mais informações, como o registro de data e hora em que foi entregue, se o usuário abriu ou clicou na mensagem e muito mais.

### Como as novas tentativas são tratadas?

Se seu bucket de armazenamento em nuvem não puder ser acessado, o Braze tentará novamente até três vezes com um [jitter de backoff](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/#Jitter). As novas tentativas de limite de frequência do AWS S3 são tratadas automaticamente pela Braze.

### O que acontecerá se minhas credenciais forem inválidas?

Se suas credenciais de armazenamento em nuvem se tornarem inválidas em algum momento, o Braze não poderá salvar nenhuma mensagem em seu bucket de armazenamento em nuvem, e essas mensagens serão perdidas. Recomendamos configurar a preferência [de notificação de erros de credenciais da AWS]({{site.baseurl}}/user_guide/administrative/company_settings/notification_preferences) para que você receba alertas sobre qualquer problema com as credenciais.

### Por que o registro de data e hora do meu arquivo `sent_at` é ligeiramente diferente do registro de data e hora enviado no Currents?

A cópia renderizada é feita upload imediatamente antes de enviar a mensagem ao usuário. Devido aos tempos de upload do armazenamento em nuvem, pode haver uma postergação de alguns segundos entre o registro de data e hora `sent_at` na cópia renderizada e a hora real em que o envio ocorre.

[1]: {% image_buster /assets/img/message_archiving_settings.png %}
