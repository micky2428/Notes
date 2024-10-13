---
title: '[筆記]物件導向程式設計ch.8_-多重繼承&虛擬基礎類別'

---

 # [筆記]物件導向程式設計ch.6
:::info 
:bulb: 本筆記內容源自溫宏斌老師的物件導向程式設計OCW。
:::

## :+1: 章節重點

### :small_blue_diamond: 多重繼承
### :small_blue_diamond: 虛擬基礎類別


## 🖊️ 多重繼承(multiple inheritance)
(一)概念
1.衍生類別繼承多個父類別，作法一個個列出來被繼承的類別(父類別)。

2.回顧繼承特性(假設class Boo 公開繼承Bum和Foo)
(1)支援Bum和Foo公開/受保護的方法
(2)由於是衍生類別，Boo的物件可以轉換成Bum或Foo的物件(如前一章圓vs圓柱體)。
(3)當你想創造新的Boo物件，你也會呼叫Bum或Foo預設的constructors，並用反著呼叫destructors。

💡注意: 呼叫建構子的順序是**按照宣告順序**從左到右，而非初始化的順序(見本章第三部分)。


3.多重繼承以圖示來看如下圖
![螢幕擷取畫面 2024-10-13 095202](https://hackmd.io/_uploads/ryP0Pju1Jl.png)

4.缺點:
多重繼承較單繼承來得容易混淆，但如果用到多重繼承，且兩個父類別有相同的member，就要使用**界定符號**resolution operator(::)。



```
class Sofa{
public: void sit(){
    cout << "sit" <<endl;}
    void SetWeight(int a=0){weight=a;}
    ....
};

class Bed{
public: void lie(){
    cout << "lie" <<endl;}
    void SetWeight(int a=0){weight=a;}
    ....
};
//公開繼承
class Sofabed:public Sofa, public Bed{{
public: void fold(){
    cout << "fold" <<endl;}

//
int main()
{
    Sofabed myfur;
    myfur.sit();
    myfur.lie();
    
    return 0;
}
```

(二)多重繼承產生的模糊地帶
1.發生情境
(1)從父類別呼叫了相同名字的member
(2)呼叫到共同基礎類別的member，也就是說，父類別也是繼承某類別來的(p.9)

2.重載同名成員以後出現的副作用:
(1)重載基礎類別底下同名的member後，會使他們不能直接被存取(access)。
```
//基礎類別
class CB{
public:
    void f(){cout << "CB's f()"<<endl;}
    void f(int x){cout << "CB's f()"<<endl;}
}
//衍生類別:公開繼承
class CD: public CB{
public:
    void f(){cout << "CD's f()"<<endl;}
}
//main()
CD obj;
obj.f();
obj.f(5); //錯誤，會顯示不該有參數
```
例如上面的程式碼因衍生類別CD裡面有void f()蓋掉了基礎類別中void f()和void f(int x)，即便參數數量不同，但因函式名稱相同還是被蓋掉，所以下半部obj.f(5)會error，除非用obj.CB::f(5)。

(2)父類別也是繼承其他類別而來，除了產生歧異性或混淆不清的情況，還會浪費記憶體。
![螢幕擷取畫面 2024-10-13 095720](https://hackmd.io/_uploads/SkdMFsOJke.png)
如上圖，CB繼承CA、CC繼承CA，CD包含了兩個copy的CA。
用程式碼來看，可以發現錯誤在於:
```
//衍生類別:公開繼承
class CD: public CB, public CC{
public:
    int w;
    CD(int a = 0,int b = 0,int c = 0,int d = 0,int e = 0):CB(a,b),CC(c,d){w=e;}
    ....
}
//main()
CD obj(5,4,3,2,1);//錯誤，因為CB和CC中的x應該是同一個，但因硬寫成兩次，導致兩個x copy最終出現的值不同。
```
3.解方
虛擬基礎類別(如下)

## 🖊️ 虛擬基礎類別
(一)概念
虛基類的用途在於當定義一個衍生類別，且這個衍生類別是繼承到同一個基礎類別時，只保留一份的copy，如前例CB和CC都有繼承到CA的x，此時只會留下一份x。
```
//CA
class CA{
public:
    int x;
    CA(int a=0){x=a;}
};
//CB:虛擬繼承CA
class CB:**virtual** public CA{
public:
    int y;
    CB(int a=0, int b=0):CA(a){y=b;}
};
//CC:虛擬繼承CA
class CB:**virtual** public CA{
public:
    int z;
    CC(int a=0, int b=0):CA(a){z=b;}
};

//CD:
class CD: public CB, public CC{
public:
    int w;
    //在呼叫CB,CC以前，用CA的建構子初始化x(a)欄位，x的結果會是一致的。
    CD(int a = 0,int b = 0,int c = 0,int d = 0,int e = 0):**CA(a)**,CB(a,b),CC(c,d){w=e;}
    ....
}
```
⭐⭐虛基類的constructor要寫在最前面，不能沒寫CA(a)，否則他就會回到預設初始值

(二)重構前面沙發的例子
1.redesign SofaBed在Sofa和Bed之上再定一層
![螢幕擷取畫面 2024-10-13 095909](https://hackmd.io/_uploads/SJZFKjO1kg.png)

```
//作為共同的base class
class Furniture{
protected: int weight;
public:
    void SetWeight(int a=0){weight=a;}
    ...
};

//Sofa
class Sofa: virtual public Furniture {
public: void sit(){
    cout << "sit" <<endl;}
};

class Bed: virtual public Furniture {
public: void lie(){
    cout << "lie" <<endl;}
};

//Sofabed
class Sofabed:public Sofa, public Bed{
public: void fold(){
    cout << "fold" <<endl;}
};

//
int main()
{
    Sofabed obj;
    obj.SetWeight(100);//因為使用虛基類，所以是Furniture的SetWeight，把她餵進Furniture的void SetWeight。
    
    return 0;
}
//Bed
```

## 🖊️ 建構子和解構子的執行順序⭐
1.從**宣告的順序**，而非始化順序找虛基類是誰，先做虛基類的初始化，做完以後才找其他類別的初始化，以下圖為例，由於宣告順序是CB再來CC，所以會從CB找到虛基類CA，初始化CA->CB->CC。

![螢幕擷取畫面 2024-10-13 111126](https://hackmd.io/_uploads/SkQO5nd1ke.png)

2.解構子是從相反順序

![螢幕擷取畫面 2024-10-13 111313](https://hackmd.io/_uploads/ByG1i2dkJg.png)


![螢幕擷取畫面 2024-10-13 111240](https://hackmd.io/_uploads/HyCn5n_k1e.png)



## 🤔 疑問
目前無


## 📖 下一章節主題預告
多型


