# TVC-configuration-manager
A tiny tool that allows you to update all your configuration without going through the GUI. This is an advanced tool that requires to understand what you are doing.

THIS TOOL IS MODIFYING THE DATABASE DIRECTLY AND CAN MESS UP YOUR TVC CONFIGURATION. USE IT AT YOUR OWN RISK
## Usage
Download the script from the latest [release](https://github.com/triat/TVC-configuration-manager/releases) and place it anywhere in your TVC server.

Execute the script with the parameters you want `./TVC_CM ...` and this should be it.

Depending on the rights you have on your system, you might need to allow your script to be run. Use the command `sudo chmod 755 TVC_CM`.

## Parameters
You can find all the parameters using `./TVC_CM --help`

## Database configuration
This list is not an official list from TVC and can contains old fields. If this is the case, please open [an issue](https://github.com/triat/TVC-configuration-manager/issues) or report to Biwaa#7257 (Discord)

```
|+--------------------+---------------+------+-----+---------+--------------+|
| Field              | Type          | Null | Key | Default | Extra          |
|+--------------------+---------------+------+-----+---------+--------------+|
| ID                 | int           | NO   | PRI | NULL    | auto_increment |
| Enabled            | tinyint(1)    | YES  |     | 1       |                |
| Exchange           | varchar(255)  | NO   | MUL | NULL    |                |
| Username           | varchar(255)  | NO   | MUL | NULL    |                |
| Symbol             | varchar(31)   | NO   |     | NULL    |                |
| Side               | varchar(31)   | NO   |     | NULL    |                |
| BaseSize           | decimal(13,8) | NO   |     | NULL    |                |
| BaseSizeType       | varchar(15)   | NO   | MUL | NULL    |                |
| SafetyBaseSize     | decimal(13,8) | NO   |     | NULL    |                |
| SafetyBaseSizeType | varchar(15)   | NO   |     | NULL    |                |
| EntryType          | varchar(15)   | NO   | MUL | NULL    |                |
| Leverage           | varchar(31)   | NO   |     | NULL    |                |
| CrossLeverage      | tinyint(1)    | NO   |     | NULL    |                |
| UseTakeProfit      | tinyint(1)    | YES  |     | 0       |                |
| TakeProfitDistance | decimal(5,2)  | YES  |     | NULL    |                |
| UseStoploss        | tinyint(1)    | YES  |     | 0       |                |
| StoplossDistance   | decimal(5,2)  | YES  |     | NULL    |                |
| TakeProfitTrailing | tinyint(1)    | YES  |     | 0       |                |
| TakeProfitTrail    | decimal(4,2)  | NO   |     | NULL    |                |
| UseDCA             | tinyint(1)    | YES  |     | 0       |                |
| ManualDCA          | tinyint(1)    | YES  |     | 0       |                |
| DCACount           | int           | YES  |     | NULL    |                |
| DCADeviation       | decimal(5,2)  | YES  |     | NULL    |                |
| DCAVolumeScale     | decimal(4,2)  | YES  |     | NULL    |                |
| DCAStepScale       | decimal(4,2)  | YES  |     | NULL    |                |
|+--------------------+---------------+------+-----+---------+--------------+|
```

# Support
If you like my work and want to support me

- USDT (BEP20): 0xDF978Cdc19d603525d6BCC065106Bdcb7B50CaAE
- BTC: 13kiZ8JXV7yYShrzTzNarmJywp1UnXjKCP
- USDT/ETH (ERC20): 0xDF978Cdc19d603525d6BCC065106Bdcb7B50CaAE

Thank you!
