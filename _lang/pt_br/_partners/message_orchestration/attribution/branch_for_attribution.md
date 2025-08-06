---
nav_title: Filial para Atribuição
article_title: Filial para Atribuição
alias: /partners/branch_for_attribution/
description: "Este artigo de referência descreve a parceria entre a Braze e a Branch, uma plataforma de links móveis que ajuda você a adquirir, engajar e medir em todos os dispositivos, canais e plataformas."
page_type: partner
search_tag: Partner
---

# Filial para atribuição {#branch}

{% multi_lang_include video.html id="PwGKqfwV-Ss" align="right" %}

> A [Branch](https://docs.branch.io/pages/integrations/braze/) é uma plataforma de deeplinking móvel que ajuda a adquirir, engajar e medir em todos os dispositivos, canais e plataformas por meio de uma visão holística de todos os pontos de contato dos usuários.

_Essa integração é mantida pela Branch._

## Sobre a integração

A integração entre a Branch e a Braze ajudam a entender exatamente quando e onde aconteceu a aquisição de um usuário e a personalizar a jornada de cada um por meio de atribuição e [deeplinking]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/).

## Pré-requisitos

| Requisito | Descrição |
|---|---|
| Conta da agência | É necessário ter uma conta Branch para usar a parceria. |
| app iOS ou Android | Essa integração é compatível com os apps para iOS e Android. Dependendo de sua plataforma, os trechos de código podem ser necessários em seu aplicativo. Consulte detalhes sobre esses requisitos na etapa 1 do processo de integração. |
| SDK da Branch | Além do SDK da Braze obrigatório, você deve instalar o [SDK da Branch](https://help.branch.io/developers-hub/docs/native-sdks-overview). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: Mapear IDs de dispositivos

#### Android 

Se você tiver um app para Android, precisará passar um ID de dispositivo da Braze exclusivo para a Branch. Este ID pode ser definido no método `setRequestMetadataKey()` do SDK da Branch. O seguinte trecho de código deve ser incluído antes de chamar `initSession`. Você também deve inicializar o SDK da Braze antes de definir os metadados da solicitação no SDK da Branch.

{% tabs local %}
{% tab Java %}
```java
Branch.getInstance().setRequestMetadata("$braze_install_id", Braze.getInstance(context).deviceId); 
```
{% endtab %}
{% tab Kotlin %}
```kotlin
Branch.getInstance().setRequestMetadata("$braze_install_id", Braze.getInstance(context).deviceId)
```
{% endtab %}
{% endtabs %}

#### iOS

{% alert important %}
Antes de fevereiro de 2023, nossa integração de atribuição da Branch usava o IDFV como o identificador principal para corresponder aos dados de atribuição do iOS. Não é necessário que os clientes da Braze que usam Objective-C busquem o `device_id` da Braze e o enviem para a Branch na instalação, pois não haverá interrupção do serviço.
{% endalert%}

Para quem usa o SWIFT SDK v5.7.0+, se você deseja continuar usando o IDFV como o identificador mútuo, confirme se o campo `useUUIDAsDeviceId` está definido como `false` para que não haja interrupção da integração. 

Se estiver definido como `true`, implemente o mapeamento de ID do dispositivo iOS para SWIFT a fim de passar o `device_id` da Braze para a Branch na instalação do app para que a Braze possa corresponder adequadamente as atribuições do iOS.

{% tabs local %}
{% tab Objective C %}
```objc
[braze deviceIdOnQueue:dispatch_get_main_queue() completion:^(NSString * _Nonnull deviceId) {
  [[Branch getInstance] setRequestMetadataKey:@"$braze_install_id" value:deviceId];
  // Branch init
}];
```
{% endtab %}
{% tab SWIFT %}

```swift
braze.deviceId { deviceId in
  Branch.getInstance.setRequestMetadata("$braze_install_id", deviceId)
  // Branch init 
}
```

{% endtab %}
{% endtabs %}

### Etapa 2: Obtenha a chave de importação de dados do Braze

Na Braze, navegue até **Integrações de parceiros** > **Parceiros de tecnologia** e selecione **Branch**. 

Aqui você encontra o endpoint REST e gera sua chave de importação de dados da Braze. Depois que a chave é gerada, você pode criar outra ou invalidar uma existente. A chave de importação de dados e o endpoint REST são usados na próxima etapa ao configurar um postback no dashboard da Branch.<br><br>![Esta imagem mostra a caixa "Importação de dados para instalar atribuição" encontrada na página de tecnologia da Branch. Nessa caixa, você verá a chave de importação de dados e o ponto de extremidade REST.]({% image_buster /assets/img/attribution/branch.png %}){: style="max-width:90%;"}

### Etapa 3: Configurar Data Feeds

1. Em Branch, na seção **Exportações**, selecione **Data Feeds**.
2. Na página **Data Feeds Manager**, selecione a guia **Data Integrations (Integrações de dados** ) na parte superior da página. 
3. Selecione Braze na lista de parceiros de dados disponíveis. 
4. Na página de exportação do Braze, forneça a chave de importação de dados e o ponto de extremidade REST que você encontrou no dashboard do Braze e selecione **Capacitar**.

### Etapa 4: Confirmar a integração

Depois que a Braze receber os dados de atribuição da Branch, o indicador de status da conexão na página de parceiros de tecnologia da Branch na Braze mudará de "Não conectado" para "Conectado". Um carimbo de data/hora da última solicitação bem-sucedida também será incluído. 

Observe que isso não acontecerá até recebermos dados sobre uma instalação atribuída. Instalações orgânicas, que devem ser excluídas do postback da Branch, são ignoradas pela nossa API e não são contadas ao determinar se uma conexão bem-sucedida foi estabelecida.

## Dados de atribuição do Facebook e X (anteriormente Twitter)

Os dados de atribuição para campanhas do Facebook e do X (antigo Twitter) não estão disponíveis por meio de nossos parceiros. Essas fontes de mídia não permitem que seus parceiros compartilhem dados de atribuição com terceiros e, portanto, nossos parceiros não podem enviar esses dados para a Braze.

## URLs de rastreamento de clique da Branch na Braze (opcional)

Usar links de rastreamento de cliques em suas campanhas da Braze permitirá que você veja facilmente quais campanhas estão gerando instalações de apps e reengajamento. Como resultado, você será capaz de medir seus esforços de marketing de forma mais eficaz e tomar decisões baseadas em dados sobre onde investir mais recursos para obter o máximo retorno sobre o investimento.

Para começar a usar os links de rastreamento de cliques da Branch, consulte [documentação](https://help.branch.io/using-branch/docs/ad-links) da Branch. Você pode inserir os links de rastreamento de cliques do Branch diretamente em suas campanhas do Braze. A Branch usará então suas [metodologias de atribuição probabilística](https://help.branch.io/using-branch/docs/branch-attribution-logic-settings) para atribuir o usuário que clicou no link. Recomendamos anexar seus links de rastreamento da Branch com um identificador de dispositivo para melhorar a precisão das atribuições de suas campanhas da Braze. Isso atribuirá de forma determinística o usuário que clicou no link.

{% tabs local %}
{% tab Android %}
Para Android, a Braze permite que os clientes façam a aceitação da [coleta do ID de publicidade do Google (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). O GAID também é coletado nativamente pela integração SDK da Branch. Você pode incluir o GAID nos seus links de rastreamento de cliques da Branch utilizando a seguinte lógica Liquid:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
user_data_aaid={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Para iOS, tanto a Braze quanto a Branch coletam de modo automático o IDFV nativamente através das nossas integrações de SDK. Isso pode ser usado como o identificador do dispositivo. Você pode incluir o IDFV nos seus links de rastreamento de cliques da Branch utilizando a seguinte lógica Liquid:

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
user_data_idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert note %}
**Esta recomendação é puramente opcional**<br>
Se você não usa identificadores de dispositivo, como o IDFV ou GAID, nos seus links de rastreamento de cliques nem planeja adotá-los, a Branch ainda será capaz de atribuir esses cliques através de um modelo probabilístico.
{% endalert %}


