# OrangeHRM
Test project for testing technical skills

###Running Test Case:
It is to go to Project Home Folder `OrangeHRM`

(Using Allure) `behave -f allure_behave.formatter:AllureFormatter -o allure/results .\Tests\Test_Scenarios\ -D browser=chrome`

(Using behave) `behave .\Tests\Test_Scenarios\Login.feature -D browser=chrome`

Where Browser can be either `chrome` or `edge` or `firefox`. 

It should support both Windows & Mac (Project is only tested on Win10)

###Test Data
There is an file in Project Folder > Lib > `Test_Data.txt`

This is an `Comma (,)` separated file which has 3 columns
1. Username 
2. Password
3. Result: Which determines if the combination of both is valid or not

##For Generating Report: 
One needs to have Allure installed locally. 


Steps to install Allure: https://docs.qameta.io/allure/#_installing_a_commandline

After running Test Case, User needs to run `allure serve .\allure\results\` for generating & displaying report


###Known Issue
1. Allure is not reporting trend correctly, as it works best with CI / CD
2. TestData driven test cases are not properly captured in Allure as it is counting test scenario results (Need more time to debug this)
