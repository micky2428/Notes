---
title: '[筆記]單元測試的藝術ch.1 - 單元測試基礎'

---

# [筆記]單元測試的藝術ch.1 - 單元測試基礎

:::info 
:bulb: 以前製作的2-3個side project，都是以Web Form的UI介面進行測試，甚至偏向整合測試，希望自己在程式設計上能更完善，所以讀了《單元測試的藝術》第二版，並做了筆記。
:::


## :+1: 章節重點

### :small_blue_diamond: 單元測試的定義
### :small_blue_diamond: 單元測試與整合測試的比較
### :small_blue_diamond: 簡單的單元測試
### :small_blue_diamond: 理解測試驅動開發

## 🖊️  單元測試介紹

 (一) 定義
 1. 單元測試的概念早在1970年代，早期使用smalltalk設計程式時，就已出現。
 2. 被測試程式所測試的對象稱為「被測試系統」(System Under Test, SUT)，或稱CUT(Class/Code Under Test)。
 3. 作者認為一個單元測試是**一段程式呼叫「一個工作單元」**，並**驗證**工作單元的**最終結果**。如果最終結果的假策錯誤，那麼單元測試就失敗。所謂的**最終結果**，作者認為可以是以下其中一種形式:
 - 被呼叫的公開方法回傳一個結果值(非void function)。
 - 被呼叫方法的前後，系統可見的狀態或行為發生變化，且這個變化不需要透過查詢私有狀態就能取得。
 - 呼叫一個不受測試所控制的第三方系統，且第三方系統不回傳任何值，或是系統不使用這個回傳值。
4. 早期認為單元測試是測試一段程式碼，但這樣的定義似乎有點狹隘，因為如果把工作單元縮到最小，可能會需要偽造一些返回的結果，反而不是真實的最終結果。

(二) 特質
1. 自動化，且可以被重複執行
2. 容易被實現
3. 非臨時性，第二天都還有存在意義
4. 任何人都可以一鍵執行
5. 執行速度應該很快
6. 執行結果應該一致
7. 應該要能完全掌控被測試的單元
8. 應該要獨立於其他測試
9. 如果他的執行結果是失敗的，應該要能很清楚呈現發生原因為何

## 🖊️  單元測試與整合測試的比較
1. 作者認為如果測試需要用到系統真實的時間、檔案或資料庫，這種測試屬於**整合測試**的領域。
2. 作者將整合測試定義為「對一個工作單元進行測試，而這個測試對被測試的單元**沒有完全控制**，而且使用該單元一個或多個真實依賴的相依物件」。所以測試過程可能發現很多失敗點，較難除錯。

## 🖊️  簡單的單元測試

1. 本章節先提及不用框架的單元測試，用Python(書中是用C#舉例)簡單舉例就是用Try..Except...。

2. 範例: 假設今天要測試Class(SimpleParser)，SimpleParser裡面包含一個Method(ParseAndSum):
- 輸入是由零個或多個逗號(,)分開的數字所組成的字串
- 如果字串不包含任何數字，回傳 0
- 如果只有單一數字則回傳該數 int 值
- 如包含多個數字，則將數字相加後回傳總和。
```
// 範例目前只能處理零個或是單一數字
class SimpleParser:
    def parse_and_sum(self, numbers: str) -> int:
        if len(numbers) == 0:
            return 0
        if ',' not in numbers:
            return int(numbers)
        else:
            raise ValueError("I can only handle 0 or 1 numbers for now!")
```
TestReturnsZeroWhenEmptyString 會驗證 ParseAndSum 的回傳結果，若不正確或是有例外會輸出錯誤訊息到 Console。
```
class SimpleParserTests:
    @staticmethod
    def test_returns_zero_when_empty_string():
        try:
            p = SimpleParser()
            //傳入空字串
            result = p.parse_and_sum("")
            if result != 0:
                print("***SimpleParserTests.test_returns_zero_when_empty_string: " +
                      "------ Parse and sum should have returned 0 on an empty string")

        except Exception as e:
            print(e)


```
控制台測試程式
```
def main():
    try:
        SimpleParserTests.test_returns_zero_when_empty_string()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
```

## 🖊️  理解測試驅動開發(TDD)
:::success
:bulb: 啟發:由於以往在程式碼中使用try...except...傾向先寫程式才測試，TDD提供不同觀點。
:::
1. 選擇在撰寫產品**前**寫單元測試的方法稱為測試優先或測試驅動開發(Test-Driven Development,TDD)。
2. 操作流程:
- 先寫執行會失敗的測試，證明功能缺失。
- 透過完成產品程式碼，通過失敗的測試。(同時具有對測試程式碼進行測試的功用)
- 對程式碼進行重構或選擇繼續撰寫下一個失敗測試。

3.優點:
- 減少debug時間。
- 協助確保測試程式的測試覆蓋率，確認測試可以被信任。

![448758149_681227364161157_518008953613687010_n (1)](https://hackmd.io/_uploads/ryDSIkyP0.jpg)



## 🤔 疑問

#### 1.什麼是WinForm?  
Ans: Windows Forms是微軟的.NET開發框架的圖形使用者介面的一部分。


## 📖 下一章節主題預告
        
在了解基本定義後，作者將用.Net框架帶領實作。