#Author: Balaji G
#date: 27 JAN 2020.


# Capturing Starting seconds and minutes
$start = (Get-Date).Second
$start1 = (Get-Date).Minute

# Path of template.json file
$templateFilePath = "G:\ArmTemplates\Windows2016Datacenter-IIS\Win-IIS\CSIIStemp.json"

#Path of Parameter.json file
$parametersFilePath = "G:\ArmTemplates\Windows2016Datacenter-IIS\Win-IIS\CSIISparam.json"

#Subscription ID
$subscription = "#######-####-####-####-#######b315"

#ResourceGroupName
$resourceGroupName = "balajiresources"

#ResourceGroupLocation
$resourceGroupLocation = "centralus"

#DeploymentName
$deploymentName = "Mywin-iis3"

# Logging in Azure 
Write-Host "Logging in...";
Login-AzureRmAccount

#Selecting Subscription
Write-Host "Selecting subscription '$subscription'";
Select-AzureRmSubscription -SubscriptionID $subscription;

#Create or check for existing resource group
$resourceGroup = Get-AzureRmResourceGroup
if(!$resourceGroup)
{
      $resourceGroupLocation = Read-Host "resourceGroupLocation";
      Write-Host "Creating resource group '$resourceGroupName' in location '$resourceGroupLocation'";
     New-AzureRmResourceGroup -Name $resourceGroupName -Location $resourceGroupLocation
     New-AzureRmResourceGroupDeployment -ResourceGroup $resourceGroupName -Name MyIISDeploy -TemplateParameterFile $parametersFilePath -TemplateFile $templateFilePath -Verbose
}
else{
    Write-Host "Using existing resource group '$resourceGroupName'";
}

# Starting the deployment
Write-Host "Starting deployment...";
New-AzureRmResourceGroupDeployment -ResourceGroupName balajiresources -TemplateFile $templateFilePath -TemplateParameterFile $parametersFilePath  -Verbose

# Capturing the End Second and Minutes of the Script
$End = (Get-Date).Second
$End1 = (Get-Date).Minute

# Calculating Script Runtime and saving in logfile
$scriptDuration = Write-Host "The deployments of Windows 2016 Datacenter with pre installed IIS took $($End1 - $start1) Minutes and $($End - $start) seconds" 
Out-file -InputObject $scriptDuration "D:\Log Book\ARM DEPLOYMENTS/log.txt"



