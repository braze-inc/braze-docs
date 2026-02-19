---
nav_title: monitoramento de localização
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

- [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=android)
- [Web]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=web)

Em geral, aplicativos móveis usam o chip GPS do dispositivo e outros sistemas (como a varredura de Wi-Fi) para rastrear a localização do usuário. Aplicativos da web usam WPS (Sistema de Posicionamento por Wi-Fi) para rastrear a localização do usuário. Todas essas plataformas exigem que os usuários optem por participar do monitoramento de localização. A precisão dos seus dados de monitoramento de localização pode ser afetada pelo fato de os usuários terem ou não o Wi-Fi ativado em seus dispositivos. Os usuários de Android também podem escolher diferentes modos de local - os usuários que estão no modo "Economia de bateria" ou "Somente dispositivo" podem ter dados imprecisos.

### Local do usuário do SDK por endereço IP

Braze detecta as localizações dos usuários a partir do país geolocalizado usando o endereço IP do início da primeira sessão do SDK. 

Anteriormente, Braze usava o código do país da localidade do dispositivo durante a criação do usuário do SDK e durante a primeira sessão. Somente após o processamento do início da primeira sessão, o endereço IP seria usado para definir o país mais confiável do usuário. Isso significava que o país do usuário era definido com maior precisão apenas a partir da segunda sessão em diante, somente após o início da primeira sessão ser processado.

Agora, Braze usa o endereço IP para definir o valor do país nos perfis de usuário criados via SDK, e essa configuração de país baseada em IP está disponível durante e após a primeira sessão.

## Direcionamento do local

Usando dados e segmentos de monitoramento de localização, é possível configurar campanhas e estratégias baseadas no local. Por exemplo, talvez você queira executar uma campanha promocional para usuários que moram em uma determinada região ou excluir usuários de uma região com regulamentos mais rígidos.

Consulte [Direcionamento de local]({{site.baseurl}}/user_guide/engagement_tools/segments/location_targeting/) para obter mais informações sobre como criar um segmento de local.

## Definição da atribuição do local padrão

Você também pode usar o [endpoint`users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) em nossa API para atualizar o [`current_location`]({{site.baseurl}}/api/objects_filters/user_attributes_object/) atribuição padrão. Um exemplo é:

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

- [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/)
- [Infillion]({{site.baseurl}}/partners/message_personalization/location/infillion/)
- [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/)

## Perguntas frequentes

### Quando o Braze coleta dados de local?

A Braze só coleta o local quando o aplicativo está aberto em primeiro plano. Como resultado, nosso filtro `Most Recent Location` direciona os usuários com base no local em que eles abriram o aplicativo pela última vez (também chamado de início da sessão).

Você também deve ter em mente as seguintes nuances:

- Se a localização estiver desativada, o filtro `Most Recent Location` mostra a última localização registrada.
- Se um usuário já teve uma localização armazenada em seu perfil, ele se qualifica para o filtro `Location Available`, mesmo que tenha optado por não participar do monitoramento de localização desde então.

### Qual é a diferença entre os filtros Localidade mais recente do dispositivo e Local mais recente?

O `Most Recent Device Locale` vem das configurações do dispositivo do usuário. Por exemplo, isso aparece para usuários de iPhone em seu dispositivo em **Configurações** > **Geral** > **Idioma & Região**. Esse filtro é usado para capturar a formatação regional e de idioma, como datas e endereços, e é independente do filtro `Most Recent Location`.

O endereço `Most Recent Location` é o último local GPS conhecido do dispositivo. Isso é atualizado no início da sessão e é armazenado no perfil do usuário.

### Se um usuário optar por não participar do monitoramento de localização, os dados de localização anteriores são removidos do Braze?

Não. Se um usuário já teve uma localização armazenada em seu perfil, esses dados não são removidos automaticamente se ele optar por não participar do monitoramento de localização posteriormente.

## Solução de problemas

### Nenhum usuário tem localizações disponíveis

Braze captura a localização mais recente de um usuário por padrão através do SDK. Isso normalmente significa que o "local recente" é o local em que o usuário usou o app mais recentemente. Se você enviar dados de localização em segundo plano à Braze, poderá ter dados mais granulares disponíveis.

Se nenhum usuário tiver locais disponíveis, duas verificações rápidas podem ajudá-lo a confirmar a coleta de dados e a transferência de datas.

#### Coleta de dados

Confirme se o seu app está coletando dados locais:

- Para o iOS, isso significa que os usuários aceitam compartilhar seus dados de local por meio de um pedido de aceitação em algum ponto da jornada do usuário. 
- Para Android, confirme se seu app solicita permissões de localização fina ou bruta na instalação.

Para ver se os dados de usuários estão sendo enviados ao Braze, use o filtro **Localização disponível**. Esse filtro permite ver a porcentagem de usuários com um "local mais recente".

![Um segmento "Localização de Teste" que usa o filtro "Localização Disponível".]({% image_buster /assets/img_archive/trouble7.png %})

#### Transferência de dados

Confirme se seus desenvolvedores estão passando dados de local para o Braze. Normalmente, a passagem de dados de localização é tratada automaticamente pelo SDK depois que o usuário dá permissões, mas seus desenvolvedores podem ter desativado o monitoramento de localização na Braze. Mais informações sobre o monitoramento de localização podem ser encontradas em:
- [Android]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=web)