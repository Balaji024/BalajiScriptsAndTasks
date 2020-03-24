try{
    New-NetFirewallRule -DisplayName "WinRM_HTTPS" -Direction Inbound -Action Allow -EdgeTraversalPolicy Allow -Protocol TCP -LocalPort 5986    
}
catch
{
Write-outpu "Operation Failed Sorry"
}


