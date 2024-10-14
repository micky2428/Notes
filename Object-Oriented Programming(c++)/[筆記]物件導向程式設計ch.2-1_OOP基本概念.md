---
title: '[筆記]物件導向程式設計ch.2-1_OOP基本概念'
tags: [物件導向程式設計]

---

# [筆記]物件導向程式設計ch.2-1
:::info 
:bulb: 本筆記內容源自溫宏斌老師的物件導向程式設計OCW。
:::

## :+1: 章節重點

### :small_blue_diamond: OOP基本概念


## 🖊️ OOP定義與範例

(一)基本定義
1.OOP是程式設計的風格。相較於程序化程式設計(procedural programming)較注重功能性，OOP除了功能性外，也會注重data，適合大而複雜的程式。
比如下圖是程式化的寫法，但是當要加上第四人時，會改動到程式實體，在過程中較易產生錯誤。
```
struct SScore{
    char name[20];
    int subj[3];
};
double computeAverage(SScore one){
    return (one.subj[0]+one.subj[1]+one.subj[2]+/3);
}
```


2.名詞定義:
Object = data fields + methods(每個物件有自己的實體、狀態(data filed，內存資料)和行為(所有函式的集合))
program = object + object + ... + object(物件之間的作用)

★★<font color="#AC19C9">類別是物件的抽象化，每個物件是類別的實例。</font>我們用抽象的類別(不佔memory)來宣告他的結構和會做什麼事情。但由這個結構產生出具體的物件(佔memory)才是具有實體的東西，下圖4-1和4-2舉例如何建構stack-based和heap based object。

(二)範例
1.建立類別
```
//Airticket.h
#include <string>
class AirTicket {
    private:            //定義兩種資料
        std::string name;
        int miles;
    public:             //定義六種方法
        AirTicket();    //建構子(constructor)
        ~AirTicket();   //解構子(destructor)，自動刪除空間
        std::string getName();
        void setName(std::string inName);
        void setMiles(int inMiles); //透過setMiles把inMiles設定到private的miles裡面
        int calculatePrice();
    }
```
2.定義方法實體(建構子和解構子)
```
//Airticket.cpp  //常用相同名字.cpp來定義動作的實體
#include <iostream>
#include "Airticket.h"
using namespace std;

//constructor
//每次建構物件時，就會初始化name和miles的值，分別設成unknown和0
AirTicket::AirTicket() {
    name = "unknown";
    miles = 0;
    }

//destructor
AirTicket::~AirTicket() {
    name = "unknown";
    miles = 0;
    }
```

註:雖然在此解構子無事可做，但是遇到動態空間分配(如在AirTicket:: AirTicket()分配空間)時，解構子就要還回空間，不然會產生memory garbage。

3.定義方法實體(getName、setName和setMiles)
```
//Airticket.cpp  //常用相同名字.cpp來定義動作的實體

//getName[宣告std::string getName();]
string AirTicket::getname() {  
    return name
    }

//setName[宣告void setName(std::string inName);]
void AirTicket:: setName(string inName) {
    name = inName;       //不像C string需要透過拷貝，用=即可
    }

//setName[宣告void setMiles(int inMiles);]
void AirTicket::setMiles(int inMiles) {
    miles = inMiles;
    }

//calculatePrice[宣告int calculatePrice();]
int AirTicket::calculatePrice(){
    int rPrice = 0;
    if (miles > 10000)
        rPrice = (int) (miles*0.095);
    else
        rPrice = (int) (miles*0.1);
    return rPrice
}
```
4-1. 若是建立stack物件(用靜態記憶體處理)
ch.1有說main()是程式執行時會找的第一個函式，在此主程式我們命名為main.cpp。
```
//main.cpp  //常用相同名字.cpp來定義動作的實體

#include <iostream>
#include "Airticket.h"
using namespace std;

int main(int argc, char ** argv {
    AirTicket tkt1;  //建立一個stack物件(沒有加上任何*)
    
    tkt1.setName("Peter");
    tkt1.setMiles(25000);
    
    cout << tkt1.getName() << "pays" 
         << tkt1.calculatePrice() << endl;
    ......

```

4-2. 若是建立heap物件(用動態記憶體處理)
ch.1有說main()是程式執行時會找的第一個函式，在此主程式我們命名為main.cpp。
```
//main.cpp  //常用相同名字.cpp來定義動作的實體

    ......
    AirTicket *tkt2 = new AirTicket ;  //new配置空間
    
    tkt2->setName("Clara");
    tkt2->setMiles(35000);
    
    cout << tkt2->getName() << "pays" 
         << tktl2->calculatePrice() << endl;
    
    //使用動態記憶體時，要自己刪除(當初創建出來無名字的物件)
    delete tkt2;
    
    return 0;
}

```
4.終端執行
執行(compile)他以後會產生.o檔，就是讓機器讀的語言。
Linker就是把AirTicket.o和Main.o 連接起來成一個主程式。
(流程圖見ch.1筆記)
```
>ls                         //AirTicket.cpp AirTicket.h main.cpp
>g++ -c AirTicket.cpp 
>g++ -c main.cpp
>g++ -o prog AirTicket.0 main.0  //g++ -o 加要link起來的程式碼，link起來以後的程式叫做prog
>ls                         //AirTicket.cpp AirTicket.h AirTicket.0 main.cpp mian.o prog
>make                       //快速compile程式的工具
>./prog                     //Peter pays xxx...
```

    

## 🖊️  存取修飾詞(Member access modifier)
(一)定義
存取修飾詞是用來來控制class在不同的class與package之間的關係。同時也是封裝性（Encapsulation）實踐的方式。

封裝的概念就是在程式碼中設置權限，讓不同的物件之間有不同的存取限制，而不是把所有資料都攤在陽光下讓大家使用。

(二)種類
從「OOP定義與範例」中範例的第一點，可以看到class的定義，在定義class時，資料成員(data member)和成員方法(member functions)主要有三種修飾符可以使用，用來決定「什麼成員可以存取類別/實體裡面被定義的資料」。依據類別中**資料或函式的開放程度**可分為**Public、Private、Protected。**


| Public | Private(class預設) | Protected |
| -------- | -------- | -------- |
| 完全開放給**所有人**使用 | 只開放給**同類別的其他成員**| 只開放給**同類別的其他成員**或著是**衍生出來**的類別(子類別的成員可以存取到父類別裡的成員)。承接**繼承**的觀念而來 |



## 🖊️  封裝、繼承和多型 ⭐ ⭐ ⭐
OOP三大重點核心特性:
(一)	**封裝（Encapsulation）**：把資料和函式綁定在膠囊內，把物件實體看成是資料和函式的組合，只保留特定的方法與外界聯絡。封裝可避免資料被破壞，增加資料的安全性。
(二)	**繼承（Inheritance）**：新程式(子類別)多從舊程式(父類別)來，優點減少重複開發相類似的功能。
(三)	**多型(物件多樣化，Polymorphism)**：在不同物件上使用相同功能的函式。
(vs.C++在重載函式設定上可以用相同名稱，不同參數。但和多型的觀念不同，這裡是定義在物件[資料和函式]上的，不過，不可否認多型的觀念包含了重載函式的觀念，因為可以在不同物件上使用同樣的函式)



## 🤔 疑問
Q1.python有Public、Private、Protected的概念嗎?
A1:
Python 沒有像 C++ 或 Java 這樣的明確的訪問控制符號（如 public, private, protected）。Python 透過命名慣例來表示。private用雙底線，protected用單底線。

Q2.python有封裝、繼承和多型的概念嗎?
A2:
1.封裝
Python 主要透過命名慣例來實現封裝。
```
//透過在屬性或方法名稱前加上雙底線 __，表示該屬性或方法是private。
class MyClass:
    def __init__(self):
        self.public_var = "公共變數"
        self.__private_var = "私有變數"

    def __private_method(self):
        print("這是私有方法")

obj = MyClass()
print(obj.public_var)  # 正常訪問
print(obj.__private_var)  # 無法訪問，會報錯

//透過在屬性或方法名稱前加上單底線 _，表示該屬性或方法是protected。
class MyClass:
    def __init__(self):
        self._protected_var = "保護變數"
```

2.繼承
Python 支援類別繼承，子類別可以繼承父類別的屬性和方法，並且可以覆寫（override）父類別的方法。
```
class ParentClass:
    def say_hello(self):
        print("Hello from Parent")

class ChildClass(ParentClass):
    def say_hello(self):
        print("Hello from Child")

child = ChildClass()
child.say_hello()  # 覆寫並呼叫子類別的方法
```
3.多型
多型的實現依賴於方法覆寫。
```
class Animal:
    def sound(self):
        raise NotImplementedError("子類別必須實現這個方法")

class Dog(Animal):
    def sound(self):
        return "汪汪"

class Cat(Animal):
    def sound(self):
        return "喵喵"

animals = [Dog(), Cat()]

for animal in animals:
    print(animal.sound())  # 根據物件的具體類別，呼叫對應的 `sound` 方法
```


## 📖 下一章節主題預告
指標(*)、參考(&)和動態記憶體分配

