# This is the output of analyzeImage.py (each value indicates a RGB color)
myScreenshot = """
        0        4      264      267      527      530      789    66328
    66588    66591    66849   132388   132647   132650   132908   198447
   198706   198708   264503   264505   330299   330557   330560   396354
   396612   462150   462408   527946   528204   593998   594000   659794
   660052   725590   791383   791641   857435   857437   923230   989024
   989026  1054819  1120613  1120870  1186408  1252201  1252459  1318252
  1384046  1384047  1449841  1515634  1515892  1581429  1647222  1713016
  1713273  1779066  1844860  1910397  1976190  1976447  2042241  2108034
  2173827  2239364  2239621  2305415  2371208  2437001  2502794  2568587
  2568844  2634381  2700174  2765968  2831761  2897554  2963347  3029140
  3029397  3095190  3160983  3226520  3292313  3358106  3423899  3489692
  3555485  3621278  3687071  3752864  3818656  3884449  3950242  4016035
  4081828  4147621  4147878  4213671  4279464  4345256  4411049  4476842
  4542635  4608428  4739757  4805550  4871342  4937135  5002928  5068721
  5134514  5200306  5266099  5331892  5397685  5463477  5529270  5595063
  5660856  5726648  5792441  5858234  5924027  5989819  6121148  6186941
  6252734  6318526  6384319  6450112  6515904  6581953  6647746  6779074
  6844867  6910660  6976452  7042245  7108038  7173830  7239623  7370952
  7436744  7502793  7568586  7634378  7700171  7765964  7897292  7963085
  8028877  8094670  8160719  8226511  8357840  8423632  8489425  8555218
  8621010  8752339  8818387  8884180  8949973  9015765  9147094  9212886
  9278679  9344727  9410520  9541849  9607641  9673434  9739226  9870555
  9936603 10002396 10068188 10133981 10265309 10331102 10397150 10462943
 10594272 10660064 10725857 10791905 10923234 10989026 11054819 11120611
 11251940 11317988 11383781 11515109 11580902 11646694 11712743 11844071
 11909864 11975656 12106985 12173033 12238826 12304618 12435947 12501995
 12567787 12699116 12764908 12830701 12962285 13028078 13093870 13159663
 13291247 13357040 13422832 13554161 13619953 13686001 13817330 13883122
 13948915 14080499 14146292 14212084 14343412 14409461 14475253 14606582
 14672374 14738423 14869751 14935543 15066872 15132920 15198713 15330041
 15396090 15461882 15593210 15659003 15725051 15856380 15922172 16053500
 16119549 16185341 16316670 16382718 16448510 16579839 16645631 16777215
"""

# https://www.i2phd.org/images/argo143screen.gif
webScreenshot = """
        0        4      264      267      527      530      789    66328
    66588    66591    66849   132388   132647   132650   132908   198447
   198706   198708   264503   264505   330299   330557   330560   396354
   396612   462150   462408   527946   528204   593998   594000   659794
   660052   725590   791383   791641   857435   857437   923230   989024
   989026  1054819  1120613  1120870  1186408  1252201  1252459  1318252
  1384046  1384047  1449841  1515634  1515892  1581429  1647222  1713016
  1713273  1779066  1844860  1910397  1976190  1976447  2042241  2108034
  2173827  2239364  2239621  2305415  2371208  2437001  2502794  2568587
  2568844  2634381  2700174  2765968  2831761  2897554  2963347  3029140
  3029397  3095190  3160983  3226520  3292313  3358106  3423899  3489692
  3555485  3621278  3687071  3752864  3818656  3884449  3950242  4016035
  4081828  4147621  4147878  4213671  4279464  4345256  4411049  4476842
  4542635  4608428  4739757  4805550  4871342  4937135  5002928  5068721
  5134514  5200306  5266099  5331892  5397685  5463477  5529270  5595063
  5660856  5726648  5792441  5858234  5924027  5989819  6121148  6186941
  6252734  6318526  6384319  6450112  6515904  6581953  6647746  6779074
  6844867  6910660  6976452  7042245  7108038  7173830  7239623  7370952
  7436744  7502793  7568586  7634378  7700171  7765964  7897292  7963085
  8028877  8094670  8160719  8226511  8357840  8423632  8489425  8555218
  8621010  8752339  8818387  8884180  8949973  9015765  9147094  9212886
  9278679  9344727  9410520  9541849  9607641  9673434  9739226  9870555
  9936603 10002396 10068188 10133981 10265309 10331102 10397150 10462943
 10594272 10660064 10725857 10791905 10923234 10989026 11054819 11120611
 11251940 11317988 11383781 11515109 11580902 11646694 11712743 11844071
 11909864 11975656 12106985 12173033 12238826 12304618 12435947 12501995
 12567787 12699116 12764908 12830701 12962285 13028078 13093870 13159663
 13291247 13357040 13422832 13554161 13619953 13686001 13817330 13883122
 13948915 14080499 14146292 14212084 14343412 14409461 14475253 14606582
 14672374 14738423 14869751 14935543 15066872 15132920 15198713 15330041
 15396090 15461882 15593210 15659003 15725051 15856380 15922172 16053500
 16119549 16185341 16316670 16382718 16448510 16579839 16645631 16777215
"""


if __name__ == "__main__":
    values = [x.strip() for x in myScreenshot.replace(",", " ").split(" ")]
    values = [int(x) for x in values if len(x)]
    assert (len(values) == 256)

    txt = f"# colormap argo\n"

    for i in range(256):
        int32 = values[i] * 255  # alpha
        txt += f"{int32:010d}, "
        if i % 8 == 7:
            txt += "\n"

    with open(f"../analyzed2/argo.csv", 'w') as f:
        f.write(txt)

    print(txt)
