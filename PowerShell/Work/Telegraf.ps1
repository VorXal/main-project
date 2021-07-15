##
#  Смотрит есть ли Telegraf вообще в списке сервисов, если он есть, то:
#  Ищет его среди списка ЗАПУЩЕННЫХ сервисов
#  Если его там нет, то пытается запустить
#  Повторно проверяет запущен ли Telegraf
#  Если снова нет, то ... ничего не делает, а мог бы
##

$Telegraf = Get-Service | Out-String
if ($Telegraf -match "Telegraf") {
    $Telegraf = Get-Service | Where-Object {$_.Status -EQ "Running"} | Out-String
        if ($Telegraf -notmatch "Telegraf") {
        Write-Output "Telegraf not running, trying run..."
        Start-Service Telegraf
        $Telegraf = Get-Service | Where-Object {$_.Status -EQ "Running"} | Out-String
        if ($Telegraf -notmatch "Telegraf") {
            Write-Output "Success! Telegraf running."
        }
        else {
            # Оповещение на почту?
            Write-Output "Failure! Something went wrong..."
        }
    }
    else {
        Write-Output "Telegraf running!"
    }
}
else {
    Write-Output "Telegraf not found!"
}
