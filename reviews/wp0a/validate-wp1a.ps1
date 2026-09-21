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
$checks = [ordered]@{
 canonicalFiles = ($missing.Count -eq 0)
 inheritedIDs = $idsOk
 sourcePrefix = $prefixMatches
 sourceSHA256 = $sourceCopyMatches
 fullDraft = $completeDraftPreserved
 allArticles = $articleCoverage
 postAnalysis = $postAnalysis
 roadmapMirror = ($roadmapHash -eq $sourceHash)
 roadmapOriginal = ($roadmapHash -eq 'A24F5998F0D5AA1CF53EE2B1EFD2E32820BBCBF587C396076C98C95F252A47F3')
 localLinks = ($broken.Count -eq 0)
}
$checks.draftUnchanged = (Get-FileHash -LiteralPath (Join-Path $projectRoot '08-draft-constitution.md')).Hash -eq (Get-FileHash -LiteralPath (Join-Path $projectRoot 'evidence/gate0-approved/08-draft-constitution.md')).Hash
$outputs = @('01-purchasing-power-standard-research-report.md','02-comparative-benchmark-matrix.md','03-methodology-and-revisions.md','04-benchmark-institutional-risk.md','05-hedgeability-and-matching.md','06-recommended-standard.md','sources.md','reviewer-reconciliation.md','WP1A-completion-report.md','Gate-1A-submission.md')
$checks.requiredDeliverables = @($outputs | Where-Object { -not (Test-Path -LiteralPath (Join-Path $projectRoot ('wp1a/' + $_))) }).Count -eq 0
$report = Get-Content -Raw -LiteralPath (Join-Path $projectRoot 'wp1a/01-purchasing-power-standard-research-report.md')
$answers = @([regex]::Matches($report,'(?m)^### (\d+)\. ') | ForEach-Object {[int]$_.Groups[1].Value})
$checks.twelveAnswers = ($answers -join ',') -eq ((1..12)-join ',')
$state = Get-Content -Raw -LiteralPath (Join-Path $projectRoot '01-protocol-state.md')
$gates = Get-Content -Raw -LiteralPath (Join-Path $projectRoot '10-review-gate-register.md')
$questions = Get-Content -Raw -LiteralPath (Join-Path $projectRoot '05-unresolved-questions.md')
$approval = Get-Content -Raw -LiteralPath (Join-Path $projectRoot 'evidence/gate0-approval-wp1a-authorization.md')
$library = Get-Content -Raw -LiteralPath (Join-Path $projectRoot '06-research-library-index.md')
$checks.gate0Evidence = $approval.Contains('APPROVED WITH CONDITIONS') -and $gates.Contains('APPROVED WITH CONDITIONS')
$checks.q019Closed = $questions.Contains('**Q-019 — Primary architecture-conversation review.** CLOSED')
$checks.q003ReviewPending = $questions.Contains('RESEARCH ANSWER COMPLETE / REVIEW PENDING')
$checks.permanentProvenance = $library.Contains('never represented as a formal platform export') -and $approval.Contains('user-confirmed recovery')
$checks.gate1AStop = $state.Contains('AWAITING REVIEW / NOT APPROVED') -and $state.Contains('WP1B — Target Calculation; NOT AUTHORIZED') -and $state.Contains('next authorized package NONE')
$checks.priorityRule = $report.Contains('Proposed decision rule') -and $report.Contains('Brad and primary review affirm')
$reconcile = Get-Content -Raw -LiteralPath (Join-Path $projectRoot 'wp1a/reviewer-reconciliation.md')
$checks.nineReviewFindings = $true
1..9 | ForEach-Object { if(-not $reconcile.Contains(('W1A-AR{0:D2}' -f $_))){$checks.nineReviewFindings=$false} }
$checks.reviewInputHash = (Get-FileHash -LiteralPath (Join-Path $projectRoot 'evidence/wp1a-claude-review-input.txt')).Hash -eq '3C2242E8A7FCA9551C717425FBFF1DE9B707B89BEF4E619E8913634ACE95970A'
$checks.providerPDFHash = (Get-FileHash -LiteralPath (Join-Path $projectRoot 'evidence/wp1a-trucpi-us-methodology-v1.4.pdf')).Hash -eq 'AA7E491342387F15F24CDD1F1AFB45E1003FD8D22BF8148F1A77F5A1AC4B8567'
$checks.allStableIDs = $true
foreach($spec in @(@{file='02-decision-register.md';pattern='PPU-D\d{3}'},@{file='03-risk-register.md';pattern='R-\d{3}'},@{file='04-active-hypotheses.md';pattern='H-\d{3}'},@{file='05-unresolved-questions.md';pattern='Q-\d{3}'})) {
 $prior = Get-Content -Raw -LiteralPath (Join-Path $projectRoot ('evidence/gate0-approved/' + $spec.file))
 $current = Get-Content -Raw -LiteralPath (Join-Path $projectRoot $spec.file)
 foreach($id in @([regex]::Matches($prior,$spec.pattern).Value | Sort-Object -Unique)){if(-not $current.Contains($id)){$checks.allStableIDs=$false}}
}
$numbers = [ordered]@{lag3=100*([math]::Pow(1.03,0.25)-1);lag10=100*([math]::Pow(1.10,0.25)-1);lag20=100*([math]::Pow(1.20,0.25)-1);shock=100*(1/1.10-1);crossMonth=100*(325.604/324.122-1);global=1.04*0.90}
$checks.arithmetic = [math]::Round($numbers.lag3,3)-eq 0.742 -and [math]::Round($numbers.lag10,3)-eq 2.411 -and [math]::Round($numbers.lag20,3)-eq 4.664 -and [math]::Round($numbers.shock,3)-eq -9.091 -and [math]::Round($numbers.crossMonth,3)-eq 0.457 -and [math]::Abs($numbers.global-0.936)-lt 0.0000001
$checks.statusTextIntegrity=$true
foreach($name in $required + @('README.md')){if((Get-Content -Raw -LiteralPath (Join-Path $projectRoot $name)) -cmatch '\b(Umerica|Wmerica|OOMPLETE|UUTHORIZED|WP0U|SRO-)'){$checks.statusTextIntegrity=$false}}
$failed = @($checks.Keys | Where-Object {-not $checks[$_]})
$result = [ordered]@{checkedAt=(Get-Date).ToString('o');scope='WP1A integrity, not economic certification';checks=$checks;failed=$failed;brokenLocalLinks=$broken;arithmetic=$numbers;gate0='APPROVED WITH CONDITIONS';wp1a='COMPLETE FOR REVIEW';gate1a='AWAITING REVIEW / NOT APPROVED';nextAuthorized='NONE';pass=($failed.Count-eq 0)}
$result | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath (Join-Path $projectRoot 'wp1a/validation.json') -Encoding utf8
$result | ConvertTo-Json -Depth 8
if($failed.Count-gt 0){throw 'WP1A validation failed'}

