# include <iostream>
# include <fstream>
# include <algorithm>
using
namespace
std;
# include <math.h>
# include <map>
int
r, kolvo;
int
w, h;
int
mas[1000][1000];
int
used[1000][1000];
int
used1[1000][1000];
void
obhod(int
x, int
y){
    used[x][y] = 1;
if (x + 1 == h)
{r = 0;
return;}
if (used[x][y + 1] == 0 and mas[x][y + 1] == 0) {obhod(x, y + 1); used[x][y + 1] = 0;}
if (r == 0)
return;
if (used[x][y - 1] == 0 and mas[x][y - 1] == 0) {obhod(x, y - 1); used[x][y - 1] = 0;}
if (r == 0) return;
if (used[x + 1][y] == 0 and mas[x + 1][y] == 0) {obhod(x + 1, y); used[x + 1][y] = 0;}

}
int
main()
{
cin >> w >> h;
for (int x = 0; x < h; ++x){
for (int y = 0; y < w; ++y){
cin >> mas[x][y];
used[x][y] = 0;

}
}
int
otvet = 0;
for (int x = 0; x < h; ++x){
for (int y = 0; y < w; ++y){
if (mas[x][y] == 0){
r = 1;
kolvo = 0;
obhod(x, y);
used[x][y] = 0;
if (r) otvet++;
}

}
}

cout << otvet;
}