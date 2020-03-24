#Author: Balaji G
#Date: 24 Jan 2020 

#Installing IIS

Install-WindowsFeature Web-server,Web-Asp-Net45,NET-Framework-Features


# Install the .NET Core SDK
Invoke-WebRequest https://go.microsoft.com/fwlink/?linkid=848827 -outfile $env:temp\dotnet-dev-win-x64.1.0.6.exe
Start-Process $env:temp\dotnet-dev-win-x64.1.0.6.exe -ArgumentList '/quiet' -Wait


## Install the .NET Core Windows Server Hosting bundle
Invoke-WebRequest https://go.microsoft.com/fwlink/?LinkId=817246 -outfile $env:temp\DotNetCore.WindowsHosting.exe
Start-Process $env:temp\DotNetCore.WindowsHosting.exe -ArgumentList '/quiet' -Wait


# Restart the web server so that system PATH updates take effect
Stop-Service was -Force
Start-Service w3svc