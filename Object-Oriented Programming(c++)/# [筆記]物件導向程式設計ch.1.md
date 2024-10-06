---
title: '# [筆記]物件導向程式設計ch.1'
tags: [物件導向程式設計]

---

# [筆記]物件導向程式設計ch.1
:::info 
:bulb: 本筆記內容源自溫宏斌老師的物件導向程式設計OCW。
:::

## :+1: 章節重點

### :small_blue_diamond: 基本C++操作


## 🖊️  如何建立C++程式?

(一)預處理(preprocessor)
1.標明泛資訊(meta-information)之處，如#開頭的指導語句(directives)#include後面加的函式庫就是泛資訊。
2.常見的指導語句包含
 (1) #include <[file]>
 (2) #define[key] [value]，ex.#define π 3.14
 (3) #ifdef [key] #ifndef [key] #endif
(二)編譯(compiler)
把c++原始碼(Source code)翻譯成機器可讀的機械碼(Machine code)，所以翻譯完後就不能跨平台使用。
(三)連結器(linker)
作用在於連結各個編譯出來的物件，合併成執行檔(execution files)。

![螢幕擷取畫面 2024-10-03 223634](https://hackmd.io/_uploads/HJON2QnAA.png)
圖片來源:周志遠教授作業系統ch.8講義

## 🖊️  C++程式範例

```
#include<iostream>

int main(int argc, char **argv) 
{
    std::cout << "Hello"
              << std::endl;
    return 0;
}

```
1.main()程式執行時會找的第一個函式
2.int main() 表示回傳的值是整數
3.argc 在終端執行程式時，告訴你有多少個參數被傳遞給程式。
4.argv 字串陣列，argv[0]通常是程式的名稱或是程式路徑，之後的元素則是終端中傳入的參數。

## 🖊️  Namespaces
(一)作用是解決不同區塊程式之間的命名衝突
(二)使用方式:
有兩份程式碼，一份叫myspace.h
```
namespace mycode{
    void foo(){
    ...
    }
}
```

另一份叫usernamespaces.cpp
```
#include "myspace.h"
using namespace mycode;
int main(){
    foo();
}
```
(三)如果沒有這樣的引用，就要用mycode::foo()標註函式來源。

## 🖊️  資料結構
(一)內建
1.列表:
![圖片1](https://hackmd.io/_uploads/SkiK1NhCA.png)
圖片來源:溫宏斌老師物件導向程式設計L1

2.C++可以做資料轉型
(1)方法1:assign給someBool以前就把整數轉成Boolean
```
bool someBool = (bool)someInt;
```
(2)方法2:宣告一個沒有名字的boolean變數，然後把它初始成SomeInt的值，再把這個boolean變數compute到另一個變數someBool裡
```
bool someBool = bool(someInt);
```
(3)方法3:編譯前強制靜態轉型的方法
```
bool someBool = static_cast<bool>(someInt);
```
(二)使用者定義
1.列舉型態(enumerated type)
```
enum fruit {  //fruit:typename
    apple,    //id1
    banana,   //d2
    lemon,
    mango,
    orange
};
```
2.struct type
```
struct tagename
{
    type_1 member_1;
    ...
};
```

## 🖊️ for loop 與 while loop
(一)for loop
```
for (int i = 0; i< 5; i++){
    cout << "good!" <<endl;
}
```
(二)while loop
```
int i = 0;
while (i < 5){
    cout << "good!" <<endl; 
    i++;
}
```
## 🖊️ Function
(一)由三個部分組成，且缺一不可
1.宣告(protype or signature，函式原型或稱標籤，定義函示要怎麼存取)
2.定義
3.呼叫
```
//宣告
double totalCost(int num,double price);
//定義
double totalCost(int num,double price){
    return (num*price*1.05)
}
//呼叫
totalCost(8,9.5); 
```


| double | totalCost | int num,double price |
| -------- | -------- | -------- |
| 回傳型態     | 函式名稱     | 參數     |

(二)inline function
加上inline讓函式可以在每次被呼叫時，不用重新連結(link)。效果就是只要看到area這個函式，就用return(len*wid)替代掉。通常用於一兩行可以結束的程式。
```
inline float area(float len, float wid){
    return (len*wid);
}
```

## 🖊️ C++的記憶體管理議題
(一)C++程式的記憶體由stack和heap組成
(二)function有自己的stack frame
1.可以隔離各自程式的記憶體空間
2.如果f1()呼叫f2()，會出現一個新的frame在f1()上面，此時f1()內的變數var看不到f2()。當拿掉f2()的stack frame(不再占用記憶體)，又可以看到f1()。
3.C ++中的array就是因此需要先訂大小，也就是說
```
int arraysize = 10;
int MyArray[arraysize];
```
會出現無法預期的狀況。->解法:只能變成動態array(使用pointer)
```
int* MyVariableSizeArray; //先定義指標
int* MyVariableSizeArray = new int[arraysize];  //初始化指標成heap
MyVariableSizeArray[3] = 2;
delete [] MyVariableSizeArray; //需要手動回收
```

(三)heap
1.和stack比，結構較鬆散，且沒有先後的觀念。
2.動態宣告會使用Pointer*，而動態變數的宣告不會因為function出現而出現或消失而消失。

## 🖊️ Array
1.C++中array的大小是常數，呈上所述是因為stack frame size是事先決定的。
2.array是由同樣的資料型態所組成。
```
char ticTacToe[3][3];
for (int idx=0; idx<3; idx++){
    for (int jdx=0; jdx<3; jdx++){
        ticTacToe[idx][jdx] = 'x';
    }
}
```

## 🖊️ 指標的運用
指標和heap memory有很大關係。
(一)透過**解參考**(derefrencing)的方式，指向單一的值
```
int * MyIntPtr = new int; //在heap裡面找一個沒有名字的int的空間，把它的位置回傳給MyIntPtr
*MyIntPtr = 8;            //循著指標變數*MyIntPtr指到的位置存取到int的空間，並把它寫成8
```
(二)用**取位置**(&)的方式讀到既有變數stack variable的值
```
int i = 8;                //在compile以前就配置好
int * MyIntPtr = &i;      //循著指標變數*MyIntPtr指到該值的位置
```
(三) 指向struct變數，並搭配**解參考**和**箭頭**
```
EmployeeT * Worker = getEmployee(); //取到getEmployee()的位置，並將位置寫到指標*Worker
cout << Work->salary << endl; //Worker可以指到EmployeeT內的一個變數(如salary)
```

## 🖊️ C++中的string
(一)範例

1.佔了stack memory的20個字元
```
char cString[20] = "Hello, World";
```

2.只佔剛剛好的stack memory(13個字元)

```
char* ptrString[20] = "Hello, World";
```

(二)不同於C要用strcmp()，有==的用法
```
cout << (str4 == 'Monday')? "yes":"no"
     << endl;
```


## 🤔 疑問
暫無


## 📖 下一章節主題預告
        
物件導向程式設計(Object-oriented programming,Oop)，本節課重點在於封裝(encapsulation)、繼承(inheritance)和多型(polymorphism)。
