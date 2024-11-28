---
nav_title: Integrações móveis
article_title: Integrações móveis do Geofence
page_order: 2
page_type: reference
description: "Este artigo de referência aborda as integrações móveis necessárias envolvidas no uso de geofences."
tool: Location

---

# Integrações móveis

> Este artigo de referência aborda as integrações móveis necessárias envolvidas no uso de geofences.

## Requisitos para várias plataformas

As campanhas disparadas por geofence estão disponíveis no iOS e no Android. Para oferecer suporte a geofences, os seguintes itens devem estar em vigor:

1. Sua integração deve suportar notificações por push em segundo plano.
2. As geofences do Braze ou a coleta de locais devem estar ativadas.
3. Para dispositivos com iOS versão 11 ou superior, o usuário deve sempre permitir o acesso ao local para que o geofencing funcione.

{% alert important %}
A partir da versão 3.6.0 do SDK do Braze, a coleta de locais do Braze é desativada por padrão. Para verificar se a capacitação está ativada no Android, confirme se `com_braze_enable_location_collection` está definido como `true` em seu `braze.xml`.
{% endalert %}

## Configuração de geofence

### Latitude e longitude

O centro geográfico da geofence.

### Raio

O raio da geofence em metros, medido a partir do centro geográfico. Recomendamos definir um raio mínimo de 100 a 150 metros para todas as geofences.

Consulte estes guias para obter mais orientações com base em sua plataforma:
- [Android](https://developer.android.com/develop/sensors-and-location/location/geofencing#choose-the-optimal-radius-for-your-geofence)
- [iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html#//apple_ref/doc/uid/TP40009497-CH9-SW5)

### Resfriamento

Os usuários recebem notificações disparadas por geofences depois de realizar transições de entrada ou saída em geofences individuais. Após a ocorrência de uma transição, há um tempo predefinido durante o qual o usuário não pode realizar a mesma transição nessa geofence individual novamente. Esse tempo é chamado de "cooldown" e é predefinido pelo Braze. Seu principal objetivo é evitar solicitações de rede desnecessárias.

### Parceiros tecnológicos

Você também pode aproveitar as geofences com alguns de nossos parceiros, por exemplo: 

- [Radar][12]
- [Foursquare][13]

## Perguntas frequentes

Acesse [Perguntas frequentes sobre geofences][5] para tirar dúvidas sobre geofences.

[3]: https://developers.google.com/android/reference/com/google/android/gms/location/package-summary
[4]: https://developer.apple.com/library/content/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html
[5]: {{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/faqs/#geofences
[12]: {{site.baseurl}}/partners/data_augmentation/contextual_location/radar/
[13]: {{site.baseurl}}/partners/data_augmentation/contextual_location/foursquare/

