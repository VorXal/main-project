#Очищаем экран
Clear-Host

# Head
$Open = 'True'
$Alert = 'False'
$Warning = 0
$MainGateway = 'Your Main Gateway'
$SpareGateway = 'Your Spare Gateway'

# Body
while ($Open -eq 'True') {
    
    # Проверяем доступ в интернет
    Write-Output "Проверка доступности интернета"
    while ($Alert -eq 'False') {
        
        $InternetAccesss = Test-Connection -Count 1 -computer 8.8.8.8 -quiet
        Wait-Event -Timeout 1

        # Если потерян пакет заходим в цикл и добавляем 1 Warning
        if ($InternetAccesss -match 'False') {
            $Warning = $Warning + 1
            Write-Output "Потеряно пакетов $Warning"

            # Считаем кол-во потерянных пакетов
            while ($Warning -ne 0) {
                $InternetAccess = Test-Connection -Count 1 -computer 8.8.8.8 -quiet
                Wait-Event -Timeout 1

                # Если пакет потерян добавляем 1 Warning
                if ($InternetAccess -match 'False') {
                    $Warning = $Warning + 1
                    Write-Output "Потеряно пакетов $Warning "

                    # Если потеряно 10 пакетов, то выходим из цикла проверки доступа и меняем шлюз
                    if ($Warning -eq 10) {
                        $Warning = 0
                        $Alert = "True"
                        Write-Output "Интернет недоступен"
                    }
                }
                # Если хоть один пакет прошел, выходим из цикла подсчета
                else {
                    $Warning = 0
                    Write-Output "Проверка доступности интернета"
                }
            }
        }
    }

    # Записываем текущий шлюз
    $EthernetGate = Get-NetRoute | where {$_.DestinationPrefix -eq '0.0.0.0/0'} | select $_.NextHop

     # Если шлюз равен (Main), то делаем (Spare)
     if ($EthernetGate.NextHop -eq $MainGateway) {
         # Меняем шлюз на другой
         Write-Output("Switch gateway on $SpareGateway")
         Wait-Event -Timeout 30
         # Отправка оповещения на почту?
         $Alert = 'False'
     }

     # Если шлюз равен (Spare), то делаем (Main)
     elseif ($EthernetGate.NextHop -eq $SpareGateway) {
          # Меняем шлюз на другой
          Write-Output("Switch gateway on $MainGateway")
          Wait-Event -Timeout 30
          # Отправка оповещения на почту?
          $Alert = 'False'
        }

        #Иначе указан неверный шлюз
        else {
        Write-Output("Invalid gateway specified")
        Wait-Event -Timeout 30
        # Отправка оповещения на почту?
        $Alert = 'False'
        }
}
