# Preflight 2026-10-22 (curl, Browser-UA, --max-time 20)

| host | http | bytes | robots.txt (* / Claude) | hinweis | probe-url |
|---|---|---|---|---|---|
| beckmann-kg.de | 200 | 189749 B | 23 Disallow (*/Claude): /*ekomiRating$, /*hideEkomiBadge$, /?otp2*, /?type*, /?websale8*, /agb | — | https://beckmann-kg.de/ |

Deutung: 403/503/err oder Challenge → curl nicht nutzbar (Register: webfetch/browser?); 2xx mit wenigen Bytes → JS-Gerüst, kein Händlerbefund; robots-Sperren gelten auch bei http 200 (Pfadliste in <host>.robots.txt). Browser-Verbindung (claude-in-chrome) hier nicht geprüft.
