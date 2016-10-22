import random
from operator import itemgetter

king = [('live_like_a_king', [1000, 25, [1,2,3,4,5,6,7,8], [9]], {"epsilon":1E-5}, 2688.8725285249125),
        ('live_like_a_king', [1000, 25, [1,2,3,4,5,6,7], [8,9]], {"epsilon":1E-5}, 1156.1591045573746),
        ('live_like_a_king', [1000, 25, [1,2,3,4,5,6], [7,8,9]], {"epsilon":1E-5}, 649.5079972223655),
        ('live_like_a_king', [1000, 25, [1,2,3,4,5], [6,7,8,9]], {"epsilon":1E-5}, 399.2157664712041),
        ('live_like_a_king', [1000, 25, [1,2,3,4], [5,6,7,8,9]], {"epsilon":1E-5}, 251.34432441341954),
        ('live_like_a_king', [1000, 25, [1,2,3], [4,5,6,7,8,9]], {"epsilon":1E-5}, 154.58473051947612),
        ('live_like_a_king', [1000, 25, [1,2], [3,4,5,6,7,8,9]], {"epsilon":1E-5}, 86.95168995603333),
        ('live_like_a_king', [1000, 25, [1], [2,3,4,5,6,7,8,9]], {"epsilon":1E-5}, 37.456909600909086),
        ('live_like_a_king', [1000, 25, [], [1,2,3,4,5,6,7,8,9]], {"epsilon":1E-5}, 0.0),
        ('live_like_a_king', [1000, 25, [1,2,3,4,5,6,7,8], [9]], {"epsilon":1E-3}, 2688.8725285249125),
        ('live_like_a_king', [1000, 25, [1,2,3,4,5,6], [7,8,9]], {"epsilon":1E-3}, 649.5079972223655),
        ('live_like_a_king', [1000, 25, [1,2,3,4], [5,6,7,8,9]], {"epsilon":1E-3}, 251.34432441341954),
        ('live_like_a_king', [1000, 25, [1,2], [3,4,5,6,7,8,9]], {"epsilon":1E-3}, 86.95168995603333),
        ('live_like_a_king', [1000, 25, [1], [2,3,4,5,6,7,8,9]], {"epsilon":1E-3}, 37.456909600909086),
        ('live_like_a_king', [1000, 25, [], [1,2,3,4,5,6,7,8,9]], {"epsilon":1E-3}, 0.0),
        ('live_like_a_king', [0, 25, [1,2,3,4], [5,6,7,8,9]], {"epsilon":1E-5}, 0.0),
        ('live_like_a_king', [1000, 0, [1,2,3,4], [5,6,7,8,9]], {"epsilon":1E-5}, 0.0),
        ('live_like_a_king', [1000, 25, [-1,-2,-3,-4], [-5,-6,-7,-8,-9]], {"epsilon":1E-5}, 155.2908745356438),
        ('live_like_a_king', [1000, 25, [0,0,0,0,0], [0,0,0,0]], {"epsilon":1E-5}, 312.5),
        ('live_like_a_king', [1000, 25, [1,2,3,4], [5,6,-100,8,9]], {"epsilon":1E-5}, 0.0),
        ('live_like_a_king', [1000, 25, [1,2,3,4], [5,6,7,8,-100]], {"epsilon":1E-5}, 0.0),
        ('live_like_a_king', [1000, 25, [10], [0]], {"epsilon":1E-5}, 250.0),
        ('live_like_a_king', [1000, 25, [1,2,3,4], [-99.9,600,700,800,900]], {"epsilon":1E-5}, 0.9037396758231389),
        ('live_like_a_king', [1000, 25, [1,2,3,4], [5,6,7,8,9],1E-5], {}, 251.34432441341954),
        ('live_like_a_king', [],{"salary":1000, "save":25, "pre_retire_growth_rates":[1,2,3,4], "post_retire_growth_rates":[5,6,7,8,9],"epsilon":1E-5}, 251.34432441341954)
        ]

_names = ("h2","h4","h6","h8","h1","h3","h5","h7","h9")

bubble = [('bubble_sort_2nd_value',[[]],{},[]),
          ('bubble_sort_2nd_value',[[("h1",100)]],{},[]),
          ('bubble_sort_2nd_value',[[("h1",100),("h2",200)]],{},[]),
          ('bubble_sort_2nd_value',[[("h2",100),("h1",200)]],{},[]),
          ('bubble_sort_2nd_value',[[("h1",200),("h2",100)]],{},[]),
          ('bubble_sort_2nd_value',[[("h2",200),("h1",100)]],{},[]),
          ('bubble_sort_2nd_value',[[("h1",100),("h2",100)]],{},[]),
          ('bubble_sort_2nd_value',[[("h2",100),("h1",100)]],{},[]),
          ('bubble_sort_2nd_value',[list(zip(_names,(10,21,34,45,58,67,73,87,99)))],{},[]),
          ('bubble_sort_2nd_value',[list(zip(_names,(91,82,73,64,55,46,37,28,19)))],{},[]),
          ('bubble_sort_2nd_value',[list(zip(_names,(28,63,2,72,20,6,6,40,18)))],{},[]),
          ('bubble_sort_2nd_value',[list(zip(_names,(36, 45, 42, 16, 1, 15, 32, 18, 14)))],{},[]),
          ('bubble_sort_2nd_value',[list(zip(_names,(14, 32, 30, 3, 54, 35, 18, 12, 8)))],{},[]),
          ('bubble_sort_2nd_value',[list(zip(_names,(18, 28, 12, 5, 12, 72, 8, 63, 10)))],{},[]),
          ('bubble_sort_2nd_value',[list(zip(_names,(8, 30, 7, 54, 72, 8, 7, 15, 24)))],{},[]),
          ('bubble_sort_2nd_value',[list(zip(_names,(1, 12, 24, 24, 12, 18, 25, 56, 63)))],{},[]),
          ('bubble_sort_2nd_value',[list(zip(_names,(32, 54, 9, 35, 8, 42, 1, 10, 72)))],{},[]),
          ('bubble_sort_2nd_value',[list(zip(_names,(30, 4, 4, 81, 28, 56, 18, 8, 15)))],{},[]),
          ('bubble_sort_2nd_value',[list(zip(_names,(12, 12, 12, 72, 72, 12, 25, 7, 7)))],{},[]),
          ('bubble_sort_2nd_value',[],{"tuple_list":list(zip(_names,(1, 15, 16, 45, 32, 8, 54, 49, 18)))},[]),
          ]

for r in bubble:
    r[3].extend(sorted(r[1][0] if r[1] else r[2]["tuple_list"] ,key = itemgetter(1)))
    
choose = [('choosing_retirement_home',[1000,[0],[]],{},None),
          ('choosing_retirement_home',[1000,[0],[("h1",100)]],{},"h1"),
          ('choosing_retirement_home',[1000,[0],[("h1",999)]],{},"h1"),
          ('choosing_retirement_home',[1000,[0],[("h1",1001)]],{},None),
          ('choosing_retirement_home',[1000,[0],[("h1",10000)]],{},None),
          ('choosing_retirement_home',[1000,[0],[("h1",100),("h2",900)]],{},"h2"),
          ('choosing_retirement_home',[1000,[0],[("h1",100),("h2",9000)]],{},"h1"),
          ('choosing_retirement_home',[1000,[0],[("h1",1100),("h2",9000)]],{},None),
          ('choosing_retirement_home',[110,[-50],(list(zip(_names,range(100,1000,100))))],{},None),
          ('choosing_retirement_home',[110,[0],(list(zip(_names,range(100,1000,100))))],{},"h2"),
          ('choosing_retirement_home',[110,[100],(list(zip(_names,range(100,1000,100))))],{},"h4"),
          ('choosing_retirement_home',[110,[200],(list(zip(_names,range(100,1000,100))))],{},"h6"),
          ('choosing_retirement_home',[110,[400],(list(zip(_names,range(100,1000,100))))],{},"h1"),
          ('choosing_retirement_home',[110,[500],(list(zip(_names,range(100,1000,100))))],{},"h3"),
          ('choosing_retirement_home',[110,[700],(list(zip(_names,range(100,1000,100))))],{},"h7"),
          ('choosing_retirement_home',[110,[800],(list(zip(_names,range(100,1000,100))))],{},"h9"),
          ('choosing_retirement_home',[110,[900],(list(zip(_names,range(100,1000,100))))],{},"h9"),
          ('choosing_retirement_home',[1000,[5,10,15,20,25,30,35,40,45,50],(list(zip(_names,range(100,1000,100))))],{},"h4"),
          ('choosing_retirement_home',[0,[1000],(list(zip(_names,range(100,1000,100))))],{},None),
          ('choosing_retirement_home',[],{"savings":110,"growth_rates":[-100],"retirement_houses":(list(zip(_names,range(100,1000,100))))},None),
          ]

def f0(home):
    return home[1]+1

def f1(home):
    return home[1]+home[2]

def f2(home):
    return home[1]+home[2]**2/2

def f3(home):
    return home[1]+home[2]**3/6

def op_homes(seed,opps):
    r = random.Random()
    r.seed(seed)
    opps=list(opps)
    r.shuffle(opps)
    res = list(zip(_names,range(100,1000,100),opps))
    r.shuffle(res)
    return res

opponent = [('choose_retirement_home_opponents',[1000,f3,[]],{},None),
            ('choose_retirement_home_opponents',[1000,f3,[("h1",100,20)]],{},"h1"),
            ('choose_retirement_home_opponents',[1000,f2,[("h1",999,20)]],{},"h1"),
            ('choose_retirement_home_opponents',[1000,f1,[("h1",1001,20)]],{},None),
            ('choose_retirement_home_opponents',[1000,f0,[("h1",10000,20)]],{},None),
            ('choose_retirement_home_opponents',[1000,f2,[("h1",100,0),("h2",900,0)]],{},"h2"),
            ('choose_retirement_home_opponents',[1000,f2,[("h1",100,20),("h2",900,5)]],{},"h2"),
            ('choose_retirement_home_opponents',[1000,f2,[("h1",100,80),("h2",900,20)]],{},"h1"),
            ('choose_retirement_home_opponents',[1000,f2,[("h1",100,20),("h2",9000,60)]],{},"h1"),
            ('choose_retirement_home_opponents',[1000,f2,[("h1",100,5),("h2",9000,5)]],{},"h1"),
            ('choose_retirement_home_opponents',[1000,f2,[("h1",1100,150),("h2",9000,200)]],{},None),
            ('choose_retirement_home_opponents',[1000,f2,[("h1",1100,1500),("h2",9000,10)]],{},None),
            ('choose_retirement_home_opponents',[55,f0,op_homes(55,range(111,1000,111))],{},None),
            ('choose_retirement_home_opponents',[110,f1,op_homes(1,range(111,1000,111))],{},"h2"),
            ('choose_retirement_home_opponents',[220,f2,op_homes(2,[0]*9)],{},"h4"),
            ('choose_retirement_home_opponents',[550,f3,op_homes(5,[400]*9)],{},"h1"),
            ('choose_retirement_home_opponents',[770,f0,op_homes(7,range(999,0,-111))],{},"h5"),
            ('choose_retirement_home_opponents',[880,f1,op_homes(8,range(999,0,-111))],{},"h3"),
            ('choose_retirement_home_opponents',[990,f2,op_homes(9,range(49,0,-5))],{},"h1"),
            ('choose_retirement_home_opponents',[],{"budget":1110,"key":f3,"retirement_houses":op_homes(11,range(12,0,-1))},"h5"),
            ]

badinputs = [('live_like_a_king', [-1000, 25, [1,2,3,4], [5,6,7,8,9]], {"epsilon":1E-5}, None),
             ('live_like_a_king', [1000, -25, [1,2,3,4], [5,6,7,8,9]], {"epsilon":1E-5}, None),
             ('live_like_a_king', [1000, 125, [1,2,3,4], [5,6,7,8,9]], {"epsilon":1E-5}, None),
             ('live_like_a_king', [1000, 25, [-101,2,3,4], [5,6,7,8,9]], {"epsilon":1E-5}, None),
             ('live_like_a_king', [1000, 25, [1,-102,3,4], [5,6,7,8,9]], {"epsilon":1E-5}, None),
             ('live_like_a_king', [1000, 25, [1,2,3,4], [5,6,7,8,9]], {"epsilon":-1E-5}, None),
             ('live_like_a_king', [1000, 25, [1,2,3,4], [5,6,7,8,9]], {"epsilon":0}, None),
             ('live_like_a_king', [1000, 25, [1,2,3,4], []], {"epsilon":1E-5}, None),
             ('live_like_a_king', [0, 25, [1,2,3,4], []], {"epsilon":1E-5}, None),
             ('live_like_a_king', [1000, 25, [1,2,3,4], []], {"epsilon":1E-5}, None),
             ('live_like_a_king', [0, 25, [1,2,3,4], []], {"epsilon":1E-5}, None),
             ('live_like_a_king', [1000, 25, [1,2,3,4], []], {"epsilon":1E-5}, None),
             ('live_like_a_king', [0, 25, [1,2,3,4], []], {"epsilon":1E-5}, None),
             ('choosing_retirement_home',[-100,[9,8],[("h1",100),("h2",900)]],{},None),
             ('choosing_retirement_home',[100,[-109,8],[("h1",100),("h2",900)]],{},None),
             ('choosing_retirement_home',[100,[9,-108],[("h1",100),("h2",900)]],{},None),
             ('choosing_retirement_home',[100,[],[("h1",100),("h2",900)]],{},None),
             ('choosing_retirement_home',[100,[-109,-108],[("h1",100),("h2",900)]],{},None),
             ('choose_retirement_home_opponents',[-1000,f2,[("h1",100,80),("h2",900,20)]],{},None),
             ('choose_retirement_home_opponents',[-0.1,f2,[("h1",100,80),("h2",900,20)]],{},None),
             ]

rtset={
    "bubble"    : bubble,
    "choose"    : choose,
    "opponent"  : opponent,
    "badinputs" : badinputs,
    }

eset={    "king"      : king }

_vals = (0,1,5,10,50,100,500,1000,10000,1000000)

_inputs = list(zip(("h"+str(i) for i in range(20)),_vals+tuple(float(v) for v in _vals),_vals+_vals[::-1]))

fset={ "keygetter" : [('get_value_key', [0.0],{"_input":_inputs},[0.0, 1.0, 5.0, 10.0, 50.0, 100.0, 500.0, 1000.0, 10000.0, 1000000.0, 0.0, 1.0, 5.0, 10.0, 50.0, 100.0, 500.0, 1000.0, 10000.0, 1000000.0]),
                      ('get_value_key', [0.5],{"_input":_inputs},[0.0, 1.5, 7.5, 15.0, 75.0, 150.0, 750.0, 1500.0, 15000.0, 1500000.0, 500000.0, 5001.0, 505.0, 260.0, 100.0, 125.0, 505.0, 1002.5, 10000.5, 1000000.0]),
                      ('get_value_key', [1.0],{"_input":_inputs},[0.0, 2.0, 10.0, 20.0, 100.0, 200.0, 1000.0, 2000.0, 20000.0, 2000000.0, 1000000.0, 10001.0, 1005.0, 510.0, 150.0, 150.0, 510.0, 1005.0, 10001.0, 1000000.0]),
                      ('get_value_key', [5],{"_input":_inputs},[0.0, 6.0, 30.0, 60.0, 300.0, 600.0, 3000.0, 6000.0, 60000.0, 6000000.0, 5000000.0, 50001.0, 5005.0, 2510.0, 550.0, 350.0, 550.0, 1025.0, 10005.0, 1000000.0]),
                      ('get_value_key', [10.0],{"_input":_inputs},[0.0, 11.0, 55.0, 110.0, 550.0, 1100.0, 5500.0, 11000.0, 110000.0, 11000000.0, 10000000.0, 100001.0, 10005.0, 5010.0, 1050.0, 600.0, 600.0, 1050.0, 10010.0, 1000000.0]),
                      ('get_value_key', [50],{"_input":_inputs},[0.0, 51.0, 255.0, 510.0, 2550.0, 5100.0, 25500.0, 51000.0, 510000.0, 51000000.0, 50000000.0, 500001.0, 50005.0, 25010.0, 5050.0, 2600.0, 1000.0, 1250.0, 10050.0, 1000000.0]),
                      ('get_value_key', [100.0],{"_input":_inputs},[0.0, 101.0, 505.0, 1010.0, 5050.0, 10100.0, 50500.0, 101000.0, 1010000.0, 101000000.0, 100000000.0, 1000001.0, 100005.0, 50010.0, 10050.0, 5100.0, 1500.0, 1500.0, 10100.0, 1000000.0]),
                      ('get_value_key', [500],{"_input":_inputs},[0.0, 501.0, 2505.0, 5010.0, 25050.0, 50100.0, 250500.0, 501000.0, 5010000.0, 501000000.0, 500000000.0, 5000001.0, 500005.0, 250010.0, 50050.0, 25100.0, 5500.0, 3500.0, 10500.0, 1000000.0]),
                      ('get_value_key', [1000.0],{"_input":_inputs},[0.0, 1001.0, 5005.0, 10010.0, 50050.0, 100100.0, 500500.0, 1001000.0, 10010000.0, 1001000000.0, 1000000000.0, 10000001.0, 1000005.0, 500010.0, 100050.0, 50100.0, 10500.0, 6000.0, 11000.0, 1000000.0]),
                      ('get_value_key', [10000],{"_input":_inputs},[0.0, 10001.0, 50005.0, 100010.0, 500050.0, 1000100.0, 5000500.0, 10001000.0, 100010000.0, 10001000000.0, 10000000000.0, 100000001.0, 10000005.0, 5000010.0, 1000050.0, 500100.0, 100500.0, 51000.0, 20000.0, 1000000.0]),
                      ]}
       
