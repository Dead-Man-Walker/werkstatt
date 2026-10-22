# Preflight 2026-10-22 (curl, Browser-UA, --max-time 20)

| host | http | bytes | robots.txt (* / Claude) | hinweis | probe-url |
|---|---|---|---|---|---|
| katalog.sarei.de | 200 | 2009 B | robots 404/291B | **200 mit 2009 B = Gerüst/leer** | https://katalog.sarei.de/ |
| sarei.de | 200 | 201323 B | 1 Disallow (*/Claude): /wp-content/uploads/wpo/wpo-plugins-tables-list.json | ld+json; Preisfelder | https://sarei.de/ |

Deutung: 403/503/err oder Challenge → curl nicht nutzbar (Register: webfetch/browser?); 2xx mit wenigen Bytes → JS-Gerüst, kein Händlerbefund; robots-Sperren gelten auch bei http 200 (Pfadliste in <host>.robots.txt). Browser-Verbindung (claude-in-chrome) hier nicht geprüft.
