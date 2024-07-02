---
title: '[筆記]單元測試的藝術ch.2 - 第一個單元測試(下)'

---

# [筆記]單元測試的藝術ch.2 - 第一個單元測試(下)

:::info 
:bulb: 以前製作的2-3個side project，都是以Web Form的UI介面進行測試，甚至偏向整合測試，希望自己在程式設計上能更完善，所以讀了《單元測試的藝術》第二版，並做了筆記。
:::


## :+1: 章節重點

### :small_blue_diamond: 探討.Net的單元測試框架
### :small_blue_diamond: 使用NUnit撰寫第一個單元測試
### :small_blue_diamond: 使用NUnit的特性
### :small_blue_diamond: 了解一個工作單元的三種輸出類型


## 🖊️  NUnit操作

繼(上)篇執行完第一個程式以後，作者在講解**重構程式碼**的過程中，介紹了NUnit幾個重要的操作。
(六) [TestCase]
1. NUnit有個功能叫參數化測試(parameterizedd tests)，要使用的話，需按以下方式修改程式碼:
- 把[Test]換成[TestCase]
- 把測試中寫死的值，替換成這個測試方法的參數
- 把被替換掉的值放到**特性**的括號裡，如[TestCase(param1, param2,...)]
- 用比較共同的方式，重新命名測試方法
- 在這個測試方法上，對每個需要合併的測試方法，用其測試值新增一個[TestCase(...)]特性
- 移除其他測試，只保留一個帶有多個[TestCase]特性的測試方法

2.範例如下

這裡使用的是**正向測試**的程式碼，比起(上)篇測試錯誤的副檔名，如果採用測試驅動開發的方式開發，這裡所用的測試就會用正向測試，確保檔名是對的，而非排除掉錯的。

原本正向測試的程式碼:
```
[Test] //測試小寫的副檔名
public void IsValidLogFileName_GoodExtensionLowercase_ReturnsTrue()
{
    // Arrange
    LogAnalyzer analyzer = new LogAnalyzer();
    // Act
    bool result = analyzer.IsValidLogFileName("filewithgoodextension.slf");
    // Assert
    Assert.True(result);
}

[Test] //測試大寫的副檔名
public void IsValidLogFileName_GoodExtensionUppercase_ReturnsTrue()
{
    // Arrange
    LogAnalyzer analyzer = new LogAnalyzer();
    // Act
    bool result = analyzer.IsValidLogFileName("filewithgoodextension.SLF");
    // Assert
    Assert.True(result);
}
```
修改後:
```
[TestCase("filewithgoodextension.slf")] //測試小寫的副檔名
[TestCase("filewithgoodextension.SLF")] //測試大寫的副檔名
public void IsValidLogFileName_VaildExtensions_ReturnTrue(string file)
{
    LogAnalyzer analyzer = new LogAnalyzer();
    bool result = analyzer.IsValidLogFileName(file);
    Assert.True(result);
}

```
加入負面測試:
```
[TestCase("filewithgoodextension.slf",true)] 
[TestCase("filewithgoodextension.SLF",true)] 
[TestCase("filewithbadextension.foo",false)]
public void IsValidLogFileName_VariousExtensions_CheckThem(string file, bool expected)
{
    LogAnalyzer analyzer = new LogAnalyzer();
    bool result = analyzer.IsValidLogFileName(file);
    Assert.True(expected, result);
}

```

(七) [Setup]和[TearDown]

1. 進行單元測試時，重要的一點是要確保之前測試過程所遺留下的資料或執行個體得以銷毀，也就是說新測試的狀態是被重置過的。
2. [Setup]和[Test]一樣可加在方法上，但缺點是使用越多[Setup]可讀性就會越差；[TearDown]則在每個測試執行完畢後被呼叫。不過在實際工作中，作者並不使用setup來初始化被測試類別的物件執行個體，只是說明有這種用法，作者較常使用的是**工廠方法**(factory method)(詳參ch.7)。
4. 實際上TearDown不太會用到，通常是遇到相依檔案系統或資料庫，此時寫的是整合測試。
```
using NUnit.Framework;
[TestFixture] //測試小寫的副檔名
public class LogAnalyzerTests
{
 private LogAnalyzer m_analyzer = null;
 [Setup]
 public void Setup()
 {
     m_analyzer = new LogAnalyzer();
 }
 [Test]
 public void IsValidFileName_validFileLowerCased_ReturnsTrue()
 {
    bool result = m_analyzer.IsValidFileName("whatever.slf");
    Assert.IsTrue(result, "filename should be valid!");
 }
 [Test]
 public void IsValidFileName_validFileUpperCased_ReturnsTrue()
 {
    bool result = m_analyzer.IsValidFileName("whatever.SLF");
    Assert.IsTrue(result, "filename should be valid!");
 }
 [TearDown]
 public void TearDown()
 {
    ... 
 }
```

(八) [ExpectedException] vs. Assert.Catch<T> 

1. 作者接著解釋如何測試應該**由產品程式碼拋出例外**的情況。
2. 比較不建議的方式是[ExpectedException]，[ExpectedException]裡面沒有使用Assert，是因為他本身就包含驗證檢查，範例如下。至於，不推薦的原因是因為不知道在整個測試方法的大區塊出現的例外，是不是我們所期望的那個。
```
[Test] 
[ExpectedException(typeof(ArgumentException),
    ExpectedMessage = "fils has to be provided")]
public void IsValidFileName_EmptyFileName_ThrowException()
{
    m_analyzer.IsValidLogFileName(string.Empty);
}
private LogAnalyzer MakeAnalyzer()
 {
    return new LogAnalyzer();  
 }
```
3. Assert.Catch<T>(delegate)是作者推薦的方式，範例如下:
```
[Test] 
public void IsValidFileName_EmptyFileName_Throws()
{
    LogAnalyzer la = MakeAnalyzer();
 var ex = Assert.Catch<Exception>(() => la.IsValidLogFileName(""));
 StringAssert.Contains("filename has to be provided",
                                         ex.Message);
}
``` 
- 在這段程式碼中，使用Assert.Catch傳入一個不帶參數的Lamba表達式，表達式是呼叫la.IsValidLogFileName("")。而我們希望看到的就是Lamba中的程式碼拋出一個符合預期的例外。
- StringAssert則是能夠簡化字串驗證的輔助函數。
    
※ 補充: 流利語法(多使用Assert.That開頭)
```
[Test] 
public void IsValidFileName_EmptyFileName_ThrowsFluent()
{
    LogAnalyzer la = MakeAnalyzer();
 var ex = Assert.Catch<ArgumentException>(() => la.IsValidLogFileName(""));
 Assert.That(ex.Message,
    Is.StringContaining()"filename has to be provided"));
}
``` 
    
(九) [Ignore]

有時因為時間緊迫，即便測試程式有問題，不得不先將測試程式遷入版本庫中，而加上[Ignore]。

```
[Test] 
[Ignore("there is a problem with this test")]
public void IsValidLogFileName_ValidFile_ReturnsTrue()
{
    ...
}
```
(十) [Category]

可以把測試按其分類來執行。

```
[Test] 
[Category("Fast Tests")]
public void IsValidLogFileName_ValidFile_ReturnsTrue()
{
    ...
}
```



## 🤔 疑問
暫時沒有

 

## 📖 下章節主題預告
        
作者在本章著重講解針對**回傳值**來進行測試的方法，接下來他將介紹**如何測試系統的改變**。