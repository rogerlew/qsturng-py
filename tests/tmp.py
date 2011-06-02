cases = """\
0.75 30 12.0 5.01973488482
0.975 15 18.0 6.00428263999
0.1 8 11.0 1.76248712658
0.995 6 17.0 6.13684839819
0.85 15 18.0 4.65007986215
0.75 17 18.0 4.33179650607
0.75 60 16.0 5.50520795792
0.99 100 2.0 50.3860723433
0.9 2 40.0 2.38132493732
0.8 12 20.0 4.15361239056
0.675 8 14.0 3.35011529943
0.75 30 24.0 4.77976803574
0.75 2 18.0 1.68109190167
0.99 7 120.0 5.00525918406
0.8 19 15.0 4.70694373713
0.8 15 8.0 4.80392205906
0.5 12 11.0 3.31672775449
0.85 30 2.0 10.2308503607
0.675 20 18.0 4.23706426096
0.1 60 60.0 3.69215469278
0.8 60 40.0 5.39898584214
0.8 8 40.0 3.6234380878
0.75 60 60.0 5.17410044144
0.1 14 7.0 2.26916731727
0.995 6 9.0 7.40650212848
0.9 7 3.0 6.51193823824
0.99 3 13.0 4.96126407666
0.75 40 11.0 5.33201167216
0.999 3 3.0 23.2936337598
0.9 10 3.0 7.28635545121
0.9 3 17.0 3.10923439816
0.8 14 11.0 4.53405418962
0.95 80 18.0 7.10861770558
0.5 9 11.0 3.01292049364
0.8 18 40.0 4.39938505414
0.675 2 17.0 1.43339659709
0.975 14 24.0 5.69616145809
0.5 15 30.0 3.46671564864
0.9 19 30.0 4.98782422868
0.75 11 6.0 4.34876171895
0.75 3 40.0 2.28865064889
0.75 17 30.0 4.22464123677
0.85 2 17.0 2.13215287108
0.9 100 19.0 6.67303339861
0.999 20 24.0 7.99858967307
0.675 11 15.0 3.68168707529
0.85 12 20.0 4.38716978329
0.8 2 15.0 1.89590263242
0.99 8 6.0 8.61304083587
0.995 30 120.0 6.3842181475
0.95 5 1.0 37.0747080082
0.85 16 19.0 4.69304786816
0.75 15 1e+38 3.95091555576
0.99 5 4.0 9.96137704729
0.675 4 60.0 2.42557604522
0.1 18 14.0 2.5789330703
0.95 12 9.0 5.98277087597
0.5 100 18.0 5.08752122604
0.5 16 4.0 3.81934929939
0.95 11 1.0 50.5890799215
0.1 7 18.0 1.63888378407
0.9 11 5.0 5.96521287663
0.675 10 19.0 3.54218744672
0.75 19 7.0 4.87132698306
0.975 8 30.0 5.01679490047
0.995 16 17.0 7.31312030107
0.1 16 4.0 2.2847253572
0.99 100 10.0 10.379878518
0.999 14 5.0 18.13743331
0.95 7 16.0 4.74105859981
0.5 30 10.0 4.19638923615
0.675 16 3.0 4.98823504064
0.1 7 40.0 1.66170353571
0.975 30 3.0 15.6159662623
0.5 40 1e+38 4.27301260509
0.99 30 30.0 6.77104919336
0.999 7 1e+38 5.72967211955
0.99 40 18.0 7.6960082979
0.975 8 16.0 5.4120241731
0.1 6 19.0 1.46241069997
0.75 100 120.0 5.47495635718
0.975 8 11.0 5.83109858577
0.5 5 7.0 2.37318973277
0.675 30 7.0 4.95972604517
0.999 15 60.0 6.77339726262
0.995 7 2.0 39.952288193
0.995 6 3.0 18.0670553297
0.75 15 24.0 4.14590005143
0.995 15 1e+38 5.69905479513
0.995 40 6.0 13.5456365264
0.1 14 60.0 2.43809729928
0.5 4 18.0 2.0169401191
0.9 80 7.0 7.81844782527
0.99 40 14.0 8.20493017728
0.5 18 120.0 3.60362770658
0.95 11 13.0 5.43088480225
0.9 11 12.0 4.88608537667
0.999 16 2.0 114.150830301
0.9 30 14.0 5.83578826474
0.1 13 30.0 2.33146225352""".split('\n')
from pprint import pprint
l = [tuple(float(v) for v in line.split()) for line in cases]

for p,r,v,q in l:
    print p,r,v,q 