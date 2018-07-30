#include <stdio.h>
#include <stdlib.h>
#include <string.h>


char ChuSo[10][20] = {" không "," một "," hai "," ba "," bốn "," năm "," sáu "," bảy "," tám "," chín "};
char Tien[6][20] = {"", " nghìn", " triệu", " tỷ", " nghìn tỷ", " triệu tỷ"};

//1. Hàm đọc số có ba chữ số;
char* DocSo3ChuSo(int baso)
{
    int tram;
    int chuc;
    int donvi;
    char* KetQua = malloc(1000);
    tram=(baso/100);
    chuc=((baso%100)/10);
    donvi=baso%10;
    if(tram==0 && chuc==0 && donvi==0) 
        return KetQua;
    if(tram!=0)
    {
        strcat(KetQua, ChuSo[tram]);
        strcat(KetQua, " trăm ");
        if ((chuc == 0) && (donvi != 0)) 
            strcat(KetQua, " linh ");
    }
    if ((chuc != 0) && (chuc != 1))
    {
        strcat(KetQua, ChuSo[chuc]);
        strcat(KetQua, " mươi");
        if ((chuc == 0) && (donvi != 0)) 
            strcat(KetQua, " linh ");
    }
    if (chuc == 1) 
        strcat(KetQua, " mười ");
    switch (donvi)
    {
        case 1:
            if ((chuc != 0) && (chuc != 1))
            {
                strcat(KetQua, " mốt ");
            }
            else
            {
                strcat(KetQua, ChuSo[donvi]);
            }
            break;
        case 5:
            if (chuc == 0)
            {
                strcat(KetQua, ChuSo[donvi]);
            }
            else
            {
                strcat(KetQua, " lăm ");
            }
            break;
        default:
            if (donvi != 0)
            {
                strcat(KetQua, ChuSo[donvi]);
            }
            break;
        }
    return KetQua;
}

//2. Hàm đọc số thành chữ (Sử dụng hàm đọc số có ba chữ số)

char* DocTienBangChu(int SoTien)
{
    int lan=0;
    int i=0;
    int so=0;
    char* KetQua=malloc(1000);
    char* tmp;
    int ViTri[10];
    if(SoTien<0) 
        return 0;
    if(SoTien==0) 
        return 0;
    if(SoTien>0)
    {
        so=SoTien;
    }
    else
    {
        so = -SoTien;
    }
    if (SoTien > 8999999999999999)
    {
        //SoTien = 0;
        return 0;
    }
    ViTri[5] = (so / 1000000000000000);
    so = so - (ViTri[5]) * 1000000000000000;

    ViTri[4] = (so / 1000000000000);
    so = so - (ViTri[4]) * 1000000000000;

    ViTri[3] = (so / 1000000000);
    so = so - (ViTri[3]) * 1000000000;

    ViTri[2] = (so / 1000000);

    ViTri[1] = ((so % 1000000) / 1000);

    ViTri[0] = (so % 1000);

    if (ViTri[5] > 0)
    {
        lan = 5;
    }
    else if (ViTri[4] > 0)
    {
        lan = 4;
    }
    else if (ViTri[3] > 0)
    {
        lan = 3;
    }
    else if (ViTri[2] > 0)
    {
        lan = 2;
    }
    else if (ViTri[1] > 0)
    {
        lan = 1;
    }
    else
    {
        lan = 0;
    }
    for (i = lan; i >= 0; i--)
    {
        tmp = DocSo3ChuSo(ViTri[i]);
        strcat(KetQua, tmp);
        if (ViTri[i] > 0) 
            strcat(KetQua, Tien[i]);
    }
   return KetQua;
}

int main() {
    int t;
    scanf("%d", &t);
    char *r = DocTienBangChu(t);
    if (r!=0)
        puts(r);
    else
        printf("Error");
    return 0;
}
