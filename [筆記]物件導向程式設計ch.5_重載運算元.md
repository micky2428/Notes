---
title: '[筆記]物件導向程式設計ch.5_重載運算元'

---

# [筆記]物件導向程式設計ch.5
:::info 
:bulb: 本筆記內容源自溫宏斌老師的物件導向程式設計OCW。
:::

## :+1: 章節重點

### :small_blue_diamond: 重載運算元(overloading operator)

## 🖊️ 重載運算元
(一)為什麼需要重載運算元
1.提高可讀性和可維護性:舉例來說，c1 + c2 比 c1.add(c2) 更直觀。
2.提供簡化操作:開發者可以直接對兩個物件進行加減乘除等數學運算。

(二)定義
1.概念上類似重載函式
2.運算元本身就是function的名稱

※複習: 函式若可以重載，表示他有同名的函式，但有不同的回傳型態、不同參數的個數和型態。

(三)重載運算元的方法有二:

|  | 重載成員函式 |重載友緣函式 |
| -------- | --------  |--------  |
| 重載方法   |透過member function完成 | 透過外部的friend function完成|
| 常用於   | 雙元運算元|單元運算元 |

※註1:單元是指只接一個運算子(像是x-=y)，雙元指的是後面接了兩個運算子。

※註2:成員函式方便處理雙元運算元，是因為它自帶隱含的 this 指針。實際上，**兩者都可以重載單元和雙元運算元**。

※註3:如果用member function，當有**雙元**運算元，第一個運算元會當成呼叫函式的人，所以她**只會吃一個參數**。若是**單元**，()裡面就**沒有參數**。

Friend function因為函式在外面定義，**binary吃兩個參數，uniary吃一個參數**。
當兩者都吃一個參數時，有可能會混淆member function和friend function，但實際意義上有不同。


1.用成員函式重載(雙元)的例子
```
class CComplex{
    double real, imag;
public:
    CComplex(){real = 0; imag=0;}
    CComplex(double r, double i){
        real=r, imag=i;}
    CComplex **cdd**(CComplex & o2);
    void display(){...}
};
//將兩個 CComplex 物件相加
CComplex CComplex::**cadd**(CComplex & o2){
    CComplex c; c.real=real+o2.real;
    c.image=imag+o2.imag, return c;
}
```

2.用友緣函式重載(雙元)的例子
```
class CComplex{
    double real, imag;
public:
    CComplex(){real = 0; imag=0;}
    CComplex(double r, double i){
        real=r, imag=i;}
    **friend** CComplex operator+(CComplex & o1,CComplex & o2);
    void display(){...}
};

CComplex operator+(CComplex & o1,CComplex & o2){
    return CComplex(o1.real+o2.real, o1.imag+02.imag)
}
```

(四)可以重載的運算元包含:
![圖片1](https://hackmd.io/_uploads/r14spEEkkx.png)

(四)不能重載的，不然運算上會出問題⭐⭐
1.	點運算
2.	指標(*)
3.	範圍界定符號(::)
4.	條件(?:)
5.	Sizeof
6.	自創的符號
7.	已經是內建的資料型態



## 🤔 疑問
目前無


## 📖 下一章節主題預告
i/o

