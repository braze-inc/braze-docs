#!/bin/bash
mkdir -p .git/hooks/
cp -f scripts/hooks/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
