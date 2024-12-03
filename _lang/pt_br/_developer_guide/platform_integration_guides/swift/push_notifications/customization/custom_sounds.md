---
nav_title: Sons personalizados
article_title: Sons personalizados de notificações por push para iOS
platform: Swift
page_order: 3
description: "Este artigo aborda a implementação de sons personalizados do iOS no Swift SDK."
channel:
  - push

---

# Sons personalizados

## Etapa 1: Hospedagem do som no app

Os sons de notificação por push personalizados devem ser hospedados localmente no pacote principal de seu app. São aceitos os seguintes formatos de dados de áudio:

- PCM linear
- MA4
- µLaw
- aLaw

É possível empacotar os dados de áudio em um arquivo AIFF, WAV ou CAF. No Xcode, adicione o arquivo de som ao seu projeto como um recurso não localizado do pacote de aplicativos.

{% alert note %}
Os sons personalizados devem ter menos de 30 segundos quando reproduzidos. Se um som personalizado estiver acima desse limite, o som padrão do sistema será reproduzido.
{% endalert %}

### Conversão de arquivos de som

Você pode usar a ferramenta afconvert para converter sons. Por exemplo, para converter o som do sistema PCM linear de 16 bits Submarine.aiff para áudio IMA4 em um arquivo CAF, use o seguinte comando no terminal:

```bash
afconvert /System/Library/Sounds/Submarine.aiff ~/Desktop/sub.caf -d ima4 -f caff -v
```

{% alert tip %}
Você pode inspecionar um som para determinar seu formato de dados abrindo-o no QuickTime Player e escolhendo **Mostrar Inspetor de Filme** no menu **Filme**.
{% endalert %}

## Etapa 2: Fornecimento de um URL de protocolo para o som

Você deve especificar um URL de protocolo que direcione para o local do arquivo de som em seu app. Há dois métodos para fazer isso:

* Use o parâmetro `sound` do [objeto Apple push]({{site.baseurl}}/api/objects_filters/messaging/apple_object#apple-push-object) para passar o URL para o Braze.
* Especifique o URL no dashboard. No [criador do push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#step-3-select-notification-type-ios-and-android), selecione **Configurações** e insira o URL do protocolo no campo **Som**. 

![O criador do push no dashboard do Braze]({% image_buster /assets/img_archive/sound_push_ios.png %})

Se o arquivo de som especificado não existir ou se a palavra-chave “default” for inserida, a Braze usará o som de alerta padrão do dispositivo. Além de nosso dashboard, o som também pode ser configurado por meio de nossa [API de envio de mensagens][12].

Consulte a documentação para desenvolvedores da Apple sobre a [preparação de sons de alerta personalizados](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SupportingNotificationsinYourApp.html) para obter informações adicionais.

