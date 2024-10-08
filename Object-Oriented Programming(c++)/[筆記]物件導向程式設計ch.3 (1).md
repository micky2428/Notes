---
title: '[筆記]物件導向程式設計ch.3'
tags: [物件導向程式設計]

---

# [筆記]物件導向程式設計ch.3
:::info 
:bulb: 本筆記內容源自溫宏斌老師的物件導向程式設計OCW。
:::

## :+1: 章節重點

### :small_blue_diamond: 類別的基本概念_data member、member function


## 🖊️ 類別

(一)基本定義
類別是OOP的基礎，其中的變數是物件。
如OOP基本概念筆記所述，類別是物件的抽象化，每個物件是類別的實例。
常見的作法是先宣告類別，再宣告物件，如下所示:

```
class someclass
{
    ....
};
someclass obj1, obj2...;
```
(二)範例

類別由data member(變數)和member function(方法)組成。
```
//Airticket.h
#include <string>
class AirTicket {
    private:            //定義兩種資料
        std::string name;
        int miles;
    public:             //定義六種方法
        AirTicket();    
        ~AirTicket();   
        std::string getName();
        void setName(std::string inName);
        void setMiles(int inMiles); //透過setMiles把inMiles設定到private的miles裡面
        int calculatePrice();
    }
```
由於實際上同一類別下不同物件所使用member functions都是相同的。為了避免浪費記憶體，C++在member functions這塊是共想記憶體的，在data members部分才是由各物件各自宣告。



(三)member function
Class失去member functions，跟struct幾乎一模一樣，差別在struct針對成員的預設存取權限是public，class的預設值是private。

1.把宣告和實體分開
這麼做的好處在於可以隱藏資訊和保護財產權，尤其是對軟體vendor來說。
```
class CScore
{
private:
    char name[20];
    int  subj[2];
public:
    double computerAverage();
    void setName(char *inName);
};
//功能的實體寫在外面
inline double CScore::computerAverage()
{
    return (subj[0]+subj[1])/2.0;

}
```

2. preventing multiple declarations
```
//假設之前都沒看到circle.h
#ifndef CIRCLE_H
//我就來定義這個符號
#define CIRCLE_H
class CCircle {
...
};

#endif
```


4. accessor和mutator
(1)accessor:寫get function讀取private data
`returnType getPropertyName()`
(2)mutator:寫set function，來做更新、覆寫
`void setPropertyName(datatype value)`
(3)範例
```
class CScore
{
con
private:
    char name[20];
    int  subj[2];
public:
    double computerAverage(){
        return (subj[0]+subjp[1])/2.0;
    };
    //mutator
    void setName(char * inName){
        strncpy(name, inName, 20);
    }
    //accessor
    char *getName(){
        return name;
    }

```

4.建構函式(construtors)
指派值，寫進data member裡面，使用時機:創造物件時(物件初始化)，範例如下:
![圖片1](https://hackmd.io/_uploads/rkDAgFZJyl.png)
由上圖可已發現，建構函式有與其類別相同的名稱，且沒有回傳型態，需是public或protected。
5.解構函式(destructor):
收回記憶體用。
![圖片2](https://hackmd.io/_uploads/HJqgzF-1kx.png)

由上圖可已發現，解構函式的前面有~符號，沒有回傳型態和參數，需是public。

composition



(四)如何讀取物件裡的資料
1.點運算
```
//類別  物件
CScore stu1;
stu1.computerAverage();
```

2.指標
CScore * pStu 指到CScore類別的指標，取&stu1的位址。
用pStu底下的箭頭，循著現在位址找到實體，然後呼叫實體裡面的computeAverage() function。
```
CScore * pstu = &stu1;
pstu->computerAverage();
```

3.參考運算:宣告一變數時，讓他變成別名
rStu和stu1是同一塊變數，所以用rStu呼叫computeAverage() function。
```
CScore & rstu = stu1;
rstu.computerAverage();
```



## 🤔 疑問
目前無


## 📖 下一章節主題預告
類別的進階討論_this指標、修飾字、friend function

