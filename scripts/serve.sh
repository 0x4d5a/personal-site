#!/usr/bin/env bash
set -euo pipefail

PORT="${1:-4000}"
cd "$(dirname "$0")/.."

echo "Serving personal-site at http://127.0.0.1:${PORT}"
python3 -m http.server "$PORT"
