#Author: Balaji.G (50777)
#date: Jan 23 2020


# Installing PsExcel Module
Install-Module PSExcel

# Importing PSExcel Module
Import-Module PSExcel

# Path of the file to be filtered
$path = "H:\Assignments\Assignments\FirstFlight.xlsx"

# Importing Excel file
$import = Import-XLSX -Path $path

# Showing Result
$import 

#Column name
$column = "SCM"

#Respective Rows for separation
$value  = "TFS"
$value1 = "TFS (1 team project)"
$value2 = "TFS-GIT"
$value3 = "TFS-GIT (1 team project if common code base)"

#FileOutputs
#$save= Read-Host "Enter the path"

# Sorting the value & Storing file
$import | Where-Object {$_.$column -eq $value} | Export-XLSX  -path  "H:\Docs\TFS.XLSX"
$import | Where-Object {$_.$column -eq $value1} | Export-XLSX -Path "H:\Docs\TFS (1 team project).XLSX"
$import | Where-Object {$_.$column -eq $value2} | Export-XLSX -Path "H:\Docs\TFS-GIT.XLSX"
$import | Where-Object {$_.$column -eq $value3} | Export-XLSX -Path "H:\Docs\TFS-GIT (1 team project if common code base).XLSX"