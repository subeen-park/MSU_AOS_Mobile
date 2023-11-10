import unittest
import os
import time
from unittest import suite
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import subprocess


from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.mobileby import MobileBy as AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
import time
import pyperclip
import pyautogui
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.keys import Keys
from appium.webdriver.extensions.android.nativekey import AndroidKey
import subprocess


import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class TableSearchTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4001/wd/hub',
            desired_capabilities={
                "platformName": "Android",
                "appium:platformVersion": "10.0.0",
                "appium:deviceName": "SM-G965N",
                "appium:app": "D:\Appium_Github\MSU_AOS_Mobile\Appium\\io.metamask_7.9.0.apk",
                "appium:udid": "21d9b36401037ece",
                "appium:automationName" : "UIAutomator2",
                'newCommandTimeout' : '300'
            })

    def test_addToAsset(self):
        driver = self.driver
       # driver.get("https://qa.nexpace.io/msu-market")
        wait = WebDriverWait(driver, 300)

        
        


    
        print("test_addToAsset1 시작")
        time.sleep(7)
        driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"시작하기\"]").click()
        print("test_addToAsset1 종료")

        wait.until(EC.visibility_of_element_located((By.XPATH, '//android.widget.TextView[@text=\"비밀복구구문을 활용해 가져오기\"]')))
        driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"비밀복구구문을 활용해 가져오기\"]").click()
        time.sleep(1)

        
        driver.swipe(470, 1400, 470, 950, 100) # 스크롤 다운 (start_x, start_y, end_x, end_y, duration)
        

        driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"동의합니다\"]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//android.view.ViewGroup[@resource-id=\"terms-of-use-scroll-end-arrow-button-id\"]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"본인은 MetaMask의 사용과 관련 모든 기능에 적용되는 이용약관에 동의합니다\"]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"수락\"]").click()
        time.sleep(1)


        ####### 메타 마스크 비밀번호 설정 과정 #######
        # 비밀번호 복구 구문 입력, 
        meta_login_seed = driver.find_element(By.XPATH, "//android.widget.EditText[@resource-id=\"import-from-seed-screen-seed-phrase-input-id\"]")
        meta_login_seed.send_keys("dove fetch photo mouse brain way rookie actress undo kiss cat differ")
        #비밀번호
        meta_login_password = driver.find_element(By.XPATH, "//android.widget.EditText[@resource-id=\"create-password-first-input-field\"]")
        meta_login_password.send_keys("1234qwer")
        #컨펌
        meta_login_password2 = driver.find_element(By.XPATH, value="//android.widget.EditText[@resource-id=\"create-password-second-input-field\"]")
        meta_login_password2.send_keys("1234qwer")
        driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"가져오기\"]").click()

        


        ###### 거래소 진입 ######
        wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text=\"괜찮습니다\"]')))
        driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"괜찮습니다\"]").click()

        

        wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text=\"아니요, 괜찮습니다\"]')))
        driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"아니요, 괜찮습니다\"]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//android.view.ViewGroup[@resource-id=\"tab-bar-item-Browser\"]/android.view.ViewGroup/android.view.ViewGroup").click()
        time.sleep(3)




      

        driver.find_element(By.XPATH, "//android.widget.EditText").click() # URL 입력창 클릭
        time.sleep(2)                                  
        url_input = driver.find_element(By.XPATH, value="//android.widget.EditText[@resource-id=\"url-input\"]")
        url_input.send_keys("https://qa.nexpace.io/msu-market")
        time.sleep(1)


        

        
        driver.find_element(By.XPATH, "//android.widget.FrameLayout[@resource-id=\"android:id/content\"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.view.ViewGroup[1]").click()

        #cmd_path = r"D:\Appium_Metamask\Appium_run.cmd"
        #p = subprocess.Popen(cmd_path, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) 
        #p.stdin.write(b"input keyevent 66\n")
        #p.stdin.write(b'sleep 6\n')
        #p.stdin.flush()
        #out, err = p.communicate()
        time.sleep(6)


        ## test_addToAsset3
        print("test_addToAsset3 시작")
        ###### 페이지 진입 후 로그인 #######
        driver.find_element(By.XPATH, "//android.widget.Button").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//android.view.View[@resource-id=\"__next\"]/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View").click() #login 버튼
        time.sleep(1)
        print("로그인 버튼 클릭 완료 후 continue with metamask 버튼 누르기 전.")
        

        ### 메타마스크 연결 ###
        time.sleep(2) # continue with metamask~
        cmd_path = r"D:\Appium_Github\MSU_AOS_Mobile\Appium_run.cmd"
        p = subprocess.Popen(cmd_path, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) 
        p.stdin.write(b"input keyevent 61\n") #tab
        p.stdin.write(b"input keyevent 66\n") #enter
        p.stdin.write(b'sleep 3\n')
        p.stdin.flush()  
        out, err = p.communicate()


        driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"연결\"]").click() # 연결
        time.sleep(3) 
        driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"서명\"]").click() # 서명 
        time.sleep(2)
        driver.find_element(By.XPATH, "//android.widget.Button[@text=\"Switch network\"]").click() # 네트워크 전환
        time.sleep(5)

        driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"승인\"]").click() # 승인
        time.sleep(3)
        driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"네트워크 변경\"]").click() # Switch Networks
        time.sleep(2)
        driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"컨펌\"]").click() # 컨펌
        time.sleep(3)
        print("메타마스크 연결완료")





        ### NFT 아이템 판매 진행 ###
        cmd_path = r"D:\Appium_Github\MSU_AOS_Mobile\Appium_run.cmd"
        p = subprocess.Popen(cmd_path, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) 
        p.stdin.write(b"input keyevent 61\n") #tab // 메뉴 진입
        p.stdin.write(b"input keyevent 61\n") #tab
        p.stdin.write(b"input keyevent 61\n") #tab
        p.stdin.write(b"input keyevent 66\n") #enter
        p.stdin.write(b'sleep 3\n')

        p.stdin.write(b"input keyevent 61\n") #tab // 인벤토리 진입
        p.stdin.write(b"input keyevent 61\n") #tab
        p.stdin.write(b"input keyevent 61\n") #tab
        p.stdin.write(b"input keyevent 61\n") #tab
        p.stdin.write(b"input keyevent 66\n") #enter
        p.stdin.write(b'sleep 3\n')


        p.stdin.write(b"input keyevent 61\n") #tab // NFT 아이템 상세페이지 진입
        p.stdin.write(b"input keyevent 61\n") #tab
        p.stdin.write(b"input keyevent 61\n") #tab
        p.stdin.write(b"input keyevent 61\n") #tab
        p.stdin.write(b"input keyevent 61\n") #tab
        p.stdin.write(b"input keyevent 61\n") #tab
        p.stdin.write(b"input keyevent 61\n") #tab
        p.stdin.write(b"input keyevent 61\n") #tab
        p.stdin.write(b"input keyevent 61\n") #tab
        p.stdin.write(b"input keyevent 66\n") #enter
        p.stdin.write(b'sleep 3\n')
        p.stdin.write(b"input keyevent 93\n") #PageDown
        p.stdin.write(b'sleep 1\n')
        p.stdin.flush()  
        out, err = p.communicate()

        time.sleep(1)
        driver.find_element(By.XPATH, "//android.widget.Button[@text=\"Sell\"]").click() # 판매

        cmd_path = r"D:\Appium_Github\MSU_AOS_Mobile\Appium_run.cmd"
        p = subprocess.Popen(cmd_path, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        p.stdin.write(b'sleep 1\n') 
        p.stdin.write(b"input keyevent 61\n") #tab // 가격기입
        p.stdin.write(b"input keyevent 8\n") # 1
        p.stdin.write(b"input keyevent 7\n") # 0
        p.stdin.write(b"input keyevent 7\n") # 0
        p.stdin.write(b"input keyevent 7\n") # 0
        p.stdin.write(b"input keyevent 7\n") # 0
        p.stdin.write(b"input keyevent 7\n") # 0
        p.stdin.write(b"input keyevent 66\n") #enter
        p.stdin.write(b'sleep 1\n')
        p.stdin.flush()  
        out, err = p.communicate()

        time.sleep(1)
        driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"서명\"]").click() # 서명
        cmd_path = r"D:\Appium_Github\MSU_AOS_Mobile\Appium_run.cmd"
        p = subprocess.Popen(cmd_path, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        p.stdin.write(b'sleep 0.5\n') 
        p.stdin.write(b"input keyevent 111\n") #인벤토리로 돌아옴
        p.stdin.flush()  
        out, err = p.communicate()
        print("NFT 아이템 판매 완료")




        ### 인벤토리 > 캐릭터 필터 선택 > 캐릭터 판매 ###

        cmd_path = r"D:\Appium_Github\MSU_AOS_Mobile\Appium_run.cmd"
        p = subprocess.Popen(cmd_path, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) 
        p.stdin.write(b"input keyevent 20\n") # down
        p.stdin.write(b"input keyevent 20\n") # down
        p.stdin.write(b"input keyevent 20\n") # down
        p.stdin.write(b"input keyevent 20\n") # down
        p.stdin.write(b"input keyevent 20\n") # down
        p.stdin.write(b"input keyevent 61\n") # tab
        p.stdin.write(b"input keyevent 66\n") # enter
        p.stdin.write(b"input keyevent 61\n") # tab // 필터 진입
        p.stdin.write(b"input keyevent 61\n") # tab
        p.stdin.write(b"input keyevent 66\n") # enter
        p.stdin.write(b"input keyevent 20\n") # down
        p.stdin.write(b"input keyevent 66\n") # enter
        p.stdin.write(b"input keyevent 61\n") # tab 
        p.stdin.write(b"input keyevent 61\n") # tab
        p.stdin.write(b"input keyevent 61\n") # tab
        p.stdin.write(b"input keyevent 61\n") # tab
        p.stdin.write(b"input keyevent 66\n") # enter
        p.stdin.write(b"input keyevent 61\n") # tab // 캐릭터 판매
        p.stdin.write(b"input keyevent 66\n") # enter
        p.stdin.write(b"input keyevent 93\n") #PageDown
        p.stdin.write(b'sleep 1\n')
        p.stdin.flush()  
        out, err = p.communicate()

        time.sleep(1)
        driver.find_element(By.XPATH, "//android.widget.Button[@text=\"Sell\"]").click() # 판매
        time.sleep(1)

        cmd_path = r"D:\Appium_Github\MSU_AOS_Mobile\Appium_run.cmd"
        p = subprocess.Popen(cmd_path, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) 
        p.stdin.write(b'sleep 1\n') 
        p.stdin.write(b"input keyevent 61\n") #tab // 가격기입
        p.stdin.write(b"input keyevent 8\n") # 1
        p.stdin.write(b"input keyevent 7\n") # 0
        p.stdin.write(b"input keyevent 7\n") # 0
        p.stdin.write(b"input keyevent 7\n") # 0
        p.stdin.write(b"input keyevent 7\n") # 0
        p.stdin.write(b"input keyevent 7\n") # 0
        p.stdin.write(b"input keyevent 66\n") #enter
        p.stdin.write(b'sleep 1\n')
        p.stdin.flush()  
        out, err = p.communicate()

        time.sleep(1)
        driver.find_element(By.XPATH, "//android.widget.TextView[@text=\"서명\"]").click() # 서명
        cmd_path = r"D:\Appium_Github\MSU_AOS_Mobile\Appium_run.cmd"
        p = subprocess.Popen(cmd_path, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        p.stdin.write(b'sleep 0.5\n') 
        p.stdin.write(b"input keyevent 111\n") #인벤토리로 돌아옴
        p.stdin.flush()  
        out, err = p.communicate()
        print("캐릭터 판매 완료")















    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TableSearchTest)
    unittest.TextTestRunner(verbosity=2).run(suite)