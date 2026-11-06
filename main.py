import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
messages = [{"pays": "Cameroun", "nom": "Fondateur", "msg": "Bienvenue sur EDU-NET Mondial ! Depuis Yaounde !"}]
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        html_msg = ""
        for m in messages[-50:]:
            html_msg += f"<div style='background:white;padding:10px;margin:8px;border-radius:10px'><b>{m['pays']} - {m['nom']}</b><br>{m['msg']}</div>"
        html = f"<html><head><meta name='viewport' content='width=device-width, initial-scale=1'><title>EDU-NET</title></head><body style='font-family:sans-serif;background:#f0f2f5;padding:15px'><div style='background:#0A1931;color:white;padding:20px;border-radius:15px;text-align:center'><h1>EDU-NET MONDIAL</h1><p>Learn Together. Talk Together. Anywhere.</p><p>Depuis le Cameroun</p></div><h2>WORLD CHAT</h2>{html_msg}<form method='POST' style='background:white;padding:15px;border-radius:15px'><input name='nom' placeholder='Ton prenom' required style='width:100%;padding:10px;margin:5px 0;border-radius:8px'><br><input name='pays' placeholder='Ton pays' required style='width:100%;padding:10px;margin:5px 0;border-radius:8px'><br><input name='msg' placeholder='Ton message' required style='width:100%;padding:10px;margin:5px 0;border-radius:8px'><br><button style='width:100%;background:#0A1931;color:white;padding:12px;border:none;border-radius:10px'>ENVOYER AU MONDE</button></form></body></html>"
        self.wfile.write(html.encode('utf-8'))
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        data = urllib.parse.parse_qs(self.rfile.read(length).decode())
        nom = data.get('nom', ['Anonyme'])[0]
        pays = data.get('pays', ['Monde'])[0]
        msg = data.get('msg', [''])[0]
        if msg:
            messages.append({"pays": pays, "nom": nom, "msg": msg})
        self.send_response(303)
        self.send_header('Location', '/')
        self.end_headers()
port = int(os.environ.get('PORT', 10000))
HTTPServer(('0.0.0.0', port), Handler).serve_forever()
