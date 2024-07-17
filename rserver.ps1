Stop-Service -DisplayName "odoo-server-17.0"
Remove-Item -Path 'C:\Program Files\Odoo\server\odoo.log'
Start-Service -DisplayName "odoo-server-17.0"