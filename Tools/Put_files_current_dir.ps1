param([String]$port="COM7") #Get Port param
# Close MobaXterm process
# Get-Process MobaXterm | Foreach-Object { $_.CloseMainWindow() | Out-Null } | stop-process –force


$files = Get-ChildItem
foreach ($f in $files){
    ampy --port $port put $f
}
# Open powershell
#Start-Process -FilePath "C:\Program Files (x86)\Mobatek\MobaXterm\MobaXterm.exe"