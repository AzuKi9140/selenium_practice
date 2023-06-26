import datetime
import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from src.create_directory import create_directory_if_not_exists

load_dotenv()


def screenshot(date: datetime):
    """スクリーンショットを撮影する

    Args:
        date (datetime): 現在の日付

    Returns:
        None
    """

    # Chromeを起動
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # 指定したURLに遷移する
    driver.get(
        "https://www.data.jma.go.jp/obd/stats/data/mdrr/tem_rct/index_mxtem.html"
    )

    # 拡大ボタンを1回目クリック
    element = driver.find_element(By.CSS_SELECTOR, "#plusbutton")
    element.click()

    # 2回目のクリック前に要素を再取得
    element = driver.find_element(By.CSS_SELECTOR, "#plusbutton")
    element.click()

    # background-positionの値を設定
    x_position = os.getenv("X_POSITION")
    y_position = os.getenv("Y_POSITION")

    script = f"""
    var element = document.getElementById('pic2');
    element.style.backgroundPosition = '{x_position}px {y_position}px';
    """
    driver.execute_script(script)

    # スクリーンショットを撮影
    if os.getenv("SCREENSHOT"):
        wait = WebDriverWait(driver, 10)
        element = wait.until(
            expected_conditions.visibility_of_element_located(
                (By.CSS_SELECTOR, "#pic2")
            )
        )

        element = driver.find_element(By.CSS_SELECTOR, "#pic2")

        # 保存先のディレクトリを作成
        directory = create_directory_if_not_exists(date)
        hour = date.strftime("%H")
        file_path = os.path.join(directory, f"{hour}_screenshot.png")
        print(file_path)
        element.screenshot(file_path)
        print(f"{date}_screenshot.pngを保存しました。")
