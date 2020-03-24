#Author: BalajiG (50777)
#Date: Jan 23 2020 


#Adding Server ip in TrustedHosts file
Set-Item WSMan:localhost\client\trustedhosts -value 52.165.26.161

#Enabling Psremoting Thereby starting WinRm Service
Enable-PSRemoting -SkipNetworkProfileCheck -Force

#To allow psremoting within and out of subnet
Set-NetFirewallRule -name "WINRM-HTTP-In-TCP" -RemoteAddress Any

#For Azure Vm
#NSG should allow Inbound to 5985 and 5986. 

#Saving the credentials of server in variable
$cred = Get-Credential 

# Creating a session with the server
$session = New-PSSession -ComputerName 52.165.26.161 -Credential $cred

#Excluding MVCProj.csproj.Vspcc file  and Copying folders to Server

$Exclude = "H:\Assignments\Assignments\MVCProj\MVCProj\MVCProj.csproj.vspscc"
Copy-Item -Path "H:\Assignments\Assignments\MVCProj" -Destination "D:/Docs" -Exclude $Exclude -ToSession $session -Recurse 



