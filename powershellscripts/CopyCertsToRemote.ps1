#Author: Balaji G
#Date : 23 Jan 2020


#Creating a Self-Signed Certificate
New-SelfSignedCertificate -DnsName "mydns" -CertStoreLocation "cert:\LocalMachine\My"

# Credentials for Server
$cred = Get-credential 

#Session for server
$session = New-PSSession -ComputerName 52.165.26.161 -Credential $cred

#Certficate path in local
$certpath = "Cert:\LocalMachine\My"

#Listing all available certs to export the cert by copying thumbprint
Get-ChildItem -Path $certpath 

#Store the copied Thumbprint
$certthumb= "D4EDBCD1A2C9803674A59892C01A45DDB73DFDB2"

#Exact cert to export
$cert = (Get-ChildItem -Path $certpath\$certthumb)

# Exporting cert in .cer format
Export-Certificate -Cert $cert -FilePath "H:\Docs\mycert.cer"

# Copying the cert to remote server therby catching Exceptions
try
{
copy-item -Path "H:\Docs\mycert.cer" -Destination "D:/Docs" -ToSession $session -Recurse
}
catch
{
Write-Output "Error"
} 

