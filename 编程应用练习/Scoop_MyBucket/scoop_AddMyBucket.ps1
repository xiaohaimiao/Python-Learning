# 检查是否已安装 Scoop
if (!(Test-Path $env:USERPROFILE\scoop)) {
    # 如果未安装 Scoop，则执行安装
    Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')
}

# 添加本地 _MyBucket_
$currentDir = (Get-Location).Path # 获取当前脚本所在目录
scoop bucket add MyBucket $currentDir\_MyBucket_

# 安装 packages.txt 指定的包
$packages = Get-Content "$currentDir\packages.txt"
foreach ($package in $packages) {
    scoop install $package
}