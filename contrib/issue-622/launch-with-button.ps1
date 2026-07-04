# Start helper + GitHub Copilot with in-app Open on GitHub button (issue #622).
param(
  [int]$CdpPort = 9333,
  [int]$HelperPort = 19622,
  [switch]$ForceRestart
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
$Py = Join-Path $Root "open-repo-on-github.py"
$Inject = Join-Path $Root "inject\cdp-inject.py"
$App = Join-Path $env:LOCALAPPDATA "Programs\GitHub Copilot\github.exe"

function Test-PortListening([int]$Port) {
  try {
    $c = New-Object System.Net.Sockets.TcpClient("127.0.0.1", $Port)
    $c.Close()
    return $true
  } catch { return $false }
}

function Test-CdpReady([int]$Port) {
  try {
    $r = Invoke-RestMethod -Uri "http://127.0.0.1:$Port/json/list" -TimeoutSec 2
    return ($null -ne $r)
  } catch { return $false }
}

if (-not (Test-PortListening $HelperPort)) {
  Start-Process -WindowStyle Hidden python3 -ArgumentList @($Py, "serve", "--port", $HelperPort)
  for ($i = 0; $i -lt 20; $i++) {
    if (Test-PortListening $HelperPort) { break }
    Start-Sleep -Milliseconds 250
  }
}

$env:WEBVIEW2_ADDITIONAL_BROWSER_ARGUMENTS = "--remote-debugging-port=$CdpPort"
if (-not (Test-Path $App)) { throw "GitHub Copilot not found: $App" }

$needsRestart = $ForceRestart -or -not (Test-CdpReady $CdpPort)
if ($needsRestart) {
  Get-Process -Name "github" -ErrorAction SilentlyContinue | Stop-Process -Force
  Start-Sleep -Seconds 2
  Start-Process $App
  for ($i = 0; $i -lt 40; $i++) {
    if (Test-CdpReady $CdpPort) { break }
    Start-Sleep -Milliseconds 500
  }
}

if (-not (Test-CdpReady $CdpPort)) {
  Write-Error "CDP not available on port $CdpPort. Close GitHub Copilot and re-run."
}

python3 $Inject $CdpPort
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
Write-Host "Open on GitHub button injected (helper :$HelperPort, CDP :$CdpPort)."
