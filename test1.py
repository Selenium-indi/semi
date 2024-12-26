# 필요한 라이브러리 임포트
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager

# def setup_driver():
#     try:
#         # 브라우저 옵션 설정
#         chrome_options = Options()
#         chrome_options.add_experimental_option("detach", True)
        
#         # 크롬 드라이버 설정
#         service = Service(ChromeDriverManager().install())
        
#         # 드라이버 생성
#         driver = webdriver.Chrome(service=service, options=chrome_options)
        
#         return driver
    
#     except Exception as e:
#         print(f"드라이버 설정 중 오류 발생: {e}")
#         return None

# def main():
#     # 드라이버 설정
#     driver = setup_driver()
    
#     if driver is None:
#         print("드라이버 초기화 실패")
#         return
    
#     try:
#         # 페이지 로딩 대기 시간 설정
#         driver.implicitly_wait(10)
        
#         # 올리브영 접속
#         driver.get("https://www.oliveyoung.co.kr/store/main/main.do")
        
#         # 명시적 대기 설정
#         wait = WebDriverWait(driver, 10)
        
#         # 검색창 찾기 및 검색어 입력
#         search_box = wait.until(EC.presence_of_element_located((By.ID, "query")))
#         search_keyword = "선크림"
#         search_box.clear()
#         search_box.send_keys(search_keyword)
    
        
#             # Enter 키를 눌러 검색
#     search_box.send_keys(Keys.RETURN)
        
#     except Exception as e:
#         print(f"실행 중 오류 발생: {e}")
    
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    try:
        # 브라우저 옵션 설정
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        
        # 크롬 드라이버 설정
        service = Service(ChromeDriverManager().install())
        
        # 드라이버 생성
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        return driver
    
    except Exception as e:
        print(f"드라이버 설정 중 오류 발생: {e}")
        return None

def main():
    # 드라이버 설정
    driver = setup_driver()
    
    if driver is None:
        print("드라이버 초기화 실패")
        return
    
    try:
        # 페이지 로딩 대기 시간 설정
        driver.implicitly_wait(10)
        
        # 올리브영 접속
        driver.get("https://www.oliveyoung.co.kr/store/main/main.do")
        
        # 명시적 대기 설정
        wait = WebDriverWait(driver, 10)
        
        # 검색창 찾기 및 검색어 입력
        search_box = wait.until(EC.presence_of_element_located((By.ID, "query")))
        search_keyword = "선크림"  # 원하는 검색어로 변경 가능
        search_box.clear()
        search_box.send_keys(search_keyword)
        
        # Enter 키로 검색 실행
        search_box.send_keys(Keys.RETURN)
        
    except Exception as e:
        print(f"실행 중 오류 발생: {e}")
    
if __name__ == "__main__":
    main()