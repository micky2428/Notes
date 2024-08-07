# [筆記]Clean Code_chap. 1 無暇的程式碼

:::info 
:bulb: 「怎麼樣能讓自己的程式碼寫得越來越好」、「怎麼樣的程式碼可以跟別人合作愉快」，這是在成為軟體工程師的路上，出現的疑問，於是找到了這本書。
:::


## :+1: 章節重點

### :small_blue_diamond: Clean Code 的定義


## 🖊️  什麼是Clean Code

本書作者認為讓開發速度變快的唯一方法是「**隨時隨地**確保程式碼**整齊潔淨**」。

作者彙整了他請教的工程師所提出的定義，並把本書界定為**整潔程式碼之物件學派**，將他對Clean Code的定義，包含怎樣才算是整潔的變數名稱、函式、類別，寫成這本書的內容。

(一) C++發明人Bjarne Stroustrup的定義
 1. 邏輯直接瞭當，錯誤無處可躲。盡量降低程式的相依性，以減輕維護的功夫...盡可能最佳化程式效能...Clean Code只做好一件事。
 2. 此外，處理錯誤的程式碼必須完備，避免記憶體流失(memory leak)、競爭情況(race conditions)、不一致的命名方式等。
 
 --> 顯現了Clean Code對於**細節**的在意


(二) Eclipse策略教父Dave Thomos的定義
 1. Clean Code是可以被原作者以外的開發者閱讀與增強的。他應當包含單元測試與驗收測試...應該只提供一種而非多種途徑來完成某項任務...應藉由明確地定義，並提供清楚而盡可能少一點的API，以盡量減少相依性。
 
 --> 顯現了Clean Code對於**可讀性**的在意
 
 (三) Ron Jeffries
 1. Clean Code的特質包含
 - 能通過所有測試
 - 沒有重複的程式碼
 - 充分表達系統設計的構思
 - 具有最少數量的實體(entities)，所謂實體如類別、方法、函式等。
 
 --> 顯現了Clean Code對於**可讀性**的在意

## 🖊️  雜亂程式碼的代價
1. 作者認為儘管開發團隊在開發初期時發展迅速，然而，在一兩年後，會發現發展速度如蝸牛。這是因為每次修改都會讓程式分裂成兩塊或三塊，產生更多混亂。
2. 為了修補混亂，公司會僱用更多員工，但是新的員工對於系統設計不熟，在面臨產能壓力下，又製造更多雜亂的程式碼，最終，在團隊反抗下，老闆即便同意打造新的系統，但在新舊系統接軌期間已經過很長的時間，又可能面臨人員更換，要求再重新設計系統。

## 🖊️  本書會提到的原則
作者表示，在本書他會使用到他另一本探討物件導向設計原則的著作PPP中所提到的原則，包含單一職責原則(SRP)、開放封閉原則(OCP)、相依性反向原則(DIP)。

※註:在單元測試的藝術第三章提到接縫概念時(p.65)有提到OCP原則，類別的功能開放擴充彈性，但不允許直接修改該功能內實作的程式碼。

## 🤔 疑問

#### 1.什麼是競爭情況(race conditions)?  
Ans: Race Conditions 出現的條件包含(1)平行處理、(2)對同一個資源同時進行存取操作，最終可能導致結果是不正確的。

※參考:[後端工程師面試考什麼](https://myapollo.com.tw/blog/interview-question-race-condition/)、周志遠教授作業系統OCW

#### 2.什麼是相依性反向原則(DIP)?  
Ans: 相依性反向原則指的是原始碼的依賴關係應只涉及**抽象**而不涉及具體。抽象通常指的是介面(Interface)及抽象類別(Abstract Class)，也就是如何讓系統依賴性降至最低。

#### 3.什麼是Eclipse?
Ans: Eclipse是一套開放原始碼(Open Source)的整合開發環境(IDE,Integrated Development Environment)，可用來編輯、編譯、執行和除錯特定語言的程式。


## 📖 下一章節主題預告
        
在了解基本定義後，下一章要談的是有意義的命名。