---
title: '[筆記]物件導向程式設計ch.6_i/o stream、file stream、string stream'
tags: [物件導向程式設計]

---

 # [筆記]物件導向程式設計ch.6
:::info 
:bulb: 本筆記內容源自溫宏斌老師的物件導向程式設計OCW。
:::

## :+1: 章節重點

### :small_blue_diamond: i/o stream
### :small_blue_diamond: file stream
### :small_blue_diamond: string stream 


## 🖊️ i/o stream
相較於C只提供低階的檔案讀取方式，C++對高階和低階都有提供。

雖然低階讀取方式可以處理較快速處理大資料量，不過這邊特別討論高階讀檔是因為，一般檔案都不會太大量，且資料已格式化成有意義的資料群，比如4 bytes會知道是要讀整數。

(一)串流函式庫的繼承關係圖:
iostream函式庫由istream(從串流萃取資料)和ostream(把資料推入串流)函式庫(類別)組成，該兩者又是從ios輸入輸出函式庫繼承而來。
![螢幕擷取畫面 2024-10-10 100304](https://hackmd.io/_uploads/Sy0ckGSJyl.png)


(二)cin與cout
cin/cout本身是iostream所宣告出的物件，因為是物件，所以提供了很多class member(functions & data)可以使用。

兩者cout 具有**多型**(Polymorphism，允許不同類型的物件以相同的介面進行操作，後續會再談)的觀念，通常體現在它們可以處理不同類型的數據。例如，cout 可以處理不同類型的數據，像是整數、浮點數、字元和字串。這是因為 ostream 類對不同類型的數據**重載**了 operator<<。

1.cin
(1) cin會搭配 >> 符號
`cin >> somevariable`
(2)作為物件，cin可搭配使用的成員函式
- get():抓取串流中未格式化的資料
```
//輸入別名參數
//return a reference to object
istream& get(char &);
//get可以連續使用
//原因:每次調用 get() 後，仍然返回輸入流對象本身
//所以可以對同一個輸入流進行多次連續操作。
char first,middle,last;
cin.get(first)
cin.get(middle).get(last);
```

描述的仔細一點是，第一次調用 get(middle) 從輸入流中讀取一個字符到 middle裡面，並返回 cin（istream&）。因此，接下來可以立即再調用 .get(last) 從同一個輸入流中讀取下一個字符到 last。

get()還有其他表現形式:
```
//可以不放參數
//回傳integer
int get();

//或放很多參數，當get()被重載時
istream& get(char *str, int len, char c ='\n')
```

- getline:抓取串流中的一行行資料
使用方式和前者第三種表現方式一樣。
`istream& getline(char *str, int len, char c ='\n');`
不過，他必須要分配空間給str，不然會遇上違法使用記憶體的情況，而出現segmentation fault。意思是，通常會用這種方式補救`char cline [256]… `靜態配置

- ignore():選擇從第幾個字開始抓取資料
`istream& ignore(int length = 1, char c ='\n');`

2.cout
(1)cout會搭配 << 符號使用
(2)可搭配使用的成員函式
- setf():控制輸出數據的顯示格式，如`ios::left / ios::right`左對齊或右對齊數據。
```
cout.set(ios::dec);
cout << 4.2;
```
- unsetf():還原成預設的格式化設定。
- precision():用來設置浮點數輸出的精確度。
- width():用來設置每次輸出的寬度。

※補充:與i/o manipulators（輸出操縱器）相比
輸出操縱器像是 setprecision() 和 setw() ，是專門用來操縱輸出格式的函式，它們通常是在 iostream 庫中以**非成員函式的形式**，直接在輸出流上使用。例如：
```
cout << setprecision(3) << 3.14159;  // 使用i/o操縱器設置精度
cout << setw(10) << 123;  // 設置輸出欄位寬度
```


## 🖊️ file stream
(一)檔案串流函式庫的繼承關係圖:
檔案串流是繼承iostream來的，輸入檔案串流也是繼承輸入串流來，輸出檔案串流也是繼承輸出串流來的。**檔案串流串可以想像成輸入串流和輸出串流的子集合**。
![螢幕擷取畫面 2024-10-10 162613](https://hackmd.io/_uploads/BJ2hJfrk1e.png)


(二)檔案串流會使用到的函式庫
`#include<iostream>`和`#include<fstream>`

(三)輸出檔案串流
1.格式
輸出檔案串流包含object的名字，後面加上檔名，如此一來，檔案串流和外面實體檔案就會形成連結，以便讀取外面檔案的內容。
`ostream outFile("Data,txt")`
或是
```
ostream outFile;
outDFile.open("Data,txt");
```

2.打開檔案的模式:
`ios:in `為了輸入而打開檔案，`ios:out`為了寫入而打開檔案(預設)等。

💡重點提醒:要先檢查開檔案有無成功(可搭配good()/bad()使用)，有的話才會接續寫入的動作。如果沒開成功要馬上跳出通知，範例如下:

```
#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;
    
int main(){
    fstream myfile;
    myfile.open("test.dat", ios::in);
    if (myFile.good())
        cout << "File opened!" <<endl;
    else
        cout << "Cannot open!" <<endl;
    return 0;
}
```


除此之外，雖然說istream有提供解構子會自動關閉檔案，但是還是可以使用close()自行關閉檔案。

(四)輸入檔案串流
1.格式
讀取檔案，用ifstream輸入檔案串流
`iftream someData("Data,txt")`

2.輸入檔案串流也有open,close()用法，還有file modes，也可以另外呼叫close()，以釋放資源。


## 🖊️ string stream ⭐
(一)字串串流函式庫的繼承關係圖:
iostream的延伸，stringstream分成istreamstream/ostreamstream。
![螢幕擷取畫面 2024-10-10 110017](https://hackmd.io/_uploads/SkjikGry1l.png)


(二)istringstream與ostreamstream

1.istringstream

(1)範例
```
string buffer;
getline(cin,buffer);
**istringstream** inStr(buffer);
long value = 0;
double data = 0.0;
`inStr >> value >> data`;
```
(2)上述程式碼說明:
由於字串串流隨時可以變成字串，也可以吃字串(方便串流和字串間轉換而設計)。
假設今天設計一字串叫buffer，然後從鍵盤上讀一行line讀進buffer裡面，但發現讀入後很不好用，該怎麼辦?

宣告一個istringstream inStr(buffer) ，**istringstream 可以將一個字串轉換成串流**，把字串以sequence of byte的方式重新推到串流裡面，又串流化了

接下來，我們可以從 inStr 這個串流中使用輸入運算符 >> 提取數據。這裡的 inStr >> value >> data; 會依次從 buffer 中讀取兩個數值，一個是 long 類型的 value，另一個是 double 類型的 data。
 
(3)串流化的好處
這樣做的好處是，istringstream 可以很方便地處理字串中的數據。假設我們在 buffer 中有兩個數字，例如 "1234 56.78"，通過 inStr >> value >> data; 可以輕鬆地將 1234 解析成 long 類型的 value，並將 56.78 解析成 double 類型的 data。

總結來說，這種「串流化」的操作讓我們可以像從 cin 或檔案中讀取數據一樣，從字串中提取數據，非常適合用於數據的解析和處理。

2. ostreamstream
(1)範例
```
osstringstream outStr;
double number = 2.5;
outStr << "number = " << (3*number/2);
string output = outStr.str()

stringstream ss; 
int data = 200;
int result;
ss << data;
ss >> result;
```
(2)上述程式碼說明:
以前需要把數字對應到字串(switch case)，用這個方法就不用了，直接把2.5用**outStr <<推到osstringstream裡面**，他自動會轉成字串。使用上只需要**outStr.str()**，就會**把串流轉成字串**，寫進output。

Stringstram ss;也可以不限定是輸入或輸出字串[可雙向操作]，可以對他抓資料，也可以對他推資料。



## 🤔 疑問
目前無


## 📖 下一章節主題預告
繼承


