---
title: '[筆記]Clean Code_chap. 2 有意義的命名'
tags: [書本-Clean Code]

---

# [筆記]Clean Code_chap. 2 有意義的命名

:::info 
:bulb: 「怎麼樣能讓自己的程式碼寫得越來越好」、「怎麼樣的程式碼可以跟別人合作愉快」，這是在成為軟體工程師的路上，出現的疑問，於是找到了這本書。
:::


## :+1: 章節重點

### :small_blue_diamond: 何謂有意義的命名
### :small_blue_diamond: 構成有意義命名的基本原則


## 🖊️  什麼是有意義的命名

作者認為不管是變數、函式或類別的名稱都要告訴人**為什麼會在這裡出現**、**要做什麼**，以及**如何使用**它。舉例而言，
較差的命名方式:
```
pulic List<int[]> getThem() {
    List<int[]> list1 = new ArrayList<int[]>();
    for (int[] x: theList)
        if (x[0]==4)
            list1.add(x);
    return list1;
}
```

修改後，才知道原來是插旗遊戲
```
pulic List<int[]> getFlaggedCells() {
    List<int[]> flaggedCells = new ArrayList<int[]>();
    for (int[] cell: gameBoard)
        if (cell[STATUS_VALUE]== FLAGGED)
            flaggedCells.add(cell);
    return flaggedCells;
}
```
甚至可以創造類別**Cell**，並在類別中設計有意圖的函式(isFlagged)，取代整數陣列
```
pulic List<Cell> getFlaggedCells() {
    List<Cell> flaggedCells = new ArrayList<Cell>();
    for (Cell cell: gameBoard)
        if (cell.isFlagged())
            flaggedCells.add(cell);
    return flaggedCells;
}
```

## 🖊️  有意義命名的基本原則
**Do**

(一)產生有意義的區別
1. 像是使用數字序列命名法(a1,a2,a3...an)就違背此原則。
2. 用Info、Data或variable這種不可區分的無意義字詞。
3. 像是money和moneyAmount、theMessage和message、CustomerInfo和Customer就沒有區別性。

(二)使用可以念得出來的名稱

1. genymdhms(意指產生日期、年、月、天、小時...) vs. generationTimestamp，相較之下，前者還需要額外解釋。

(三)使用可被搜尋的名字
1. 使用單一字母或數值命名不容易在文中被找到，因此，有時長命名勝過短命名。
2. 較差的範例:
```
for(int j=0 j<34; j++){
    s += (t[j]*4)/5;
}
```
較佳的範例:
```
int realDaysPerIdealDay = 4;
const int WORK_PER_WEEK = 5;
int sum = 0;
    for(int j=0 j<NUMBER_OF_TASKS; j++){
        int realTaskDays = taskEstimat[j]*realDaysPerIdealDay;
        ...
}
```

(四)每個概念使用一種字詞

為一抽象概念挑選一字詞，並持續使用，如同一程式庫中，DeviceManager和ProtocalController若無實質差異的話是不是都可改成controller或manager?

(五)使用解決方案/問題領域的命名

1. 盡量使用行話，如AccountVisitor或JobQueue。
2. 若沒有CS行話，就用Domain Knowledge領域的術語。

(六)加上有意義的上下文資訊，但不能無理由添加
1. 利用字首增加上下文資訊，如addFirstName。
2. 像是accountAddress、customerAddress對於物件實體是不錯命名，但對於類別來說不是。適合類別的命名是Address。

(七) 類別的命名建議用名詞或名詞片語，如Customer、Account等。

(八) 方法的命名建議用動詞或動詞片語，如deletePage。
1. 根據javabean標準，取出器(accessors)會用get當字首，如getName()。
2. 修改器(mutators)會使用set當字首，而判定(predicates)會使用is當字首。
3. 當建構子多載(overloaded)，建議使用名稱含有參數資訊的靜態工廠方法，如FromRealNumber(23.0)，以及將對應的建構子設定為私有(private)函式。

**DON'T**

(一)避免使用誤導性字詞
1. 避免使用與原意相違背的字詞，如hp、aix、sco，因為他們是Unix平台的名稱。
2. 使用accountList當成帳戶變數，但是資料型態卻不是List，此時建議用accountGroup。
3. 用l或O命名，因為他們太像數字1、0了。

(二)避免編碼

1. 早期會將型態或視野資訊編碼到名稱或是在成員變數前加m_，現在不用這麼做了。
2. 特例情況下使用編碼，如在抽象工廠的概念下，工廠(介面)會命名為ShapeFactory，而實作的部分命名為ShapeFactoryImp。

(三)避免思維轉換

除了像是迴圈計數變數在約定俗成上會使用i、j、k。

(四)避免使用雙關語

像是add和append(附加)和insert(插入)在使用情境上不同，所以不能互相通用。




## 🤔 疑問

#### 1.什麼是jar檔、war檔、ear檔?  
Ans: JAR (Java ARchive) 檔是 Java 平台上用於封裝多個檔案（通常是 Java 類和資源檔案）到單一壓縮檔案的格式；WAR (Web Application Archive) 檔是用於分發和部署 Java Web 應用程式的壓縮檔案；EAR (Enterprise Archive) 檔是用於分發和部署 Java EE（企業版）應用程式的壓縮檔案。

#### 2.什麼是靜態工廠模式?  
Ans: 簡單工廠又稱為靜態工廠模式，一般來說，同一工廠內所產生的類別會有一個共同的父類別(介面)。

假設有一冒險者(父類別)訓練營(簡單工廠)，冒險者種類有弓箭手(實體產品)、鬥士(實體產品)。今天若要增加種類(如法師)，就得要修改訓練營類別內的程式碼，在冒險者方法中增加分支，因此簡單工廠不能算是一個健全的設計模式。

不過在小型的軟體架構中很好用，實務上也常常會用到這個簡單的模式。

※資料來源:[簡單工廠模式](https://skyyen999.gitbooks.io/-study-design-pattern-in-java/content/simpleFactory.html)

簡單工廠:
```
public class TrainingCamp {
    public static Adventurer trainAdventurer(String type){
        switch(type){
            case "archer" : {
                System.out.println("訓練一個弓箭手");
                return new Archer();             
            }
            case "warrior": {
                ...               
            }
}
```
父類別:
```
// 冒險者(Product)
public interface Adventurer {
    //告訴別人你是哪種冒險者
    String getType();
}

// 弓箭手(ConcreteProduct)
public class Archer implements Adventurer {
    @Override
    public String getType() {
        System.out.println("我是弓箭手");
        return  this.getClass().getSimpleName();
    }
}
```
測試碼:
```
public class VillageTest {
    @Test
    public void test(){
        //新手村訓練冒險者
        Adventurer memberA = Village.trainAdventurer("archer");
        //這邊用Junit來幫我們判斷訓練出來的冒險者是不是我們想要的
        Assert.assertEquals(memberA.getType(), "Archer");
        //ouput:我是弓箭手
    }
}
```

#### 3.什麼是抽象工廠(Abstract Factory)?  
Ans:為了改善簡單工廠模式需要直接修改工廠類別裡面的程式碼，破壞開放/封閉原則的問題，在工廠模式中，將工廠(Factory)提升為一種**抽象**的概念--介面(Interface)。

工廠介面只會規範實體工廠類別(Concrete Factory)應該返回哪種產品，實際上要如何製作產品則交給實體工廠來實作。

以前例來說，新手村現在建立了兩座訓練營，弓箭手訓練營、鬥士訓練營。如果想要修改弓箭手的訓練流程，就修改弓箭手訓練營裡面的程式碼。如果增加訓練種類，就多蓋一座訓練營。

※資料來源:[抽象工廠模式](https://skyyen999.gitbooks.io/-study-design-pattern-in-java/content/abstractFactory1.html)

工廠介面與實作的差別:
```
/**
 *  冒險者訓練營介面(Factory)-這邊只是一個概念或規範，要訓練什麼，怎麼訓練留給子類別實作
 */
public interface TrainingCamp {
    //訓練冒險者的過程，訓練後請給我一個冒險者
    public Adventurer trainAdventurer();
}

/**
 * 弓箭手訓練營(ConcreteFactory)
 */
public class ArcherTrainingCamp implements TrainingCamp {

    @Override
    public Adventurer trainAdventurer() {
        System.out.println("訓練一個弓箭手");
        return new Archer(); 
    }

}
```

#### 4.為什麼當建構子多載時，使用靜態工廠方法優於直接使用建構子?  
```
Complex FUL = Complex.FromRealNumber(23.0)
Complex FUL =  new Complex(23.0) //直接用建構子
```
Ans:因為工廠方法具備名稱可以明確描述物件的創建意圖和上下文、避免建構子多載的混淆工廠方法、允許在創建物件時執行額外的邏輯或檢查、可以返回不同型別的物件等優點。

又所謂建構子多載意指一個類別中定義多個建構子（Constructor），這些建構子的名稱相同，但參數的數量、類型或順序不同。

#### private & public差在哪？
Ans:public在別的class或是main裡面也可以用。


## 📖 下一章節主題預告
        
在了解基本定義後，下一章要談的是函式。