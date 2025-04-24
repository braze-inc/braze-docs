---
nav_title: Monitoramento de localização
article_title: Monitoramento de localização
page_order: 0
page_type: reference
description: "Este artigo de referência explica como usar o monitoramento de localização e o direcionamento de localização em seus apps e quais parceiros oferecem suporte ao rastreamento de localização."
tool: Location
search_rank: 2
---

# monitoramento de localização

> A coleta de local captura o local mais recente do usuário quando o app foi aberto usando dados de localização GPS. É possível usar essas informações para segmentar dados com base nos usuários que estavam em um local definido.

## Ativação do monitoramento de localização

Para ativar a coleta de locais em seu app, consulte o guia do desenvolvedor da plataforma que está usando:

- [iOS][2]
- [Android][3]
- [Web][4]

Em geral, os apps móveis usam o chip GPS do dispositivo e outros sistemas (como o monitoramento de localização por Wi-Fi) para rastrear o local do usuário. Os apps da Web usarão o WPS (Wi-Fi Positioning System) para rastrear os locais do usuário. Todas essas plataformas exigirão que os usuários aceitem o monitoramento de localização. A precisão dos seus dados de monitoramento de localização pode ser afetada pelo fato de os usuários terem ou não o Wi-Fi ativado em seus dispositivos. Os usuários de Android também podem escolher diferentes modos de local - os usuários que estão no modo "Economia de bateria" ou "Somente dispositivo" podem ter dados imprecisos.

### Local do usuário do SDK por endereço IP

A partir de 26 de novembro de 2024, o Braze detectará os locais dos usuários do país geolocalizado usando o endereço IP do início da primeira sessão do SDK. 

Antes disso, o Braze usava o código do país da localização do dispositivo durante a criação do usuário do SDK e na duração da primeira sessão. Somente após o processamento do início da primeira sessão, o endereço IP seria usado para definir o país mais confiável do usuário. Isso significa que o país do usuário foi definido com maior precisão apenas a partir da segunda sessão, somente depois que o início da primeira sessão foi processado.

Agora, o Braze usará o endereço IP para definir o valor do país nos perfis de usuário criados por meio do SDK, e essa configuração de país baseada em IP estará disponível durante e após a primeira sessão.

## Direcionamento do local

Usando dados e segmentos de monitoramento de localização, é possível configurar campanhas e estratégias baseadas no local. Por exemplo, talvez você queira executar uma campanha promocional para usuários que moram em uma determinada região ou excluir usuários de uma região com regulamentos mais rígidos.

Consulte [Direcionamento de local][1] para obter mais informações sobre como criar um segmento de local.

## Definição da atribuição do local padrão

Você também pode usar o [endpoint`users/track` ][8] em nossa API para atualizar o [`current_location`][9] atribuição padrão. Um exemplo é:

```
https://[your_braze_rest_endpoint]/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "attributes": [ 
 	{
 	  "external_id" : "XXX",
 	  "current_location" : {"longitude":-0.118092, "latitude": 51.509865}
      }
   ]
}
```

## Suporte de parceria para beacon e geofence

A combinação do suporte a beacon ou geofence existente com nossos recursos de direcionamento e envio de mensagens fornece mais informações sobre as ações físicas dos usuários para que você possa enviar mensagens de acordo com elas. Você pode aproveitar o monitoramento de localização com alguns de nossos parceiros: 

- [Radar][6]
- [Infillion][10]
- [Foursquare][7]

## Perguntas frequentes

Consulte nossas Perguntas [frequentes sobre][11] locais para obter respostas às perguntas mais frequentes sobre locais.

[1]: {{site.baseurl}}/user_guide/engagement_tools/segments/location_targeting/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/location_tracking/
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/location_tracking/
[6]: {{site.baseurl}}/partners/data_augmentation/contextual_location/radar/
[7]: {{site.baseurl}}/partners/data_augmentation/contextual_location/foursquare/
[8]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[9]: {{site.baseurl}}/api/objects_filters/user_attributes_object/
[10]: {{site.baseurl}}/partners/message_personalization/location/infillion/
[11]: {{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/faqs/#locations
