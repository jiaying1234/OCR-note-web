# OCR-note-web
 Convert your images to text
# 概述

基於 Flask + Pytesseract + TextBlob 開發的圖片轉文字網站，實現了圖片上傳、OCR 字符識別和簡單的自然語言處理，前端使用 HTML、CSS、JavaScript 來構建和處理用戶界面。

# 環境配置

開發環境：Windows 10　，　Visual Studio Code

# 運行步驟：

1.安裝必要的依賴

`pip install Flask pytesseract pillow textblob`

2.運行 Flask 應用

`python app.py`

3.確保本地建立了 uploads 資料夾來儲存上傳的圖片。

*****

 
# 初始介面

![image](https://github.com/user-attachments/assets/32d1670a-6204-4ab1-b593-e059b6d71239)

# 創建筆記介面

上傳圖片即可轉文字(可編輯文字)

![image](https://github.com/user-attachments/assets/89664b0e-9889-4681-9249-42c9708f2b93)

![image](https://github.com/user-attachments/assets/fc9c1214-d384-483c-adcf-68d5265a6fdf)


# 查看筆記介面(可編輯或刪除文字)

![image](https://github.com/user-attachments/assets/bd14b217-af11-4dfb-b0f3-76bb1739de50)
