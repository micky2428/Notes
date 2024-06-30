# [筆記]單元測試的藝術ch.2 - 第一個單元測試

:::info 
:bulb: 以前製作的2-3個side project，都是以Web Form的UI介面進行測試，甚至偏向整合測試，希望自己在程式設計上能更完善，所以讀了《單元測試的藝術》第二版，並做了筆記。
:::


## :+1: 章節重點

### :small_blue_diamond: 探討.Net的單元測試框架
### :small_blue_diamond: 使用NUnit撰寫第一個單元測試
### :small_blue_diamond: 使用NUnit的特性
### :small_blue_diamond: 了解一個工作單元的三種輸出類型

## 🖊️  單元測試框架

 (一) 介紹

1. 雖然VS內建的是MSTest，但本書作者使用NUnit作為範例，因為他認為在撰寫單元測試方面，NUnit支援較好的功能，以及提供**測試特性**幫助撰寫可維護性。
2. 單元測試框架的命名，通常是由他們所支援的程式語言開頭字母加上Unit，如C++的CppUnit、Java的JUnit等。
3. 單元測試框架示意圖:
![448920248_1155039788873109_5042901094466490104_n](https://hackmd.io/_uploads/r1PUPgJwC.jpg)

4. 單元測試框架的優點: 
![448852893_1694571854644843_5553435279238478538_n](https://hackmd.io/_uploads/rJn8PxkDA.jpg)


## 🖊️  本書測試案例介紹:LogAn專案
1. LogAn專案的功能是對log檔進行分析，並在其中搜尋特定的情況和事件。當找到特定情況或事件後會通知相關人員。
2. 我們要撰寫的測試則是要驗證LogAn的解析、事件辨識以及通知功能。

## 🖊️  NUnit操作

(一) 安裝
1. 從VS的擴充套件管理器(Extension Manager)中下載NuGet Package Manager。
2. 安裝後重啟VS，並打開選單Tools > Library Package Manager > Package Manager Console，在彈出的命令視窗中輸入Install-Package NUnit。
3. 確認有看到「安裝成功」。

(二) 載入方案的方式

1. 找到[Github](https://github.com/royosherove/aout2)資料夾裡的ArtOfUnitTesting2ndEd.Samples.sln檔案，還有資料夾LogAn和LogAn.UnitTests。成功下載的話，前面圖示會變成c#
![螢幕擷取畫面 2024-07-01 003306](https://hackmd.io/_uploads/HJoZtZ1vR.png)


```
public class LogAnalyzer
{
    public bool IsValidLogFileName(string fileName)
    {
        if(fileName.EndsWith(".SLF")) //這裡埋了一個bug，filename前面要加"!"才對
        {
            return false;
        }
        return true;
    }
}
```
2. 測試命名與位置的基本規則
![448791959_1310433413677275_3859685926772785856_n](https://hackmd.io/_uploads/BJ7O5gkv0.jpg)
比如用來測試LogAn的測試專案名稱，作者取名為LogAn.UnitTests，測試LogAnalyzer Class的測試類別名稱為LogAnalyzerTests。對IsValidFileName方法進行測試的名稱命名為IsValidFileName_BadExtension_ReturnsFalse()。


(三) 在程式中使用NUnit的特性

1. [TestFixture]標記包含自動化NUnit測試的Class
2. [Test]加在method的上方
3. 需注意:NUnit要求測試Method需是public和void，在基本設定情況下，不允許傳入參數。
```
[TestFixture]
public class LogAnalyzerTests
{
    [Test]
    public void IsValidFileName_BadExtension_ReturnsFalse()
    {
    
    }
}
```


(四) 撰寫第一個測試程式

一個單元測試通常包含
- 準備(Arrange)物件、建立物件、進行必要設定
- 操作(Act)物件
- 驗證(Assert)某件事符合預期 

```
[Test]
public void IsValidFileName_BadExtension_ReturnsFalse()
{
    // Arrange
    LogAnalyzer analyzer = new LogAnalyzer();
    // Act
    bool result = analyzer.IsValidLogFileName("filewithbadextension.foo");
    // Assert
    Assert.False(result);
}
```

(五) 執行第一個測試
1. 使用VS Test Runner的 NUnit Test Adapter的NUnit執行器擴充套件
2. 使用Resharper測試執行器
3. 使用TestDriven.Net測試執行器
4. 使用 NUnit圖形化介面




## 🤔 疑問

#### 1.什麼是Assert?  
Ans: Assert(Class)是屬於NUnit.Framework的命名空間裡提供的靜態方法，是程式碼與NUnit測試框架間的橋梁，用來確認該假設下某期望應該會成立。Assert下的method包含:
- Assert.IsTrue
- Assert.IsFalse
- Assert.AreEqual(expectedObject,actualObject,message)，如Assert.AreEqual(2,1+1,"Math is broken")
- Assert.AreSame(expectedObject,actualObject,message)用來驗證兩個參數是否指向同一物件

#### 2.測試程式有風格嗎?  
Ans:本書作者認為測試程式的「風格」和「可讀性」和一般程式碼不完全一致，包含以下特點:
- 測試名稱可以很長，避免遺漏重要資訊
- **可讀性**是最重要的考量，在準備物件、操作物件以及驗證階段的程式碼間要留空白行
- 盡量把驗證和操作物件的程式碼分開

#### 3.如何設計測資?
還未找到解答

## 📖 (下)篇主題預告
        
在了解第一次操作測試後，由於前面舉例的測試程式不容易維護，所以(下)篇將重構程式碼。