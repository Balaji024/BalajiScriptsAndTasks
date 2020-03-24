#Author : Balaji G
#Date : 23 Jan 2020

#Registry Values From Remote
 $cred= Get-Credential
Invoke-Command -ComputerName 52.165.26.161 -Credential $cred -ScriptBlock {Get-Item “HKLM:\Software\Microsoft\Windows\CurrentVersion\Run”}

 