#!/bin/bash
# Abre o pitch do Lili.AI por um servidor local, para o vídeo, o som e o roteiro em pop-up funcionarem.
cd "$(dirname "$0")/../.." || exit 1
PORT=8765
while lsof -iTCP:$PORT -sTCP:LISTEN >/dev/null 2>&1; do PORT=$((PORT+1)); done
python3 -m http.server "$PORT" --bind 127.0.0.1 >/dev/null 2>&1 &
PID=$!
trap 'kill $PID 2>/dev/null' EXIT INT TERM
sleep 1
URL="http://127.0.0.1:$PORT/demo/hackathon/pitch.html"
if [ -d "/Applications/Google Chrome.app" ]; then open -a "Google Chrome" "$URL"; else open "$URL"; fi
echo ""
echo "  Pitch aberto em $URL"
echo "  Deixe esta janela aberta durante a apresentação. Para encerrar: Ctrl+C ou feche a janela."
echo ""
wait $PID
