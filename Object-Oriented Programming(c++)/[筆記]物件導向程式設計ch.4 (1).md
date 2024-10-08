---
title: '[筆記]物件導向程式設計ch.4'

---

# [筆記]物件導向程式設計ch.4
:::info 
:bulb: 本筆記內容源自溫宏斌老師的物件導向程式設計OCW。
:::

## :+1: 章節重點

### :small_blue_diamond: 類別的進階討論_物件和指標間的互動、類別中的修飾字、friend function


## 🖊️ 物件和指標間的互動
在物件導向-指標(*)、參考(&)、動態記憶體分配的筆記中談了指標是程式的重要概念，指涉的可以是變數、指標和函數的位址。以下談論更多其與物件的互動:

1.呼叫類別底下的function

```
CScore *pStu = new (CName);
pstu->computeAverage();
delete pStu;
```
2.指標指向member function

```
//StuAry[2]是一個物件陣列(object array)
CScore * p1 = &(StuAry[2]);
cout << p1->computeAverage();
double (CScore:: *p2)() =
         &CScore::computeAverage;
cout << (p1->*p2)();
```
3.指標指向data member

```
class X{...}
//此時pa還沒有實體可以依附
int X:: * pa = &X::a;
//產生物件
X obj1;
//解參考以後obj1.a =10
obj1.*pa =10;
cout << "value a =" << obj1.*pa';
```
4.this pointer⭐⭐
This 指標保障了C++可以在所有data member在reference時，可以正確地透過member function，指到正確的資料位置。以下例來說:

```
class Box{
public:
    Box(int h = 6, int w=8, int l =10):
        hgt(h),wid(w),len(l){}
    int vol {return hgt*wid*len;}
private:
    int hgt, wid, len;
};

Box a(2,4,6), b(3,5,7);
```

若呼叫a.vol和b.vol，他們用的是同一個vol funtion，compiler要怎麼知道hgt,wid,len指到的是a還是b的值?

**所有member function都包含了this 指標**，就像是如果呼叫a.vol()，就等同於呼叫`(a->hgt)*(a->wid)*(a->len);`，帶入的就會是a的參數。

顯性使用的例子如下:
```
class Cpoint{
public:
    Cpoint offset(int diff){
        //位移量
        x += diff; y+= diff;
        //回傳這個點，並解參考回傳CPoint的物件回去給外面的人(定位x,y的功能)
        return *this
    }
};
```

## 🖊️ 類別中的修飾字⭐⭐
C++有許多修飾字可以選擇，本節課談到的有:

| 修飾字 | 作用 |
| -------- | --------  |
| static   | 把data member, member function定義成靜態成員|
| const   | 把data member, member function定義成常數|
| mutable   |用來搭配常數，有時我們希望常數是可變的|
| explicit   | 尤其呼叫constructor時，用來分辨到底是呼叫constructor還是在做assignment|



## 🖊️ friend function
(一)為什麼要了解friend function
雖然OOP提供的封裝性的優點在於保留資料的隱蔽性，但有時過度保護，會造成使用上的不便，friend function(友緣函式)可以突破class的限制。

(二)基本定義
friend function會**宣告在類的定義**裡，並有friend這個關鍵字，但因為不屬於類別(class)的一部分，要**定義在class的外部**，所以不能被繼承，但是卻可以取用class內的private member。

(三)使用時機
1.想在兩個以上的class間存取他們的資料時。
2.遇到overloading operator和i/o時 (後續筆記會談到)。

(四)範例

```
class CPoint{
    int x,y;
    //friend開頭，在class內宣告
    friend CPoint offset(CPoint &, int);
public:
    CPoint() {x = 0; y =0;}
    CPoint(int a, int b) {x = a; y =b;}
    void Print() {cout << x << "" 
                       << y << endl;}
};

//定義在class的外部
//若只是Cpoint offset應該讀取不到Cpoint的內部資料private data，但因為他是friend function，所以可以。
CPoint offset (CPoint &pt, int diff){
    pt.x += diff; pt.y+=diff;
    return pt;
}

//in main()
CPoint p1(3,5); p1.Print();
offset(p1,4);p1.Print();
```
## 🖊️ friend class
friend class是把friend的概念擴張。但要注意類別b是a的朋友，不代表逆向也通(one-way)。
(一)使用時機
當一類別的所有member function，都需要存取到另一類別的內部資料時。

```
//in CPoint.h
class CPoint{
    friend class CLine;
    int x,y;
    void Offset(int diff) {
        x += diff; y+=diff;}
    friend CPoint offset(CPoint &, int);
public:
    CPoint(){x=0;y=0;}
    CPoint(int a, int b){x=a;y=b;}
    void set(int a, int b){...}
    void Print(){...}
}

//in CLine.h
class CLine{
    CPoint p1,p2;
public:
    CLine(int...){...}
    void Print()(){...}
    void Display()(){...}
};

//in main()
#include "CPoint.h"
#include "CLine.h"

int main()
{
    CPoint p1(2,4);p2(6,8);
    p1.Print(); p2.Print();
    p1.Offset(3); //錯誤，因為main不是CPoint的friend，只有 CPoint 的 friend 類 CLine 可以訪問。
    CLine l1(1,3,5,7),l2(2,4,6,8);
    l1.Print();
    l2.Display();
    return 0;
}

//解法:將 Offset 函數改成公共成員函數或保持 Offset 為私有並使用 friend 函數，像是定義
CPoint offset(CPoint &p, int diff) {
    p.Offset(diff); 
    return p;
}

```


## 🤔 疑問
目前無


## 📖 下一章節主題預告
Friend的概念和重載運算元(overloading operator)


