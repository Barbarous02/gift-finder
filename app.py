from flask import Flask, render_template, request
import sqlite3


def finder(d):
        good = [('Введите другие значения', 'https://lh3.googleusercontent.com/proxy/atrbsnO7cE28gJliMaW0NgI-hBv-J8qSYXuX8vPcpGtg7iCfdgKnMZ43Eko-dW-SxUdZsBzZq0FPeVq9ggtaVhYaXHXxeuLypnOX6HrfSq6ln8k1EALeWmZm-Er3QJEYNW51VoRaUIFpTmoBzTKEQUENO859cOXmVXOJamUfr17LKmsYGzA', 'https://www.google.com/'),
                ('Введите другие значения', 'https://lh3.googleusercontent.com/proxy/atrbsnO7cE28gJliMaW0NgI-hBv-J8qSYXuX8vPcpGtg7iCfdgKnMZ43Eko-dW-SxUdZsBzZq0FPeVq9ggtaVhYaXHXxeuLypnOX6HrfSq6ln8k1EALeWmZm-Er3QJEYNW51VoRaUIFpTmoBzTKEQUENO859cOXmVXOJamUfr17LKmsYGzA', 'https://www.google.com/'),
                ('Введите другие значения', 'https://lh3.googleusercontent.com/proxy/atrbsnO7cE28gJliMaW0NgI-hBv-J8qSYXuX8vPcpGtg7iCfdgKnMZ43Eko-dW-SxUdZsBzZq0FPeVq9ggtaVhYaXHXxeuLypnOX6HrfSq6ln8k1EALeWmZm-Er3QJEYNW51VoRaUIFpTmoBzTKEQUENO859cOXmVXOJamUfr17LKmsYGzA', 'https://www.google.com/')
               ]
    

        good1 = [0, 0, 0]
#         try:
        if True:
            
            connection = sqlite3.connect('all_gifts.db')
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM gifts;")
            all_g = cursor.fetchall()
            connection.commit()
            connection.close()
            
            any_g = []
            if int(d['age']) < 1:
                return good
            for i in all_g:
    
                if d['gender'] == 'm' and i[1] == 0:
                    continue
                if d['gender'] == 'w' and i[2] == 0:
                    continue
                if 1 <= int(d['age']) <= 10  and i[3] == 0:
                    continue
                if 11 <= int(d['age']) <= 18  and i[4] == 0:
                    continue
                if 19 <= int(d['age']) <= 30  and i[5] == 0:
                    continue
                if 31 <= int(d['age']) <= 60  and i[6] == 0:
                    continue
                if 61 <= int(d['age'])  and i[7] == 0:
                    continue
                if d['occupation'] == 'school' and i[8] == 0:
                    continue
                if d['occupation'] == 'student' and i[9] == 0:
                    continue
                if d['occupation'] == 'work' and i[10] == 0:
                    continue
                if d['sport'] == 'no' and i[11] != 0 or d['sport'] == 'dn' and i[11] != 0:
                    continue
                if d['pet'] == 'cat' and i[13] != 0 or d['pet'] == 'cat' and i[14] != 0:
                    continue
                if d['pet'] == 'dog' and i[12] != 0 or d['pet'] == 'dog' and i[14] != 0:
                    continue
                if d['pet'] == 'fish' and i[12] != 0 or d['pet'] == 'fish' and i[13] != 0:
                    continue
                if d['pet'] == 'dn' and i[12] != 0 or d['pet'] == 'dn' and i[13] != 0 or d['pet'] == 'dn' and i[14] != 0:
                    continue
                any_g.append(i)
        
            for i in any_g:
            
                if int(d['price']) < i[15]:
                    continue
                a = i
                b = 0
                for j in range(1, 15):
                    b += int(a[j])
                
                if b > good1[2]:
                    if b > good1[1]:
                        if b > good1[0]:
                            good1[2] = good1[1]
                            good[2] = good[1]
                            good1[1] = good1[0]
                            good[1] = good[0]
                            good1[0] = b
                            good[0] = [a[16], a[17], a[18]]
                        else:
                            good1[2] = good1[1]
                            good[2] = good[1]
                            good1[1] = b
                            good[1] = [a[16], a[17], a[18]]
                    else:
                        good1[2] = b
                        good[2] = [a[16], a[17], a[18]]            
            return good
#         except:
#             good = [('Введите другие значения', 'https://lh3.googleusercontent.com/proxy/atrbsnO7cE28gJliMaW0NgI-hBv-J8qSYXuX8vPcpGtg7iCfdgKnMZ43Eko-dW-SxUdZsBzZq0FPeVq9ggtaVhYaXHXxeuLypnOX6HrfSq6ln8k1EALeWmZm-Er3QJEYNW51VoRaUIFpTmoBzTKEQUENO859cOXmVXOJamUfr17LKmsYGzA', 'https://www.google.com/'),
#                 ('Введите другие значения', 'https://lh3.googleusercontent.com/proxy/atrbsnO7cE28gJliMaW0NgI-hBv-J8qSYXuX8vPcpGtg7iCfdgKnMZ43Eko-dW-SxUdZsBzZq0FPeVq9ggtaVhYaXHXxeuLypnOX6HrfSq6ln8k1EALeWmZm-Er3QJEYNW51VoRaUIFpTmoBzTKEQUENO859cOXmVXOJamUfr17LKmsYGzA', 'https://www.google.com/'),
#                 ('Введите другие значения', 'https://lh3.googleusercontent.com/proxy/atrbsnO7cE28gJliMaW0NgI-hBv-J8qSYXuX8vPcpGtg7iCfdgKnMZ43Eko-dW-SxUdZsBzZq0FPeVq9ggtaVhYaXHXxeuLypnOX6HrfSq6ln8k1EALeWmZm-Er3QJEYNW51VoRaUIFpTmoBzTKEQUENO859cOXmVXOJamUfr17LKmsYGzA', 'https://www.google.com/')
#                ]
#             return good   


app = Flask(__name__)


@app.route('/param', methods=['GET'])
def param():
    global mydict

    mydict['id'] = request.args.get('id')
    
    # if key doesn't exist, returns None
    mydict['gender'] = request.args.get('gender')

    # if key doesn't exist, returns None
    mydict['age'] = request.args['age']

    # if key doesn't exist, returns None
    mydict['occupation'] = request.args.get('occupation')

    # if key doesn't exist, returns None
    mydict['sport'] = request.args.get('sport')

    # if key doesn't exist, returns None
    mydict['pet'] = request.args.get('pet')
    
     # if key doesn't exist, returns None
    mydict['price'] = request.args.get('price')
    
    
    
    print(mydict)
    id_gifts[mydict['id']] = finder({'id': '1', 'gender': 'm', 'age': '18', 'occupation': 'work', 'sport': 'dn', 'pet': 'dog', 'price': '3000'})
    
    
    return '''{}
{}
{}
{}
{}
{}
{}'''.format(mydict['id'],mydict['gender'], mydict['age'], mydict['occupation'], mydict['sport'], mydict['pet'], mydict['price'])


@app.route('/gifts', methods=['GET'])
def gifts():
    global id_gifts

    himid = request.args.get('id')
    number = int(request.args.get('number')) - 1 #порядок подарка начиная с 1
    print(id_gifts[himid])
    
    return '''{}
{}
{}'''.format(id_gifts[himid][number][0], id_gifts[himid][number][1], id_gifts[himid][number][2])




mydict = {'id': 0,'gender': 0, 'age': 0, 'occupation': 0, 'sport': 0, 'pet': 0, 'price': 0}
myid = dict()

id_gifts = dict()




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4568)
