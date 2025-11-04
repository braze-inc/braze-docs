---
nav_title: Kochava
article_title: Kochava
alias: /partners/kochava/
description: "Este artigo de referência descreve a parceria entre o Braze e a Kochava, uma plataforma de atribuição móvel que oferece insights de atribuição e análise de dados para ajudá-lo a aproveitar seus dados para crescer."
page_type: partner
search_tag: Partner

---

# Kochava

> A Kochava oferece atribuição e análise de dados para dispositivos móveis que ajudam a utilizar seus dados em prol do crescimento. Com a Kochava Audience Platform, é possível planejar, direcionar, ativar, medir e otimizar suas campanhas de apps.

_Essa integração é mantida pela Kochava._

## Sobre a integração

A integração entre o Braze e a Kochava ajuda a proporcionar uma compreensão mais holística de suas campanhas, enviando dados de atribuição ao Braze para entender melhor quais campanhas estão gerando instalações, atividades no aplicativo e muito mais.

## Pré-requisitos

| Requisito | Descrição |
|---|---|
| Conta Kochava | É necessário ter uma conta Kochava para aproveitar essa parceria. |
| App para iOS ou Android | Essa integração é compatível com os apps para iOS e Android. Dependendo de sua plataforma, os trechos de código podem ser necessários em seu aplicativo. Consulte os detalhes sobre esses requisitos na etapa 1 do processo de integração. |
| Kochava SDK | Além do SDK da Braze obrigatório, você deve instalar o [SDK da Kochava](https://support.kochava.com/sdk-integration/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: Mapear IDs de usuários

#### Android

O SDK para [Android](https://support.kochava.com/sdk-integration/sdk-kochavatracker-android/class-tracker?scrollto=marker_3) gera um GUID como o ID da Braze no início da sessão. Esse é o identificador que recomendamos passar para o método Kochava `IdentityLink`, pois ele permite que o Braze reconcilie os dados de volta ao perfil de usuário correto. O ID da Braze pode ser recuperado usando o seguinte método:

```java
Apppboy.getInstance(context).getDeviceId();
```

#### iOS

{% alert important %}
Antes de fevereiro de 2023, nossa integração de atribuição Kochava usava o IDFV como o identificador principal para corresponder aos dados de atribuição do iOS. Não é necessário que os clientes do Braze que usam Objective C busquem o Braze `device_id` e o enviem para a Kochava durante a instalação, pois não haverá interrupção do serviço.
{% endalert%}

Para quem usa o SWIFT SDK v5.7.0+, se você deseja continuar usando o IDFV como o identificador mútuo, confirme se o campo `useUUIDAsDeviceId` está definido como `false` para que não haja interrupção da integração. Se estiver definido como `true`, implemente o mapeamento de ID do dispositivo iOS para SWIFT a fim de passar o `device_id` da Braze para a Kochava na instalação do app para que a Braze possa corresponder adequadamente as atribuições do iOS.

A Braze tem duas APIs que produzirão o mesmo valor, uma com um manipulador de conclusão e outra usando o novo suporte de simultaneidade do Swift. Note que você precisará modificar os seguintes trechos de código para que fiquem em conformidade com as instruções do [SDK para iOS](https://support.kochava.com/sdk-integration/ios-sdk-integration/) da Kochava. Para obter ajuda adicional, entre em contato com o suporte da Kochava.

##### Manipulador de conclusão
```
AppDelegate.braze?.deviceId(completion: { deviceId in
  // Use `deviceId`
})
```
##### Concorrência Swift
```
let deviceId = await AppDelegate.braze?.deviceId()
```

### Etapa 2: Obter a chave de importação de dados do Braze

Na Braze, navegue até **Integrações de parceiros** > **Parceiros de tecnologia** e selecione **Kochava**. 

Aqui você encontra o endpoint REST e gera sua chave de importação de dados da Braze. Depois que a chave é gerada, você pode criar outra ou invalidar uma existente. A chave de importação de dados e o ponto de extremidade REST são usados na próxima etapa ao configurar um postback no dashboard do Kochava.<br><br>![Esta imagem mostra a caixa "Data Import for Install Attribution" (Importação de dados para atribuição de instalação) encontrada na página de tecnologia do Kochava. Nessa caixa, você verá a chave de importação de dados e o ponto de extremidade REST.]({% image_buster /assets/img/attribution/kochava.png %}){: style="max-width:90%;"}

### Etapa 3: configure um postback da Kochava

[Adicione um postback](https://support.kochava.com/campaign-management/create-a-kochava-certified-postback) em seu dashboard do Kochava. Você será solicitado a fornecer a chave de importação de dados e o ponto de extremidade REST que encontrou no dashboard do Braze.

### Etapa 4: Confirmar a integração

Quando o Braze receber dados de atribuição da Kochava, o indicador de status de conexão na página de parceiros de tecnologia da Kochava no Braze mudará de "Não conectado" para "Conectado". Um registro de data e hora da última solicitação bem-sucedida também será incluído. 

Observe que isso não acontecerá até recebermos dados sobre uma instalação atribuída. Instalações orgânicas, que devem ser excluídas do postback da Kochava, são ignoradas pela nossa API e não são contadas ao determinar se uma conexão bem-sucedida foi estabelecida.

## Dados de atribuição do Facebook e do X (antigo Twitter)

Os dados de atribuição para campanhas do Facebook e do X (antigo Twitter) não estão disponíveis por meio de nossos parceiros. Essas fontes de mídia não permitem que seus parceiros compartilhem dados de atribuição com terceiros e, portanto, nossos parceiros não podem enviar esses dados para a Braze.

## URLs de rastreamento de cliques do Kochava no Braze (opcional)

O uso de links de rastreamento de cliques em suas campanhas do Braze permitirá que você veja facilmente quais campanhas estão gerando instalações de aplicativos e reengajamento. Como resultado, você poderá medir seus esforços de marketing de forma mais eficaz e tomar decisões baseadas em dados sobre onde investir mais recursos para obter o máximo de ROI.

Para começar a usar os links de rastreamento de cliques do Kochava, visite sua [documentação](https://support.kochava.com/reference-information/attribution-overview/). Você pode inserir os links de rastreamento de cliques da Kochava diretamente em suas campanhas do Braze. A Kochava usará então suas [metodologias de atribuição probabilística](https://www.kochava.com/getting-prepared-for-ios-14/) para atribuir o usuário que clicou no link. Recomendamos anexar seus links de rastreamento do Kochava com um identificador de dispositivo para melhorar a precisão das atribuições de suas campanhas do Braze. Isso atribuirá de forma determinística o usuário que clicou no link.

{% tabs local %}
{% tab Android %}
Para Android, a Braze permite que os clientes façam a aceitação da [coleta do ID de publicidade do Google (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). O GAID também é coletado nativamente por meio da integração do SDK da Kochava. É possível incluir o GAID em seus links de rastreamento de cliques do Kochava utilizando a seguinte lógica Liquid:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Para iOS, tanto a Braze quanto a Kochava coletam de modo automático o IDFV nativamente através das nossas integrações de SDK. Isso pode ser usado como identificador do dispositivo. É possível incluir o IDFV em seus links de rastreamento de cliques do Kochava utilizando a seguinte lógica Liquid:

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert note %}
**Essa recomendação é puramente opcional**<br>
Se você não usa atualmente nenhum identificador de dispositivo - como o IDFV ou GAID - em seus links de rastreamento de cliques, ou não planeja fazê-lo no futuro, a Kochava ainda poderá atribuir esses cliques por meio de sua modelagem probabilística.
{% endalert %}


