---
title: '[筆記]物件導向程式設計ch.9_多型'

---

# [筆記]物件導向程式設計ch.9
:::info 
:bulb: 本筆記內容源自溫宏斌老師的物件導向程式設計OCW。
:::

## :+1: 章節重點

### :small_blue_diamond: 多型


## 🖊️ 多型
(一)概念⭐⭐
多型是OOP三大概念之一，包含之前提到
1.編譯(compile)時進行函式或運算元的重載(overloading)。
(1)與靜態綁定、Early-binding有關。
(2)優點:因為已經知道記憶體位置，可以直接跳過去，所以效率較好。

2.執行(runtime)時進行函式複寫(overriding)

(1)透過**繼承**和**虛函數**(Virtual function)的觀念完成。
(2)與動態綁定、Late-binding有關。
(3)動態多型的優點:
- 可以降低複雜度和開發的時間(減少重複開發
- 允許程式設計員設計共同介面，這個介面可以給不同但是相關的物件使用。


※補充:靜態與動態綁定
1.綁定
編譯器在記憶體裡面預留空間，給使用者定義(user-defined)的函式使用，且會為每個函式追蹤記憶體位址(memory addresses)，也就是說編譯器會建立出function table，讓每個函式能對應記憶體位置。

2.每個函式被綁定在函式位址上，函式位址(function addresses)就是記憶體裡function code的起始位置

3.靜態/動態綁定
(1)靜態綁定(早期/先期綁定)
- 編譯器在編譯時就知道某函式呼叫要連結到哪個記憶體位置。
- 具體而言，假設讀到f1()，編譯器會去查function table，看這個函式的記憶體位置在哪。

(2)	動態綁定(後期綁定)
決定是在執行時才決定某函式呼叫的位置，也就是說綁定的過程，取決於函式呼叫的順序，而函式呼叫的順序取決於user做的行為。

(二)範例
1.overloading
```
//基礎類別
class CPoint
{
    double x,y;
public:
    CPoint(double a=0, double b=0):
         x(a),y(b){}
    void SetPoint(double a =0, double b=0){
        x=a; y=b;}
    double GetX() const {return x;}
    double GetY() const {return y;}
    friend ostream & operator << (ostream &, const CPoint&);
    **string ToString() const{
        return "CPoint"**;
    }
};
//衍生類別
class CRect: public CPoint{
double lg,wd;
public:
     CRect(double a, double b,
         double c. double d):lg(c),wd(d)
         {SetPoint(a,b);}
     void SetRect(double a, doubel b, double c, double d)
         {SetPoint(a,b); lg=c;wd=d;}
     double GetL() const {return lg;}
     double GetW() const {return wd;}
     double Area() const {return lg*wd;}
     friend ostream & operator << (ostream &, const CRect &);
     **string ToString() const{return "CRect";**}
};

//int main()
{
    CRect cr1(2,3,20,10);
    cout << "old:" <<cr1<<endl;
    cr1.SetRect(5,5,9,7);
    cout << "new:" <<cr1 <<endl;
    //用CPoint宣告，overloading上面的函式，只會印出5,5
    CPoint &rRf = cr1;
    cout << "rRf:" <<rRf <<endl;
    return 0;
}
```

💡用什麼類別宣告reference，可以使用的範圍就會受到該類別的限制(只能用該類別的function)

2.virtual用法(Overriding)
```
//基礎類別
class CPoint	//base class: class CPoint
{		
    double x, y;
public:
    CPoint(double a=0, double b=0): 
		x(a), y(b) {} 
	void SetPoint(double a=0, double b=0) { 
		x=a; y=b;                      }
	double GetX() const { return x; }
	double GetY() const { return y; }
	friend ostream & operator << (ostream &, const CPoint&);
    **virtual** string ToString() const { 
		return "CPoint";	}
};
//衍生類別
class CRect: public CPoint{
double lg,wd;
public:
     CRect(double a, double b,
         double c. double d):lg(c),wd(d)
         {SetPoint(a,b);}
     void SetRect(double a, doubel b, double c, double d)
         {SetPoint(a,b); lg=c;wd=d;}
     double GetL() const {return lg;}
     double GetW() const {return wd;}
     double Area() const {return lg*wd;}
     friend ostream & operator << (ostream &, const CRect &);
     **string ToString() const{return "CRect";**}
};

class CCuboid : public CRect {
protected:
    double ht; //dp for depth
public:
    CCuboid(double a, double b, double c, double d, double e) :
        CRect(a,b,c,d) { ht = e; }
    void SetHeight(double d=1.0) { ht = d; }
    double GetHeight() const { return ht; }
    double Area() const { 
		return (2*CRect::Area()+2*GetL()*ht+2*GetW()*ht);              
	} 
    friend ostream & operator << (ostream &,
        const CCuboid &);
    string ToString() const	{ 
        return "CCuboid";   }
};

ostream & operator << (ostream & out, const CPoint& p) {
    out << p.x << " " << p.y; 
	return out;
}

....

void DisplayObject(const CPoint * p) {
    cout << **p->ToString()** << endl;         
}

int main()
{  
	CPoint o1(5,7); 
	CRect o2(2,4,5,7); 
	CCuboid o3(1,3,5,7,9); 
	DisplayObject(&o1); 
	DisplayObject(&o2);
	DisplayObject(&o3);
	
	system("pause");
	return 0;
}


```


## 🖊️  動態綁定使用的虛函式
動態綁定會在同名的函式前面加上virtual

(一)虛函式的特色

1.	可以在基礎類別和衍生類別間做轉型。
2.	可以拷貝一個衍生類別物件的位置到基礎類別的指標中。
3.	衍生類別的物件可以當成是基礎類別的參考，可以存取基礎類別的函式。
	
💡基礎類別可以被衍生類別存取(複雜的資料結構可以變簡單)，但是衍生類別無法被基礎類別存取(反向無法，因為衍生類別多了很多屬性，轉不回來)

4. 虛函數會讓基礎類別的pointer或reference可以作用衍生類別的物件上(可以指到或參考到)，而非基礎類別直接變成派生類別。



| Friend function |  virtual function |
| -------- | -------- |
| Overloading| Overriding     |
| 同名異式，只有名字相同，可能參數列或回傳型態不同| 函數名稱、參數數量、(回傳)型態都要相同   |




(二)虛解構子

1.如果基礎類別指標指到衍生類別物件被刪除的話，基礎類別的解構子會作用在該物件上，但卻刪不完整，只會刪除繼承來的部分。
```
CBase *pB =new CDerived;
...
delete pB;
```

💡解法: 記得要把基礎類別的解構子寫成virtual的形式，讓衍生類別可以繼承(解構子不能被繼承)。

```
//基礎類別
class B {public: virtual ~B() {cout << "B:~B()\n"}
};
//衍生類別
class D: public B{
     int *iary;
public:
    D(int i){iary=new int[i];}
    ~D(){
        delete [] iary;
        cout << "D::D()\n";
    }
};

//main()
    B *pB =new D(10);
    delete pB;
//他會去呼叫D的解構子，再去呼叫B底下的解構子
//D有繼承自B的資料，也有自己的資料，所以呼叫D的解構子清除新生的資料，再呼叫B底下的解構子，把B的資料清掉
```



    

## 🖊️  純虛函數⭐
(一)定義
虛函數是用來子類繼承後能夠複寫的函數。


(二)範例
```
//基礎類別
class CFig{
protected:
    double x,y;
public;
    void SetDim(double a =0,double b=0){x=a, y=b};
    //純虛函數，本身不用定義
    virtual void Area()=0; 
};

//衍生類別
class CRec:public CFig{
//強迫後面衍生類別要定義
public: void Area(int i){
    cout<<"Rec:" << x*y <<"\n";}
};

//衍生類別
class CTri:public CFig{
public: void Area(){
    cout<<"Tri:"<<x*y/2<<"\n";}
};
//main()
 CFig *pF;
 CFig t3;
 t3.SetDim(20,10);
 pF =&t3;
 //CTri的Area
 pF->Area();
 CFig &rF =t3;
 rF.SetDim(5,4);
 rF.Area();
```







## 🤔 疑問
無

## 📖 下一章節主題預告
模板

