#!/bin/bash

set -e

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR=backups
BACKUP_FILE="$BACKUP_DIR/postgres_$TIMESTAMP.sql"

mkdir -p "$BACKUP_DIR"

docker exec postgres pg_dump \
    -U carecloud \
    carecloud > "$BACKUP_FILE"

echo "Backup created successfully:"
echo "$BACKUP_FILE"
