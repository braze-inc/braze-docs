---
nav_title: APIs exportieren
article_title: APIs exportieren
page_order: 8
page_type: reference
description: "Dieser referenzierte Artikel beschreibt, warum Sie eine JSON-Datei mit Dashboard-Daten programmatisch exportieren sollten, anstatt eine CSV-Datei direkt aus dem Dashboard zu exportieren."
platform: API

---

# APIs exportieren

> Diese Seite behandelt die Braze Export APIs, mit denen Sie eine JSON-Datei mit Dashboard-Daten exportieren können. Unter [Endpunkte exportieren]({{site.baseurl}}/api/endpoints/export/) finden Sie eine Liste der Daten, auf die Sie zugreifen können, einschließlich Anweisungen und Beispielcode für den Export.

## Wann Sie Export APIs anstelle von CVS-Downloads verwenden sollten

Es gibt einige Gründe, warum Sie diese Methode dem direkten Export einer CSV-Datei aus dem Dashboard vorziehen sollten:

 - Ihre Datei ist sehr groß. Von unserem Dashboard aus können Sie eine CSV-Datei mit maximal 500.000 Zeilen exportieren. Wenn Sie Daten zu einem Segment mit mehr als 500.000 Nutzern exportieren, müssen Sie unsere Export-API verwenden, die keine Exportbegrenzung enthält.
 -  Sie möchten programmatisch mit den Daten interagieren.

{% alert tip %}
Hilfe zu CSV- und API-Exporten finden Sie unter [Fehlerbehebung bei Exporten]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

