---
title: '[筆記]Clean Code_chap. 5 編排'

---

# [筆記]Clean Code_chap. 5 編排

:::info 
:bulb: 「怎麼樣能讓自己的程式碼寫得越來越好」、「怎麼樣的程式碼可以跟別人合作愉快」，這是在成為軟體工程師的路上，出現的疑問，於是找到了這本書。
:::


## :+1: 章節重點

### :small_blue_diamond: 垂直編排的重點
### :small_blue_diamond: 水平編排的重點


## 🖊️  垂直編排的重點

本書作者十分強調程式碼的**可讀性**，並提醒若是團隊工作，需要有**統一的編排規則**，之後讓**自動化工具**來利用規則協助處理程式的編排。
接著，他從垂直編排的重點開始講起。

(一) 由上而下

原始檔內容應該參考報紙的寫法，程式名稱簡單易懂，且足以告訴我們，是否位在正確的模組中，而原始檔的最上方能夠提供高階的概念和演算法，細節則慢慢呈現，直到發現最低階的函式和細節。

(二) 概念間留空白
範例如下
```
package fitness.wikitext.widgets;

import java.util.regex*;

public class...

public BoldWidget...
```
(三) 程式碼間若密切相關，他們會垂直緊密編排
1. 如不會遭到無用的註解隔開
2. 不會需要跳來跳去地閱讀，因此某些宣告有建議的放置位置

  (1) 變數宣告(variable declarations)
  - 變數宣告應盡量靠近被使用處
  - 區域變數應該要在每個函式的最上方
  - 迴圈控制變數應該在迴圈敘述內
  - 極少數情況，稍長函式裡的變數可能會宣告在程式區塊的最上方
  (2) 實體變數(instance variables)
  - 被宣告在類別上方
  
  (3) 相依的函式(dependent functions)
  - 呼叫其他函式的函式要放在被呼叫的者的前面
  (4) 概念相似性(conceptual affinity)
  
  像是一個函式呼叫另一個函式或一個函式使用一個變數，或是當一連串的函式都執行類似的工作，他們具有概念上高度的相似性，盡量放一起。
  

## 🖊️  水平編排的重點
(一) 約120個字元一排(非硬性規定)

(二) 在設定運算子(assignmnt operators)後換行，但不會在函式名稱和小左括號間換行，如
```
public class Quadratic {
...
}
```
※註:空白的另一功能是強調運算子的優先權，像是乘法因子間無空白，因優先順序較高，範例如
`return b*b - 4*a*c`

(三) 縮排的應用
1. 檔案層次的敘述不會縮排，如類別的宣告。
2. 類別裡的方法會向右縮一排。
3. 方法內的實作會再縮一排。
4. 子程式區塊的內容會比母程式區塊向右縮一排。

## 🖊️  本章重構範例
![450750223_3664457803820425_5258228367715944634_n](https://hackmd.io/_uploads/S1eccrZdC.jpg)
![449807039_497203512864263_5096315546548800023_n](https://hackmd.io/_uploads/ryN99BZdC.jpg)
![450574105_1242754730022177_6880072925910265261_n](https://hackmd.io/_uploads/S1_5cBW_R.jpg)


## 🤔 疑問

#### 1.什麼是protected變數 p.91?  
Ans: protected 變數是指那些只能在**類內部及其子類中訪問**(無法在類的外部直接訪問)的變數。訪問**權限比 private 更寬鬆，但比 public 更嚴格**。

protected 變數可能會分散在不同的文件中，特別是在大型項目中，這種情況更加常見。這通常發生在以下兩種情況：

(1) 父類和子類在不同文件中：如果父類和子類定義在不同的文件中，那麼 protected 變數就會被分散在這些文件中。子類可以在其文件中訪問父類的 protected 變數。

(2) 類庫和模組的使用：在使用類庫和模組時，父類和子類可能分別定義在不同的模組或類庫中，這樣 protected 變數也會分散在這些模組的文件中。

#### 2.如何把編排規則設定到IDE?  
Ans: 以Visual Studio Code (VSCode)為例子。

(1) 安裝擴展：安裝適用於你編程語言的格式化擴展，例如Java可以使用 CheckStyle 或 Google Java Format。

(2) 打開設置：點擊左下角的齒輪圖標，然後選擇 Settings，或按 Ctrl+, (Windows/Linux) 或 Cmd+, (macOS)。

(3) 搜索格式化設置：在設置搜索欄中輸入 format。

(4) 設置格式化規則：找到 Editor: Format On Save 選項，確保它被啟用。可以進一步配置格式化擴展的具體選項。


## 📖 下一章節主題預告
        
在了解基本定義後，下一章要談的是物件及資料結構。