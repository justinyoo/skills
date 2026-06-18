#!/usr/bin/env pwsh
#
# sync-skills.ps1
#
# Copy every skill under .github/skills to .claude/skills.
# Skills that already exist in the destination are left untouched.
#
# Usage:
#   ./scripts/sync-skills.ps1
#
#Requires -Version 5.1
[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'

# Resolve the repository root (the parent of this script's directory).
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Split-Path -Parent $scriptDir

$srcDir = Join-Path $repoRoot '.github/skills'
$destDir = Join-Path $repoRoot '.claude/skills'

if (-not (Test-Path -LiteralPath $srcDir -PathType Container)) {
    Write-Error "Source directory not found: $srcDir"
    exit 1
}

if (-not (Test-Path -LiteralPath $destDir -PathType Container)) {
    New-Item -ItemType Directory -Path $destDir -Force | Out-Null
}

$copied = 0
$skipped = 0

Get-ChildItem -LiteralPath $srcDir -Directory | ForEach-Object {
    $skillName = $_.Name
    $target = Join-Path $destDir $skillName

    if (Test-Path -LiteralPath $target) {
        Write-Host "Skipping '$skillName' (already exists)."
        $skipped++
        return
    }

    Copy-Item -LiteralPath $_.FullName -Destination $target -Recurse
    Write-Host "Copied '$skillName'."
    $copied++
}

Write-Host "Done. Copied $copied skill(s), skipped $skipped."
