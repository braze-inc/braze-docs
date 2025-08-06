---
nav_title: Depreciações
article_title: Depreciações
page_order: 9
page_type: reference
description: "Esta página inclui referências a artigos obsoletos e fornece uma lista de recursos obsoletos e sem suporte."
---

# Depreciações

A tecnologia está sempre em movimento - dentro e fora da Braze! E fazemos o possível para acompanhá-lo. Aqui, você encontrará as origens da Braze e sua tecnologia - como apoiamos nossos clientes desde antes

Você pode ter chegado aqui pesquisando um termo para uma integração ou recurso que não existe mais. Esta é nossa tentativa de manter você informado sobre nosso progresso e movimento no setor de tecnologia. Você pode encontrar uma lista de recursos obsoletos e sem suporte e ler artigos obsoletos visitando os links a seguir.

## Artigos obsoletos

- [Receptor de push broadcast personalizado para Android]({{site.baseurl}}/help/release_notes/deprecations/custom_broadcast_receiver/)
- [Configuração do Eclipse SDK]({{site.baseurl}}/help/release_notes/deprecations/eclipse_setup_deprecated/)
- [Prevalência do TLS 1.0 e 1.1]({{site.baseurl}}/help/release_notes/deprecations/tls_deprecation/)
- [Integração do webhook Twilio]({{site.baseurl}}/help/release_notes/deprecations/twilio/)
- [Parceria com a Apptimize]({{site.baseurl}}/help/release_notes/deprecations/apptimize/)
- [Parceria com o Grouparoo]({{site.baseurl}}/help/release_notes/deprecations/grouparoo)
- [Interrupção do `checkout.liquid` da Shopify]({{site.baseurl}}/help/release_notes/deprecations/shopify_checkout/)

## Registro de depreciações

### Shopify `checkout.liquid`

**Suporte retirado**: Agosto de 2024 (fase 1), agosto de 2025 (fase 2)

O suporte para o `checkout.liquid` Shopify começará a ser descontinuado em agosto de 2024 e terminará em agosto de 2025. A Shopify fará a transição para o [Checkout Extensibility](https://www.shopify.com/enterprise/blog/checkout-extensibility-winter-editions), que é mais seguro, performático e personalizável.

### Receptor de push broadcast personalizado para Android

**Suporte retirado**: Outubro de 2022

O uso de um `BroadcastReceiver` personalizado para notificações por push foi descontinuado. Use [` subscribeToPushNotificationEvents()`]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#android_using-a-callback-for-push-events) em vez disso.

### Parceria com o Grouparoo

**Suporte retirado**: Abril de 2022

O suporte ao Grouparoo foi descontinuado a partir de abril de 2022.

### SDK do Braze para Windows

**24 de março de 2022**: O SDK da Braze para Windows está obsoleto, e nenhum novo app para Windows pode ser criado no dashboard da Braze.<br>
**15 de setembro de 2022**: Nenhuma mensagem nova pode ser enviada para os apps do Windows. As mensagens existentes e a coleta de dados não são afetadas.<br>
**11 de janeiro de 2024**: A Braze não enviará mais mensagens ou coletará dados de aplicativos do Windows.

### Integração com o Baidu push

**24 de março de 2022**: A integração da Braze com o Baidu push está obsoleta, e nenhum novo app do Baidu pode ser criado no dashboard da Braze. <br>
**15 de setembro de 2022**: Não é possível criar novas mensagens push do Baidu. As mensagens existentes e a coleta de dados não são afetadas.<br>
**11 de janeiro de 2024**: O Braze não enviará mais mensagens ou coletará dados dos apps da Baidu.

### Variável global appboyBridge

**Suporte retirado**: Maio de 2021<br>
**Substituído por**: `brazeBridge`

A variável global `appboyBridge` está obsoleta e foi substituída por `brazeBridge`. `appboyBridge` continuará a funcionar para os clientes existentes, mas recomendamos que você migre para `brazeBridge` se estiver usando `appboyBridge`.

### Parceria Amazon Moments

**Suporte retirado**: Junho de 2020

O suporte para o Amazon Moments foi descontinuado a partir de junho de 2020. O Amazon Moments está sendo incorporado à Amazon Advertising e descontinuou suas APIs e nossa integração.

### Parceria de fato

**Suporte retirado**: Junho de 2020

O suporte ao Factual foi descontinuado a partir de junho de 2020. A Factual foi recentemente adquirida pelo Foursquare e não se integra mais à Braze Platform.

### Integração do webhook Twilio

**Suporte retirado**: Janeiro de 2020

O suporte para a [integração do webhook Twilio]({{site.baseurl}}/partners/twilio/) foi descontinuado a partir de 31 de janeiro de 2020. Se ainda quiser acessar os serviços de SMS com o Braze, consulte nossa [documentação sobre SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/).

### Parceria com a Apptimize

**Suporte retirado**: Agosto de 2019

Se estiver usando atualmente o [Apptimize com o Braze]({{site.baseurl}}/help/release_notes/deprecations/apptimize), não haverá interrupção do serviço. Você ainda pode definir atributos personalizados do Apptimize para perfis de usuário do Braze. No entanto, não será fornecido suporte formal para esse parceiro.

### Mensagens originais no app

**Suporte retirado:** Fevereiro de 2019<br>
**Substituído por**: [Mensagem no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/)

O Braze aprimorou a aparência das mensagens no app para aderir às práticas recomendadas de UX e UI mais recentes e não oferece mais suporte às mensagens originais no app.

A Braze passou a usar uma nova forma de mensagens no app com as seguintes versões do SDK:
- iOS: `2.19.0`
- Android: `1.13.0`
- Web: `1.3.0`

Antes dessas versões, o Braze suportava "mensagens originais no app". Anteriormente, o suporte para mensagens no app originais era fornecido para qualquer cliente que executasse uma campanha no app antes da nova versão. Todas as estatísticas da campanha não foram afetadas pela alteração, e aqueles que enviaram mensagens originais no app tiveram a oportunidade de enviar outras por meio do botão **Criar campanha** na página **Campanha**.

### Widget de feedback

**Suporte retirado**: 1º de julho de 2019.

O SDK do Braze forneceu um widget de feedback que pode ser adicionado ao seu app para permitir que os usuários deixem um feedback usando o método `submitfeedback` e o transmitam para Desk.com ou Zendesk, sendo gerenciado no dashboard.

### Envio de mensagens do Google Cloud (GCM)

**Suporte retirado**: Remoção do suporte da Braze: Julho de 2018, remoção do suporte do Google: 29 de maio de 2019<br>
**Substituído por**: [Envio de mensagens do Firebase Cloud (FCM)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase)

O Google [removeu o suporte ao GCM](https://developers.googleblog.com/2018/04/time-to-upgrade-from-gcm-to-fcm.html) a partir de 29 de maio de 2019. A Braze descontinuou o suporte ao GCM dos SDKs do Android em julho de 2018, o que foi notado em nossos [changelogs do SDK do Android](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md). Isso significa que os tokens GCM existentes continuarão a funcionar, e você poderá enviar mensagens aos usuários existentes. No entanto, não será possível enviar mensagens a novos usuários.

Os clientes que ainda não migraram para o [Firebase Cloud Messaging (FCM)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase) podem ser afetados por essa alteração.

Se você não tiver feito a transição para o FCM, todos os registros de tokens por push do GCM falharão. Se os seus apps são atualmente compatíveis com o GCM, você precisará trabalhar com suas equipes de desenvolvimento na [transição do GCM para o Firebase Cloud Messaging (FCM)](https://developers.google.com/cloud-messaging/android/android-migrate-fcm).

### Eclipse

**Suporte retirado**: 2014-2015<br>
**Substituído por**: [Android Studio]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#using-android-studio)

A Braze descontinuou o suporte ao Eclipse IDE devido ao fato de o Google [ter encerrado o suporte](http://android-developers.blogspot.com/2015/06/an-update-on-eclipse-android-developer.html) ao plug-in Android Developer Tools (ADT) do Eclipse. 

Se precisar de ajuda com a integração do Eclipse antes da migração, entre em contato com [o suporte]({{site.baseurl}}/support_contact/) para obter assistência.

### A transmissão do evento Raw (RES)

**Suporte retirado**: Julho de 2018<br>
**Substituído por**: [Currents]({{site.baseurl}}/user_guide/data/braze_currents/)

O Raw Event Stream foi o predecessor do [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) e foi descontinuado para dar lugar ao futuro dos dados do Braze.

### Postergação enquanto sem atividades - recurso GCM

**Suporte retirado**: Novembro de 2016

O parâmetro Postergação enquanto sem atividades fazia parte anteriormente das [opções de push do GCM](https://developers.google.com/cloud-messaging/http-server-ref). O Google retirou o suporte a essa opção em 15 de novembro de 2016. Anteriormente, quando definido como **true**, indicava que a mensagem não deveria ser enviada até que o dispositivo se tornasse ativo.

### Pontos de extremidade personalizados

**Suporte retirado**: Dezembro de 2019

Remoção de pontos de extremidade personalizados. Se você tiver um endpoint personalizado, poderá continuar a usá-lo, mas a Braze não o fornecerá mais.


