---
nav_title: AppsFlyer Audiences
article_title: AppsFlyer Audiences
alias: /partners/appsflyer_audiences/
description: "Esse artigo de referência descreve a parceria entre o Braze e o AppsFlyer Audiences, um recurso da plataforma AppsFlyer que permite que você crie e conecte segmentos de público com eficiência a redes de parceiros."
page_type: partner
search_tag: Partner

---

# AppsFlyer Audiences

> Este artigo descreve como fazer a importação de coortes de usuários da AppsFlyer para o Braze usando a integração de [públicos da AppsFlyer](https://www.appsflyer.com/product/audiences/). Para saber mais sobre a integração da AppsFlyer e suas outras funcionalidades, como a atribuição móvel, consulte o [artigo principal da AppsFlyer]({{site.baseurl}}/partners/message_orchestration/attribution/appsflyer/appsflyer/).

## Pré-requisitos

| Requisito | Descrição |
|---|---|
| Conta da AppsFlyer | É necessário ter uma conta da AppsFlyer para aproveitar essa parceria. |
| App para iOS ou Android | Essa integração é compatível com os apps para iOS e Android. Dependendo de sua plataforma, os trechos de código podem ser necessários em seu aplicativo. Consulte os detalhes sobre esses requisitos na etapa 1 do processo de integração. |
| SDK da AppsFlyer | Além do SDK da Braze obrigatório, você deve instalar o [SDK da AppsFlyer](https://support.appsflyer.com/hc/en-us/articles/207032126-SDK-integration-overview). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração de importação de dados

### Etapa 1: Configurar o SDK da AppsFlyer

Para usar essa integração, você deve passar o ID externo do Braze do usuário para a AppsFlyer usando a função `setPartnerData()` do SDK da AppsFlyer:

#### Android 
```java
Map<String, Object> brazeData = new HashMap<>();
partnerData.put("external_user_id", "some-braze-external-id-value");
AppsFlyerLib.getInstance().setPartnerData("braze_int", brazeData);
```

#### iOS
```objc
NSDictionary *brazeInfo = @{
     @"external_user_id":@"some-braze-external-id-value"
};
[[AppsFlyerLib shared]  setPartnerDataWithPartnerId:@"braze_int" partnerInfo:brazeInfo];
```

### Etapa 2: Obter a chave de importação de dados do Braze

No Braze, navegue até **Integrações com Parceiros** > **Parceiros de Tecnologia** e selecione **a AppsFlyer**. 

Aqui você encontra o endpoint REST e gera sua chave de importação de dados da Braze. Depois que a chave é gerada, você pode criar outra ou invalidar uma existente. A chave de importação de dados e o ponto de extremidade REST são usados na próxima etapa ao configurar um postback no dashboard da AppsFlyer.<br><br>![A caixa "Importação de dados usando a importação de coortes" na página de tecnologia da AppsFlyer. Nessa caixa, você verá a chave de importação de dados e o ponto de extremidade REST.]({% image_buster /assets/img/appsflyer_audiences/appsflyer_data_import_key.png %}){: style="max-width:90%;"}

### Etapa 3: Configurar uma conexão Braze nos públicos da AppsFlyer

1. No [público da AppsFlyer](https://support.appsflyer.com/hc/en-us/articles/115002689186-Audiences-guide#managing-connections), acesse a guia **Conexões** e clique em **Adicionar conexão de parceiro**.
2. Selecione Braze como parceiro e dê um nome à conexão.
3. Forneça a chave de importação de dados e o endpoint REST da Braze.
4. Salve a conexão e ela estará disponível para ser vinculada a qualquer público novo ou existente.

![A página de configuração da conexão do parceiro da plataforma AppsFlyer para o público. A parte inferior das imagens mostra que a caixa Braze external ID está marcada.]({% image_buster /assets/img/appsflyer_audiences/appsflyer_braze_connection.png %}){: style="max-width:80%;"}

### Etapa 4: Uso de coortes de públicos da Appsflyer no Braze

Após o upload de um público da AppsFlyer para a Braze, você poderá usá-lo como um filtro ao definir segmentos na Braze, selecionando o filtro **Coortes da AppsFlyer**.

![Filtro de atributos do usuário "Coortes da AppsFlyer" selecionado.]({% image_buster /assets/img/appsflyer_audiences/appsflyer_cohorts_as_filter.png %})

{% alert important %}
Somente os usuários que já existem no Braze serão adicionados ou removidos de um coorte. A importação de coorte não criará novos usuários no Braze.
{% endalert %}

## Correspondência de usuários

Os usuários identificados podem ser combinados pelo endereço `external_id` ou `alias`. Os usuários anônimos podem ser combinados pelo site `device_id`. Os usuários identificados que foram originalmente criados como usuários anônimos não podem ser identificados pelo endereço `device_id` e devem ser identificados pelo endereço `external_id` ou `alias`.

