---
title: '[筆記]Clean Code_chap. 4 註解'
tags: [書本-Clean Code]

---

# [筆記]Clean Code_chap. 4 註解

:::info 
:bulb: 「怎麼樣能讓自己的程式碼寫得越來越好」、「怎麼樣的程式碼可以跟別人合作愉快」，這是在成為軟體工程師的路上，出現的疑問，於是找到了這本書。
:::


## :+1: 章節重點

### :small_blue_diamond: 作者對於使用註解的認知
### :small_blue_diamond: 例外得使用註解的情況


## 🖊️  作者對於使用註解的認知

1. 本書作者認為「即便在最好的情況下，註解不過是必要之惡」。他引用了Brain W. Kernighan和 P.J. Plaugher的話「不要替糟糕的程式碼寫註解--重寫他」。

      (1) 範例:
    ```
    // Check to see if the employee is eligible for full benefits
    if ((emplyee.flags & HOURLY_FLAG) && (employee.age > 65))
    ```
      (2) 改寫後:

    `if (employee.isEligiableForFullBenefits())`

2. 由此可知，作者對於註解的使用，是原則上能不用就盡量不用，**寫註解不如取個好的函式或類別名稱**。
3. 不使用的理由包含

      (1) 註解不一定每次都能跟著一起移動，有可能不小心被忽略

      (2) 註解無法彌補糟糕的程式碼

      (3) 可能產生糟糕的註解，像是
    
    - 強迫你去看其他套件的喃喃自語
    ```
    public void loadProperties()
    {
        try
        {
            String propertiesPath = propertiesLocation + "" + PROPERTIES_FILE;
            ...
        }
        catch(IOExpection e)
        {
            //No properties files means all defaults are loaded.
        }
        }
    ```
    - 沒有比程式碼本身透漏更多訊息，也沒有解釋到程式碼的多餘註解
    ```
        public abstract class ContainerBase
        implements Container, Lifecycle, Pipeline,
        MBeanRegistration, Serializable{
        
        /**
         *The processor delay for this component.
         */
        protected int backgroundProcessorDelay = -1;
        ......
        }

    ```
    - 誤導型註解
    
        出於好意，但寫下不精確的註解
    `// Utility method that returns when this.closed is true.`但實際上是，`//...when this.closed is judged to be true.`
    
    - 規定型註解
    像是在每行程式碼都打註解。
    
    - 日誌型/HTML型式註解
    
        A. 有的人會在開始編輯程式碼時，加上註解，日積月累成日誌型註解，但現在有版控系統可用。
        
        B. 註解中有HTML(範例如下)，這要用工具改善，而不是程式設計師的責任。
    ![450367349_923245349561653_5879357480707164258_n (1)](https://hackmd.io/_uploads/SJMsCbluA.jpg)

    
    - 位置的標誌物
    `像是 //Actions //////////`
    
    - 右大括號後面的註解
    
        A. 在短小封裝型函式不推薦使用
    
        B. 有深層巢狀結構時可，範例如下
    ![450013073_1115948736137607_7769133570248316198_n (1)](https://hackmd.io/_uploads/rJEMCbgdR.jpg)

    
    - 被註解的程式碼，會導致版面亂，且別人會不敢刪。
    
    - 非區域性的資訊
    
    註解是用來描述附近的程式碼，不要放入全域資訊(如預設連接埠)。
    
    - 過多的資訊
    
    不要把歷史討論紀錄或不相關細節放進註解。
    

## 🖊️  例外得使用註解的情況
(一) 法律型註解
1. 在每個原始碼檔案開頭寫入**著作權聲明**及**作者資訊**
2. 可以參考標準的許可或其他外部文件

(二) 資訊型註解

提供資訊的註解如下
```
//  format matched kk:mm:ss EEE, MMM dd, yyyy
Pattern timeMatcher = Pattern.compile(
    "\\d*:\\d*:\\d* \\w*, \\w* \\d*, \\d*");
```
就以上範例而言，作者認為把程式移到類別中，而該類別可以轉換日期和時間的格式，會更清楚，而不用再加註解。
```
import java.util.regex.*;

public class DateTimeUtils {
    private static final String TIME_PATTERN = "\\d*:\\d*:\\d* \\w*, \\w* \\d*, \\d*";
    private static final Pattern timeMatcher = Pattern.compile(TIME_PATTERN);

    public static boolean isValidTimeFormat(String timeString) {
        Matcher matcher = timeMatcher.matcher(timeString);
        return matcher.matches();
    }
}
```


(三) 對意圖的解
```
//This is the best attempt to get a race condition
//by creating large number of threads.
```

(四) 闡明

把難解的參數或回傳直翻譯成有可讀性的文字，難解的參數可能是標準函式庫的一部分或是某個不能修改的函式。

(五) 對於後果的告誡

`//don't run unless you have some time to kill.`

(六) TODO註解
```
// TODO-MdM these are needed
// We expect this to go away when we do the checkout model
```
但此種註解不得作為留下糟糕程式碼的理由。

(七) 放大重要性

放大某些看似無關緊要的事的重要性

(八) 公共API的Javadoc

## 🖊️  本章的重構範例
閱讀重點:

1.取名

2.函式由上而下的邏輯

3.必要的註解(開頭的演算法說明，以及中後段使用平方根計算的原因)
![449746217_278647338644925_7467604438634551098_n](https://hackmd.io/_uploads/BkqIvGgOA.jpg)
![450512865_1133643027866648_6039643173834998074_n](https://hackmd.io/_uploads/rJ_jvMgu0.jpg)


## 🤔 疑問

#### 1.什麼是靜態初始器?  
Ans: 是由static修飾的語句{...}。


## 📖 下一章節主題預告
        
在了解基本定義後，下一章要談的是編排 。