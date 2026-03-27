Vor dem [Erstellen von Karussell-Templates]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/template_builder/whatsapp_carousel_templates/#create-a-carousel-template) benötigen Sie:
- Ein aktives WhatsApp Business-Konto (WABA), das mit Braze verbunden ist
- Entsprechende Abo-Gruppen, die in Ihrem WABA konfiguriert sind
- Medien-Assets (Bilder oder Videos), die zum Hochladen bereit sind
- Braze-Berechtigungen für Nutzer:innen ohne Administratorrechte
    - Damit Nutzer:innen neue Templates im Template Builder erstellen können:
        - „View WhatsApp Message Templates"
        - „Edit WhatsApp Message Templates"
    - Damit Nutzer:innen Kampagnen oder Canvase mit Karussell-Templates verfassen können:
        - „View WhatsApp Message Templates"
- Grundkenntnisse in Liquid-Templating (optional, für dynamischen Content)

{% alert important %}
Alle Telefonnummern und Abo-Gruppen innerhalb desselben WhatsApp Business-Kontos (WABA) teilen sich die Templates. Wenn Sie mehrere Abo-Gruppen innerhalb eines WABA haben, können alle auf dieselben Karussell-Templates zugreifen. Templates werden jedoch nicht über verschiedene WABAs hinweg geteilt.
{% endalert %}