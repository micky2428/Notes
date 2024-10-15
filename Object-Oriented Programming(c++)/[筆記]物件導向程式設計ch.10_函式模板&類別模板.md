---
title: '[筆記]物件導向程式設計ch.10_函式模板&類別模板'

---

# [筆記]物件導向程式設計ch.9
:::info 
:bulb: 本筆記內容源自溫宏斌老師的物件導向程式設計OCW。
:::

## :+1: 章節重點

### :small_blue_diamond: 函式模板
### :small_blue_diamond: 類別模板

## 🖊️ 函式模板
(一)概念
1.函式模板也是一種函式，使用了**可變的資料型態**(尚未決定資料型態，還沒實體化)。
2.函式模板勾勒出一群函式，這些函式的差別在於參數的資料型態不同，所以和重載(差在參數個數可能不同)還是有一點差異。
3.函式模板實體化以後會產生**模板函式**(template functions)。
4.當呼叫函式模板時，編譯器會依據你傳的實際參數決定他要怎麼產生這個函式的實體程式碼。

(二)範例
函式模板的優點在於可以讓重載函式不那麼麻煩。
舉例而言:
```
//重載函式的傳統作法:需要個別定義
void swap(int& r1, int& r2){
        int tmp = r1;
        r1 = r2;
        r2 = tmp;
}

void swap(long& r1, long& r2){
        long tmp = r1;
        r1 = r2;
        r2 = tmp;
}

//使用模板以後
//這裡的T不一定要是自定義類別
template <class T>
void swap(T& t1, T& t2){
    T tmp = t1;
    t1 = t2;
    t2 =tmp;
}
//隨著T(資料型別)改變，產生不同函式的實體
```

![螢幕擷取畫面 2024-10-15 202642](https://hackmd.io/_uploads/SkZWn1hJ1l.png)


(二)重載函式模板
模板同名異式，**但參數個數要一樣**，範例如下:
```
template <class T>
T FindMax(T x, T y){
    T max =x;
    if (y > max)
        max =y;
    return max;
}
```

(三)參數不只type T，還有其他已知資料型態的參數

```
template <class T>
void repeatVakue(**T val, int times**){

    for (int x = 0; x < times; ++x){
        cout <<"#" <<(x+1)<< "" <<val <<"\n";}

class Store{
    int storeid;
    string address;
    string manager;
public:
    Store(int sid, string add,string mgr){
        storeid = sid;
        address = add;
        manager = mr;}
    friend ostream& operator<<(ostream&, Store);
};
```

## 🖊️ 類別模板
(一)概念
1.類別模板可當成一個類別的框架來產生很多類別。
2.實際上類別產生的時間是編譯時(同函式模板)。
3.使用到的類別會單獨產生，例如當有使用到整數的時候，才會產生整數的實體。
4.優點:提升使用性，降低開發的時間。
5.只要發現有一資料型態是未設定的，就可以寫類別模板。

(二)舉例

```
template <class T>
class Number{
    **T number**;
public: 
Number(T val){number=val;}
void ShowNumber(){
    cout << "Number=" << number << "\n";
    }
};

//main()
Number<int> a(65); a.SShowNumber();
Number<double> b(8.8); a.SShowNumber();
```

## 🖊️ 模板的其他討論:友緣和繼承
(一)在模板類別可以用到友緣函式，使用方法和一般類別一樣。

(二)在繼承關係上也是相同，可以產生衍生模板類別。
```
//基礎類別
template <class T>
class TBase{
private:
    T x,y;
public: 
    TBase(){}
    TBase(T a, T b): x(a), y(b){}
    ~TBase(){}
    T getX();
    T getY();
};

template <class T>
//因為函式內容在外面定義，所以要加上界定符號::
T TBase<T>:getX(){return x;}

template <class T>
T TBase<T>:getY(){return y;}

//非類別模板繼承類別模板:TDerived1不是類別模板，因為參數的資料型態都已確定
class TDerived1: public TBase<int>{
private:
    int z;
public: 
    TDerived2(int a, int b, int c):
        TBase<int>(a,b), z(c){}
    T getZ() {return z;}
};

//類別模板繼承類別模板:TDerived2也是類別模板
//繼承時保留class T，讓T保留彈性，並另外用T宣告Z變數
template <class T>
class TDerived2: public TBase<T>{
private:
    T z;
public: 
    TDerived2(T a, T b, T c):
        TBase<T>(a,b), z(c){}
    T getZ() {return z;}
};
```





## 🤔 疑問
無

## 📖 下一章節主題預告
經典讀物<<Clean Code>> ch.1 無暇的程式碼重點整理
