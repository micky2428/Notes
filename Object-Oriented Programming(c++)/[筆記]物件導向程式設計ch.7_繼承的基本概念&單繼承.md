---
title: '[筆記]物件導向程式設計ch.7_繼承的基本概念&單繼承'

---

 # [筆記]物件導向程式設計ch.6
:::info 
:bulb: 本筆記內容源自溫宏斌老師的物件導向程式設計OCW。
:::

## :+1: 章節重點

### :small_blue_diamond: 繼承的基本概念&單繼承


## 🖊️ 繼承
(一)概念
1.繼承在概念上是is-a關係，在現有的類(class)之間建立父子關係。

2.繼承的屬性包含data member(資料)和member function(方法)，不過新類別
(1)可以自己創造新的屬性和方法
(2)能重新定義基礎類別裡的一些函式
(3)在衍生類別中改變成員的屬性(比如從public變成private)。


3.建立階層化的類別架構(由通泛走向專屬的)。
![螢幕擷取畫面 2024-10-12 105404](https://hackmd.io/_uploads/SkbyrDwkyl.png)

4.上層稱基礎類別，下層稱衍生類別，由上圖可知:
(1)**基礎類別**，可以有很多個衍生類別
(2)**衍生類別**，可以繼承很多的基礎類別(大於2個->**多重繼承**)

5.繼承的作用:**程式碼的重複使用**(oop的重要觀念)。

6.有**三種情況是不能被繼承**的:⭐
(1)基礎類別的建構和解構子
(2)基礎類別的friend
(3)static data和成員函式因為是專屬一類別的，所以也不能被繼承

※補充:重載指派運算子(overloaing assignment operator)&拷貝建構式(Copy Constructor)雖不能繼承，但可以在衍生類別中使用。
以 "=" 舉例:
```
//呼叫CBase中的operator函式，並把rHand丟進去，把rHand先降級轉型成CBase的物件，丟到基礎類別的function和裡面的欄位作用。
CDerived& CDerived::operator = (
            const CDerived& rHand){
            CBase ::operator=(rhand);
}
```


(二)範例
1.	基礎類別會定義有哪些屬性是可以提供衍生類別繼承的，稱為可繼承的特質，包含public和protected。private是不可繼承的特性。
```
//基礎類別
class CCircle{
protected:
    double radius;
public:
    CCircle(double r =1.0):radius(r){;}
    void setR(double r =1.0){radius=r;}
    double calVol() **const** {
        return (PI*radious*radious);
    }
    void showVol() **const**{
    cout << "radius=" <<radius <<endl;
    cout << "volumn=" <<calVol() <<endl;
    }
};
```
※補充:上面的程式碼有兩個函式有加const。
⭐**如果函式只是一般存取器**（accessor，作用僅僅是用來讀取，不會改值）的話，**基本上在不改變私有屬性的情況都會宣告成const function**，以免以後遇到const object要呼叫這些function時無法呼叫，記得養成好習慣!

⭐Costant method可以被const呼叫也可以被非const呼叫，但如果不加的話，只有regular的可以呼叫他。


3.class<繼承類別名稱>的冒號後面是<繼承方式> <基礎類別x>
```
//衍生類別
class CCylinder:public CCircle{
protected:
    double length; //CCylinder自己新增的資料
public:
    //定義了自己的constructor，呼叫CCircle(r)並把r設定在radius裡面
    CCylinder(double r =1.0, double l =1.0):CCircler(r),length(l){;}
    void setRL(double r =1.0, double l =1.0){radius=r; length=l;}
    //這樣就不用重寫圓面積的計算公式
    double calVol() const {
        return (**CCircle::calVol()***length);
    }
    //從CCirvle繼承showVol()
    void displayVol() const{
    cout << "d radius=" <<radius <<endl;
    cout << "d volumn=" <<calVol() <<endl;
    
}
//main program
int main(){
    //圓
    CCircle cr1,cr2(4);
    //圓柱
    CCylinder cy1,cy2(2,3);
    
    cr1.setR(2);
    cr1.showVol();cr2.showVol();
    //(3,1)
    cy1.setRL(3);
    //沒有乘上長度;有乘上長度
    cy1.showVol();cy1.displayVol();
    cy2.showVol();cy2.displayVol();
    //”強制轉型”，把圓柱轉成圓
    cr1=cy1;
    //秀出圓的面積
    cr1.showVol();
    
    return 0;
}
```

(三)繼承的方式
不同的繼承方式會影響衍生類別如何存取基礎類別的成員，此時就涉及了**存取修飾符**的設定。

1.public
(1)用公開繼承可以維持基礎類別的可繼承性，如下表:

| 在公開基礎類別的成員屬性 | 在公開衍生類別的存取性 |
| -------- | -------- |
| public     | public  |
| private     | private  |
| protected     | protected  |


(2)衍生類別的member function可以直接存取基礎類別中public和protected的member。**基礎類別中Private member**雖有繼承，但不像自己類別內的member可以任意存取，要**透過基礎類別中定義的****accessor**。
```
//基礎類別
class CPoint
{
    double x,y;
public:
    CPoint(double a =0, double b=0):
        x(a), y(b){}
    //mutator:改變內容
    void SetPoint(double a =0, double b=0){
        x=a, y=b;
    }
    void MovePoint(double dx, double dy){
        x+=dx, y+=dy;
    }
    //accessor 
    double GetX() const{return x;}
    double GetY() const{return y;}

}

//衍生類別
class CRect: public CPoint
{
    double h,w; //新增私有資料
public:
    double GetH() const {return h;}
    double GetW() const {return w;}
    CRect(double a, double b,double c,double d): h(c),w(d){**SetPoint(a,b)**;}

    //mutator:改變內容
    void SetRect(double a, double b,double c,double d){
        **SetPoint(a,b)**;
        h=c; w=d;
    }
}

//main()
int main(){
    CRect cr1;
    cr1.SetRect(2,3,10,20);
    cr1.MovePoint(3,2);
    ......
}
```


(3)衍生類別產生的**物件**(如前例CCircle)只能用基礎類別的public member。

★★這時區分出public和protected的差別。public和protected在類的視野中沒有差異，所以member function都可以呼叫。**但在物件層級只能呼叫public**。



2.private
(1)為了維護封裝完整性，只要是私有類別不論繼承方式，都**不能存取**，但**仍有繼承到這些資料**(有占記憶體空間)。

| 在私有基礎類別的成員屬性 | 在私有衍生類別的存取性 |
| -------- | -------- |
| public     | private  |
| private     | inaccessible  |
| protected     | private  |

(2)衍生類別的物件就不能呼叫ㄐ任何member。衍生類別的物件只能呼叫自己寫在public的那些member。

(3)範例
```
//基礎類別
class CPoint
{
   (同上)
}
//衍生類別
class CRect: private CPoint
{
    double h,w; //新增私有資料
public:
    double GetH() const {return h;}
    double GetW() const {return w;}
    //mutator
    void SetRect(double a, double b,double c,double d){
        //透過繼承的函式來設定資料
        CPoint::**SetPoint(a,b)**;
        h=c; w=d;
    }
    //不同於前例公開繼承的衍生類別，這行是自己寫的
    void MoveRect(double dx, double dy){
        CPoint::**MovePoint(dx,dy)**;
    }
};
//main()
int main(){
    CRect cr2;
    cr2.SetRect(2,3,20,10);
    cr2.MovePoint(3,2); //錯誤
    //只能用自己寫的
    cr2.MoveRect(3,2);
    ......
}

```

3.protected
1.和private一樣，衍生類別的**物件**就不能呼叫任何member。對物件來說，效果同私有。

2.對於在基礎類別中的protected成員，在基礎類別以外，效果同私有。

3.對於繼承protected的衍生類別，protected成員，效果同公開。


| 在私有基礎類別的成員屬性 | 在私有衍生類別的存取性 |
| -------- | -------- |
| public     | protected  |
| private     | inaccessible  |
| protected     | protected  |




## 🤔 疑問
Q1: 宣告成 const 函式的重要性?
A1:
1.防止無意修改到屬性：當函式聲明為 const，編譯器會保證該函式不會修改類的任何屬性，這是一種額外的安全性。
(2.持 const 對象調用：若某個函式不修改類的成員變數，最好將它聲明為 const，這樣在 const 對象調用這些函式時不會發生編譯錯誤。
```
class MyClass {
private:
    int value;

public:
    // 一般 accessor 函式
    int getValue() const {
        return value;
    }
    
    // 非 const 函式
    void setValue(int val) {
        value = val;
    }
};

const MyClass obj;
obj.getValue();  // 可以調用，因為 getValue() 是 const 函式
obj.setValue(10);  // 錯誤，因為 setValue() 不是 const 函式
```

Q2: 什麼是拷貝建構式(Copy Constructor)?
A2:
1.定義:拷貝建構式（Copy Constructor）用於創建一個對象作為另一個同類型對象的副本。

2.何時會使用拷貝建構式？
- 對象初始化時
```
ClassName obj1;
ClassName obj2 = obj1; 
```
- 將對象作為參數傳遞給函數時
`void function(ClassName obj);`
- 從函數返回對象時
```
ClassName function() {
    ClassName obj;
    return obj;  // 調用拷貝建構式
}
```
3.拷貝建構式的作用：
確保在創建新對象時正確地複製已存在對象的數據。如果類中有**動態分配**的資源，需要**自定義拷貝**建構式來避免淺拷貝問題，導致資源衝突或錯誤。

4.預設拷貝建構式：
如果類中沒有自定義的拷貝建構式，C++ 會生成一個預設拷貝建構式，該建構式執行淺拷貝，僅拷貝每個成員的值，對於指針成員則只拷貝指向的地址。這在有動態內存的情況下可能會導致問題，因此需要自定義拷貝建構式來進行深拷貝。

## 📖 下一章節主題預告
多重繼承


