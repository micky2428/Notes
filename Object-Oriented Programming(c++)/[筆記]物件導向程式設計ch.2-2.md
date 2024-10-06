---
title: '[筆記]物件導向程式設計ch.2-2'
tags: [物件導向程式設計]

---

# [筆記]物件導向程式設計ch.2-2
:::info 
:bulb: 本筆記內容源自溫宏斌老師的物件導向程式設計OCW。
:::

## :+1: 章節重點

### :small_blue_diamond: 指標(*) 
### :small_blue_diamond: 參考(&)
### :small_blue_diamond: Const的討論
### :small_blue_diamond: 動態記憶體分配
### 🔖 本章重點比較表格:

|  | * | & |
| -------- | -------- | -------- |
| 宣告 | 指標| 別名呼叫 |
| 使用 | 解參考| 取出位址(Address of Operator) |


## 🖊️ 指標(Pointer)

(一)基本定義
指標是程式的重要概念，指涉的可以是**變數**、**指標**和**函數的位址**。
1.指涉變數位址的例子
- 直接
```
int *ptr1
//任意資料型態(先不定義內容)的變數
void *ptr2
//如ch.2-1自定義的變數
AirTicket *ptr3  
```
- 間接:解參考(Dereferencing)，**結合**取出位址符號(&)使用
```
float x = 2;
//指標pt中存放一個float變數的位址
float *pt;
//&會把x的記憶體位置抓出來，再assign到左邊的pt去，此時x的記憶體位置就會寫入pt裡面
pt = &x;
```

2.指涉指標位址的例子，如下例的變數c
```
float a = 1, *b, **c;
b = &a
c = &b
```

3.指涉函數位址的例子
由於每個function block在code section都有自己記憶體位置，就可以找指標指向這個位置
```
int fc1 (char x, char y);
//function pointer
int (*fp) (char a, int b);
fp = fc1;
fp = fc1("x",5); //錯誤，因為fc1應該要返回int，而非function pointer
```
:bulb:注意:function pointer會加上()，避免誤會成回傳是pointer!

4.指涉array中元素位址的例子
比index快

|  | array indexing | pointer notation |
| -------- | -------- | -------- |
|  第0位    | array[0]     | *array   |
|  第1位   | array[1]     | *(array+1)    |


※補充:什麼是code section?
記憶體中儲存可執行程式碼的區域。
下圖是一張說明multithreaded的圖，在多線運行時，最上排的code section data section和os資源(如檔案)是共享的。
![螢幕擷取畫面 2024-10-06 161612](https://hackmd.io/_uploads/rJDvDTkJ1g.png)

圖片來源:周志遠教授作業系統 Chap3 Processes Concept講義

(二)為什麼要使用指標
1.可以進行動態分配，避免浪費空間。
2.透過指標化直接修改實際參數(如果只是做call by value，改不到原來的參數。)

※ 補充:C++ 的求值策略(Evaluation strategy)-Call by Value, Call by Reference

|  | call by value | call by reference |
| -------- | -------- | -------- |
| 內容 | 參數引用的方式，單純是個數值，跟原本的變數毫無關聯| 引用變數而非數值 |
| 例子 | void add(int <font color="#AC19C9">a</font>, int <font color="#AC19C9">b</font>) | void add(int <font color="#AC19C9">*a</font>, int <font color="#AC19C9">*b</font>) 
 

舉例而言，由於call by reference是直接引用變數，所以呼叫函式以後，原本變數的值就會改變，如下例變數a所指涉到的位置中的值由6改為12。
```
void add(int *a, int *b) {
    *a = *a + *b;
}

int main() {
    int a = 6;
    int b = 6;
    add(&a, &b);        
    print("a = %d", a); // 這邊印出的是 a = 12
    return 0;
}
```


## 🖊️  參考(References)
(一)定義
參考被稱為淺型的pointer，它可以自動解參考(不需要*)，也就是可以自動取出被指到的值。
三種使用方式:
1.被視為獨立變數
:bulb:因為是幫別人取別名，參考對象和別名變數的資料形態要一致，在初始化就要宣告好!
```
double num = 0.07
double &refnum = num
```


2.作為參數傳遞給函數

以前面提過call by reference例子來說，語法更直觀，**不需要操作記憶體位址**。
```
//add.cpp
void add(int &a, int &b) {
    a = a + b;  
}
//main() in main.cpp
int main() {
    int a = 6;
    int b = 6;
    add(a, b);  
    cout << "a = " << a << endl;  // a = 12
    return 0;
}
```

3.由函式返回作為結果
```
//回傳的和傳入的東西用的是同一塊記憶體
int& fun(int *a, int i){
    //return a[i]這個變數(而非該變數的值) 
    if (i>0 && i<5) return a[i];
    else exit(0);
}

//iary:整數array
for (int idx=0; idx<5; idx++)
    //假設收到a[3] 會執行 a[3] = 3*2
    fun(iary,idx) = idx*2
```
:bulb:如果是int fun(int * a, int i)，就會錯誤，因為return的是int(a[i]的值)，非a[i]。



## 🖊️  Const的討論
避免函式無預警地改掉內容值，有時我們會使用constant，可分為四種類型:
1. a reference to constant
```
int x = 5;
const int& xref = x;
x = 33;         //原變數可以改變
cout << xref;  //33
xref = 15;     //前面已宣告別名變數只能讀不能改
```
3. a pointer to constant
```
int x = 5, y = 6;
const int *pt = &x;
cout << *pt;  //5
pt =&y;
cout << *pt;  //7
*pt = 11;    //錯誤，pt存取的記憶體位指可變，但位指解參考的內容不可變。
```
4. a constant pointer
常數指標，表示宣告以後指標的記憶體位址會被認為是常數，所以不能像前面更改存取的記憶體位址。Cpt指到的內容可
const 是用來修飾cpt的，只能永遠看&var1的位址
```
int var1 = 3, var2 = 5;
int * const cpt = &var1;
*cpt = 8; //8
cpt = &var2//錯誤，
```
6. a constant pointer to a constant(最嚴格)
```
const int v1 = 11, v2 = 22;
const int *cptc = &v1;
*cptc = 33     //錯誤
cout << *cptc; //11
cptc = & v2;
cout << *cptc; //22
```

## 🖊️  動態記憶體分配
(一)基本操作
不同於C常用malloc()和free()來操作動態記憶體分配，C++使用new和delete，範例如下:
```
//宣告一個指標dpt，並用new分配空間給他
double *dpt = new double(0,0);
if (dpt == NULL)
{
    cout << "insuffcient memory.\n";
    exit(1);
}
*dpt = 3.4;
//將空間還給heap
delete dpt;
```
值得注意的是，針對compile前已經宣告的變數，也就是使用stack記憶體的變數，如果只單純delete p不會真正消滅stack裡的p，而是歸還*p指到的位址。
```
int *p = new int(5);
delete pl
```
動態分配記憶體時，要注意有無歸還空間，避免浪費記憶體。

(二)如何創立動態Array
在資料結構課程中，一般的Array是a set of index and value，且大小是一開始就宣告好的。不過缺點是可能浪費記憶體空間。
於是，就有了dynamic arrays

```
int iSize = 0;
cin >> iSize;
typedef double* DoublePtr;
DoublePtr d;
//創設dynamic arrays
d = new double[iSize];
...
//歸還空間
delete []d;
//表示沒有指到任何真實空間
d = NULL;
```



## 🤔 疑問
Q1.python是Call by Value,還是 Call by Reference?
A1:Python 是Pass by Assignment。
引數傳的是物件的參照(Call by Object Reference)，但此處的Reference 是由 Pass by Value 的方式實作。
※參考文章: 
[Python 是 Pass By Value, Pass by Reference, 還是 Pass by Sharing？](https://medium.com/starbugs/python-%E4%B8%80%E6%AC%A1%E6%90%9E%E6%87%82-pass-by-value-pass-by-reference-%E8%88%87-pass-by-sharing-1873a2c6ac46)
[Python官方文件](https://docs.python.org/3/faq/programming.html#how-do-i-write-a-function-with-output-parameters-call-by-reference)



## 📖 下一章節主題預告
怎麼定義類別

