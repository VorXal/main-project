[Console]::OutputEncoding = [System.Text.Encoding]::GetEncoding('cp866')
Clear-Host

# Если в записи ipconfig'а присутсвует надпись "Аренда получена" => IP Динамический
$check_static_ip = ipconfig /all | out-String
$check_static_ip = $check_static_ip.Contains('Аренда получена')
if ($check_static_ip -eq 'True') {
    Write-Output "IP динамический"
}
else {
    Write-Output "IP статический"
}
