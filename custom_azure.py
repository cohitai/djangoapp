from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'pointcloud1' # Must be replaced by your <storage_account_name>
    account_key = '2+G3qwZZXh13ShcSpoUHxFxj6i/3YYTurFibVeKoVBI6HrwdOHwc2sgEQydY5VTzSwavVRiFrL5Uf5MQSF4oFA==' # Must be replaced by your <storage_account_key>
    azure_container = '1643101965-99733'
    expiration_secs = None

