# Preflight 2026-10-22 (curl, Browser-UA, --max-time 20)

| host | http | bytes | robots.txt (* / Claude) | hinweis | probe-url |
|---|---|---|---|---|---|
| 4rain.com | 200 | 113562 B | robots 200/113562B | ld+json; Preisfelder | https://4rain.com/ |
| arves.de | 200 | 212123 B | 1 Disallow (*/Claude); **Disallow: / → gesperrt**: / | — | https://arves.de/ |
| garantia.de | 200 | 117721 B | robots 200/117721B | ld+json; Preisfelder | https://garantia.de/ |

Deutung: 403/503/err oder Challenge → curl nicht nutzbar (Register: webfetch/browser?); 2xx mit wenigen Bytes → JS-Gerüst, kein Händlerbefund; robots-Sperren gelten auch bei http 200 (Pfadliste in <host>.robots.txt). Browser-Verbindung (claude-in-chrome) hier nicht geprüft.
