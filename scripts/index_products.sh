#!/usr/bin/env bash
set -euo pipefail

python -m app.jobs.index_products "$@"
