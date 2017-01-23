from appium import webdriver
import time
import os
import pdb

success = True
desired_caps = {}
desired_caps['platformName'] = 'android'
desired_caps['platformVersion'] = '5.1.1'
# desired_caps['udid'] = '330023539faf2357'
desired_caps['deviceName'] = '330023539faf2357'
desired_caps['appActivity'] = 'ui.signin.SignInActivity'
desired_caps['appPackage'] = 'com.treeboxsolutions.ontalk.flash'
desired_caps['newCommandTimeout'] = '3000'
desired_caps['noReset'] = 'true'
# desired_caps['app'] = '/Users/jerryzhao/Dropbox/Treebox/automate-tests/ontalk.auto.parallel/app/OnTalk.apk'

# desired_caps['bundleId'] = 'com.apple.Preferences'
# desired_caps['xcodeConfigFile'] = '/usr/local/lib/node_modules/appium-xcuitest-driver/myconfig.xcconfig'

wd = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
