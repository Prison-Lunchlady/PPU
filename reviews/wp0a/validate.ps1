 $ErrorActionPreference = 'Stop'
 $projectRoot = Split-Path $PSScriptRoot -Parent
 $required = @('01-protocol-state.md','02-decision-register.md','03-risk-register.md','04-active-hypotheses.md','05-unresolved-questions.md','06-research-library-index.md','07-development-roadmap.md','08-draft-constitution.md','09-work-package-register.md','10-review-gate-register.md')
 $missing = @($required | Where-Object { -not (Test-Path -LiteralPath (Join-Path $projectRoot $_)) })
 $capture = Get-Content -Raw -LiteralPath (Join-Path $projectRoot 'evidence/conversation-recovered.json') | ConvertFrom-Json
 $oldResponse = $capture.turns[1].items[1].text
 $draftText = $oldResponse.Substring($oldResponse.IndexOf('# PPU MONETARY CONSTITUTION v0.1'))
 $currentDraft = Get-Content -Raw -LiteralPath (Join-Path $projectRoot '08-draft-constitution.md')
 $normalize = { param($value) $value.Replace("`r`n", "`n") }
 $draftPreserved = (& $normalize $currentDraft).Contains((& $normalize $draftText))
 $fullPath = Join-Path $projectRoot 'evidence/PPU_full_recovered_source.txt'
 $full = Get-Content -Raw -LiteralPath $fullPath
 $alignment = { param($v) (($v.Replace("`r`n","`n") -replace '[^]*','' -replace '(?m)^:::writing.*\n','') -replace '(?m)[ \t]+$','').Trim() }
 $prefixMatches = (& $alignment $full).StartsWith((& $alignment $oldResponse))
 $fullNormalized = & $normalize $full
 $constitutionStart = $fullNormalized.IndexOf('# PPU MONETARY CONSTITUTION v0.1')
 $constitutionEnd = $fullNormalized.IndexOf('### Why I think')
 $fullConstitution = $fullNormalized.Substring($constitutionStart,$constitutionEnd-$constitutionStart).TrimEnd()
 $completeDraftPreserved = (& $normalize $currentDraft).Contains($fullConstitution)
 $expectedArticles = @('I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX','XXI','XXII','XXIII','XXIV')
 $foundArticles = @([regex]::Matches($fullNormalized,'(?m)^# ARTICLE ([IVX]+) —') | ForEach-Object { $_.Groups[1].Value })
 $articleCoverage = (($foundArticles -join ',') -eq ($expectedArticles -join ','))
 $postAnalysis = $fullNormalized.Contains('### Why I think this is a materially better starting architecture') -and $fullNormalized.Contains('### What Phase 2 should test first') -and $fullNormalized.TrimEnd().EndsWith('before we write a single production smart contract.**')
 $fullHash = (Get-FileHash -LiteralPath $fullPath).Hash
 $sourceCopyMatches = $fullHash -eq '237A8EEA4F2D64B6B83C597DFA11C7AC02E9BD9A10DE1536083A8D37BA48953E'
 $roadmapHash = (Get-FileHash -LiteralPath (Join-Path $projectRoot '07-development-roadmap.md')).Hash
 $sourceHash = (Get-FileHash -LiteralPath (Join-Path $projectRoot 'evidence/roadmap-v0.1-original.txt')).Hash
 $decision = Get-Content -Raw -LiteralPath (Join-Path $projectRoot '02-decision-register.md')
 $risk = Get-Content -Raw -LiteralPath (Join-Path $projectRoot '03-risk-register.md')
 $hypothesis = Get-Content -Raw -LiteralPath (Join-Path $projectRoot '04-active-hypotheses.md')
 $idsOk = $true
 1..5 | ForEach-Object { if (-not $decision.Contains(('PPU-D{0:D3}' -f $_))) { $idsOk = $false } }
 1..15 | ForEach-Object { if (-not $risk.Contains(('R-{0:D3}' -f $_))) { $idsOk = $false } }
 1..8 | ForEach-Object { if (-not $hypothesis.Contains(('H-{0:D3}' -f $_))) { $idsOk = $false } }
 $broken = @()
 Get-ChildItem -LiteralPath $projectRoot -Recurse -Filter '*.md' | Where-Object { $_.FullName -notlike '*\evidence\*' } | ForEach-Object {
   $file = $_
   $body = Get-Content -Raw -LiteralPath $file.FullName
   foreach ($match in [regex]::Matches($body, '\]\(([^)]+)\)')) {
     $target = $match.Groups[1].Value
     if ($target -match '^(https?:|#)' -or $target -eq 'reviews/validation.json') { continue }
     if (-not (Test-Path -LiteralPath (Join-Path $file.DirectoryName $target))) { $broken += ($file.Name + ': ' + $target) }
   }
 }
 $result = [ordered]@{
   checkedAt = (Get-Date).ToString('o')
   requiredCanonicalFiles = $required.Count
   missingFiles = $missing
   inheritedIdCoverage = $idsOk
   recoveredDraftVerbatim = $draftPreserved
   roadmapByteIdentical = ($roadmapHash -eq $sourceHash)
   roadmapSHA256 = $roadmapHash
   brokenLocalLinks = $broken
   sourceResponseTruncated = $capture.turns[1].items[1].truncated
   fullEvidenceSHA256 = $fullHash
   suppliedSourceCopyMatches = $sourceCopyMatches
   normalizedPrefixMatches = $prefixMatches
   articleCoverage24 = $articleCoverage
   postAnalysisAndFinalBoundary = $postAnalysis
   completeConstitutionPreservation = $completeDraftPreserved
   provenance = 'User-supplied complete recovery; not independent platform export'
   q001 = 'CLOSED'
   gate0 = 'AWAITING REVIEW / NOT APPROVED'
   wp1a = 'NOT AUTHORIZED / NOT STARTED'
   localIntegrityPass = ($missing.Count -eq 0 -and $idsOk -and $draftPreserved -and $completeDraftPreserved -and $prefixMatches -and $sourceCopyMatches -and $articleCoverage -and $postAnalysis -and $roadmapHash -eq $sourceHash -and $broken.Count -eq 0)
 }
 $result | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath (Join-Path $PSScriptRoot 'validation.json') -Encoding utf8
 $result | ConvertTo-Json -Depth 5
 if (-not $result.localIntegrityPass) { throw 'Documentation integrity check failed' }
