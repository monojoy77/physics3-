#!/usr/bin/env python3
"""
KINETIQ Development Web Server
Zero external dependencies - runs with standard Python 3.
Serves the website on localhost (camera access requires localhost/HTTPS).
"""

import http.server
import socketserver
import webbrowser
import mimetypes
import os
import sys

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

# Windows registries often map .js/.css wrongly (text/plain), which makes the
# browser refuse the stylesheet. Force correct types.
mimetypes.add_type("application/javascript", ".js")
mimetypes.add_type("text/css", ".css")
mimetypes.add_type("application/wasm", ".wasm")


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        super().end_headers()

    def log_message(self, fmt, *args):
        # Show only errors (404s etc.) so missing files are easy to spot
        if args and str(args[1]).startswith(("4", "5")):
            super().log_message(fmt, *args)


class Server(socketserver.TCPServer):
    allow_reuse_address = True  # avoids "port in use" right after a restart


def main():
    os.chdir(DIRECTORY)

    # Warn loudly if project files are missing
    needed = ["index.html", "css/styles.css"] + [
        f"js/{n}.js" for n in (
            "physics-engine", "synthetic-demo", "mediapipe-tracker",
            "charts-dashboard", "gesture-classifier", "playground",
            "model-comparison", "hero-visualizer", "app")
    ]
    missing = [f for f in needed if not os.path.exists(os.path.join(DIRECTORY, f))]
    if missing:
        print("  [!] MISSING FILES (site will be broken):")
        for f in missing:
            print("      -", f)

    for port in range(PORT, PORT + 10):
        try:
            httpd = Server(("127.0.0.1", port), Handler)
        except OSError:
            print(f"  [!] Port {port} is in use, trying {port + 1}...")
            continue
        url = f"http://localhost:{port}"
        print("=" * 65)
        print("  KINETIQ - Sanchar Saathi & FIOL Communication Platform")
        print("=" * 65)
        print(f"  [+] Serving from : {DIRECTORY}")
        print(f"  [+] Local URL    : {url}")
        print("  [+] Stop Server  : Ctrl + C")
        print("=" * 65)
        webbrowser.open(url)
        with httpd:
            httpd.serve_forever()
        return
    print("  [x] No free port found between 8000-8009.")
    sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n  [OK] Server stopped.")
        sys.exit(0)