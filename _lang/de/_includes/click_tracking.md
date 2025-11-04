{% if include.section == "UTM parameters" %}

Während Sie mit Linkverkürzungen Ihre URLs automatisch verfolgen können, können Sie auch UTM-Parameter zu Ihren URLs hinzufügen, um die Leistung von Kampagnen in Analysetools von Drittanbietern, wie Google Analytics, zu verfolgen.

Um UTM-Parameter zu Ihrer URL hinzuzufügen, gehen Sie wie folgt vor:

1. Beginnen Sie mit Ihrer Basis-URL. Dies ist die URL der Seite, die Sie verfolgen möchten (z. B. `https://www.example.com`).
2. Fügen Sie ein Fragezeichen (?) nach Ihrer Basis-URL ein.
3. Fügen Sie jeden UTM-Parameter durch ein kaufmännisches Und (&) getrennt hinzu.

Ein Beispiel ist `https://www.example.com?utm_source=newsletter&utm_medium=sms`.

{% endif %}

{% if include.section == "Frequently Asked Questions" %}

## Häufig gestellte Fragen

### Sind die Links, die ich beim Testversand erhalte, echte URLs?

Wenn die Kampagne vor dem Testversand als Entwurf gespeichert wurde, ja. Andernfalls handelt es sich um einen Platzhalter-Link. Beachten Sie, dass sich die bei der tatsächlichen Kampagne übermittelte URL von der in der Testsendung unterscheiden kann.

### Kann ich UTM-Parameter zu einer URL hinzufügen, bevor sie gekürzt wird?

Ja Es können sowohl statische als auch dynamische Parameter hinzugefügt werden. 

### Wie lange bleiben verkürzte URLs gültig?

Personalisierte URLs sind ab dem Zeitpunkt der URL-Registrierung zwei Monate lang gültig.

### Muss das Braze SDK installiert sein, um Links zu kürzen?

Nein. Die Linkverkürzung funktioniert ohne SDK-Integration.

{% endif %}

{% if include.section == "Custom Domains" %}

## Angepasste Domains

Die Verkürzung von Links ermöglicht es Ihnen auch, Ihre eigene Domain zu verwenden, um das Erscheinungsbild Ihrer verkürzten URLs zu personalisieren und so ein konsistentes Markenimage zu vermitteln. Weitere Informationen finden Sie unter [Angepasste Domains]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/custom_domains/).

{% endif %}